# Scientific review: Deferribacter Medium

- Review: 20261028T163814Z-culturemech-008235-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T16:12:06.991443Z
- Finished UTC: 2026-10-28T16:38:14.478229Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

NBRC882 identity is confirmed, but the record needs source-unit and stock-stage repair, correct local stock references, omitted preparation and supplied-form corrections. The owner water-sum repair and seven independently authenticated comparison-stock claims are credited. Same-name DSM935 and the linked MediaDive stocks remain separate formulations. All four original canonical checks passed; the full scoped review is complete with explicit denominator and stereochemistry limits.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch072 index 03
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008235 | data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml | generated | deferribacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:008235 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:008235 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:008235 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:008235 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact primary identity and stock boundary

identity: concern. Targets: CultureMech:008235.

TOGO M1677 and NBRC882 identity match. Same-label DSM935 is a distinct formulation and is not merged by assumption. The two linked MediaDive stocks are incompatible name matches, despite their own valid identities.

### Basic classification and scope

scope: concern. Targets: CultureMech:008235.

Bacterial liquid scope is consistent with the record; COMPLEX/UNDEFINED is unsupported by a complete formula of named chemical components. No organism or growth assertion is inferred.

### Unchanged values and retained claim support

evidence: concern. Targets: CultureMech:008235.

All selected and comparison fields are inventoried. Seven attached comparison-stock concentrations remain verified; their evidence is not transferred. Matching main batch digits alone do not validate G_PER_L, and VARIABLE gas placeholders do not imply known dissolved amounts.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:008235.

