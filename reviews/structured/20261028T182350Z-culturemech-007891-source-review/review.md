# Scientific review: Desulfobacterium Oleovorans Medium

- Review: 20261028T182350Z-culturemech-007891-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:07:11.030364Z
- Finished UTC: 2026-10-28T18:23:50.049696Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact M1354/JCM1258 identity is supported, but the selected target and maintained owner retain mixed water stages, wrong amount units, flattened stock inputs and missing preparation. Scoped M180/M190 repairs are credited; remaining M431/M401 amounts and M180 hydrate mappings require bounded curation.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch074 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007891 | data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml | generated | desulfobacterium_oleovorans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:007891 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:007891 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:007891 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:007891 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and dependency identity

identity: supported. Targets: CultureMech:007891.

Selected TOGO M1354 is JCM1258. The lower-case duplicate report refers to another generated comparison and its KOMODO/DSM owners, not additional current owners here. Only named JCM187/197/431/403 subsections transfer.

### Classification and nonquantitative assertions

consistency: concern. Targets: CultureMech:007891.

LIQUID is compatible and no target-organism claim is present. COMPLEX/UNDEFINED is not supported by the specified formulation; generic applications do not establish strain growth. Source stock names and gas descriptions remain meaningful, while Unknown solution names are placeholders.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:007891.