85 current concentration fields are covered by 52 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","quantity_field_count":85,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The primary separately supplies 1 L input water in main, trace and vitamin recipes. Generated 3.0 G_PER_L sums different batches and has the wrong dimension. The owner repairs that identical sum to 1.0 but retains the wrong G_PER_L dimension and collapsed scope; credit that limited repair. None of these water inputs states a measured final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 32 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 46 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Distilled water&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;L&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The primary separately supplies 1 L input water in main, trace and vitamin recipes. Generated 3.0 G_PER_L sums different batches and has the wrong dimension. The owner repairs that identical sum to 1.0 but retains the wrong G_PER_L dimension and collapsed scope; credit that limited repair. None of these water inputs states a measured final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The primary separately supplies 1 L input water in main, trace and vitamin recipes. Generated 3.0 G_PER_L sums different batches and has the wrong dimension. The owner repairs that identical sum to 1.0 but retains the wrong G_PER_L dimension and collapsed scope; credit that limited repair. None of these water inputs states a measured final volume."}]},{"quantity_id":"q2","label":"CaCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Stored 0.247 G_PER_L adds the main 0.147 g batch amount to the trace-stock 0.1 g batch amount. They belong to different solution stages and cannot be summed as a final-medium total. Retain each original mass and the 1 ml trace receiving dose; no final-volume denominator is established.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.147&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.147,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"conflict","rationale":"Stored 0.247 G_PER_L adds the main 0.147 g batch amount to the trace-stock 0.1 g batch amount. They belong to different solution stages and cannot be summed as a final-medium total. Retain each original mass and the 1 ml trace receiving dose; no final-volume denominator is established."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[1].concentration","decision":"conflict","rationale":"Stored 0.247 G_PER_L adds the main 0.147 g batch amount to the trace-stock 0.1 g batch amount. They belong to different solution stages and cannot be summed as a final-medium total. Retain each original mass and the 1 ml trace receiving dose; no final-volume denominator is established."}]},{"quantity_id":"q3","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.136","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.136","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The unchanged numeric 0.136 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.136&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.136,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.136 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.136 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.535","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.535","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The unchanged numeric 0.535 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;tr&gt;\n                            &lt;td colspan=\"2\" id=\"medium-comp\"&gt;&lt;table width='600' border='0'&gt;&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;NH&lt;sub&gt;4&lt;/sub&gt;Cl&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.535&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.535,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.535 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.535 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."}]},{"quantity_id":"q5","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source supplies 1 mg resazurin to the main batch, not the stored 1 G_PER_L. Preserve the literal mass and unresolved final-volume basis. The source says resazurin without a sodium qualifier, so neutral CHEBI:8806 is not shown to be the wrong supplied form.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Resazurin&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"conflict","rationale":"The source supplies 1 mg resazurin to the main batch, not the stored 1 G_PER_L. Preserve the literal mass and unresolved final-volume basis. The source says resazurin without a sodium qualifier, so neutral CHEBI:8806 is not shown to be the wrong supplied form."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[4].concentration","decision":"conflict","rationale":"The source supplies 1 mg resazurin to the main batch, not the stored 1 G_PER_L. Preserve the literal mass and unresolved final-volume basis. The source says resazurin without a sodium qualifier, so neutral CHEBI:8806 is not shown to be the wrong supplied form."}]},{"quantity_id":"q6","label":"MgCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.204","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.204","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The unchanged numeric 0.204 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.204&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"MgCl2·6H2O\",\n          \"volume\": 0.204,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.204 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.204 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."}]},{"quantity_id":"q7","label":"Na2S·9H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The unchanged numeric 0.5 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.5&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"Na2S·9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.5 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.5 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."}]},{"quantity_id":"q8","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.52","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.52","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The unchanged numeric 2.52 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;NaHCO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;2.52&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 2.52,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The unchanged numeric 2.52 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The unchanged numeric 2.52 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."}]},{"quantity_id":"q9","label":"Sodium acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.82","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.82","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The unchanged numeric 0.82 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Sodium acetate&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.82&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"Sodium acetate\",\n          \"volume\": 0.82,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\": \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.82 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.82 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."}]},{"quantity_id":"q10","label":"Sodium nitrate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.85","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.85","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The unchanged numeric 0.85 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Sodium nitrate&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.85&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Sodium nitrate\",\n          \"volume\": 0.85,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001049\",\n          \"gmo_id\": \"GMO_001049\",\n          \"label\": \"Sodium nitrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.85 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The unchanged numeric 0.85 matches the primary g batch mass, but neither NBRC nor TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator. Retain source mass as batch evidence; do not silently convert the 1 L solvent input into final volume."}]},{"quantity_id":"q11","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;Mix ingredients except for vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O, and autoclave under H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) condition. Separately autoclave Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O as a 5% solution under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O solution, and pressurize inoculated bottles to 150 kPa with H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O, and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to 150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration."}]},{"quantity_id":"q12","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;Mix ingredients except for vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O, and autoclave under H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) condition. Separately autoclave Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O as a 5% solution under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O solution, and pressurize inoculated bottles to 150 kPa with H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O, and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to 150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration."}]},{"quantity_id":"q13","label":"Hydrogen gas","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;Mix ingredients except for vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O, and autoclave under H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) condition. Separately autoclave Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O as a 5% solution under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O solution, and pressurize inoculated bottles to 150 kPa with H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[14]","quote":"{\n          \"component_name\": \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\": \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O, and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to 150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa bottle pressurization. Preserve the placeholder if retained, but add the exact preparation context rather than infer a numeric dissolved concentration."}]},{"quantity_id":"q14","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 28 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;NaCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The source 1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The source 1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q15","label":"Na2MoO4·2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.024 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.024&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Na2MoO4·2H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The source 0.024 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The source 0.024 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.01 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.01&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The source 0.01 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The source 0.01 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q17","label":"MnCl2·4H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;4H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"MnCl2·4H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The source 0.1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The source 0.1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q18","label":"CoCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.024 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage. The explicitly supplied hexahydrate also conflicts with the local anhydrous ontology assertion.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.024&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The source 0.024 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage. The explicitly supplied hexahydrate also conflicts with the local anhydrous ontology assertion."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The source 0.024 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage. The explicitly supplied hexahydrate also conflicts with the local anhydrous ontology assertion."}]},{"quantity_id":"q19","label":"NiCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.12","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.12 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage. The explicitly supplied hexahydrate also conflicts with the local anhydrous ontology assertion.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 29 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.12&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"NiCl2·6H2O\",\n          \"volume\": 0.12,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The source 0.12 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage. The explicitly supplied hexahydrate also conflicts with the local anhydrous ontology assertion."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The source 0.12 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage. The explicitly supplied hexahydrate also conflicts with the local anhydrous ontology assertion."}]},{"quantity_id":"q20","label":"CuCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.025 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;middot;2H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.025&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"CuCl2·2H2O\",\n          \"volume\": 0.025,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The source 0.025 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The source 0.025 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q21","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;ZnCl&lt;sub&gt;2&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.1&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The source 0.1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The source 0.1 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q22","label":"FeCl3·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1.35","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1.35","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 1.35 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;FeCl&lt;sub&gt;3&lt;/sub&gt;&amp;middot;6H&lt;sub&gt;2&lt;/sub&gt;O&lt;/td&gt;&lt;td width='20%' align='right'&gt;1.35&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"FeCl3·6H2O\",\n          \"volume\": 1.35,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001047\",\n          \"gmo_id\": \"GMO_001047\",\n          \"label\": \"Iron(III) chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The source 1.35 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The source 1.35 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q23","label":"Nitrilotriacetic acid (NTA)","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"12.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"12.8","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 12.8 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Nitrilotriacetic acid (NTA)&lt;/td&gt;&lt;td width='20%' align='right'&gt;12.8&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[11]","quote":"{\n          \"component_name\": \"Nitrilotriacetic acid (NTA)\",\n          \"volume\": 12.8,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The source 12.8 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The source 12.8 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q24","label":"Na2WO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.004 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 31 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.004&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[12]","quote":"{\n          \"component_name\": \"Na2WO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001086\",\n          \"gmo_id\": \"GMO_001086\",\n          \"label\": \"Sodium tungstate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The source 0.004 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The source 0.004 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q25","label":"Na2SeO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source 0.004 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 30 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;4&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.004&lt;/td&gt;&lt;td width='15%' align='left'&gt;g&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[13]","quote":"{\n          \"component_name\": \"Na2SeO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001602\",\n          \"gmo_id\": \"GMO_001602\",\n          \"label\": \"Sodium selenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The source 0.004 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The source 0.004 g belongs to the named trace-stock recipe with 1 L water input and a separate 1 ml receiving dose. It is wrongly flattened into main ingredients at the unscaled numeric value. Neither main nor stock final volume is explicitly declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q26","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"conflict","rationale":"The unknown NaOH amount is appropriately unquantified, but its root-medium placement loses the trace-stock pH-adjustment scope. Source first adjusts that stock to pH 6.5 then final pH 7.0; no NaOH strength, dose or main pH is supplied.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 34 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;First dissolve nitrilotriacetic acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[14]","quote":"{\n          \"component_name\": \"NaOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\": 7,\n      \"comment\": \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The unknown NaOH amount is appropriately unquantified, but its root-medium placement loses the trace-stock pH-adjustment scope. Source first adjusts that stock to pH 6.5 then final pH 7.0; no NaOH strength, dose or main pH is supplied."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The unknown NaOH amount is appropriately unquantified, but its root-medium placement loses the trace-stock pH-adjustment scope. Source first adjusts that stock to pH 6.5 then final pH 7.0; no NaOH strength, dose or main pH is supplied."}]},{"quantity_id":"q27","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 2 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 37 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Biotin&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 2 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 2 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q28","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 1 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 44 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;&lt;i&gt;p&lt;/i&gt;-Aminobenzoic acid&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 1 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 1 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q29","label":"Thiamine-HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 40 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Thiamine-HCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q30","label":"Ca-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator. The source calcium salt is not the local (R)-pantothenate anion; stereochemistry is not specified by the source.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 43 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Ca-pantothenate&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator. The source calcium salt is not the local (R)-pantothenate anion; stereochemistry is not specified by the source."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator. The source calcium salt is not the local (R)-pantothenate anion; stereochemistry is not specified by the source."}]},{"quantity_id":"q31","label":"Pyridoxine-HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 10 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 39 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Pyridoxine-HCl&lt;/td&gt;&lt;td width='20%' align='right'&gt;10&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 10 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 10 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q32","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 2 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 38 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Folic acid&lt;/td&gt;&lt;td width='20%' align='right'&gt;2&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 2 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 2 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q33","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 0.01 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 45 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Vitamin B&lt;sub&gt;12&lt;/sub&gt;&lt;/td&gt;&lt;td width='20%' align='right'&gt;0.01&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.01,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 0.01 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 0.01 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q34","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 41 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Riboflavin&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q35","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 42 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='50%' align='left' colspan='2'&gt;Nicotinic acid&lt;/td&gt;&lt;td width='20%' align='right'&gt;5&lt;/td&gt;&lt;td width='15%' align='left'&gt;mg&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The source vitamin-stock amount is 5 mg, while the local root ingredient uses the same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve the literal stock mass, its 1 L solvent input and 1 ml receiving dose without inventing a final-volume denominator."}]},{"quantity_id":"q36","label":"Trace elements solution*","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium denominator is unresolved. The reference is to the locally defined M1677 stock, not a same-name MediaDive solution; retain exact stock identity and batch addition.","source_stage":"receiving stock addition","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Trace elements solution*&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Trace elements solution*\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1677\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium denominator is unresolved. The reference is to the locally defined M1677 stock, not a same-name MediaDive solution; retain exact stock identity and batch addition."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium denominator is unresolved. The reference is to the locally defined M1677 stock, not a same-name MediaDive solution; retain exact stock identity and batch addition."}]},{"quantity_id":"q37","label":"Vitamin solution**","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium denominator is unresolved. The reference is to the locally defined M1677 stock, not a same-name MediaDive solution; retain exact stock identity and batch addition.","source_stage":"receiving stock addition","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='60%' align='left' colspan='4'&gt;Vitamin solution**&lt;/td&gt;&lt;td width='20%' align='right'&gt;1&lt;/td&gt;&lt;td width='15%' align='left'&gt;ml&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"Vitamin solution**\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M1677\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium denominator is unresolved. The reference is to the locally defined M1677 stock, not a same-name MediaDive solution; retain exact stock identity and batch addition."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium denominator is unresolved. The reference is to the locally defined M1677 stock, not a same-name MediaDive solution; retain exact stock identity and batch addition."}]},{"quantity_id":"q38","label":"Missing staged main preparation","local_fields":[],"decision":"evidence_only","rationale":"Add exact source preparation at the main/late-addition stages: exclude vitamins and sulfide from initial autoclaving, preserve the H2/CO2 80/20 atmosphere and subsequent aseptic anaerobic additions and 150 kPa pressurization. These controls do not prove strain growth, an autoclave temperature/duration, a pressure reference basis, or final volume.","source_stage":"main preparation","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;Mix ingredients except for vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O, and autoclave under H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) condition. Separately autoclave Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O as a 5% solution under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O solution, and pressurize inoculated bottles to 150 kPa with H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O, and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to 150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Separate sulfide 5% preparation","local_fields":[],"decision":"evidence_only","rationale":"The source explicitly calls for separately autoclaved Na2S·9H2O as a 5% solution under nitrogen. Preserve the bare percent without inventing w/v or v/v basis, strength-to-volume conversion or receiving aliquot. The main batch mass is separately stated.","source_stage":"late sulfide preparation","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;Mix ingredients except for vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O, and autoclave under H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt; (80/20) condition. Separately autoclave Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O as a 5% solution under a N&lt;sub&gt;2&lt;/sub&gt; atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na&lt;sub&gt;2&lt;/sub&gt;S&amp;middot;9H&lt;sub&gt;2&lt;/sub&gt;O solution, and pressurize inoculated bottles to 150 kPa with H&lt;sub&gt;2&lt;/sub&gt;/CO&lt;sub&gt;2&lt;/sub&gt;.&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O, and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to 150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Trace-stock pH sequence","local_fields":[],"decision":"evidence_only","rationale":"Preserve first dissolving NTA, adjusting trace-stock pH to 6.5 with NaOH, then adding minerals and final stock pH 7.0. This does not supply main-medium pH or NaOH dose.","source_stage":"trace-stock preparation","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML table row 34 (zero-based)","quote":"&lt;tr height='1px'&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='5%'&gt;&amp;nbsp;&lt;/td&gt;&lt;td width='90%' colspan='5'&gt;First dissolve nitrilotriacetic acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.&lt;/td&gt;&lt;/tr&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\": 7,\n      \"comment\": \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"Comparison solution6129 ZnSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"8.82","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\": 35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 8.82,\n                \"unit\": \"g\",\n                \"g_l\": 8.82,\n                \"mmol_l\": 30.6718,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882."}]},{"quantity_id":"q42","label":"Comparison solution6129 MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1.44","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.44,\n                \"unit\": \"g\",\n                \"g_l\": 1.44,\n                \"mmol_l\": 7.27622,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882."}]},{"quantity_id":"q43","label":"Comparison solution6129 MoO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.71","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"MoO3\",\n                \"compound_id\": 235,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.71,\n                \"unit\": \"g\",\n                \"g_l\": 0.71,\n                \"mmol_l\": 4.93227,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882."}]},{"quantity_id":"q44","label":"Comparison solution6129 CuSO4 x 5 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1.57","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"CuSO4 x 5 H2O\",\n                \"compound_id\": 121,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.57,\n                \"unit\": \"g\",\n                \"g_l\": 1.57,\n                \"mmol_l\": 6.2879,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[3].concentration","decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882."}]},{"quantity_id":"q45","label":"Comparison solution6129 Co(NO3)2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.49","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\": 6,\n                \"compound\": \"Co(NO3)2 x 6 H2O\",\n                \"compound_id\": 541,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.49,\n                \"unit\": \"g\",\n                \"g_l\": 0.49,\n                \"mmol_l\": 1.68365,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[4].concentration","decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882."}]},{"quantity_id":"q46","label":"Comparison solution6129 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"This synthetic See source for composition placeholder is not a chemical ingredient or a supported quantity. The explicit composition exists; keep it out of positive recipe evidence and reconcile the stale incomplete_composition flag separately.","source_stage":"comparison metadata only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.name","quote":"\"name\": \"Trace elements solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"ingredients[0].concentration","decision":"not_quantified","rationale":"This synthetic See source for composition placeholder is not a chemical ingredient or a supported quantity. The explicit composition exists; keep it out of positive recipe evidence and reconcile the stale incomplete_composition flag separately."}]},{"quantity_id":"q47","label":"Comparison solution6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882."}]},{"quantity_id":"q48","label":"Comparison solution6241 Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The existing attached exact raw snippet, stated digest, row identity and explicit provider g_l support this unchanged stock-local concentration. This current-byte authentication does not recreate the original access event and does not make this stock equivalent to NBRC882."}]},{"quantity_id":"q49","label":"Comparison solution6241 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The separate solution6241 explicitly supplies 200 micrograms biotin and makes up to 100 ml, supporting 0.002 g/L for this stock only; 2000.0 G_PER_L is inconsistent. This explicit final makeup is not transferred to NBRC882 or its distinct nine-vitamin stock.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","decision":"conflict","rationale":"The separate solution6241 explicitly supplies 200 micrograms biotin and makes up to 100 ml, supporting 0.002 g/L for this stock only; 2000.0 G_PER_L is inconsistent. This explicit final makeup is not transferred to NBRC882 or its distinct nine-vitamin stock."}]},{"quantity_id":"q50","label":"Comparison solution6241 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The separate solution6241 source instructs makeup to 100 ml with water. Stored 1000.0 PERCENT_V_V is not that instruction. Retain the explicit final-stock makeup rather than assert an unsupported solvent percentage or receiving-medium dose.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","decision":"conflict","rationale":"The separate solution6241 source instructs makeup to 100 ml with water. Stored 1000.0 PERCENT_V_V is not that instruction. Retain the explicit final-stock makeup rather than assert an unsupported solvent percentage or receiving-medium dose."}]},{"quantity_id":"q51","label":"Comparison solution6241 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"This synthetic See source for composition placeholder is not a chemical ingredient or a supported quantity. The explicit composition exists; keep it out of positive recipe evidence and reconcile the stale incomplete_composition flag separately.","source_stage":"comparison metadata only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.name","quote":"\"name\": \"Vitamin solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","decision":"not_quantified","rationale":"This synthetic See source for composition placeholder is not a chemical ingredient or a supported quantity. The explicit composition exists; keep it out of positive recipe evidence and reconcile the stale incomplete_composition flag separately."}]},{"quantity_id":"q52","label":"Comparison6241 retained final makeup","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The existing preparation correctly retains the source final makeup to 100 ml. Credit it independently of the erroneous biotin/water fields and do not transfer this basis to NBRC882.","source_stage":"comparison stock preparation","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The existing preparation correctly retains the source final makeup to 100 ml. Credit it independently of the erroneous biotin/water fields and do not transfer this basis to NBRC882."}]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml":["composition","ingredients[0]"],"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":["composition","ingredients[0]","preparation_notes"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:008235.

Every asserted CHEBI object, label and packaged MIM slot is checked. All canonical labels resolve, yet the cobalt/nickel hydrate and calcium-pantothenate anion/salt assertions are wrong supplied forms. Generic resazurin is retained without importing a sodium-salt claim. Generic B12 is not silently narrowed to cyanocobalamin, and calcium-salt stereochemistry remains unspecified. Compatible other salts, hydrates, acids and vitamins are unchanged; exact MIM preferred-row rejection does not overturn independent source/form evidence.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:008235.

All eight complete historical reports and two selected plan rows were read, including the distinct CM002108 DSM935 comparison and September CM008235 report. Seven current dependency raw snippets/digests authenticate content, not original access events. Current TOGO stock separation/unit conversion/comment behavior, name-based stock migration, duplicate repair/cleanup, grounding migrations and conservative merger were read. The normalized water repair is credited; generated staleness and mixed calcium parts remain. Original histories are preserved; no native diagnostics were rerun.

## Findings

### f1: Restore source units and separate three recipe stages

major / open / confirmed; issue key: culturemech-008235-units-and-stock-stage.

Water, calcium, resazurin, vitamin and stock-dose fields combine unrelated stages or retain raw numerals with incompatible units. The owner corrected the summed water from 3.0 to 1.0, but both retain G_PER_L; generated output is stale. Calcium still combines 0.147 g main and 0.1 g stock masses. Twelve other trace constituents and nine vitamin constituents remain flattened; resazurin and all nine vitamin rows lose their mg units. Preserve source batch amounts and distinct 1 ml stock additions, with all three 1 L water inputs separate. A solvent input is not final volume.

### f2: Replace name-only stock identity with exact NBRC882 definitions

major / open / confirmed; issue key: culturemech-008235-wrong-stock-identity.

Both 1 ml source additions refer to the locally defined M1677 stocks. Linked MediaDive6129 instead contains five differently composed mineral salts; 6241 contains three vitamins and a 100 ml final-stock makeup, not the NBRC nine-vitamin recipe. Their valid local source claims do not support equivalence. Resolve the exact trace and vitamin definitions, retaining the original source scope, and replace both Unknown solution display placeholders. Current name-only migration is an observed risk, not proof of its exact historic execution.

### f3: Restore main and stock-local preparation without borrowing conditions

major / open / confirmed; issue key: culturemech-008235-missing-preparation.

The source gas stages, 80/20 mixture, separate sulfide 5% solution, filter-sterile late vitamin addition, anaerobic additions and 150 kPa pressure are missing from maintained/generated preparation. The trace-stock pH 6.5 then 7.0 sequence belongs to that stock. Preserve all exact comments and bind claims at the schema-supported root evidence field with explicit paths. Keep unknown temperature, duration, pressure reference and percent basis unknown; the gas VARIABLE placeholders themselves do not assert false numeric amounts.

### f4: Correct cobalt, nickel and calcium-pantothenate supplied forms

major / open / confirmed; issue key: culturemech-008235-supplied-form-grounding.

CoCl2·6H2O is mapped to anhydrous CHEBI:35696; NiCl2·6H2O uses anhydrous CHEBI:34887 in both slots. Ca-pantothenate is mapped in both slots to CHEBI:29032, the (R)-pantothenate anion lacking calcium. Verify exact supplied-form objects and canonical labels without inventing calcium-salt stereochemistry. Other named hydrates, generic resazurin, sodium tungstate/selenate and generic vitamin B12 are compatible with the primary wording. Preserve current MIM REJECTED versus MAPPED row statuses rather than treating membership as chemical proof.

### f5: Correct separate solution6241 biotin and water representations

major / open / confirmed; issue key: culturemech-008235-comparison6241-amounts.

The independently referenced comparison stock6241 retains 2000.0 G_PER_L biotin and 1000.0 PERCENT_V_V water. Its exact source supplies 200 micrograms biotin and explicitly makes up to 100 ml; this supports 0.002 g/L biotin and a final-makeup instruction, not those stored values. Its existing cyanocobalamin/thiamine source claims and retained preparation remain credited. Curate this stock separately; it is not the NBRC882 vitamin recipe.

### f6: Review defined composition and remaining secondary links

minor / open / confirmed; issue key: culturemech-008235-classification-and-secondary-gaps.

The complete NBRC882 formula contains named chemical substances rather than an undefined complex extract; review the inherited COMPLEX/UNDEFINED classification against this exact composition. MnCl2·4H2O and CoCl2·6H2O also lack secondary MIM/CHEBI links, while gas placeholders have primary identity only. Preserve those known identities and fix cobalt form before adding links; absence from an exact preferred spelling is not absence of the identifier from the full index.

### f7: Keep claim credit and historical limits explicit

minor / open / confirmed; issue key: culturemech-008235-evidence-history-scope.

The selected medium has no attached concentration claims, while seven exact claims on comparison6129/6241 are authenticated against current raw bytes and digests. Earlier October no-source-check rows and September denominator/dilution recommendations are not independent source proof; retain literal masses and avoid their assumed final liter. The owner water repair is valid limited local history, not complete source curation. Preserve original events, including timezone-naive dependency events, and append verified context. Reconcile each comparison stock placeholder/incomplete_composition flag with its present composition without claiming all remaining quantities are curated.

## Recommended Actions And Acceptance Checks

### a1

Water, calcium, resazurin, vitamin and stock-dose fields combine unrelated stages or retain raw numerals with incompatible units. The owner corrected the summed water from 3.0 to 1.0, but both retain G_PER_L; generated output is stale. Calcium still combines 0.147 g main and 0.1 g stock masses. Twelve other trace constituents and nine vitamin constituents remain flattened; resazurin and all nine vitamin rows lose their mg units. Preserve source batch amounts and distinct 1 ml stock additions, with all three 1 L water inputs separate. A solvent input is not final volume.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Both 1 ml source additions refer to the locally defined M1677 stocks. Linked MediaDive6129 instead contains five differently composed mineral salts; 6241 contains three vitamins and a 100 ml final-stock makeup, not the NBRC nine-vitamin recipe. Their valid local source claims do not support equivalence. Resolve the exact trace and vitamin definitions, retaining the original source scope, and replace both Unknown solution display placeholders. Current name-only migration is an observed risk, not proof of its exact historic execution.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source gas stages, 80/20 mixture, separate sulfide 5% solution, filter-sterile late vitamin addition, anaerobic additions and 150 kPa pressure are missing from maintained/generated preparation. The trace-stock pH 6.5 then 7.0 sequence belongs to that stock. Preserve all exact comments and bind claims at the schema-supported root evidence field with explicit paths. Keep unknown temperature, duration, pressure reference and percent basis unknown; the gas VARIABLE placeholders themselves do not assert false numeric amounts.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

CoCl2·6H2O is mapped to anhydrous CHEBI:35696; NiCl2·6H2O uses anhydrous CHEBI:34887 in both slots. Ca-pantothenate is mapped in both slots to CHEBI:29032, the (R)-pantothenate anion lacking calcium. Verify exact supplied-form objects and canonical labels without inventing calcium-salt stereochemistry. Other named hydrates, generic resazurin, sodium tungstate/selenate and generic vitamin B12 are compatible with the primary wording. Preserve current MIM REJECTED versus MAPPED row statuses rather than treating membership as chemical proof.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The independently referenced comparison stock6241 retains 2000.0 G_PER_L biotin and 1000.0 PERCENT_V_V water. Its exact source supplies 200 micrograms biotin and explicitly makes up to 100 ml; this supports 0.002 g/L biotin and a final-makeup instruction, not those stored values. Its existing cyanocobalamin/thiamine source claims and retained preparation remain credited. Curate this stock separately; it is not the NBRC882 vitamin recipe.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

The complete NBRC882 formula contains named chemical substances rather than an undefined complex extract; review the inherited COMPLEX/UNDEFINED classification against this exact composition. MnCl2·4H2O and CoCl2·6H2O also lack secondary MIM/CHEBI links, while gas placeholders have primary identity only. Preserve those known identities and fix cobalt form before adding links; absence from an exact preferred spelling is not absence of the identifier from the full index.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a7

The selected medium has no attached concentration claims, while seven exact claims on comparison6129/6241 are authenticated against current raw bytes and digests. Earlier October no-source-check rows and September denominator/dilution recommendations are not independent source proof; retain literal masses and avoid their assumed final liter. The owner water repair is valid limited local history, not complete source curation. Preserve original events, including timezone-naive dependency events, and append verified context. Reconcile each comparison stock placeholder/incomplete_composition flag with its present composition without claiming all remaining quantities are curated.