51 current concentration fields are covered by 54 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b074-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","quantity_field_count":51,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"11.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"11.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The current 11 g/L combines 1 L basal input and 10 mL stearic-stock water as naked numbers. Preserve both stage-specific input volumes; do not sum incompatible units or claim final volume.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the current g/L assertion has no explicit final-volume basis. The main table lists 1 L input water and later additions; provider J1258 uses its separate 1052 mL normalization, not the local unchanged number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.25","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the current g/L assertion has no explicit final-volume basis. The main table lists 1 L input water and later additions; provider J1258 uses its separate 1052 mL normalization, not the local unchanged number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.25&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the current g/L assertion has no explicit final-volume basis. The main table lists 1 L input water and later additions; provider J1258 uses its separate 1052 mL normalization, not the local unchanged number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.25","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the current g/L assertion has no explicit final-volume basis. The main table lists 1 L input water and later additions; provider J1258 uses its separate 1052 mL normalization, not the local unchanged number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.25&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies 0.5 mg resazurin, whereas the local value is 0.5 g/L. Preserve the source mass and receiving stage; no measured final volume is established.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"3.4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"3.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the current g/L assertion has no explicit final-volume basis. The main table lists 1 L input water and later additions; provider J1258 uses its separate 1052 mL normalization, not the local unchanged number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 3.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.4&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the current g/L assertion has no explicit final-volume basis. The main table lists 1 L input water and later additions; provider J1258 uses its separate 1052 mL normalization, not the local unchanged number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"Na2SO4\",\n          \"volume\": 4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;4.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves dissolved amount unquantified. Source gas atmospheres and stock versus basal placement must be recorded separately; no gas concentration is derived.","source_stage":"basal atmosphere or stearic-stock atmosphere","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Nitrogen gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves dissolved amount unquantified. Source gas atmospheres and stock versus basal placement must be recorded separately; no gas concentration is derived.","source_stage":"basal atmosphere or stearic-stock atmosphere","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves dissolved amount unquantified. Source gas atmospheres and stock versus basal placement must be recorded separately; no gas concentration is derived.","source_stage":"basal atmosphere or stearic-stock atmosphere","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"Heat the solution in a closed vial under a N2 atmosphere in a boiling water bath. Shake until stearic acid is dissolved and autoclave. Add the solution to the medium while stearic acid is dissolved. Re-melt if stearic acid is solidified.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Stearic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.36","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.36","unit":"G_PER_L"}}],"decision":"correct","rationale":"The 0.36 g is a stearic-stock batch mass, not a direct receiving-medium g/L value. Preserve the stock and its 10 mL receiving addition separately.","source_stage":"stearic stock","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"Stearic acid\",\n          \"volume\": 0.36,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002068\",\n          \"gmo_id\": \"GMO_002068\",\n          \"label\": \"Stearic acid\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Stearic acid                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.36&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"FeCl2 solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The basal input or nested-stock batch dose is not an established dose per final liter. Resolve only the named subsection, retaining the source spelling and exact reference identity.","source_stage":"basal receiving batch","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Trace element solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The basal input or nested-stock batch dose is not an established dose per final liter. Resolve only the named subsection, retaining the source spelling and exact reference identity.","source_stage":"basal receiving batch","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Selenite--tungstate solution (see Medium [M431])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The basal input or nested-stock batch dose is not an established dose per final liter. Resolve only the named subsection, retaining the source spelling and exact reference identity.","source_stage":"basal receiving batch","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M431\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Selenite-tungstate solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=431\"&gt;431&lt;/a&gt;)      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"8% NaHCO3 solution**","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The post-cooling table explicitly says per liter; retain its receiving-dose basis without declaring a measured total volume. The percentage label has no stated w/w, w/v or v/v basis; do not infer mass.","source_stage":"post-cooling receiving dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"8% NaHCO3 solution**\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution**                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"5% Na2S・9H2O solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The post-cooling table explicitly says per liter; retain its receiving-dose basis without declaring a measured total volume. The percentage label has no stated w/w, w/v or v/v basis; do not infer mass.","source_stage":"post-cooling receiving dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\": \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"Trace vitamins (see Medium [M190])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The post-cooling table explicitly says per liter; retain its receiving-dose basis without declaring a measured total volume. Resolve only the named subsection, retaining the source spelling and exact reference identity.","source_stage":"post-cooling receiving dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace vitamins* (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\"&gt;197&lt;/a&gt;)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"Vitamin B12 solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The post-cooling table explicitly says per liter; retain its receiving-dose basis without declaring a measured total volume. Resolve only the named subsection, retaining the source spelling and exact reference identity.","source_stage":"post-cooling receiving dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Vitamin B12 solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;12&lt;/sub&gt; solution* (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Stearic solution (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The post-cooling table explicitly says per liter; retain its receiving-dose basis without declaring a measured total volume. Resolve only the named subsection, retaining the source spelling and exact reference identity.","source_stage":"post-cooling receiving dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Stearic solution (see below)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1354\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Steric solution (see below)                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"2 N NaOH solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[8].concentration","stored":{"value":"0.63","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[8].concentration","stored":{"value":"0.63","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source amount is a liquid addition, not grams per liter. The basal input or nested-stock batch dose is not an established dose per final liter. The 0.63 mL of 2 N NaOH belongs inside the stearic stock; normality is not silently converted to molarity.","source_stage":"stearic-stock internal reagent","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"2 N NaOH solution\",\n          \"volume\": 0.63,\n          \"unit\": \"ml\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 2 N NaOH solution                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.63&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Basal handling and late additions","local_fields":[],"decision":"evidence_only","rationale":"Record the exact stage-specific source procedure, including the explicit atmosphere and illustrative vessel volume. The general JCM sterilization default is distinct from stock-specific handling; no culture growth claim is inferred.","source_stage":"source-only preparation","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, aseptically and anaerobically add per liter the following solutions (autoclaved or *filter-sterilized and stored under a N2 gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Stearic-stock heat, atmosphere and redissolution","local_fields":[],"decision":"evidence_only","rationale":"Record the exact stearic-stock heating, nitrogen atmosphere, autoclaving and redissolution procedure in its own stock scope. The 10 mL Balch-tube example belongs to the main-medium procedure, not this stock. No culture growth claim is inferred.","source_stage":"source-only preparation","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"Heat the solution in a closed vial under a N2 atmosphere in a boiling water bath. Shake until stearic acid is dissolved and autoclave. Add the solution to the medium while stearic acid is dissolved. Re-melt if stearic acid is solidified.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"JCM default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The primary page supplies 121 C for 15 min unless otherwise stated. This is source procedure context, not an organism growth assertion.","source_stage":"source-only default","sources":[{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"jcm1258.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"Retained M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Retained M180 FeCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Retained M180 Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Retained M180 Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Retained M180 H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Retained M180 MnCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Retained M180 CoCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Retained M180 NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Retained M180 CuCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Retained M180 ZnCl2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing attached literal source claim and its original digest match the current source bytes. Retain this exact stock batch input, not a measured final-volume concentration; historical duplicate notes are superseded context.","source_stage":"M180 iron or trace stock only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Retained nested HCl solutions[0].solutions[0].composition[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Explicit 7.7 M reagent strength is supported by its attached exact claim; the accompanying 25% basis is unspecified.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Retained nested HCl solutions[0].solutions[0].concentration","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"The root evidence contains an additional exact HCl excerpt and this nested descriptor locator, authenticating 10 mL = 0.01 L into the iron stock; it is not the excluded parent-medium receiving dose.","source_stage":"M180 iron-stock nested reagent","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Retained HCl input-dose note","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].notes","stored":"Source stock addition: 10 ml = 0.01 L per receiving batch, not grams per liter or a dose per final liter."}],"decision":"verified","rationale":"The retained numeric note has the same exact scoped root attachment as the nested descriptor; no new dose or final concentration is inferred.","source_stage":"M180 nested HCl","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch074/source09-extra/apiTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T18:06:53.336358Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Scoped M431 Na2SeO3・5H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source lists 6 mg in the selenite-tungstate stock with 1 L input water. The stored g/L copies a milligram number and loses stock stage. Do not transfer the parent medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Scoped M431 Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source lists 8 mg in the selenite-tungstate stock with 1 L input water. The stored g/L copies a milligram number and loses stock stage. Do not transfer the parent medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Scoped M431 NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source lists 0.4 g NaOH in the selenite-tungstate stock with 1 L input water, and current APIJ1258 solution4172 explicitly supplies g_l=0.4 on its declared stock basis. Credit that provider stock-rate support; the current M431 direct main-medium g/L placement is unsupported because this is a separate stock. The source water alone does not independently measure final stock volume, and no parent receiving dose is transferred.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\": \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\": \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Selenite stock water","local_fields":[],"decision":"evidence_only","rationale":"The source 1 L is stock input water, not the local collapsed water row and not measured final volume.","source_stage":"source-only selenite stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Retained vitamin Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Retained vitamin Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Retained vitamin p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Retained vitamin Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Retained vitamin Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Retained vitamin Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Retained vitamin Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Retained vitamin Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"Retained vitamin Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Retained vitamin Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"Retained vitamin Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Existing exact attached source claim and digest authenticate this batch input. Retain the repaired water unit or mass note, without restoring unsupported g/L or importing the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"M401 B12 stock mass","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary B12 stock lists 5 mg in 100 mL input water. Current 5 g/L both misreads the mass unit and lacks supported stock-volume normalization. Preserve 5 mg, not an inferred final-medium contribution.","source_stage":"B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T18:07:09.242182Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T18:07:08.803574Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"B12 stock water","local_fields":[],"decision":"evidence_only","rationale":"100 mL is stock input water; the shared parent collapsed water is excluded and is not a final-stock-volume measurement.","source_stage":"source-only B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T18:07:09.242182Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T18:07:08.803574Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml":["ingredients[27]","ingredients[28]","ingredients[29]","solutions[1].name","solutions[1].preferred_term","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition","solutions[1].preferred_term"],"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml":["ingredients[25]","solutions[3].name","solutions[3].preferred_term","solutions[3].composition"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:007891.

Every in-scope primary/secondary slot and preferred-name MIM lookup is enumerated against the exact packaged snapshot and fresh OLS. Scoped cobalt/nickel hexahydrate mismatches are confirmed. Other supplied salt hydrates are compatible; generic calcium pantothenate and vitamin B12 do not establish stereochemistry or a specific vitamer. Canonical label agreement is separate from chemical-form support; current linkage coverage and its denominator are recorded per document.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:007891.

All 21 exact reports are read through lossless current line-cell reconstruction, with previously personally read identical cells reused by an explicit proof and 48 new cells read now. Both selected stock-repair plan rows exactly match previously read originals. Historical baseline and source-aware reports are derivative, not newly run checks. Current M180/M190 exact raw digest and snippets authenticate the retained batch repairs, including the scoped root HCl excerpt, without recovering old access events. Current importer/merge code is more conservative than the legacy flattening and duplicate-water history; no old execution is attributed from current code alone.

## Findings

### f1: Restore basal and stock stages before concentration curation

major / open / confirmed; issue key: culturemech-007891-stage-units.

The maintained M1354 owner and generated target combine 1 L basal water with 10 mL stearic-stock water as 11 g/L; resazurin 0.5 mg becomes 0.5 g/L. All nine liquid solution doses are G_PER_L, and stearic acid plus its 2 N NaOH reagent are flattened into the recipient. Restore each source batch/stock and exact unit, preserve the explicit late-addition per-liter basis, and leave other final-volume rates unresolved rather than substituting provider 1052 mL metadata.

### f2: Resolve exactly named stock subsections and retain existing repairs

major / open / confirmed; issue key: culturemech-007891-stock-references.

Resolve M180 iron/trace, M190 vitamins, M431 selenite-tungstate and M401 B12 only. M180/M190 already preserve authenticated batch inputs and nested HCl; keep those repairs. M431 still flattens 6 mg selenium and 8 mg tungstate as 6 and 8 g/L, and M401 B12 carries 5 g/L for a 5 mg stock input. Keep their parent formulations and receiving doses outside this review; stock water is input, not measured final volume.

### f3: Restore source preparation with exact stage boundaries

major / open / confirmed; issue key: culturemech-007891-preparation.

Neither selected document carries the main boil/cool and 4:1 N2/CO2 handling, late sterile additions, or separate stearic-stock heating/redissolution procedure. Restore source-specific preparation, the illustrative vessel volume and JCM sterilization default with explicit stage scope. Keep gas VARIABLE placeholders truthful; do not turn atmosphere ratios into dissolved concentrations.

### f4: Correct scoped trace-stock supplied-form mappings

major / open / confirmed; issue key: culturemech-007891-trace-hydrates.

M180 trace composition[4] and [5] explicitly name cobalt and nickel hexahydrates, but their primary terms assert anhydrous CHEBI:35696 and CHEBI:34887. Fresh OLS objects distinguish these from hexahydrates CHEBI:53503 and CHEBI:53542. Correct the exact scoped primary slots with evidence, without changing any retained mass or importing parent quantities.

### f5: Refine classification and stock names

minor / open / confirmed; issue key: culturemech-007891-classification-placeholders.

The exact recipe contains specified salts, vitamins and stearic acid; COMPLEX/UNDEFINED is a default classification needing source-based refinement, while LIQUID is compatible. Replace the nine selected Unknown solution names from their existing preferred terms. The scoped M180 iron/trace, M431 Se/W and M401 B12 placeholder names also need identity-only correction; no formulation change follows from renaming.

## Recommended Actions And Acceptance Checks

### a1

The maintained M1354 owner and generated target combine 1 L basal water with 10 mL stearic-stock water as 11 g/L; resazurin 0.5 mg becomes 0.5 g/L. All nine liquid solution doses are G_PER_L, and stearic acid plus its 2 N NaOH reagent are flattened into the recipient. Restore each source batch/stock and exact unit, preserve the explicit late-addition per-liter basis, and leave other final-volume rates unresolved rather than substituting provider 1052 mL metadata.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Resolve M180 iron/trace, M190 vitamins, M431 selenite-tungstate and M401 B12 only. M180/M190 already preserve authenticated batch inputs and nested HCl; keep those repairs. M431 still flattens 6 mg selenium and 8 mg tungstate as 6 and 8 g/L, and M401 B12 carries 5 g/L for a 5 mg stock input. Keep their parent formulations and receiving doses outside this review; stock water is input, not measured final volume.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Neither selected document carries the main boil/cool and 4:1 N2/CO2 handling, late sterile additions, or separate stearic-stock heating/redissolution procedure. Restore source-specific preparation, the illustrative vessel volume and JCM sterilization default with explicit stage scope. Keep gas VARIABLE placeholders truthful; do not turn atmosphere ratios into dissolved concentrations.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

M180 trace composition[4] and [5] explicitly name cobalt and nickel hexahydrates, but their primary terms assert anhydrous CHEBI:35696 and CHEBI:34887. Fresh OLS objects distinguish these from hexahydrates CHEBI:53503 and CHEBI:53542. Correct the exact scoped primary slots with evidence, without changing any retained mass or importing parent quantities.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The exact recipe contains specified salts, vitamins and stearic acid; COMPLEX/UNDEFINED is a default classification needing source-based refinement, while LIQUID is compatible. Replace the nine selected Unknown solution names from their existing preferred terms. The scoped M180 iron/trace, M431 Se/W and M401 B12 placeholder names also need identity-only correction; no formulation change follows from renaming.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm1258 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258; REVIEW_WORK/batch074/source07-08-10/jcm1258.json; exact original raw/text/hash/time metadata | context_only | Exact selected JCM1258 source; stock sections and their receiving doses remain distinct. |
| apiJ1258 | https://mediadive.dsmz.de/rest/medium/J1258; REVIEW_WORK/batch074/source07-08-10/apiJ1258.json; exact original raw/text/hash/time metadata | context_only | Provider comparison for selected JCM1258; current bytes only. |
| currentTogo1354 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354; REVIEW_WORK/batch074/source07-08-10/currentTogo1354.json; exact original raw/text/hash/time metadata | context_only | Full selected TOGO M1354 source |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; REVIEW_WORK/batch074/source07-08-10-shared/jcm187.json; exact original raw/text/hash/time metadata | context_only | JCM187 iron and trace stocks only; parent medium excluded. |
| currentTogo180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; REVIEW_WORK/batch074/source07-08-10-shared/currentTogo180.json; exact original raw/text/hash/time metadata | context_only | Exact M180 current iron/trace subsections; parent receiving doses excluded. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; REVIEW_WORK/batch074/source07-08-10-shared/jcm197.json; exact original raw/text/hash/time metadata | context_only | JCM197 trace-vitamin stock only; basal parent medium excluded. |
| currentTogo190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; REVIEW_WORK/batch074/source07-08-10-shared/currentTogo190.json; exact original raw/text/hash/time metadata | context_only | Exact M190 trace-vitamin subsection; parent receiving doses excluded. |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; REVIEW_WORK/batch074/source07-08-10-shared/jcm431.json; exact original raw/text/hash/time metadata | context_only | JCM431 selenite-tungstate stock only; parent basal medium and other stock sections excluded. |
| currentTogo431 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431; REVIEW_WORK/batch074/source07-08-10-shared/currentTogo431.json; exact original raw/text/hash/time metadata | context_only | Exact M431 selenite-tungstate subsection only; no parent formulation transfer. |
| jcm403 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403; REVIEW_WORK/batch074/source07-08-10/jcm403.json; exact original raw/text/hash/time metadata | context_only | VitaminB12 stock subsection only for selected1258 reference; parent formulation and receiving doses excluded. |
| currentTogo401 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401; REVIEW_WORK/batch074/source07-08-10/currentTogo401.json; exact original raw/text/hash/time metadata | context_only | VitaminB12 stock subsection only; parent formulation, other stocks and receiving doses excluded |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch074/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch074/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-21 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_oleovorans_medium__e2b50742.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-32 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-33 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-34 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-35 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-36 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-37 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-38 | reports/yaml_record_review/20260921T083439Z-ACETOBACTERIUM_SUBMARINUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-39 | reports/yaml_record_review/20260921T131114Z-anoxic_medium_for_strain_acbe2_1.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-40 | reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-41 | reports/yaml_record_review/20260921T231153Z-bn3_medium__59600ad0.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-42 | reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| dependency-M180 | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; solutions[0/1] composition and nested HCl | context_only | Only iron/trace-stock composition, retained batch notes and nested HCl reagent; parent-medium quantities and receiving doses are excluded. Full history is provenance only. |
| dependency-M431 | data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml; ingredients[27:30], solutions[1] excluding concentration | context_only | Only selenite-tungstate composition identity and its empty descriptor; basal medium, other trace stocks, shared collapsed water and parent receiving doses are excluded. |
| dependency-M190 | data/normalized_yaml/bacterial/togo_medium_m190.yaml; solutions[1].composition | context_only | Trace-vitamin composition and retained batch notes only; all parent receiving doses, mineral stock and parent procedure excluded. |
| dependency-M401 | data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml; ingredients[25], solutions[3] identity | context_only | Only the vitamin B12 stock; other vitamin stocks, parent medium, shared collapsed water and receiving dose excluded. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _local_batch_volume_ml, _extract_primary_components, _parse_unit, _extract_preparation_steps | context_only | Current _extract_primary_components separates primary and named stock sections; _parse_unit maps mL to ML_PER_L, L to L and mg to MG_PER_L. This improves the old flattened representation but bare batch units still do not establish final-volume concentration. _extract_preparation_steps retains comments without stage containers. No historical execution is inferred. |
| writer-stock-repair | scripts/repair_jcm_stock_preparations.py; Source guards and repair construction for M180/M190 | context_only | Current source-pinned stock repair preserves batch water and notes, exact snippets and nested HCl instead of inventing final concentrations. Current repaired M180/M190 values are credited independently from this code. |
| historical-reading | REVIEW_WORK/batch074/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch074/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch074/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch074/record07/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch074/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch074/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch074/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch074/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch074/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch074/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch074/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch074/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; REVIEW_WORK/batch074/source07-08-10/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; REVIEW_WORK/batch074/source07-08-10/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi28842 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28842; REVIEW_WORK/batch074/source07-08-10/chebi28842.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; REVIEW_WORK/batch074/source07-08-10/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch074/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch074/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch074/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; REVIEW_WORK/batch074/source07-08-10/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch074/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch074/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch074/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; REVIEW_WORK/batch074/source07-08-10/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; REVIEW_WORK/batch074/source07-08-10/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; REVIEW_WORK/batch074/source07-08-10/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch074/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch074/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch074/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; REVIEW_WORK/batch074/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch074/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; REVIEW_WORK/batch074/source07-08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch074/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; REVIEW_WORK/batch074/source07-08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch074/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; REVIEW_WORK/batch074/source07-08-10/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch074/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch074/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch074/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch074/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch074/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch074/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch074/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch074/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch074/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch074/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch074/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The original JCM spells the receiving stearic addition “Steric solution”; its immediately defined Stearic solution and exact TOGO subsection support the bounded crosswalk. The source does not explicitly measure the final recipient or stearic-stock volume. No unrelated DSM/KOMODO variant is transferred.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T182350Z-culturemech-007891-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Desulfobacterium Oleovorans Medium'
started_at: '2026-10-28T18:07:11.030364Z'
finished_at: '2026-10-28T18:23:50.049696Z'
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
summary: The exact M1354/JCM1258 identity is supported, but the selected target and
  maintained owner retain mixed water stages, wrong amount units, flattened stock
  inputs and missing preparation. Scoped M180/M190 repairs are credited; remaining
  M431/M401 amounts and M180 hydrate mappings require bounded curation.
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
  - path: data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml
    sha256: bc55603d29704f490a43b75b4576ac7486d7d469208962abaf63459af8def258
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
    sha256: cc012c3686848e4979d3c9d5a7859b5690955dae9fd2da1ce8ea0838f0f023da
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.md
    sha256: 623e08d6e5c29b939fa513d47a08ad4bf8cef66ad757c24d3faa5de57fa9986f
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_oleovorans_medium__e2b50742.md
    sha256: 480135a744650c9e9b3c742b135cc121e2004c2b508a6d7b002f8167014ccdd9
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.md
    sha256: d8db036db131c011ddd568b689234d9e7c238640df2cda6784c56dd579ffc11e
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
  selection: Authoritative batch074 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007891
targets:
- target_id: CultureMech:007891
  path: data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml
  label: desulfobacterium_oleovorans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
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
  - CultureMech:007891
  command: just validate-schema data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml
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
  - CultureMech:007891
  command: just validate-strict data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml
    --out REVIEW_WORK/batch074/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:007891
  command: just validate-terms data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml
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
  - CultureMech:007891
  command: just validate-references data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm1258
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258
  accessed_at: '2026-10-28T18:07:07.808577Z'
  locator: REVIEW_WORK/batch074/source07-08-10/jcm1258.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected JCM1258 source; stock sections and their receiving doses
    remain distinct.
  snapshot_sha256: da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a
- evidence_id: apiJ1258
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1258
  accessed_at: '2026-10-28T18:07:08.248619Z'
  locator: REVIEW_WORK/batch074/source07-08-10/apiJ1258.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Provider comparison for selected JCM1258; current bytes only.
  snapshot_sha256: 3058ea6f1017c2fada748909e8077f0efc4dee4a5aed8d9a2a5af462af9e47c7
- evidence_id: currentTogo1354
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354
  accessed_at: '2026-10-28T18:07:09.262275Z'
  locator: REVIEW_WORK/batch074/source07-08-10/currentTogo1354.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Full selected TOGO M1354 source
  snapshot_sha256: e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b
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
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  accessed_at: '2026-10-28T18:10:04.175069Z'
  locator: REVIEW_WORK/batch074/source07-08-10-shared/jcm431.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: JCM431 selenite-tungstate stock only; parent basal medium and other stock
    sections excluded.
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: currentTogo431
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431
  accessed_at: '2026-10-28T18:10:04.432722Z'
  locator: REVIEW_WORK/batch074/source07-08-10-shared/currentTogo431.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact M431 selenite-tungstate subsection only; no parent formulation transfer.
  snapshot_sha256: e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570
- evidence_id: jcm403
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403
  accessed_at: '2026-10-28T18:07:08.803574Z'
  locator: REVIEW_WORK/batch074/source07-08-10/jcm403.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: VitaminB12 stock subsection only for selected1258 reference; parent formulation
    and receiving doses excluded.
  snapshot_sha256: b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61
- evidence_id: currentTogo401
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401
  accessed_at: '2026-10-28T18:07:09.242182Z'
  locator: REVIEW_WORK/batch074/source07-08-10/currentTogo401.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: VitaminB12 stock subsection only; parent formulation, other stocks and
    receiving doses excluded
  snapshot_sha256: 380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1
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
  reference: data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T18:16:08.436433Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: bc55603d29704f490a43b75b4576ac7486d7d469208962abaf63459af8def258
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T18:16:08.436565Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: cc012c3686848e4979d3c9d5a7859b5690955dae9fd2da1ce8ea0838f0f023da
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T18:16:08.436590Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T18:16:08.436879Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T18:16:08.436902Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T18:16:08.436922Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T18:16:08.436945Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437334Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437369Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437401Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 56c93a375dbd090f5c559648722a46359964a01d1b6b9ab3225281a08d8d2b40
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437424Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: fe4feab50de92089379d903e0b47e6e7a2e92dc6f4822f4f7a81297f177c8dc4
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437446Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 623e08d6e5c29b939fa513d47a08ad4bf8cef66ad757c24d3faa5de57fa9986f
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFUROCOCCUS_AMYLOLYTICUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437471Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 432876a053b21f5ac650332fd411f8fb3ee09f57f3321f215d1d174ade488f46
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437491Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 621b5623818337fb8c650369b29975144ef31d41449a02885ea8ec7652da9d63
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437511Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 089a797d0ea2b3ddc0a978f5aae488e26d54b8124a1aafcc992cf6032108cc49
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_oleovorans_medium__e2b50742.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437531Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 480135a744650c9e9b3c742b135cc121e2004c2b508a6d7b002f8167014ccdd9
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfurococcus_amylolyticus_medium__88cf0911.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437551Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 7ba8b4c2ac4a371fab0ad69230c1b53376bdcb648cfa0cea53896e1c59ebcdae
- evidence_id: report-32
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437571Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
- evidence_id: report-33
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437592Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
- evidence_id: report-34
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437613Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d8db036db131c011ddd568b689234d9e7c238640df2cda6784c56dd579ffc11e
- evidence_id: report-35
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437633Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 59f87cd1f3b048e72411c775bb1c80c7bea3287c1c0ba712a3bcfe5c84d18abe
- evidence_id: report-36
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437656Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
- evidence_id: report-37
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437677Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
- evidence_id: report-38
  kind: prior_review
  reference: reports/yaml_record_review/20260921T083439Z-ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437701Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1f5db491b2f11f287acd60655a5b0b44466da08a39cbd2a57fb467bf31ea2610
- evidence_id: report-39
  kind: prior_review
  reference: reports/yaml_record_review/20260921T131114Z-anoxic_medium_for_strain_acbe2_1.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437722Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 84e487ca27d245977a3572b823e5d447a44bbb8daa8a8715e49b7084e880b07c
- evidence_id: report-40
  kind: prior_review
  reference: reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437743Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f7b264f4b7f3aa84c40ec049d8d89f48d67f8bd0cb7f723e250de0ecdc068b0a
- evidence_id: report-41
  kind: prior_review
  reference: reports/yaml_record_review/20260921T231153Z-bn3_medium__59600ad0.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437764Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 9c4941a859f60a9fc2adc04147052815d6fcf04f9e0453326d98a5732260de19
- evidence_id: report-42
  kind: prior_review
  reference: reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md
  locator: Complete report
  accessed_at: '2026-10-28T18:16:08.437785Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 6497a50f712e4169a8f7a7cf4ae62d97e909b6695d86b7c522679b8f08909d7f
- evidence_id: dependency-M180
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: solutions[0/1] composition and nested HCl
  accessed_at: '2026-10-28T18:16:08.461447Z'
  support: context_only
  summary: Only iron/trace-stock composition, retained batch notes and nested HCl
    reagent; parent-medium quantities and receiving doses are excluded. Full history
    is provenance only.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: dependency-M431
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
  locator: ingredients[27:30], solutions[1] excluding concentration
  accessed_at: '2026-10-28T18:16:08.471537Z'
  support: context_only
  summary: Only selenite-tungstate composition identity and its empty descriptor;
    basal medium, other trace stocks, shared collapsed water and parent receiving
    doses are excluded.
  snapshot_sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
- evidence_id: dependency-M190
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: solutions[1].composition
  accessed_at: '2026-10-28T18:16:08.490379Z'
  support: context_only
  summary: Trace-vitamin composition and retained batch notes only; all parent receiving
    doses, mineral stock and parent procedure excluded.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: dependency-M401
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
  locator: ingredients[25], solutions[3] identity
  accessed_at: '2026-10-28T18:16:08.499795Z'
  support: context_only
  summary: Only the vitamin B12 stock; other vitamin stocks, parent medium, shared
    collapsed water and receiving dose excluded.
  snapshot_sha256: 16bfd52c74b4968fb71d19de9eeec863417b8f1e5711a8e1413b7b0917cae25c
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _local_batch_volume_ml, _extract_primary_components,
    _parse_unit, _extract_preparation_steps
  accessed_at: '2026-10-28T18:16:08.500581Z'
  support: context_only
  summary: Current _extract_primary_components separates primary and named stock sections;
    _parse_unit maps mL to ML_PER_L, L to L and mg to MG_PER_L. This improves the
    old flattened representation but bare batch units still do not establish final-volume
    concentration. _extract_preparation_steps retains comments without stage containers.
    No historical execution is inferred.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-stock-repair
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: Source guards and repair construction for M180/M190
  accessed_at: '2026-10-28T18:16:08.500629Z'
  support: context_only
  summary: Current source-pinned stock repair preserves batch water and notes, exact
    snippets and nested HCl instead of inventing final concentrations. Current repaired
    M180/M190 values are credited independently from this code.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/historical-reading.json
  accessed_at: '2026-10-28T18:16:08.510872Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 9da6319cc2a35bfc65f2a8d5fafe30f40e521c24eb25673fce739f9c28ca2511
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T18:16:08.511012Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: cf3cd596f441d9dc9343617a2c2ac9f5ba96354689c9304d1557ed78e3a00bc0
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/complete-document-reader.json
  accessed_at: '2026-10-28T18:16:08.511359Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: cc8b800f22122324897daa307bdb740d687fe44dfacaab1116877fa4d0464ebc
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T18:16:08.511489Z'
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
  accessed_at: '2026-10-28T18:16:08.511532Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch074/record07/historical-current-object-joins.json
  accessed_at: '2026-10-28T18:16:08.511559Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 8434a7fb83c370cd91ba9b1ebef82e326f8435978358d7b9e61488eecc2072ad
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
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  accessed_at: '2026-10-28T18:07:10.047410Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi16526.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  accessed_at: '2026-10-28T18:07:11.190254Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi28842
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28842
  accessed_at: '2026-10-28T18:07:11.811885Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi28842.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c2c69104163eaff591a32524b3f0e21670c6aba647560b70577c06dda9b986e5
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
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  accessed_at: '2026-10-28T18:07:09.344241Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi131361.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  accessed_at: '2026-10-28T18:07:14.868848Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi63939.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  accessed_at: '2026-10-28T18:07:12.970370Z'
  locator: REVIEW_WORK/batch074/source07-08-10/chebi32145.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
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
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:23:50.049379Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: cdba75e12caf49b889f8b3237ba903ad81eb86c191bd3f75b13280b5d990bc12
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:16:08.624070Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: e5b66f75fa1d72a9a80907f885ba6a98cc933f8b7e79b7c13b6437764342fd42
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:16:08.624187Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 0f3913cf13343c7ce9360ccf8e116a9341697656ff2cd3fe0e32a15bddbbe0b0
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:16:08.624358Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 73f87610d827144fbed68bc8f9a3fb18318069a07bb4f21204511a2490cdf567
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:16:08.624505Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 2f85ff792d00f7df850251ab433bbbb4bce9c9809869e527344ba6f165168800
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:16:08.624543Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 07bd568d6e61b2865658448657a8a56da090d78ab65865258956baedf7276a2d
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch074/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T18:16:08.624566Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 0c20d32d7b2476a22017f78bbf4927d8124c9d0f96883902de433ab7dfbb7db5
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch074/record07/schema-result.json
  accessed_at: '2026-10-28T18:07:12.063595Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 5d064737fbf1c70a10d016404821b57703a4cbbf49918a176f387c9847b397f0
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch074/record07/strict-result.json
  accessed_at: '2026-10-28T18:07:12.983306Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 3d10605607203fb3f43831c4c741f49425fa055f51026b493d4363ca9653a63b
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch074/record07/terms-result.json
  accessed_at: '2026-10-28T18:07:13.985196Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: d169c683f0ef1a2e47284f80acfaac7eab074692e83d08f3b5b755410e9603b8
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch074/record07/references-result.json
  accessed_at: '2026-10-28T18:07:14.692083Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: c10ff00b539f87bb397bc4b3d30a9037a72b49d8dbfedcf49151695c0bc3a613
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and dependency identity
  outcome: supported
  summary: Selected TOGO M1354 is JCM1258. The lower-case duplicate report refers
    to another generated comparison and its KOMODO/DSM owners, not additional current
    owners here. Only named JCM187/197/431/403 subsections transfer.
  target_ids:
  - CultureMech:007891
  evidence_ids:
  - target
  - owner
  - jcm1258
  - currentTogo1354
  - historical-reading
- assessment_id: classification
  area: consistency
  topic: Classification and nonquantitative assertions
  outcome: concern
  summary: LIQUID is compatible and no target-organism claim is present. COMPLEX/UNDEFINED
    is not supported by the specified formulation; generic applications do not establish
    strain growth. Source stock names and gas descriptions remain meaningful, while
    Unknown solution names are placeholders.
  target_ids:
  - CultureMech:007891
  evidence_ids:
  - target
  - owner
  - jcm1258
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 51 current concentration fields are covered by 54 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:007891
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b074-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","quantity_field_count":51,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"11.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"11.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    current 11 g/L combines 1 L basal input and 10 mL stearic-stock water as naked
    numbers. Preserve both stage-specific input volumes; do not sum incompatible units
    or claim final volume.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                        </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the current g/L assertion has no explicit
    final-volume basis. The main table lists 1 L input water and later additions;
    provider J1258 uses its separate 1052 mL normalization, not the local unchanged
    number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.25","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the current g/L assertion has no explicit
    final-volume basis. The main table lists 1 L input water and later additions;
    provider J1258 uses its separate 1052 mL normalization, not the local unchanged
    number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.25&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the current g/L assertion has no explicit
    final-volume basis. The main table lists 1 L input water and later additions;
    provider J1258 uses its separate 1052 mL normalization, not the local unchanged
    number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.25","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the current g/L assertion has no explicit
    final-volume basis. The main table lists 1 L input water and later additions;
    provider J1258 uses its separate 1052 mL normalization, not the local unchanged
    number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.25,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\":
    \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.25&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies 0.5 mg resazurin, whereas the local value is 0.5 g/L. Preserve
    the source mass and receiving stage; no measured final volume is established.","source_stage":"basal
    batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 0.5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\":
    \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"3.4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"3.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the current g/L assertion has no explicit
    final-volume basis. The main table lists 1 L input water and later additions;
    provider J1258 uses its separate 1052 mL normalization, not the local unchanged
    number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 3.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.4&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the current g/L assertion has no explicit
    final-volume basis. The main table lists 1 L input water and later additions;
    provider J1258 uses its separate 1052 mL normalization, not the local unchanged
    number.","source_stage":"basal batch; stearic water separate","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"Na2SO4\",\n          \"volume\": 4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\":
    \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;4.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Carbon
    dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves dissolved amount unquantified. Source gas atmospheres and stock
    versus basal placement must be recorded separately; no gas concentration is derived.","source_stage":"basal
    atmosphere or stearic-stock atmosphere","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Nitrogen gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves dissolved amount unquantified. Source gas atmospheres and stock
    versus basal placement must be recorded separately; no gas concentration is derived.","source_stage":"basal
    atmosphere or stearic-stock atmosphere","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves dissolved amount unquantified. Source gas atmospheres and stock
    versus basal placement must be recorded separately; no gas concentration is derived.","source_stage":"basal
    atmosphere or stearic-stock atmosphere","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"Heat the solution in a closed vial under a N2 atmosphere
    in a boiling water bath. Shake until stearic acid is dissolved and autoclave.
    Add the solution to the medium while stearic acid is dissolved. Re-melt if stearic
    acid is solidified.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Stearic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.36","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.36","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    0.36 g is a stearic-stock batch mass, not a direct receiving-medium g/L value.
    Preserve the stock and its 10 mL receiving addition separately.","source_stage":"stearic
    stock","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"Stearic acid\",\n          \"volume\": 0.36,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002068\",\n          \"gmo_id\": \"GMO_002068\",\n          \"label\":
    \"Stearic acid\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Stearic acid                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.36&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"FeCl2
    solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The basal input or nested-stock
    batch dose is not an established dose per final liter. Resolve only the named
    subsection, retaining the source spelling and exact reference identity.","source_stage":"basal
    receiving batch","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Trace
    element solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The basal input or nested-stock
    batch dose is not an established dose per final liter. Resolve only the named
    subsection, retaining the source spelling and exact reference identity.","source_stage":"basal
    receiving batch","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Selenite--tungstate
    solution (see Medium [M431])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The basal input or nested-stock
    batch dose is not an established dose per final liter. Resolve only the named
    subsection, retaining the source spelling and exact reference identity.","source_stage":"basal
    receiving batch","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M431\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Selenite-tungstate solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=431\">431</a>)      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"8%
    NaHCO3 solution**","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The post-cooling table
    explicitly says per liter; retain its receiving-dose basis without declaring a
    measured total volume. The percentage label has no stated w/w, w/v or v/v basis;
    do not infer mass.","source_stage":"post-cooling receiving dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"8% NaHCO3 solution**\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"conc_value\":
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
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution**                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q17","label":"5% Na2S・9H2O solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The post-cooling table
    explicitly says per liter; retain its receiving-dose basis without declaring a
    measured total volume. The percentage label has no stated w/w, w/v or v/v basis;
    do not infer mass.","source_stage":"post-cooling receiving dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"5% Na2S・9H2O solution\",\n          \"volume\": 8,\n          \"unit\": \"ml\",\n          \"conc_value\":
    5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\":
    \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\":
    \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution                       </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q18","label":"Trace vitamins (see Medium [M190])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The post-cooling table
    explicitly says per liter; retain its receiving-dose basis without declaring a
    measured total volume. Resolve only the named subsection, retaining the source
    spelling and exact reference identity.","source_stage":"post-cooling receiving
    dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace vitamins* (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\">197</a>)                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"Vitamin B12 solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The post-cooling table
    explicitly says per liter; retain its receiving-dose basis without declaring a
    measured total volume. Resolve only the named subsection, retaining the source
    spelling and exact reference identity.","source_stage":"post-cooling receiving
    dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"Vitamin B12 solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>12</sub>
    solution* (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\">403</a>)         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q20","label":"Stearic solution (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The post-cooling table
    explicitly says per liter; retain its receiving-dose basis without declaring a
    measured total volume. Resolve only the named subsection, retaining the source
    spelling and exact reference identity.","source_stage":"post-cooling receiving
    dose per liter","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"Stearic solution (see below)\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M1354\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> Steric solution (see below)                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q21","label":"2 N NaOH solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml","field_path":"solutions[8].concentration","stored":{"value":"0.63","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml","field_path":"solutions[8].concentration","stored":{"value":"0.63","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source amount is a liquid addition, not grams per liter. The basal input or nested-stock
    batch dose is not an established dose per final liter. The 0.63 mL of 2 N NaOH
    belongs inside the stearic stock; normality is not silently converted to molarity.","source_stage":"stearic-stock
    internal reagent","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"2 N NaOH solution\",\n          \"volume\": 0.63,\n          \"unit\": \"ml\",\n          \"conc_value\":
    2,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\":
    \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> 2 N NaOH solution                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.63&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Basal
    handling and late additions","local_fields":[],"decision":"evidence_only","rationale":"Record
    the exact stage-specific source procedure, including the explicit atmosphere and
    illustrative vessel volume. The general JCM sterilization default is distinct
    from stock-specific handling; no culture growth claim is inferred.","source_stage":"source-only
    preparation","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix components thoroughly, bring to a boil and cool down
    under a N2-CO2 (4:1, v/v) gas mixture. Distribute the medium into culture vessels
    (e.g., 10 ml in Balch tubes) under the same gas mixture, seal with butyl rubber
    stoppers and autoclave. After cooling, aseptically and anaerobically add per liter
    the following solutions (autoclaved or *filter-sterilized and stored under a N2
    gas atmosphere; **filter-sterilized and stored under an 80% N2-20% CO2 gas mixture):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q23","label":"Stearic-stock heat, atmosphere and redissolution","local_fields":[],"decision":"evidence_only","rationale":"Record
    the exact stearic-stock heating, nitrogen atmosphere, autoclaving and redissolution
    procedure in its own stock scope. The 10 mL Balch-tube example belongs to the
    main-medium procedure, not this stock. No culture growth claim is inferred.","source_stage":"source-only
    preparation","sources":[{"evidence_id":"currentTogo1354","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1354","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo1354.raw","raw_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","text_sha256":"e7eb9358ee1770f5e59262d91bcaf41cab8e5941b1f3721c3bda362ffd7d120b","accessed_at":"2026-10-28T18:07:09.262275Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"Heat the solution in a closed vial under a N2 atmosphere
    in a boiling water bath. Shake until stearic acid is dissolved and autoclave.
    Add the solution to the medium while stearic acid is dissolved. Re-melt if stearic
    acid is solidified.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"JCM
    default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The
    primary page supplies 121 C for 15 min unless otherwise stated. This is source
    procedure context, not an organism growth assertion.","source_stage":"source-only
    default","sources":[{"evidence_id":"jcm1258","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1258","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm1258.raw","raw_sha256":"da0932b44927a095038265e68e385d0e32da3196eafe74afcd616e5df578a26a","text_sha256":"ed40709d1b1608265520a69d25263f0050ce93d9d65a1969386657ed8734e4bb","accessed_at":"2026-10-28T18:07:07.808577Z","locator":"jcm1258.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"Retained
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Retained
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Retained
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Retained
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Retained
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Retained
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Scoped
    M431 Na2SeO3・5H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source lists 6 mg in the selenite-tungstate stock with 1 L input water. The stored
    g/L copies a milligram number and loses stock stage. Do not transfer the parent
    medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Scoped
    M431 Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source lists 8 mg in the selenite-tungstate stock with 1 L input water. The stored
    g/L copies a milligram number and loses stock stage. Do not transfer the parent
    medium dose or collapsed shared water.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Scoped
    M431 NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source lists 0.4 g NaOH in the selenite-tungstate stock with 1 L input water,
    and current APIJ1258 solution4172 explicitly supplies g_l=0.4 on its declared
    stock basis. Credit that provider stock-rate support; the current M431 direct
    main-medium g/L placement is unsupported because this is a separate stock. The
    source water alone does not independently measure final stock volume, and no parent
    receiving dose is transferred.","source_stage":"selenite-tungstate stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\":
    \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\":
    \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q41","label":"Selenite stock water","local_fields":[],"decision":"evidence_only","rationale":"The
    source 1 L is stock input water, not the local collapsed water row and not measured
    final volume.","source_stage":"source-only selenite stock","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch074/publish-sources/togo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T18:10:04.432722Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    vitamin Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Existing
    exact attached source claim and digest authenticate this batch input. Retain the
    repaired water unit or mass note, without restoring unsupported g/L or importing
    the parent receiving dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Retained
    vitamin Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q44","label":"Retained vitamin p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q45","label":"Retained vitamin Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q46","label":"Retained vitamin Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q47","label":"Retained vitamin Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q48","label":"Retained vitamin Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q49","label":"Retained vitamin Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q50","label":"Retained vitamin Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q51","label":"Retained vitamin Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q52","label":"Retained vitamin Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Existing exact attached source
    claim and digest authenticate this batch input. Retain the repaired water unit
    or mass note, without restoring unsupported g/L or importing the parent receiving
    dose.","source_stage":"M190 vitamin stock only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch074/publish-sources/togo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T18:10:04.334776Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q53","label":"M401 B12 stock mass","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary B12 stock lists 5 mg in 100 mL input water. Current 5 g/L both misreads
    the mass unit and lacks supported stock-volume normalization. Preserve 5 mg, not
    an inferred final-medium contribution.","source_stage":"B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T18:07:09.242182Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T18:07:08.803574Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"B12
    stock water","local_fields":[],"decision":"evidence_only","rationale":"100 mL
    is stock input water; the shared parent collapsed water is excluded and is not
    a final-stock-volume measurement.","source_stage":"source-only B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch074/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T18:07:09.242182Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch074/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T18:07:08.803574Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOBACTERIUM_OLEOVORANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].composition","solutions[0].solutions","solutions[1].composition"],"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml":["ingredients[27]","ingredients[28]","ingredients[29]","solutions[1].name","solutions[1].preferred_term","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].composition","solutions[1].preferred_term"],"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml":["ingredients[25]","solutions[3].name","solutions[3].preferred_term","solutions[3].composition"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every in-scope primary/secondary slot and preferred-name MIM lookup is
    enumerated against the exact packaged snapshot and fresh OLS. Scoped cobalt/nickel
    hexahydrate mismatches are confirmed. Other supplied salt hydrates are compatible;
    generic calcium pantothenate and vitamin B12 do not establish stereochemistry
    or a specific vitamer. Canonical label agreement is separate from chemical-form
    support; current linkage coverage and its denominator are recorded per document.
  target_ids:
  - CultureMech:007891
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All 21 exact reports are read through lossless current line-cell reconstruction,
    with previously personally read identical cells reused by an explicit proof and
    48 new cells read now. Both selected stock-repair plan rows exactly match previously
    read originals. Historical baseline and source-aware reports are derivative, not
    newly run checks. Current M180/M190 exact raw digest and snippets authenticate
    the retained batch repairs, including the scoped root HCl excerpt, without recovering
    old access events. Current importer/merge code is more conservative than the legacy
    flattening and duplicate-water history; no old execution is attributed from current
    code alone.
  target_ids:
  - CultureMech:007891
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-007891-stage-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore basal and stock stages before concentration curation
  description: The maintained M1354 owner and generated target combine 1 L basal water
    with 10 mL stearic-stock water as 11 g/L; resazurin 0.5 mg becomes 0.5 g/L. All
    nine liquid solution doses are G_PER_L, and stearic acid plus its 2 N NaOH reagent
    are flattened into the recipient. Restore each source batch/stock and exact unit,
    preserve the explicit late-addition per-liter basis, and leave other final-volume
    rates unresolved rather than substituting provider 1052 mL metadata.
  target_ids:
  - CultureMech:007891
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - jcm1258
  - currentTogo1354
  - apiJ1258
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-007891-stock-references
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve exactly named stock subsections and retain existing repairs
  description: Resolve M180 iron/trace, M190 vitamins, M431 selenite-tungstate and
    M401 B12 only. M180/M190 already preserve authenticated batch inputs and nested
    HCl; keep those repairs. M431 still flattens 6 mg selenium and 8 mg tungstate
    as 6 and 8 g/L, and M401 B12 carries 5 g/L for a 5 mg stock input. Keep their
    parent formulations and receiving doses outside this review; stock water is input,
    not measured final volume.
  target_ids:
  - CultureMech:007891
  field_paths:
  - solutions
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[27].concentration
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[28].concentration
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[29].concentration
  - data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml::ingredients[25].concentration
  evidence_ids:
  - jcm187
  - jcm197
  - jcm431
  - jcm403
  - quantities
  - old-claims
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
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
  issue_key: culturemech-007891-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Restore source preparation with exact stage boundaries
  description: Neither selected document carries the main boil/cool and 4:1 N2/CO2
    handling, late sterile additions, or separate stearic-stock heating/redissolution
    procedure. Restore source-specific preparation, the illustrative vessel volume
    and JCM sterilization default with explicit stage scope. Keep gas VARIABLE placeholders
    truthful; do not turn atmosphere ratios into dissolved concentrations.
  target_ids:
  - CultureMech:007891
  field_paths:
  - preparation_steps
  - sterilization
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[11].concentration
  evidence_ids:
  - jcm1258
  - currentTogo1354
  - quantities
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-007891-trace-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct scoped trace-stock supplied-form mappings
  description: M180 trace composition[4] and [5] explicitly name cobalt and nickel
    hexahydrates, but their primary terms assert anhydrous CHEBI:35696 and CHEBI:34887.
    Fresh OLS objects distinguish these from hexahydrates CHEBI:53503 and CHEBI:53542.
    Correct the exact scoped primary slots with evidence, without changing any retained
    mass or importing parent quantities.
  target_ids:
  - CultureMech:007891
  field_paths:
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[5].term
  evidence_ids:
  - jcm187
  - currentTogo180
  - chebi35696
  - chebi34887
  - chebi53503
  - chebi53542
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
- finding_id: f5
  issue_key: culturemech-007891-classification-placeholders
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Refine classification and stock names
  description: The exact recipe contains specified salts, vitamins and stearic acid;
    COMPLEX/UNDEFINED is a default classification needing source-based refinement,
    while LIQUID is compatible. Replace the nine selected Unknown solution names from
    their existing preferred terms. The scoped M180 iron/trace, M431 Se/W and M401
    B12 placeholder names also need identity-only correction; no formulation change
    follows from renaming.
  target_ids:
  - CultureMech:007891
  field_paths:
  - medium_type
  - composition_type
  - solutions
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[0].name
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].name
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::solutions[1].name
  - data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml::solutions[3].name
  evidence_ids:
  - jcm1258
  - currentTogo1354
  - groundings
  rule_id: review-yaml-record/consistency
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: The maintained M1354 owner and generated target combine 1 L basal water
    with 10 mL stearic-stock water as 11 g/L; resazurin 0.5 mg becomes 0.5 g/L. All
    nine liquid solution doses are G_PER_L, and stearic acid plus its 2 N NaOH reagent
    are flattened into the recipient. Restore each source batch/stock and exact unit,
    preserve the explicit late-addition per-liter basis, and leave other final-volume
    rates unresolved rather than substituting provider 1052 mL metadata.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007891
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
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
  description: Resolve M180 iron/trace, M190 vitamins, M431 selenite-tungstate and
    M401 B12 only. M180/M190 already preserve authenticated batch inputs and nested
    HCl; keep those repairs. M431 still flattens 6 mg selenium and 8 mg tungstate
    as 6 and 8 g/L, and M401 B12 carries 5 g/L for a 5 mg stock input. Keep their
    parent formulations and receiving doses outside this review; stock water is input,
    not measured final volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007891
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
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
  description: Neither selected document carries the main boil/cool and 4:1 N2/CO2
    handling, late sterile additions, or separate stearic-stock heating/redissolution
    procedure. Restore source-specific preparation, the illustrative vessel volume
    and JCM sterilization default with explicit stage scope. Keep gas VARIABLE placeholders
    truthful; do not turn atmosphere ratios into dissolved concentrations.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007891
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
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
  description: M180 trace composition[4] and [5] explicitly name cobalt and nickel
    hexahydrates, but their primary terms assert anhydrous CHEBI:35696 and CHEBI:34887.
    Fresh OLS objects distinguish these from hexahydrates CHEBI:53503 and CHEBI:53542.
    Correct the exact scoped primary slots with evidence, without changing any retained
    mass or importing parent quantities.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:007891
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
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
  description: The exact recipe contains specified salts, vitamins and stearic acid;
    COMPLEX/UNDEFINED is a default classification needing source-based refinement,
    while LIQUID is compatible. Replace the nine selected Unknown solution names from
    their existing preferred terms. The scoped M180 iron/trace, M431 Se/W and M401
    B12 placeholder names also need identity-only correction; no formulation change
    follows from renaming.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:007891
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1354_Desulfobacterium_Oleovorans_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
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
limitations:
- The original JCM spells the receiving stearic addition “Steric solution”; its immediately
  defined Stearic solution and exact TOGO subsection support the bounded crosswalk.
  The source does not explicitly measure the final recipient or stearic-stock volume.
  No unrelated DSM/KOMODO variant is transferred.
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