- Keep all original history and reports byte-preserved; append verified context in a new actual event.
- Retain seven authenticated existing stock claims; qualify exact current-byte authentication separately from historical access provenance and receiving-medium equivalence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| nbrc882 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882; REVIEW_WORK/batch072/source01-03-supplement/nbrc882.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| togo1677 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677; REVIEW_WORK/batch072/source01-03-supplement/togo1677.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| solution6129 | https://mediadive.dsmz.de/rest/solution/6129; REVIEW_WORK/batch072/source01-03-supplement/solution6129.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; REVIEW_WORK/batch072/source01-03-supplement/solution6241.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6129_Trace_elements_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/deferribacter_medium__4cf00e52.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/yaml_record_review/20260922T141752Z-DEFERRIBACTER_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch072/record03/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete eight historical reports. The separate DSM935 comparison record and September inferred final-volume recommendations are explicitly not transferred. |
| historical-selected-parent-rows | REVIEW_WORK/batch072/record03/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch072/record03/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete parsed selected target, maintained owner and two comparison stock documents, including full histories. Placeholder stock ingredients are not positive chemical evidence. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _local_batch_volume_ml; _parse_unit; _extract_ph; _extract_preparation_steps | context_only | Current _extract_primary_components separates main sections and named local stocks. A receiving 1 ml does not corroborate the stock water input of 1 L, so _local_batch_volume_ml leaves these local compositions unnormalized. The importer retains unquantified gases and comments, maps mg to MG_PER_L and ml to ML_PER_L, but bare-unit mapping alone proves no final-volume basis. Comments are assigned main preparation steps without stock-local filtering; autoclave takes precedence over filtration within a paragraph. Current behavior is not authenticated historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| writer-stock-match | scripts/migrate_solutions_from_ingredients.py; SolutionMigrator.__init__; _resolve_solution | context_only | Current SolutionMigrator strips trailing asterisks, looks up a lowercased name in solutions_by_name and copies an existing concentration. This name-based behavior cannot establish NBRC882 stock identity or validate its denominator. The stored migration event is separate provenance. |
| writer-duplicate-repair | scripts/repair_merged_duplicates.py; repair_ingredient; repair_record | context_only | Current repair_ingredient and repair_record collapse only sums of identical parts. The owner records the water repair, while the mixed calcium parts are intentionally left unresolved. The generated water remains stale; no source verification is implied by this local repair. |
| dep6129 | data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml; Complete file | context_only | Whole linked stock read for identity comparison; scoped composition and retained claims assessed separately, never transferred into NBRC882. |
| dep6241 | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Complete file | context_only | Whole linked stock read for identity comparison; scoped composition and retained claims assessed separately, never transferred into NBRC882. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch072/source01-03-supplement/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch072/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch072/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch072/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch072/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch072/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch072/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch072/source01-03-supplement/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch072/source01-03-supplement/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63005 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63005; REVIEW_WORK/batch072/source01-03-supplement/chebi63005.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526; REVIEW_WORK/batch072/source01-03-supplement/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997; REVIEW_WORK/batch072/source01-03-supplement/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276; REVIEW_WORK/batch072/source01-03-supplement/chebi18276.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch072/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch072/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch072/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch072/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696; REVIEW_WORK/batch072/source01-03-supplement/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch072/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch072/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch072/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254; REVIEW_WORK/batch072/source01-03-supplement/chebi86254.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557; REVIEW_WORK/batch072/source01-03-supplement/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63940; REVIEW_WORK/batch072/source01-03-supplement/chebi63940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:77775; REVIEW_WORK/batch072/source01-03-supplement/chebi77775.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; REVIEW_WORK/batch072/source01-03-supplement/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch072/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch072/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch072/source01-03-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29032 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29032; REVIEW_WORK/batch072/source01-03-supplement/chebi29032.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch072/source01-03-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch072/source01-03-supplement/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch072/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch072/source01-03-supplement/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch072/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch072/source01-03-supplement/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30627 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30627; REVIEW_WORK/batch072/source01-03-supplement/chebi30627.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31440; REVIEW_WORK/batch072/source01-03-supplement/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86214 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86214; REVIEW_WORK/batch072/source01-03-supplement/chebi86214.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439; REVIEW_WORK/batch072/source01-03-supplement/chebi17439.json; exact original raw/text/hash/time metadata | context_only | Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch072/record03/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch072/record03/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch072/record03/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch072/record03/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch072/record03/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch072/record03/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch072/record03/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch072/record03/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch072/record03/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch072/record03/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch072/record03/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- NBRC882 and TOGO1677 give batch masses and solvent inputs, not explicit final main or local-stock volumes. No mg/L, g/L or stock dilution is inferred from water alone.
- The generic calcium-pantothenate source does not establish D/R stereochemistry; verify the calcium salt without silently selecting a more specific variant. The neutral resazurin source wording does not establish sodium resazurin.
- MediaDive6241 does explicitly state its own final makeup to 100 ml; that distinct basis supports its comparison-stock correction only. The two synthetic stock placeholder ingredients are not positive composition evidence.
- No primary organism-specific growth claim is supplied by NBRC882 or TOGO1677. The DSM935 same-name report is historical comparison context only, not an alternative recipe to adopt.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T163814Z-culturemech-008235-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Deferribacter Medium'
started_at: '2026-10-28T16:12:06.991443Z'
finished_at: '2026-10-28T16:38:14.478229Z'
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
summary: NBRC882 identity is confirmed, but the record needs source-unit and stock-stage
  repair, correct local stock references, omitted preparation and supplied-form corrections.
  The owner water-sum repair and seven independently authenticated comparison-stock
  claims are credited. Same-name DSM935 and the linked MediaDive stocks remain separate
  formulations. All four original canonical checks passed; the full scoped review
  is complete with explicit denominator and stereochemistry limits.
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
  - path: data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml
    sha256: 5484d47c2212e61e788396c3f31deca3f72353c52d65020c03a05b9e5f751f5d
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    sha256: b3011ff2349dc96a4cbdeb9bf17489508666413de8b00e33ffcc6c4d5387a0b9
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml
    sha256: f8dc196d75f0176cd99b8125f6ca3f9d8377422a189e6808d16c04340109cd05
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
    sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6129_Trace_elements_solution.yaml.md
    sha256: 6329f7f95876e28ae96ba1f6856876696b1d82132fa11b2368d1b84535ec16d3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
    sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_MEDIUM.md
    sha256: 0f8571e4612b96acb6d81e91a74fdaea8840785a4e3f18a52270ce89f4f4b4ea
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/deferribacter_medium__4cf00e52.md
    sha256: f1e4de5a77b298de35d59eff0ab39942405dcee58458f17e604ba73866fea0ad
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.md
    sha256: bee6664eb485e5be5dc9006442bb9458704c36c1d933e7656804cc170311f75f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.md
    sha256: 5a554dde57f0efe6c8a967da99df9fb77470830a9083b2f617d469dbde7c6e0b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
    sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
    role: context
  - path: reports/yaml_record_review/20260922T141752Z-DEFERRIBACTER_MEDIUM.md
    sha256: d65381114362ecb93592fa1afd51377a38a0f8f3a4f01aca627558ba7aa494a7
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
  selection: Authoritative batch072 index 03
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008235
targets:
- target_id: CultureMech:008235
  path: data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml
  label: deferribacter_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:008235
  command: just validate-schema data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml
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
  - CultureMech:008235
  command: just validate-strict data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml --out
    REVIEW_WORK/batch072/record03/strict.tsv --workers 1 --quiet
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
  - CultureMech:008235
  command: just validate-terms data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml
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
  - CultureMech:008235
  command: just validate-references data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: nbrc882
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882
  accessed_at: '2026-10-28T16:12:45.623568Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/nbrc882.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216
- evidence_id: togo1677
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677
  accessed_at: '2026-10-28T16:12:45.788732Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/togo1677.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a
- evidence_id: solution6129
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6129
  accessed_at: '2026-10-28T16:12:46.437238Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/solution6129.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  accessed_at: '2026-10-28T16:12:46.444967Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/solution6241.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:38:14.315187Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 5484d47c2212e61e788396c3f31deca3f72353c52d65020c03a05b9e5f751f5d
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:38:14.315358Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: b3011ff2349dc96a4cbdeb9bf17489508666413de8b00e33ffcc6c4d5387a0b9
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T16:38:14.315394Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T16:38:14.315714Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T16:38:14.315740Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T16:38:14.315763Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:38:14.315791Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6129_Trace_elements_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316527Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 6329f7f95876e28ae96ba1f6856876696b1d82132fa11b2368d1b84535ec16d3
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316563Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316588Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 0f8571e4612b96acb6d81e91a74fdaea8840785a4e3f18a52270ce89f4f4b4ea
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/deferribacter_medium__4cf00e52.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316617Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f1e4de5a77b298de35d59eff0ab39942405dcee58458f17e604ba73866fea0ad
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316641Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: bee6664eb485e5be5dc9006442bb9458704c36c1d933e7656804cc170311f75f
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316666Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 5a554dde57f0efe6c8a967da99df9fb77470830a9083b2f617d469dbde7c6e0b
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316688Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
- evidence_id: report-26
  kind: prior_review
  reference: reports/yaml_record_review/20260922T141752Z-DEFERRIBACTER_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T16:38:14.316709Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d65381114362ecb93592fa1afd51377a38a0f8f3a4f01aca627558ba7aa494a7
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/historical-reading.json
  accessed_at: '2026-10-28T16:38:14.316739Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete eight historical reports. The separate DSM935 comparison record
    and September inferred final-volume recommendations are explicitly not transferred.
  snapshot_sha256: c6faf343325cec2dc4dc6842b2f07b45edcaa4f7978c74e30b2eeaf011998a2f
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T16:38:14.316791Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 39aae2d90ae0f0aa2889efa409120614387c37ded0ddb5ca70024dcc595b6801
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/complete-document-reader.json
  accessed_at: '2026-10-28T16:38:14.316824Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete parsed selected target, maintained owner and two comparison stock
    documents, including full histories. Placeholder stock ingredients are not positive
    chemical evidence.
  snapshot_sha256: 9c1b6458247202aeac3f8a5477cce262e4d5f5ea9ebdfe84c5fe26bf8067ac73
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T16:38:14.316910Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _local_batch_volume_ml;
    _parse_unit; _extract_ph; _extract_preparation_steps
  accessed_at: '2026-10-28T16:38:14.316935Z'
  support: context_only
  summary: Current _extract_primary_components separates main sections and named local
    stocks. A receiving 1 ml does not corroborate the stock water input of 1 L, so
    _local_batch_volume_ml leaves these local compositions unnormalized. The importer
    retains unquantified gases and comments, maps mg to MG_PER_L and ml to ML_PER_L,
    but bare-unit mapping alone proves no final-volume basis. Comments are assigned
    main preparation steps without stock-local filtering; autoclave takes precedence
    over filtration within a paragraph. Current behavior is not authenticated historical
    execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: MediaQualityFixer._merge_ingredient_group
  accessed_at: '2026-10-28T16:38:14.316968Z'
  support: context_only
  summary: Current _merge_ingredient_group keeps identical duplicate amounts and flags
    disagreements; it no longer sums duplicate quantities. It cannot establish compatible
    stock/main bases or repair a historical flattened sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-stock-match
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: SolutionMigrator.__init__; _resolve_solution
  accessed_at: '2026-10-28T16:38:14.323117Z'
  support: context_only
  summary: Current SolutionMigrator strips trailing asterisks, looks up a lowercased
    name in solutions_by_name and copies an existing concentration. This name-based
    behavior cannot establish NBRC882 stock identity or validate its denominator.
    The stored migration event is separate provenance.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-duplicate-repair
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient; repair_record
  accessed_at: '2026-10-28T16:38:14.323155Z'
  support: context_only
  summary: Current repair_ingredient and repair_record collapse only sums of identical
    parts. The owner records the water repair, while the mixed calcium parts are intentionally
    left unresolved. The generated water remains stale; no source verification is
    implied by this local repair.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: dep6129
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:38:14.323178Z'
  support: context_only
  summary: Whole linked stock read for identity comparison; scoped composition and
    retained claims assessed separately, never transferred into NBRC882.
  snapshot_sha256: f8dc196d75f0176cd99b8125f6ca3f9d8377422a189e6808d16c04340109cd05
- evidence_id: dep6241
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Complete file
  accessed_at: '2026-10-28T16:38:14.323202Z'
  support: context_only
  summary: Whole linked stock read for identity comparison; scoped composition and
    retained claims assessed separately, never transferred into NBRC882.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T16:12:47.393698Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi15377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
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
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T16:12:51.164436Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi32139.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
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
- evidence_id: chebi63005
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63005
  accessed_at: '2026-10-28T16:12:53.171672Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi63005.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f939d1fb0ecd70237f05d967ccb3c588813ee46c66ff74de2355aeca2bd22ebb
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526
  accessed_at: '2026-10-28T16:12:48.037284Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi16526.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1fc9ed85cc20ea796dc5884bab2961c0cb13288fec88089767d5ca0349e6ab66
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997
  accessed_at: '2026-10-28T16:12:49.115911Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi17997.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c4f240d59927c0f5c6c8d29c14830d0f278cfeabc4ed924be5c2b6bbe1039c05
- evidence_id: chebi18276
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276
  accessed_at: '2026-10-28T16:12:49.478228Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi18276.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e9495ec2aad65253b7f792e780c1610f9f12f2c0bb20e06c2526156d37b09ed7
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
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696
  accessed_at: '2026-10-28T16:12:52.424782Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi35696.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 22f49067d1405baa8e2bbd7c4405035d8663c69aa045b7bbacf363bb30729244
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
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254
  accessed_at: '2026-10-28T16:12:55.224124Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86254.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: b3a79ee6d9359b7b827f6f87134bc166d84d3948ec20c54965c6e706aecde3a4
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
- evidence_id: chebi63940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63940
  accessed_at: '2026-10-28T16:12:53.775024Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi63940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cd639452d53fc8afcbd2da590ff0f93a573b2abfb4f486020f4e10030b42cf7a
- evidence_id: chebi77775
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:77775
  accessed_at: '2026-10-28T16:12:54.621043Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi77775.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5e587ae9b9bdc01f8f5c6399f6e0050bf609d8c2b29a844aa28b26d07e6e42ae
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
- evidence_id: chebi29032
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29032
  accessed_at: '2026-10-28T16:12:49.727656Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi29032.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a402e7df7ea27e470b448a3c8c72e60f8deb5000961702e91e8a1f87211861c4
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
- evidence_id: chebi30627
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30627
  accessed_at: '2026-10-28T16:12:49.971616Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi30627.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 72b1e5d10eb7f4062fcc7b225c05f693cd18173e35acac1870e4e6e6ef6bcea4
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
- evidence_id: chebi86214
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86214
  accessed_at: '2026-10-28T16:12:54.937442Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi86214.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9523f9163575dfb800448b401eb6eb5e75e892c56ff33c1134894e2b5d58779c
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439
  accessed_at: '2026-10-28T16:12:48.490935Z'
  locator: REVIEW_WORK/batch072/source01-03-supplement/chebi17439.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch072 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 71dca75ee64801424c519bde7667291decd3b97f0c4e46c3d9b9405fa04a71d4
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:38:14.476926Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 0925313458a6eef8e3fe58793c81f7eb916fcd27360bac8ab62e93c9ff478fd9
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:38:14.477044Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: fee9adde7f9e48c82e799745868920ab7d58a80db8fa6759c19d3da1a3ffe6e5
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:38:14.477202Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 7b3287a36710ef2a506b3f7eea544d00cb2df4dbd348ef80910e71c65a5b13dc
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:38:14.477289Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: c2f1806591b53eb4bdb207937f645f317c2f442d669af239cfc31af0b451bc32
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:38:14.477360Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 4770ff871e1b024167f2a46e25700cd4865f9be09fb320e3fdae7c40c22b0914
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:38:14.477388Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 5096ad999869a0d1ae64b4e3756cb629c9df52786bf890b1ca4570ac0fde8239
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch072/record03/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T16:38:14.477410Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 42961f84f0ea886696cfb2c56c471f70e334528c4727d75c4b9d7df558cfe960
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch072/record03/validate-schema.json
  accessed_at: '2026-10-28T16:12:08.072541Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 550572f71b4044981d90291a9c8654d364fcd650fbc8d3c7709742048e90c6a9
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch072/record03/validate-strict.json
  accessed_at: '2026-10-28T16:12:09.055054Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: b65fabaf9c04af85a663bf24da6fccf98b93e8b2e3d0afceb1cb386c752aea20
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch072/record03/validate-terms.json
  accessed_at: '2026-10-28T16:12:10.134634Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0457dc5a5a4a96a8c09e8de22087c9638e6bf1204750f1ca0f6673379af2b3bd
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch072/record03/validate-references.json
  accessed_at: '2026-10-28T16:12:10.911925Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 85b7d12a52f283dcbf8966d7651d32394d4a09d0ce943fa0ad8c368f35088f3c
assessments:
- assessment_id: identity
  area: identity
  topic: Exact primary identity and stock boundary
  outcome: concern
  summary: TOGO M1677 and NBRC882 identity match. Same-label DSM935 is a distinct
    formulation and is not merged by assumption. The two linked MediaDive stocks are
    incompatible name matches, despite their own valid identities.
  target_ids:
  - CultureMech:008235
  evidence_ids:
  - nbrc882
  - togo1677
  - solution6129
  - solution6241
- assessment_id: classification
  area: scope
  topic: Basic classification and scope
  outcome: concern
  summary: Bacterial liquid scope is consistent with the record; COMPLEX/UNDEFINED
    is unsupported by a complete formula of named chemical components. No organism
    or growth assertion is inferred.
  target_ids:
  - CultureMech:008235
  evidence_ids:
  - nbrc882
  - target
- assessment_id: evidence
  area: evidence
  topic: Unchanged values and retained claim support
  outcome: concern
  summary: All selected and comparison fields are inventoried. Seven attached comparison-stock
    concentrations remain verified; their evidence is not transferred. Matching main
    batch digits alone do not validate G_PER_L, and VARIABLE gas placeholders do not
    imply known dissolved amounts.
  target_ids:
  - CultureMech:008235
  evidence_ids:
  - quantities
  - old-claims
  - nbrc882
  - togo1677
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 85 current concentration fields are covered by 52 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:008235
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b072-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","quantity_field_count":85,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    primary separately supplies 1 L input water in main, trace and vitamin recipes.
    Generated 3.0 G_PER_L sums different batches and has the wrong dimension. The
    owner repairs that identical sum to 1.0 but retains the wrong G_PER_L dimension
    and collapsed scope; credit that limited repair. None of these water inputs states
    a measured final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 14 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>Distilled water</td><td width=''20%''
    align=''right''>1</td><td width=''15%'' align=''left''>L</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 32 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Distilled water</td><td width=''20%'' align=''right''>1</td><td
    width=''15%'' align=''left''>L</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 46 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Distilled water</td><td width=''20%'' align=''right''>1</td><td
    width=''15%'' align=''left''>L</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The
    primary separately supplies 1 L input water in main, trace and vitamin recipes.
    Generated 3.0 G_PER_L sums different batches and has the wrong dimension. The
    owner repairs that identical sum to 1.0 but retains the wrong G_PER_L dimension
    and collapsed scope; credit that limited repair. None of these water inputs states
    a measured final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The
    primary separately supplies 1 L input water in main, trace and vitamin recipes.
    Generated 3.0 G_PER_L sums different batches and has the wrong dimension. The
    owner repairs that identical sum to 1.0 but retains the wrong G_PER_L dimension
    and collapsed scope; credit that limited repair. None of these water inputs states
    a measured final volume."}]},{"quantity_id":"q2","label":"CaCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Stored
    0.247 G_PER_L adds the main 0.147 g batch amount to the trace-stock 0.1 g batch
    amount. They belong to different solution stages and cannot be summed as a final-medium
    total. Retain each original mass and the 1 ml trace receiving dose; no final-volume
    denominator is established.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 6 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>CaCl<sub>2</sub>&middot;2H<sub>2</sub>O</td><td
    width=''20%'' align=''right''>0.147</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"CaCl2·2H2O\",\n          \"volume\": 0.147,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 23 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>CaCl<sub>2</sub>&middot;2H<sub>2</sub>O</td><td width=''20%'' align=''right''>0.1</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"CaCl2·2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"conflict","rationale":"Stored
    0.247 G_PER_L adds the main 0.147 g batch amount to the trace-stock 0.1 g batch
    amount. They belong to different solution stages and cannot be summed as a final-medium
    total. Retain each original mass and the 1 ml trace receiving dose; no final-volume
    denominator is established."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[1].concentration","decision":"conflict","rationale":"Stored
    0.247 G_PER_L adds the main 0.147 g batch amount to the trace-stock 0.1 g batch
    amount. They belong to different solution stages and cannot be summed as a final-medium
    total. Retain each original mass and the 1 ml trace receiving dose; no final-volume
    denominator is established."}]},{"quantity_id":"q3","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.136","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.136","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    unchanged numeric 0.136 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 4 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>KH<sub>2</sub>PO<sub>4</sub></td><td
    width=''20%'' align=''right''>0.136</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.136,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.136 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.136 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.535","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.535","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    unchanged numeric 0.535 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 3 (zero-based)","quote":"<tr>\n                            <td colspan=\"2\"
    id=\"medium-comp\"><table width=''600'' border=''0''><tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>NH<sub>4</sub>Cl</td><td width=''20%''
    align=''right''>0.535</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.535,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.535 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.535 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."}]},{"quantity_id":"q5","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source supplies 1 mg resazurin to the main batch, not the stored 1 G_PER_L. Preserve
    the literal mass and unresolved final-volume basis. The source says resazurin
    without a sodium qualifier, so neutral CHEBI:8806 is not shown to be the wrong
    supplied form.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 12 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>Resazurin</td><td width=''20%'' align=''right''>1</td><td
    width=''15%'' align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent
    redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"conflict","rationale":"The
    source supplies 1 mg resazurin to the main batch, not the stored 1 G_PER_L. Preserve
    the literal mass and unresolved final-volume basis. The source says resazurin
    without a sodium qualifier, so neutral CHEBI:8806 is not shown to be the wrong
    supplied form."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[4].concentration","decision":"conflict","rationale":"The
    source supplies 1 mg resazurin to the main batch, not the stored 1 G_PER_L. Preserve
    the literal mass and unresolved final-volume basis. The source says resazurin
    without a sodium qualifier, so neutral CHEBI:8806 is not shown to be the wrong
    supplied form."}]},{"quantity_id":"q6","label":"MgCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.204","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.204","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    unchanged numeric 0.204 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 5 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>MgCl<sub>2</sub>&middot;6H<sub>2</sub>O</td><td
    width=''20%'' align=''right''>0.204</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"MgCl2·6H2O\",\n          \"volume\": 0.204,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.204 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.204 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."}]},{"quantity_id":"q7","label":"Na2S·9H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    unchanged numeric 0.5 matches the primary g batch mass, but neither NBRC nor TOGO
    declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator.
    Retain source mass as batch evidence; do not silently convert the 1 L solvent
    input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 13 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>Na<sub>2</sub>S&middot;9H<sub>2</sub>O</td><td
    width=''20%'' align=''right''>0.5</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"Na2S·9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\":
    \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.5 matches the primary g batch mass, but neither NBRC nor TOGO
    declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator.
    Retain source mass as batch evidence; do not silently convert the 1 L solvent
    input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.5 matches the primary g batch mass, but neither NBRC nor TOGO
    declares final main volume. The local G_PER_L assertion lacks a demonstrated denominator.
    Retain source mass as batch evidence; do not silently convert the 1 L solvent
    input into final volume."}]},{"quantity_id":"q8","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.52","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.52","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    unchanged numeric 2.52 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 11 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>NaHCO<sub>3</sub></td><td width=''20%''
    align=''right''>2.52</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"NaHCO3\",\n          \"volume\": 2.52,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\":
    \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 2.52 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 2.52 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."}]},{"quantity_id":"q9","label":"Sodium acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.82","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.82","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    unchanged numeric 0.82 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 9 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>Sodium acetate</td><td width=''20%''
    align=''right''>0.82</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"Sodium acetate\",\n          \"volume\": 0.82,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\":
    \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.82 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.82 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."}]},{"quantity_id":"q10","label":"Sodium
    nitrate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.85","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.85","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    unchanged numeric 0.85 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 10 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>Sodium nitrate</td><td width=''20%''
    align=''right''>0.85</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Sodium nitrate\",\n          \"volume\": 0.85,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001049\",\n          \"gmo_id\": \"GMO_001049\",\n          \"label\":
    \"Sodium nitrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.85 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    unchanged numeric 0.85 matches the primary g batch mass, but neither NBRC nor
    TOGO declares final main volume. The local G_PER_L assertion lacks a demonstrated
    denominator. Retain source mass as batch evidence; do not silently convert the
    1 L solvent input into final volume."}]},{"quantity_id":"q11","label":"Carbon
    dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 16 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''90%'' colspan=''5''>Mix ingredients except
    for vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O, and autoclave
    under H<sub>2</sub>/CO<sub>2</sub> (80/20) condition. Separately autoclave Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    as a 5% solution under a N<sub>2</sub> atmosphere. Aseptically and anaerobically
    add filter-sterile vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    solution, and pressurize inoculated bottles to 150 kPa with H<sub>2</sub>/CO<sub>2</sub>.</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O,
    and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as
    a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile
    vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to
    150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration."}]},{"quantity_id":"q12","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 16 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''90%'' colspan=''5''>Mix ingredients except
    for vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O, and autoclave
    under H<sub>2</sub>/CO<sub>2</sub> (80/20) condition. Separately autoclave Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    as a 5% solution under a N<sub>2</sub> atmosphere. Aseptically and anaerobically
    add filter-sterile vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    solution, and pressurize inoculated bottles to 150 kPa with H<sub>2</sub>/CO<sub>2</sub>.</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O,
    and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as
    a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile
    vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to
    150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[11].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration."}]},{"quantity_id":"q13","label":"Hydrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration.","source_stage":"main","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 16 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''90%'' colspan=''5''>Mix ingredients except
    for vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O, and autoclave
    under H<sub>2</sub>/CO<sub>2</sub> (80/20) condition. Separately autoclave Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    as a 5% solution under a N<sub>2</sub> atmosphere. Aseptically and anaerobically
    add filter-sterile vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    solution, and pressurize inoculated bottles to 150 kPa with H<sub>2</sub>/CO<sub>2</sub>.</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[14]","quote":"{\n          \"component_name\":
    \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\":
    \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O,
    and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as
    a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile
    vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to
    150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[12].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully avoids asserting a bulk gas amount. The source names this gas in stage-specific
    preparation, including H2/CO2 80/20, separate nitrogen atmosphere and 150 kPa
    bottle pressurization. Preserve the placeholder if retained, but add the exact
    preparation context rather than infer a numeric dissolved concentration."}]},{"quantity_id":"q14","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 1 g belongs to the named trace-stock recipe with 1 L water input and a
    separate 1 ml receiving dose. It is wrongly flattened into main ingredients at
    the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 28 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>NaCl</td><td width=''20%'' align=''right''>1</td><td width=''15%''
    align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    source 1 g belongs to the named trace-stock recipe with 1 L water input and a
    separate 1 ml receiving dose. It is wrongly flattened into main ingredients at
    the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    source 1 g belongs to the named trace-stock recipe with 1 L water input and a
    separate 1 ml receiving dose. It is wrongly flattened into main ingredients at
    the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q15","label":"Na2MoO4·2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.024 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 27 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Na<sub>2</sub>MoO<sub>4</sub>&middot;2H<sub>2</sub>O</td><td width=''20%''
    align=''right''>0.024</td><td width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"Na2MoO4·2H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    source 0.024 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    source 0.024 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.01 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 26 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>H<sub>3</sub>BO<sub>3</sub></td><td width=''20%'' align=''right''>0.01</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    source 0.01 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    source 0.01 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q17","label":"MnCl2·4H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.1 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 21 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>MnCl<sub>2</sub>&middot;4H<sub>2</sub>O</td><td width=''20%'' align=''right''>0.1</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
    \"MnCl2·4H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\":
    \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    source 0.1 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    source 0.1 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q18","label":"CoCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.024 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage. The explicitly supplied
    hexahydrate also conflicts with the local anhydrous ontology assertion.","source_stage":"trace
    stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 22 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>CoCl<sub>2</sub>&middot;6H<sub>2</sub>O</td><td width=''20%'' align=''right''>0.024</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
    \"CoCl2·6H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    source 0.024 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage. The explicitly supplied
    hexahydrate also conflicts with the local anhydrous ontology assertion."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    source 0.024 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage. The explicitly supplied
    hexahydrate also conflicts with the local anhydrous ontology assertion."}]},{"quantity_id":"q19","label":"NiCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.12","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.12 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage. The explicitly supplied
    hexahydrate also conflicts with the local anhydrous ontology assertion.","source_stage":"trace
    stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 29 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>NiCl<sub>2</sub>&middot;6H<sub>2</sub>O</td><td width=''20%'' align=''right''>0.12</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
    \"NiCl2·6H2O\",\n          \"volume\": 0.12,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\":
    \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    source 0.12 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage. The explicitly supplied
    hexahydrate also conflicts with the local anhydrous ontology assertion."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    source 0.12 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage. The explicitly supplied
    hexahydrate also conflicts with the local anhydrous ontology assertion."}]},{"quantity_id":"q20","label":"CuCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.025 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 25 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>CuCl<sub>2</sub>&middot;2H<sub>2</sub>O</td><td width=''20%'' align=''right''>0.025</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
    \"CuCl2·2H2O\",\n          \"volume\": 0.025,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\":
    \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    source 0.025 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    source 0.025 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q21","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.1 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 24 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>ZnCl<sub>2</sub></td><td width=''20%'' align=''right''>0.1</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
    \"ZnCl2\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\":
    \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    source 0.1 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    source 0.1 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q22","label":"FeCl3·6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1.35","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1.35","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 1.35 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 20 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>FeCl<sub>3</sub>&middot;6H<sub>2</sub>O</td><td width=''20%'' align=''right''>1.35</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
    \"FeCl3·6H2O\",\n          \"volume\": 1.35,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001047\",\n          \"gmo_id\": \"GMO_001047\",\n          \"label\":
    \"Iron(III) chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    source 1.35 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    source 1.35 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q23","label":"Nitrilotriacetic
    acid (NTA)","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"12.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"12.8","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 12.8 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 19 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Nitrilotriacetic acid (NTA)</td><td width=''20%'' align=''right''>12.8</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[11]","quote":"{\n          \"component_name\":
    \"Nitrilotriacetic acid (NTA)\",\n          \"volume\": 12.8,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\":
    \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    source 12.8 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    source 12.8 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q24","label":"Na2WO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.004 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 31 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Na<sub>2</sub>WO<sub>4</sub></td><td width=''20%'' align=''right''>0.004</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[12]","quote":"{\n          \"component_name\":
    \"Na2WO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001086\",\n          \"gmo_id\": \"GMO_001086\",\n          \"label\":
    \"Sodium tungstate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    source 0.004 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    source 0.004 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q25","label":"Na2SeO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source 0.004 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage.","source_stage":"trace stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 30 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Na<sub>2</sub>SeO<sub>4</sub></td><td width=''20%'' align=''right''>0.004</td><td
    width=''15%'' align=''left''>g</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[13]","quote":"{\n          \"component_name\":
    \"Na2SeO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001602\",\n          \"gmo_id\": \"GMO_001602\",\n          \"label\":
    \"Sodium selenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    source 0.004 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    source 0.004 g belongs to the named trace-stock recipe with 1 L water input and
    a separate 1 ml receiving dose. It is wrongly flattened into main ingredients
    at the unscaled numeric value. Neither main nor stock final volume is explicitly
    declared; preserve stock batch mass and source stage."}]},{"quantity_id":"q26","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"conflict","rationale":"The
    unknown NaOH amount is appropriately unquantified, but its root-medium placement
    loses the trace-stock pH-adjustment scope. Source first adjusts that stock to
    pH 6.5 then final pH 7.0; no NaOH strength, dose or main pH is supplied.","source_stage":"trace
    stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 34 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''90%'' colspan=''5''>First dissolve nitrilotriacetic
    acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[1].items[14]","quote":"{\n          \"component_name\":
    \"NaOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\":
    \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\":
    7,\n      \"comment\": \"First dissolve nitrilotriacetic acid and adjust pH to
    6.5 with NaOH, and then add minerals. Final pH 7.0.\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    unknown NaOH amount is appropriately unquantified, but its root-medium placement
    loses the trace-stock pH-adjustment scope. Source first adjusts that stock to
    pH 6.5 then final pH 7.0; no NaOH strength, dose or main pH is supplied."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    unknown NaOH amount is appropriately unquantified, but its root-medium placement
    loses the trace-stock pH-adjustment scope. Source first adjusts that stock to
    pH 6.5 then final pH 7.0; no NaOH strength, dose or main pH is supplied."}]},{"quantity_id":"q27","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 2 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 37 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Biotin</td><td width=''20%'' align=''right''>2</td><td width=''15%''
    align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 2 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 2 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q28","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 1 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 44 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''><i>p</i>-Aminobenzoic acid</td><td width=''20%'' align=''right''>1</td><td
    width=''15%'' align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 1 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 1 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q29","label":"Thiamine-HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 40 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Thiamine-HCl</td><td width=''20%'' align=''right''>5</td><td width=''15%''
    align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q30","label":"Ca-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator. The source calcium salt is not the local
    (R)-pantothenate anion; stereochemistry is not specified by the source.","source_stage":"vitamin
    stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 43 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Ca-pantothenate</td><td width=''20%'' align=''right''>5</td><td
    width=''15%'' align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\":
    \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator. The source calcium salt is not the local
    (R)-pantothenate anion; stereochemistry is not specified by the source."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator. The source calcium salt is not the local
    (R)-pantothenate anion; stereochemistry is not specified by the source."}]},{"quantity_id":"q31","label":"Pyridoxine-HCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 10 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 39 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Pyridoxine-HCl</td><td width=''20%'' align=''right''>10</td><td
    width=''15%'' align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\":
    \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 10 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 10 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q32","label":"Folic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 2 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 38 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Folic acid</td><td width=''20%'' align=''right''>2</td><td width=''15%''
    align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 2 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 2 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q33","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 0.01 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 45 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Vitamin B<sub>12</sub></td><td width=''20%'' align=''right''>0.01</td><td
    width=''15%'' align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 0.01,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 0.01 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[32].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 0.01 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q34","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 41 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Riboflavin</td><td width=''20%'' align=''right''>5</td><td width=''15%''
    align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[33].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q35","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator.","source_stage":"vitamin stock","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 42 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''5%''>&nbsp;</td><td width=''50%'' align=''left''
    colspan=''2''>Nicotinic acid</td><td width=''20%'' align=''right''>5</td><td width=''15%''
    align=''left''>mg</td></tr>","quote_basis":"raw UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"ingredients[34].concentration","decision":"conflict","rationale":"The
    source vitamin-stock amount is 5 mg, while the local root ingredient uses the
    same numeral in G_PER_L. Both milligram scale and stock stage are lost. Preserve
    the literal stock mass, its 1 L solvent input and 1 ml receiving dose without
    inventing a final-volume denominator."}]},{"quantity_id":"q36","label":"Trace
    elements solution*","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium
    denominator is unresolved. The reference is to the locally defined M1677 stock,
    not a same-name MediaDive solution; retain exact stock identity and batch addition.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 7 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>Trace elements solution*</td><td width=''20%''
    align=''right''>1</td><td width=''15%'' align=''left''>ml</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Trace elements solution*\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1677\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The
    source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium
    denominator is unresolved. The reference is to the locally defined M1677 stock,
    not a same-name MediaDive solution; retain exact stock identity and batch addition."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The
    source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium
    denominator is unresolved. The reference is to the locally defined M1677 stock,
    not a same-name MediaDive solution; retain exact stock identity and batch addition."}]},{"quantity_id":"q37","label":"Vitamin
    solution**","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium
    denominator is unresolved. The reference is to the locally defined M1677 stock,
    not a same-name MediaDive solution; retain exact stock identity and batch addition.","source_stage":"receiving
    stock addition","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 8 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''60%'' align=''left'' colspan=''4''>Vitamin solution**</td><td width=''20%''
    align=''right''>1</td><td width=''15%'' align=''left''>ml</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"Vitamin solution**\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M1677\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The
    source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium
    denominator is unresolved. The reference is to the locally defined M1677 stock,
    not a same-name MediaDive solution; retain exact stock identity and batch addition."},{"path":"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The
    source receiving addition is 1 ml per stated batch, not 1 G_PER_L. A final-medium
    denominator is unresolved. The reference is to the locally defined M1677 stock,
    not a same-name MediaDive solution; retain exact stock identity and batch addition."}]},{"quantity_id":"q38","label":"Missing
    staged main preparation","local_fields":[],"decision":"evidence_only","rationale":"Add
    exact source preparation at the main/late-addition stages: exclude vitamins and
    sulfide from initial autoclaving, preserve the H2/CO2 80/20 atmosphere and subsequent
    aseptic anaerobic additions and 150 kPa pressurization. These controls do not
    prove strain growth, an autoclave temperature/duration, a pressure reference basis,
    or final volume.","source_stage":"main preparation","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 16 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''90%'' colspan=''5''>Mix ingredients except
    for vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O, and autoclave
    under H<sub>2</sub>/CO<sub>2</sub> (80/20) condition. Separately autoclave Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    as a 5% solution under a N<sub>2</sub> atmosphere. Aseptically and anaerobically
    add filter-sterile vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    solution, and pressurize inoculated bottles to 150 kPa with H<sub>2</sub>/CO<sub>2</sub>.</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O,
    and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as
    a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile
    vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to
    150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q39","label":"Separate
    sulfide 5% preparation","local_fields":[],"decision":"evidence_only","rationale":"The
    source explicitly calls for separately autoclaved Na2S·9H2O as a 5% solution under
    nitrogen. Preserve the bare percent without inventing w/v or v/v basis, strength-to-volume
    conversion or receiving aliquot. The main batch mass is separately stated.","source_stage":"late
    sulfide preparation","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 16 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''90%'' colspan=''5''>Mix ingredients except
    for vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O, and autoclave
    under H<sub>2</sub>/CO<sub>2</sub> (80/20) condition. Separately autoclave Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    as a 5% solution under a N<sub>2</sub> atmosphere. Aseptically and anaerobically
    add filter-sterile vitamin solution and Na<sub>2</sub>S&middot;9H<sub>2</sub>O
    solution, and pressurize inoculated bottles to 150 kPa with H<sub>2</sub>/CO<sub>2</sub>.</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Mix ingredients except for vitamin solution and Na2S·9H2O,
    and autoclave under H2/CO2 (80/20) condition. Separately autoclave Na2S·9H2O as
    a 5% solution under a N2 atmosphere. Aseptically and anaerobically add filter-sterile
    vitamin solution and Na2S·9H2O solution, and pressurize inoculated bottles to
    150 kPa with H2/CO2.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q40","label":"Trace-stock
    pH sequence","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    first dissolving NTA, adjusting trace-stock pH to 6.5 with NaOH, then adding minerals
    and final stock pH 7.0. This does not supply main-medium pH or NaOH dose.","source_stage":"trace-stock
    preparation","sources":[{"evidence_id":"nbrc882","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=882","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/nbrc882.bin","raw_sha256":"040bb1d435e30e6f0141535441cb91c2f4c4f54e3c7456c9426adaca5fcbb216","text_sha256":"5359c2aa5457124aa111fe796c86494497e78176035fd3fd13c2feca8d3adcff","accessed_at":"2026-10-28T16:12:45.623568Z","locator":"HTML
    table row 34 (zero-based)","quote":"<tr height=''1px''><td width=''5%''>&nbsp;</td><td
    width=''5%''>&nbsp;</td><td width=''90%'' colspan=''5''>First dissolve nitrilotriacetic
    acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.</td></tr>","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo1677","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1677","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/togo1677.bin","raw_sha256":"453acb09a368fee4fcb61a1ff734c3692eefff5dbd2c469a7c5c1173743d481a","text_sha256":"5877f5901a4e298b4abef4c7d81f56a941f14d773a70ae7e0475e99fb6cf59b0","accessed_at":"2026-10-28T16:12:45.788732Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\":
    7,\n      \"comment\": \"First dissolve nitrilotriacetic acid and adjust pH to
    6.5 with NaOH, and then add minerals. Final pH 7.0.\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q41","label":"Comparison solution6129
    ZnSO4 x 7 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"8.82","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"ZnSO4 x 7 H2O\",\n                \"compound_id\":
    35,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 8.82,\n                \"unit\":
    \"g\",\n                \"g_l\": 8.82,\n                \"mmol_l\": 30.6718,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882."}]},{"quantity_id":"q42","label":"Comparison solution6129
    MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1.44","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.44,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.44,\n                \"mmol_l\": 7.27622,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882."}]},{"quantity_id":"q43","label":"Comparison solution6129
    MoO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.71","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"MoO3\",\n                \"compound_id\":
    235,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.71,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.71,\n                \"mmol_l\": 4.93227,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882."}]},{"quantity_id":"q44","label":"Comparison solution6129
    CuSO4 x 5 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1.57","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"CuSO4 x 5 H2O\",\n                \"compound_id\":
    121,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.57,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.57,\n                \"mmol_l\": 6.2879,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[3].concentration","decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882."}]},{"quantity_id":"q45","label":"Comparison solution6129
    Co(NO3)2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.49","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"Co(NO3)2 x 6 H2O\",\n                \"compound_id\":
    541,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.49,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.49,\n                \"mmol_l\": 1.68365,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"composition[4].concentration","decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882."}]},{"quantity_id":"q46","label":"Comparison solution6129
    placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"This
    synthetic See source for composition placeholder is not a chemical ingredient
    or a supported quantity. The explicit composition exists; keep it out of positive
    recipe evidence and reconcile the stale incomplete_composition flag separately.","source_stage":"comparison
    metadata only","sources":[{"evidence_id":"solution6129","reference":"https://mediadive.dsmz.de/rest/solution/6129","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6129.bin","raw_sha256":"4ee096d7a46e81f2dc9699c9abd6b7d4721d60dd543b419c417ca5bd818bff99","text_sha256":"890726a4d9ccb3f06d639088a2d40a47ac9cd5c6a178682dd138f4332f5b7537","accessed_at":"2026-10-28T16:12:46.437238Z","locator":"data.name","quote":"\"name\":
    \"Trace elements solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml","field_path":"ingredients[0].concentration","decision":"not_quantified","rationale":"This
    synthetic See source for composition placeholder is not a chemical ingredient
    or a supported quantity. The explicit composition exists; keep it out of positive
    recipe evidence and reconcile the stale incomplete_composition flag separately."}]},{"quantity_id":"q47","label":"Comparison
    solution6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\":
    847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882."}]},{"quantity_id":"q48","label":"Comparison solution6241
    Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The
    existing attached exact raw snippet, stated digest, row identity and explicit
    provider g_l support this unchanged stock-local concentration. This current-byte
    authentication does not recreate the original access event and does not make this
    stock equivalent to NBRC882."}]},{"quantity_id":"q49","label":"Comparison solution6241
    Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    separate solution6241 explicitly supplies 200 micrograms biotin and makes up to
    100 ml, supporting 0.002 g/L for this stock only; 2000.0 G_PER_L is inconsistent.
    This explicit final makeup is not transferred to NBRC882 or its distinct nine-vitamin
    stock.","source_stage":"independent comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","decision":"conflict","rationale":"The
    separate solution6241 explicitly supplies 200 micrograms biotin and makes up to
    100 ml, supporting 0.002 g/L for this stock only; 2000.0 G_PER_L is inconsistent.
    This explicit final makeup is not transferred to NBRC882 or its distinct nine-vitamin
    stock."}]},{"quantity_id":"q50","label":"Comparison solution6241 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The
    separate solution6241 source instructs makeup to 100 ml with water. Stored 1000.0
    PERCENT_V_V is not that instruction. Retain the explicit final-stock makeup rather
    than assert an unsupported solvent percentage or receiving-medium dose.","source_stage":"independent
    comparison stock only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","decision":"conflict","rationale":"The
    separate solution6241 source instructs makeup to 100 ml with water. Stored 1000.0
    PERCENT_V_V is not that instruction. Retain the explicit final-stock makeup rather
    than assert an unsupported solvent percentage or receiving-medium dose."}]},{"quantity_id":"q51","label":"Comparison
    solution6241 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"This
    synthetic See source for composition placeholder is not a chemical ingredient
    or a supported quantity. The explicit composition exists; keep it out of positive
    recipe evidence and reconcile the stale incomplete_composition flag separately.","source_stage":"comparison
    metadata only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.name","quote":"\"name\":
    \"Vitamin solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","decision":"not_quantified","rationale":"This
    synthetic See source for composition placeholder is not a chemical ingredient
    or a supported quantity. The explicit composition exists; keep it out of positive
    recipe evidence and reconcile the stale incomplete_composition flag separately."}]},{"quantity_id":"q52","label":"Comparison6241
    retained final makeup","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make
    up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The
    existing preparation correctly retains the source final makeup to 100 ml. Credit
    it independently of the erroneous biotin/water fields and do not transfer this
    basis to NBRC882.","source_stage":"comparison stock preparation","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch072/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T16:12:46.444967Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The
    existing preparation correctly retains the source final makeup to 100 ml. Credit
    it independently of the erroneous biotin/water fields and do not transfer this
    basis to NBRC882."}]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml":["composition","ingredients[0]"],"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":["composition","ingredients[0]","preparation_notes"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Every asserted CHEBI object, label and packaged MIM slot is checked. All
    canonical labels resolve, yet the cobalt/nickel hydrate and calcium-pantothenate
    anion/salt assertions are wrong supplied forms. Generic resazurin is retained
    without importing a sodium-salt claim. Generic B12 is not silently narrowed to
    cyanocobalamin, and calcium-salt stereochemistry remains unspecified. Compatible
    other salts, hydrates, acids and vitamins are unchanged; exact MIM preferred-row
    rejection does not overturn independent source/form evidence.
  target_ids:
  - CultureMech:008235
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All eight complete historical reports and two selected plan rows were read,
    including the distinct CM002108 DSM935 comparison and September CM008235 report.
    Seven current dependency raw snippets/digests authenticate content, not original
    access events. Current TOGO stock separation/unit conversion/comment behavior,
    name-based stock migration, duplicate repair/cleanup, grounding migrations and
    conservative merger were read. The normalized water repair is credited; generated
    staleness and mixed calcium parts remain. Original histories are preserved; no
    native diagnostics were rerun.
  target_ids:
  - CultureMech:008235
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-008235-units-and-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore source units and separate three recipe stages
  description: Water, calcium, resazurin, vitamin and stock-dose fields combine unrelated
    stages or retain raw numerals with incompatible units. The owner corrected the
    summed water from 3.0 to 1.0, but both retain G_PER_L; generated output is stale.
    Calcium still combines 0.147 g main and 0.1 g stock masses. Twelve other trace
    constituents and nine vitamin constituents remain flattened; resazurin and all
    nine vitamin rows lose their mg units. Preserve source batch amounts and distinct
    1 ml stock additions, with all three 1 L water inputs separate. A solvent input
    is not final volume.
  target_ids:
  - CultureMech:008235
  field_paths:
  - ingredients
  - solutions
  - evidence
  evidence_ids:
  - nbrc882
  - togo1677
  - writer-togo
  - writer-cleanup
  - writer-duplicate-repair
  rule_id: review-yaml-record/custom-units-and-stock-stage
  native_severity: P2
  normalization_reason: 'Custom quantity rule: material source-stage, supplied-form
    or quantitative representation conflict; major repair required.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-008235-wrong-stock-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Replace name-only stock identity with exact NBRC882 definitions
  description: Both 1 ml source additions refer to the locally defined M1677 stocks.
    Linked MediaDive6129 instead contains five differently composed mineral salts;
    6241 contains three vitamins and a 100 ml final-stock makeup, not the NBRC nine-vitamin
    recipe. Their valid local source claims do not support equivalence. Resolve the
    exact trace and vitamin definitions, retaining the original source scope, and
    replace both Unknown solution display placeholders. Current name-only migration
    is an observed risk, not proof of its exact historic execution.
  target_ids:
  - CultureMech:008235
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[0].name
  - solutions[1].name
  evidence_ids:
  - nbrc882
  - togo1677
  - solution6129
  - solution6241
  - writer-stock-match
  rule_id: review-yaml-record/custom-wrong-stock-identity
  native_severity: P2
  normalization_reason: 'Custom identity rule: material source-stage, supplied-form
    or quantitative representation conflict; major repair required.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-008235-missing-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Restore main and stock-local preparation without borrowing conditions
  description: The source gas stages, 80/20 mixture, separate sulfide 5% solution,
    filter-sterile late vitamin addition, anaerobic additions and 150 kPa pressure
    are missing from maintained/generated preparation. The trace-stock pH 6.5 then
    7.0 sequence belongs to that stock. Preserve all exact comments and bind claims
    at the schema-supported root evidence field with explicit paths. Keep unknown
    temperature, duration, pressure reference and percent basis unknown; the gas VARIABLE
    placeholders themselves do not assert false numeric amounts.
  target_ids:
  - CultureMech:008235
  field_paths:
  - preparation_steps
  - solutions
  - ingredients[25]
  - evidence
  evidence_ids:
  - nbrc882
  - togo1677
  - writer-togo
  rule_id: review-yaml-record/custom-missing-preparation
  native_severity: P2
  normalization_reason: 'Custom completeness rule: material source-stage, supplied-form
    or quantitative representation conflict; major repair required.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-008235-supplied-form-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct cobalt, nickel and calcium-pantothenate supplied forms
  description: CoCl2·6H2O is mapped to anhydrous CHEBI:35696; NiCl2·6H2O uses anhydrous
    CHEBI:34887 in both slots. Ca-pantothenate is mapped in both slots to CHEBI:29032,
    the (R)-pantothenate anion lacking calcium. Verify exact supplied-form objects
    and canonical labels without inventing calcium-salt stereochemistry. Other named
    hydrates, generic resazurin, sodium tungstate/selenate and generic vitamin B12
    are compatible with the primary wording. Preserve current MIM REJECTED versus
    MAPPED row statuses rather than treating membership as chemical proof.
  target_ids:
  - CultureMech:008235
  field_paths:
  - ingredients[17].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  - ingredients[29].term
  - ingredients[29].mediaingredientmech_chebi_term
  evidence_ids:
  - nbrc882
  - togo1677
  - groundings
  - mim
  rule_id: review-yaml-record/custom-supplied-form-grounding
  native_severity: P2
  normalization_reason: 'Custom grounding rule: material source-stage, supplied-form
    or quantitative representation conflict; major repair required.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-008235-comparison6241-amounts
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Correct separate solution6241 biotin and water representations
  description: The independently referenced comparison stock6241 retains 2000.0 G_PER_L
    biotin and 1000.0 PERCENT_V_V water. Its exact source supplies 200 micrograms
    biotin and explicitly makes up to 100 ml; this supports 0.002 g/L biotin and a
    final-makeup instruction, not those stored values. Its existing cyanocobalamin/thiamine
    source claims and retained preparation remain credited. Curate this stock separately;
    it is not the NBRC882 vitamin recipe.
  target_ids:
  - CultureMech:008235
  field_paths:
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[2].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[3].concentration
  evidence_ids:
  - dep6241
  - solution6241
  - old-claims
  rule_id: review-yaml-record/custom-comparison6241-amounts
  native_severity: P2
  normalization_reason: 'Custom quantity rule: material source-stage, supplied-form
    or quantitative representation conflict; major repair required.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
- finding_id: f6
  issue_key: culturemech-008235-classification-and-secondary-gaps
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Review defined composition and remaining secondary links
  description: The complete NBRC882 formula contains named chemical substances rather
    than an undefined complex extract; review the inherited COMPLEX/UNDEFINED classification
    against this exact composition. MnCl2·4H2O and CoCl2·6H2O also lack secondary
    MIM/CHEBI links, while gas placeholders have primary identity only. Preserve those
    known identities and fix cobalt form before adding links; absence from an exact
    preferred spelling is not absence of the identifier from the full index.
  target_ids:
  - CultureMech:008235
  field_paths:
  - medium_type
  - composition_type
  - ingredients[16]
  - ingredients[17]
  evidence_ids:
  - target
  - owner
  - nbrc882
  - groundings
  - mim
  rule_id: review-yaml-record/custom-classification-and-secondary-gaps
  native_severity: P3
  normalization_reason: 'Custom completeness rule: bounded classification, linkage
    or provenance follow-up; minor severity, without redefining a native numbered
    rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
- finding_id: f7
  issue_key: culturemech-008235-evidence-history-scope
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Keep claim credit and historical limits explicit
  description: The selected medium has no attached concentration claims, while seven
    exact claims on comparison6129/6241 are authenticated against current raw bytes
    and digests. Earlier October no-source-check rows and September denominator/dilution
    recommendations are not independent source proof; retain literal masses and avoid
    their assumed final liter. The owner water repair is valid limited local history,
    not complete source curation. Preserve original events, including timezone-naive
    dependency events, and append verified context. Reconcile each comparison stock
    placeholder/incomplete_composition flag with its present composition without claiming
    all remaining quantities are curated.
  target_ids:
  - CultureMech:008235
  field_paths:
  - evidence
  - curation_history
  - data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::data_quality_flags
  evidence_ids:
  - old-reports
  - history
  - old-claims
  - writer-duplicate-repair
  rule_id: review-yaml-record/custom-evidence-history-scope
  native_severity: P3
  normalization_reason: 'Custom provenance rule: bounded classification, linkage or
    provenance follow-up; minor severity, without redefining a native numbered rule.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: Water, calcium, resazurin, vitamin and stock-dose fields combine unrelated
    stages or retain raw numerals with incompatible units. The owner corrected the
    summed water from 3.0 to 1.0, but both retain G_PER_L; generated output is stale.
    Calcium still combines 0.147 g main and 0.1 g stock masses. Twelve other trace
    constituents and nine vitamin constituents remain flattened; resazurin and all
    nine vitamin rows lose their mg units. Preserve source batch amounts and distinct
    1 ml stock additions, with all three 1 L water inputs separate. A solvent input
    is not final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008235
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
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
  description: Both 1 ml source additions refer to the locally defined M1677 stocks.
    Linked MediaDive6129 instead contains five differently composed mineral salts;
    6241 contains three vitamins and a 100 ml final-stock makeup, not the NBRC nine-vitamin
    recipe. Their valid local source claims do not support equivalence. Resolve the
    exact trace and vitamin definitions, retaining the original source scope, and
    replace both Unknown solution display placeholders. Current name-only migration
    is an observed risk, not proof of its exact historic execution.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008235
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
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
  description: The source gas stages, 80/20 mixture, separate sulfide 5% solution,
    filter-sterile late vitamin addition, anaerobic additions and 150 kPa pressure
    are missing from maintained/generated preparation. The trace-stock pH 6.5 then
    7.0 sequence belongs to that stock. Preserve all exact comments and bind claims
    at the schema-supported root evidence field with explicit paths. Keep unknown
    temperature, duration, pressure reference and percent basis unknown; the gas VARIABLE
    placeholders themselves do not assert false numeric amounts.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008235
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
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
  description: CoCl2·6H2O is mapped to anhydrous CHEBI:35696; NiCl2·6H2O uses anhydrous
    CHEBI:34887 in both slots. Ca-pantothenate is mapped in both slots to CHEBI:29032,
    the (R)-pantothenate anion lacking calcium. Verify exact supplied-form objects
    and canonical labels without inventing calcium-salt stereochemistry. Other named
    hydrates, generic resazurin, sodium tungstate/selenate and generic vitamin B12
    are compatible with the primary wording. Preserve current MIM REJECTED versus
    MAPPED row statuses rather than treating membership as chemical proof.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008235
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
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
  description: The independently referenced comparison stock6241 retains 2000.0 G_PER_L
    biotin and 1000.0 PERCENT_V_V water. Its exact source supplies 200 micrograms
    biotin and explicitly makes up to 100 ml; this supports 0.002 g/L biotin and a
    final-makeup instruction, not those stored values. Its existing cyanocobalamin/thiamine
    source claims and retained preparation remain credited. Curate this stock separately;
    it is not the NBRC882 vitamin recipe.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008235
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a6
  description: The complete NBRC882 formula contains named chemical substances rather
    than an undefined complex extract; review the inherited COMPLEX/UNDEFINED classification
    against this exact composition. MnCl2·4H2O and CoCl2·6H2O also lack secondary
    MIM/CHEBI links, while gas placeholders have primary identity only. Preserve those
    known identities and fix cobalt form before adding links; absence from an exact
    preferred spelling is not absence of the identifier from the full index.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:008235
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a7
  description: The selected medium has no attached concentration claims, while seven
    exact claims on comparison6129/6241 are authenticated against current raw bytes
    and digests. Earlier October no-source-check rows and September denominator/dilution
    recommendations are not independent source proof; retain literal masses and avoid
    their assumed final liter. The owner water repair is valid limited local history,
    not complete source curation. Preserve original events, including timezone-naive
    dependency events, and append verified context. Reconcile each comparison stock
    placeholder/incomplete_composition flag with its present composition without claiming
    all remaining quantities are curated.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:008235
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1677_Deferribacter_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6129_Trace_elements_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
  acceptance_checks:
  - Keep all original history and reports byte-preserved; append verified context
    in a new actual event.
  - Retain seven authenticated existing stock claims; qualify exact current-byte authentication
    separately from historical access provenance and receiving-medium equivalence.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- NBRC882 and TOGO1677 give batch masses and solvent inputs, not explicit final main
  or local-stock volumes. No mg/L, g/L or stock dilution is inferred from water alone.
- The generic calcium-pantothenate source does not establish D/R stereochemistry;
  verify the calcium salt without silently selecting a more specific variant. The
  neutral resazurin source wording does not establish sodium resazurin.
- MediaDive6241 does explicitly state its own final makeup to 100 ml; that distinct
  basis supports its comparison-stock correction only. The two synthetic stock placeholder
  ingredients are not positive composition evidence.
- No primary organism-specific growth claim is supplied by NBRC882 or TOGO1677. The
  DSM935 same-name report is historical comparison context only, not an alternative
  recipe to adopt.
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
