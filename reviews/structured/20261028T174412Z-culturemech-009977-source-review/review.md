# Scientific review: Desulfatibacillus Olefinivorans Medium

- Review: 20261028T174412Z-culturemech-009977-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T17:19:30.418467Z
- Finished UTC: 2026-10-28T17:44:12.502891Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Four major source-stage, preparation, hydrate and current section-routing issues plus one minor evidence/catalog follow-up require maintained-input curation. Every selected and explicitly scoped dependency concentration is accounted for; no recipe was changed.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch073 index 08
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009977 | data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml | generated | desulfatibacillus_olefinivorans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009977 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009977 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009977 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009977 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact selected and stock-source crosswalks

identity: supported. Targets: CultureMech:009977.

TOGO M581 identifies JCM576. JCM431/M431 contributes only Se/W stock, and JCM403/M401 only its vitamin/thiamine/B12 preparations. Neighboring historical Desulfatiferula and BN3 whole formulations remain comparison context.

### Complex liquid formulation

consistency: supported. Targets: CultureMech:009977.

The yeast-containing formulation supports complex, semi-defined and liquid classification. No organism growth claim is inferred.

### Original diagnostics

schema: supported. Targets: CultureMech:009977.

All four original canonical diagnostics passed once, including zero reference checks. They do not resolve scientific unit/stage or chemical-form issues.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009977.

76 current concentration fields are covered by 50 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b073-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","quantity_field_count":76,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"961.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"961.0","unit":"G_PER_L"}},{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[0].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 960.0, 1.0]"},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[0].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 960.0, 1.0]"}],"decision":"correct","rationale":"The stored961 G_PER_L sums960 mL main input and1 L SL12 input without converting units or preserving stages. Restore separate source volume inputs, with no measured-final-volume inference.","source_stage":"separate main and SL12 water inputs","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;960.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 960,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"7","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"7","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;7.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 7,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.15&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.2&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary and TOGO row specify1 mg resazurin, not1 G_PER_L. Preserve the source mass and stage before considering any concentration basis.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"Na2SO4\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"HEPES","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.38","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.38","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; HEPES                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.38&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"HEPES\",\n          \"volume\": 2.38,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001142\",\n          \"gmo_id\": \"GMO_001142\",\n          \"label\": \"HEPES\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Yeast extract (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960 mL input water plus later additions is not an explicit final-volume statement. Retain the mass as evidence; do not substitute the provider nominal1005 mL rates as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves dissolved concentration unspecified. Retain that uncertainty while separately recording source gas-handling stages and the4:1 v/v atmosphere; a gas-phase ratio is not a dissolved mass concentration.","source_stage":"gas-handling context","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients, adjust pH to 7.5 and autoclave under a N2 atmosphere. After cooling, add the following stock solutions (filter--sterilized or *autoclaved) to the solution:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Sodium palmitate","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.8","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The primary specifies2.8 g substrate in a separately autoclaved stage. Its numeric mass is supported, but no independently measured final volume establishes the local G_PER_L basis.","source_stage":"separately prepared substrate","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium palmitate                                        &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.8&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Sodium palmitate\",\n          \"volume\": 2.8,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001651\",\n          \"gmo_id\": \"GMO_001651\",\n          \"label\": \"Sodium palmitate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves dissolved concentration unspecified. Retain that uncertainty while separately recording source gas-handling stages and the4:1 v/v atmosphere; a gas-phase ratio is not a dissolved mass concentration.","source_stage":"gas-handling context","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 7,\n      \"comment\": \"To complete the medium, combine Solution A and substrate in the culture vessels under a N2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Finally, reduce the medium with 0.01 volume of 5% Na2S・9H2O solution (autoclaved and stored under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Nitrogen gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves dissolved concentration unspecified. Retain that uncertainty while separately recording source gas-handling stages and the4:1 v/v atmosphere; a gas-phase ratio is not a dissolved mass concentration.","source_stage":"gas-handling context","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\": \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 7,\n      \"comment\": \"To complete the medium, combine Solution A and substrate in the culture vessels under a N2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Finally, reduce the medium with 0.01 volume of 5% Na2S・9H2O solution (autoclaved and stored under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Na2MoO4・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;18.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 18,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"300","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"300","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;300.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 300,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"FeSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[3]","quote":"{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 1.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"MnCl2・4H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;50.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[4]","quote":"{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"CoCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"190","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[5]","quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"NiCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[6]","quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"CuCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[7]","quote":"{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"42","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;42.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[8]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 42,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"EDTA・2Na","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve its exact source g or mg amount and1 L stock input water; seven mg entries must not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; EDTA&amp;#183;2Na                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[9]","quote":"{\n          \"component_name\": \"EDTA・2Na\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001058\",\n          \"gmo_id\": \"GMO_001058\",\n          \"label\": \"Disodium EDTA\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Trace metal solution SL12 (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a liquid addition in mL at its named stage, not G_PER_L of a neat component. Restore the stock name/composition or exact scoped reference. No density or final-volume conversion is supported.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Trace metal solution SL12 (see below)\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M581\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution SL12 (see below)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Selenite--tungstate solution (see Medium [M431])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a liquid addition in mL at its named stage, not G_PER_L of a neat component. Restore the stock name/composition or exact scoped reference. No density or final-volume conversion is supported.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M431\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Selenite-tungstate solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=431\"&gt;431&lt;/a&gt;)     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"8% NaHCO3 solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a liquid addition in mL at its named stage, not G_PER_L of a neat component. Restore the stock name/composition or exact scoped reference. No density or final-volume conversion is supported. Retain the printed stock percentage with its unspecified basis and the distinct sterilization marker.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"15% MgCl2・6H2O solution*","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a liquid addition in mL at its named stage, not G_PER_L of a neat component. Restore the stock name/composition or exact scoped reference. No density or final-volume conversion is supported. Retain the printed stock percentage with its unspecified basis and the distinct sterilization marker.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"15% MgCl2・6H2O solution*\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 15,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001286\",\n          \"gmo_id\": \"GMO_001286\",\n          \"label\": \"Magnesium chloride hexahydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 15% MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O solution*                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Vitamin solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a liquid addition in mL at its named stage, not G_PER_L of a neat component. Restore the stock name/composition or exact scoped reference. No density or final-volume conversion is supported.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"Vitamin solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Thiamine solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a liquid addition in mL at its named stage, not G_PER_L of a neat component. Restore the stock name/composition or exact scoped reference. No density or final-volume conversion is supported.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Vitamin B12 solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a liquid addition in mL at its named stage, not G_PER_L of a neat component. Restore the stock name/composition or exact scoped reference. No density or final-volume conversion is supported.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Vitamin B12 solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\"&gt;403&lt;/a&gt;)       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Na2S・9H2O solutions","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary gives0.01 volume of a5% Na2S nonahydrate stock, not an unconditional10 mL or10 G_PER_L amount. Preserve its relative-volume basis and unspecified percentage basis; TOGO10 mL is a source-view normalization requiring reconciliation.","source_stage":"stock receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Na2S・9H2O solutions\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 5,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\": \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"exact text from 'To complete the medium,' through 'Trace metal solution SL12:'","quote":"To complete the medium, combine Solution A and substrate in the culture vessels under a N\n2\n-CO\n2\n(4:1, v/v) gas mixture and seal with butyl rubber stoppers. Finally, reduce the medium with 0.01 volume of 5% Na\n2\nS·9H\n2\nO solution (autoclaved and stored under a N\n2\natmosphere).\nTrace metal solution SL12:","quote_basis":"derivative text"}]},{"quantity_id":"q32","label":"M431 Na2SeO3・5H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"The input belongs to the Se/W stock only. Preserve the primary milligram selenium/tungsten amounts and0.4 g NaOH against1 L input water; local direct-medium G_PER_L does not preserve that stock boundary.","source_stage":"Se/W stock input","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Na2SeO3・5H2O\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML table row 30 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;3&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"M431 Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The input belongs to the Se/W stock only. Preserve the primary milligram selenium/tungsten amounts and0.4 g NaOH against1 L input water; local direct-medium G_PER_L does not preserve that stock boundary.","source_stage":"Se/W stock input","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 8,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML table row 31 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"M431 NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"correct","rationale":"The input belongs to the Se/W stock only. Preserve the primary milligram selenium/tungsten amounts and0.4 g NaOH against1 L input water; local direct-medium G_PER_L does not preserve that stock boundary.","source_stage":"Se/W stock input","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\": \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\": \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML table row 29 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaOH                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.4&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"M431 merged water","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"989.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[11].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 1.0, 987.0, 1.0]"}],"decision":"correct","rationale":"This shared989 G_PER_L descriptor combines three differently scoped water inputs. Only the Se/W1 L input is transferable here; split the descriptor with full parent curation and do not treat the whole989 as stock water.","source_stage":"ambiguous shared water with Se/W contribution","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML table row 32 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"M401 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"M401 p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"4","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 4,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;4.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"M401 Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"M401 Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"M401 Sodium phosphate buffer (10 mM, pH 7.1)","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup. Retain the explicit buffer molarity and pH, without inferring its individual phosphate-salt recipe.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Sodium phosphate buffer (10 mM, pH 7.1)\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001124\",\n          \"gmo_id\": \"GMO_001124\",\n          \"label\": \"Sodium phosphate buffer\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium phosphate buffer (10 mM, pH 7.1)               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"M401 DL--Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"DL--Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001936\",\n          \"gmo_id\": \"GMO_001936\",\n          \"label\": \"DL-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; DL-Calcium pantothenate                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"M401 Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"M401 Sodium phosphate buffer (25 mM, pH 3.4)","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup. Retain the explicit buffer molarity and pH, without inferring its individual phosphate-salt recipe.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Sodium phosphate buffer (25 mM, pH 3.4)\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001124\",\n          \"gmo_id\": \"GMO_001124\",\n          \"label\": \"Sodium phosphate buffer\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium phosphate buffer (25 mM, pH 3.4)               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"M401 Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve this exact input within its named vitamin, thiamine or B12 preparation; it is not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer volumes, without an independently stated final makeup.","source_stage":"referenced vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"M401 merged water","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"101.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[0].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 1.0, 100.0]"}],"decision":"correct","rationale":"The101 G_PER_L descriptor combines parent1 L and B12-stock100 mL inputs. Only the B12 water is in receiving-record scope; preserve it separately without transferring parent water.","source_stage":"B12 stock water contribution","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Missing source preparation 1","local_fields":[],"decision":"evidence_only","rationale":"Preserve the exact main/stock/substrate stage, pH and atmosphere from this source instruction. The source gas ratio is not a dissolved concentration and relative reductant volume is not an unconditional mL dose.","source_stage":"source preparation controls","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients, adjust pH to 7.5 and autoclave under a N2 atmosphere. After cooling, add the following stock solutions (filter--sterilized or *autoclaved) to the solution:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Missing source preparation 2","local_fields":[],"decision":"evidence_only","rationale":"Preserve the exact main/stock/substrate stage, pH and atmosphere from this source instruction. The source gas ratio is not a dissolved concentration and relative reductant volume is not an unconditional mL dose.","source_stage":"source preparation controls","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"Autoclave in culture vessels.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Missing source preparation 3","local_fields":[],"decision":"evidence_only","rationale":"Preserve the exact main/stock/substrate stage, pH and atmosphere from this source instruction. The source gas ratio is not a dissolved concentration and relative reductant volume is not an unconditional mL dose.","source_stage":"source preparation controls","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 7,\n      \"comment\": \"To complete the medium, combine Solution A and substrate in the culture vessels under a N2--CO2 (4:1, v/v) gas mixture and seal with butyl rubber stoppers. Finally, reduce the medium with 0.01 volume of 5% Na2S・9H2O solution (autoclaved and stored under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"SL12 input water","local_fields":[],"decision":"evidence_only","rationale":"The1 L is stock solvent input, not a separately stated final makeup.","source_stage":"SL12 stock water","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"JCM default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The source default121°C/15 min applies only where not otherwise stated; preserve the separate filter-sterilization and starred autoclave exceptions.","source_stage":"source default","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"exact text from 'Unless otherwise stated,' through '15 min.'","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml":["ingredients[11]","ingredients[27]","ingredients[28]","ingredients[29]"],"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml":["ingredients[0]","ingredients[17]","ingredients[18]","ingredients[19]","ingredients[20]","ingredients[21]","ingredients[22]","ingredients[23]","ingredients[24]","ingredients[25]"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009977.

Current exact asserted ontology objects and packaged MIM rows are assessed independently of supplied-form correspondence. Cobalt/nickel hydration contradicts two asserted terms. Source EDTA lacks a hydrate designation, so the anhydrous-specific term remains a specificity limit rather than a confirmed substitute. Vitamin B12 is a broad class; no vitamer is inferred. Existing HEPES secondary membership and scoped DL-calcium legacy linkage need bounded catalog reconciliation, with separate presence and validity populations.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:009977.

All thirteen historical report scopes were read through the lossless pool: three selected/direct-scope October reviews were source-unchecked, and dependency/sibling September findings are contextual evidence, not new source authentication. Current M431/M401 stock fields remain uncorrected in the scoped sections. Current cleanup no longer sums conflicts; current TOGO unit/stage handling and conservative formulation merging are credited while its named-section routing issue is demonstrated separately.

## Findings

### f1: Reconstruct source stages and source amount units

major / open / confirmed; issue key: culturemech-009977-stock-units.

The selected water sum combines main and SL12 inputs; resazurin1 mg and multiple SL12 mg inputs became G_PER_L, while eight liquid or relative-volume additions use mass units. Restore Solution A, separate substrate and named stocks without assuming final volume. Preserve the primary0.01-volume5% reductant instruction and explicitly reconcile TOGO10 mL. Resolve only M431 Se/W and M401 vitamin/thiamine/B12 subsections; repair their scoped mg/mL fields and shared-water contributions without importing parent quantities.

### f2: Restore the omitted staged source preparation

major / open / confirmed; issue key: culturemech-009977-missing-preparation.

The record omits Solution A pH7.5 and its N2 treatment, post-cooling stock sterilization distinctions, separately treated substrate,4:1 N2/CO2 assembly and relative reductant step. Preserve these exact source stages and JCM default exceptions. VARIABLE gas placeholders need no invented dissolved concentrations.

### f3: Resolve explicit cobalt and nickel hexahydrates

major / open / confirmed; issue key: culturemech-009977-hydrate-identity.

SL12 CoCl2·6H2O and NiCl2·6H2O are asserted as anhydrous CHEBI35696 and34887. Current exact53503 and53542 objects confirm distinct hydrated identities. Correct supplied-form correspondence without changing source masses or inferring unprinted hydrates for EDTA.

### f4: Preserve named basal and substrate sections in the current importer

major / open / confirmed; issue key: culturemech-009977-current-import-section.

Current _is_primary_section accepts only unnamed or main solution N sections. The inspected M581 payload has named Solution A and Substrate plus main solution1/2, so current _extract_primary_components selects the latter and skips the named basal/substrate sections. Repair that exact section-routing boundary while retaining current unit/stage improvements; do not rerun an importer or regenerate this medium until source fidelity is checked.

### f5: Attach claims and reconcile bounded catalog links

minor / open / confirmed; issue key: culturemech-009977-evidence-catalog.

No scoped selected or dependency quantity claims are attached. Preserve historical reports as earlier incomplete reviews and append exact new evidence after curation. Replace Unknown solution names with source-supported names. HEPES CHEBI46756 is active but its existing secondary slot has no exact packaged MIM row; scoped M401 retains legacy000926 for DL-calcium pantothenate. Resolve these catalog links without equating current absence with ontology obsolescence or replacing DL with a D-only term.

## Recommended Actions And Acceptance Checks

### a1

The selected water sum combines main and SL12 inputs; resazurin1 mg and multiple SL12 mg inputs became G_PER_L, while eight liquid or relative-volume additions use mass units. Restore Solution A, separate substrate and named stocks without assuming final volume. Preserve the primary0.01-volume5% reductant instruction and explicitly reconcile TOGO10 mL. Resolve only M431 Se/W and M401 vitamin/thiamine/B12 subsections; repair their scoped mg/mL fields and shared-water contributions without importing parent quantities.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The record omits Solution A pH7.5 and its N2 treatment, post-cooling stock sterilization distinctions, separately treated substrate,4:1 N2/CO2 assembly and relative reductant step. Preserve these exact source stages and JCM default exceptions. VARIABLE gas placeholders need no invented dissolved concentrations.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

SL12 CoCl2·6H2O and NiCl2·6H2O are asserted as anhydrous CHEBI35696 and34887. Current exact53503 and53542 objects confirm distinct hydrated identities. Correct supplied-form correspondence without changing source masses or inferring unprinted hydrates for EDTA.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Current _is_primary_section accepts only unnamed or main solution N sections. The inspected M581 payload has named Solution A and Substrate plus main solution1/2, so current _extract_primary_components selects the latter and skips the named basal/substrate sections. Repair that exact section-routing boundary while retaining current unit/stage improvements; do not rerun an importer or regenerate this medium until source fidelity is checked.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

No scoped selected or dependency quantity claims are attached. Preserve historical reports as earlier incomplete reviews and append exact new evidence after curation. Replace Unknown solution names with source-supported names. HEPES CHEBI46756 is active but its existing secondary slot has no exact packaged MIM row; scoped M401 retains legacy000926 for DL-calcium pantothenate. Resolve these catalog links without equating current absence with ontology obsolescence or replacing DL with a D-only term.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm576 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576; REVIEW_WORK/batch073/source07-08-10/jcm576.json; exact original raw/text/hash/time metadata | context_only | Exact selected JCM576 primary source. |
| apiJ576 | https://mediadive.dsmz.de/rest/medium/J576; REVIEW_WORK/batch073/source07-08-10/apiJ576.json; exact original raw/text/hash/time metadata | context_only | J576 provider comparison, distinct from current original JCM source. |
| currentTogo581 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581; REVIEW_WORK/batch073/source07-08-10/currentTogo581.json; exact original raw/text/hash/time metadata | context_only | Selected full TOGO M581 recipe |
| jcm431 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431; REVIEW_WORK/batch073/source07-08-10/jcm431.json; exact original raw/text/hash/time metadata | context_only | JCM431 selenite-tungstate subsection only; parent formulation excluded. |
| currentTogo431 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431; REVIEW_WORK/batch073/source07-08-10/currentTogo431.json; exact original raw/text/hash/time metadata | context_only | M431 selenite-tungstate stock only; parent recipe excluded |
| jcm403 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403; REVIEW_WORK/batch073/source07-08-10/jcm403.json; exact original raw/text/hash/time metadata | context_only | JCM403 vitamin, thiamine and B12 stock subsections only; parent basal and receiving doses excluded. |
| currentTogo401 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401; REVIEW_WORK/batch073/source07-08-10/currentTogo401.json; exact original raw/text/hash/time metadata | context_only | M401 vitamins/thiamine/B12 stock subsections only; parent recipe and receiving doses excluded |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch073/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch073/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfatiferula_berrense_medium__83f13d53.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-28 | reports/yaml_record_review/20260921T083439Z-ACETOBACTERIUM_SUBMARINUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-29 | reports/yaml_record_review/20260921T131114Z-anoxic_medium_for_strain_acbe2_1.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-30 | reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-31 | reports/yaml_record_review/20260921T231153Z-bn3_medium__59600ad0.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| dep-Se | data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml; Explicit document_scopes in quantity inventory | context_only | Full dependency context read; scientific assessment is limited to the declared stock fields and ambiguous merged-water descriptor, excluding parent-medium quantities, receiving doses and other stocks. |
| dep-vitamin | data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml; Explicit document_scopes in quantity inventory | context_only | Full dependency context read; scientific assessment is limited to the declared stock fields and ambiguous merged-water descriptor, excluding parent-medium quantities, receiving doses and other stocks. |
| writer-togo | src/culturemech/import/togo_importer.py; _is_primary_section; _extract_primary_components; _parse_unit; _extract_preparation_steps | context_only | Current parser preserves stock stages and maps ml to ML_PER_L and l to L, unlike these old fields. Its primary-section predicate recognizes only unnamed/main-solution sections: in current M581, presence of main solution1/2 excludes named Solution A and Substrate from primary extraction. Static current-code finding only, not historical execution proof. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group does not sum conflicting quantities; it retains the first and flags them. Historical water sums must not be attributed to unchanged current behavior. |
| writer-migration | scripts/migrate_solutions_from_ingredients.py; _resolve_solution; _migrate_media_file | context_only | Current _resolve_solution preserves existing concentration and creates referenced or empty stubs; _migrate_media_file moves detected solution rows and appends history. It does not repair the copied quantity basis. |
| historical-reading | REVIEW_WORK/batch073/record08/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch073/record08/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch073/record08/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch073/record08/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch073/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch073/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch073/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch073/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch073/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch073/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch073/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch073/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi46756 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756; REVIEW_WORK/batch073/source07-08-10/chebi46756.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; REVIEW_WORK/batch073/source07-08-10/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi234557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_234557; REVIEW_WORK/batch073/source07-08-10/chebi234557.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; REVIEW_WORK/batch073/source07-08-10/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch073/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch073/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; REVIEW_WORK/batch073/source07-08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch073/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; REVIEW_WORK/batch073/source07-08-10/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch073/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch073/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch073/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734; REVIEW_WORK/batch073/source07-08-10/chebi64734.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; REVIEW_WORK/batch073/source07-08-10/chebi131361.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; REVIEW_WORK/batch073/source07-08-10/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; REVIEW_WORK/batch073/source07-08-10/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch073/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch073/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch073/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch073/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch073/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch073/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch073/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch073/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch073/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch073/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch073/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch073/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch073/record08/existing-claim-authentication.json; Complete sidecar | context_only | The scoped existing-claim authentication sidecar is empty: no attached claims are asserted or authenticated here. Historical source-object correspondence is documented separately by historical-object-joins. |
| check-schema | REVIEW_WORK/batch073/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch073/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch073/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch073/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- M431 parent medium, other trace stock and receiving doses are excluded; M401 basal/trace recipe, growth conditions and receiving doses are excluded. Shared merged-water descriptors are assessed only to identify the relevant stock contribution and the need for separate parent reconciliation.
- The primary0.01-volume reductant instruction and provider/TOGO absolute normalizations remain distinct. Unspecified percentage bases, EDTA hydration and vitamin identities are not invented.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T174412Z-culturemech-009977-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Desulfatibacillus Olefinivorans Medium'
started_at: '2026-10-28T17:19:30.418467Z'
finished_at: '2026-10-28T17:44:12.502891Z'
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
summary: Four major source-stage, preparation, hydrate and current section-routing
  issues plus one minor evidence/catalog follow-up require maintained-input curation.
  Every selected and explicitly scoped dependency concentration is accounted for;
  no recipe was changed.
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
  - path: data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml
    sha256: 400b50fcf43fa688d8a5793fd82b76838a36e8d6dd6f2c5f611dc65dd0904d35
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    sha256: 16bfd52c74b4968fb71d19de9eeec863417b8f1e5711a8e1413b7b0917cae25c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
    sha256: 08d5af4848a07f88a4a9a69965308368bdab83082a8ac7f337b9f239b10c9de9
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
    sha256: 56c93a375dbd090f5c559648722a46359964a01d1b6b9ab3225281a08d8d2b40
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md
    sha256: fe4feab50de92089379d903e0b47e6e7a2e92dc6f4822f4f7a81297f177c8dc4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.md
    sha256: 0aca89c79aa75ee3fe2aaf757c94b9041c9fa9942e7657d7f2d1b80f43823058
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md
    sha256: 621b5623818337fb8c650369b29975144ef31d41449a02885ea8ec7652da9d63
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md
    sha256: 089a797d0ea2b3ddc0a978f5aae488e26d54b8124a1aafcc992cf6032108cc49
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfatiferula_berrense_medium__83f13d53.md
    sha256: 6e8e04950af6a349456aa5237dc682e2da2034780adffe242d603e2ad1653eb8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md
    sha256: 59f87cd1f3b048e72411c775bb1c80c7bea3287c1c0ba712a3bcfe5c84d18abe
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
    sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.md
    sha256: 25c03d9bda1e63a093fb60ce4f43cf648fd4667df90e814c1a447437a3383da9
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
  selection: Authoritative batch073 index 08
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009977
targets:
- target_id: CultureMech:009977
  path: data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml
  label: desulfatibacillus_olefinivorans_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
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
  - CultureMech:009977
  command: just validate-schema data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml
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
  - CultureMech:009977
  command: just validate-strict data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml
    --out REVIEW_WORK/batch073/record08/strict.tsv --workers 1 --quiet
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
  - CultureMech:009977
  command: just validate-terms data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml
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
  - CultureMech:009977
  command: just validate-references data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm576
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576
  accessed_at: '2026-10-28T17:19:19.015593Z'
  locator: REVIEW_WORK/batch073/source07-08-10/jcm576.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected JCM576 primary source.
  snapshot_sha256: 25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4
- evidence_id: apiJ576
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J576
  accessed_at: '2026-10-28T17:19:19.132530Z'
  locator: REVIEW_WORK/batch073/source07-08-10/apiJ576.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: J576 provider comparison, distinct from current original JCM source.
  snapshot_sha256: 673cd469bf63fa0ab9c7130e78b41ed7c98232f0fe5c5a2ef2c24870e9227760
- evidence_id: currentTogo581
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581
  accessed_at: '2026-10-28T17:19:20.397490Z'
  locator: REVIEW_WORK/batch073/source07-08-10/currentTogo581.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Selected full TOGO M581 recipe
  snapshot_sha256: 0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd
- evidence_id: jcm431
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431
  accessed_at: '2026-10-28T17:19:19.719886Z'
  locator: REVIEW_WORK/batch073/source07-08-10/jcm431.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: JCM431 selenite-tungstate subsection only; parent formulation excluded.
  snapshot_sha256: cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50
- evidence_id: currentTogo431
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431
  accessed_at: '2026-10-28T17:19:20.429435Z'
  locator: REVIEW_WORK/batch073/source07-08-10/currentTogo431.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: M431 selenite-tungstate stock only; parent recipe excluded
  snapshot_sha256: e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570
- evidence_id: jcm403
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403
  accessed_at: '2026-10-28T17:19:19.716154Z'
  locator: REVIEW_WORK/batch073/source07-08-10/jcm403.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: JCM403 vitamin, thiamine and B12 stock subsections only; parent basal and
    receiving doses excluded.
  snapshot_sha256: b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61
- evidence_id: currentTogo401
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401
  accessed_at: '2026-10-28T17:19:20.447939Z'
  locator: REVIEW_WORK/batch073/source07-08-10/currentTogo401.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: M401 vitamins/thiamine/B12 stock subsections only; parent recipe and receiving
    doses excluded
  snapshot_sha256: 380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  accessed_at: '2026-10-28T17:19:26.461390Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T17:19:26.471716Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:34:21.072714Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 400b50fcf43fa688d8a5793fd82b76838a36e8d6dd6f2c5f611dc65dd0904d35
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T17:34:21.072881Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 08d5af4848a07f88a4a9a69965308368bdab83082a8ac7f337b9f239b10c9de9
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T17:34:21.072910Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T17:34:21.073221Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T17:34:21.073245Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T17:34:21.073266Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073292Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 56c93a375dbd090f5c559648722a46359964a01d1b6b9ab3225281a08d8d2b40
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/BN3_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073319Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: fe4feab50de92089379d903e0b47e6e7a2e92dc6f4822f4f7a81297f177c8dc4
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073343Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 0aca89c79aa75ee3fe2aaf757c94b9041c9fa9942e7657d7f2d1b80f43823058
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073366Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 621b5623818337fb8c650369b29975144ef31d41449a02885ea8ec7652da9d63
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/bn3_medium__59600ad0.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073389Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 089a797d0ea2b3ddc0a978f5aae488e26d54b8124a1aafcc992cf6032108cc49
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfatiferula_berrense_medium__83f13d53.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073412Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 6e8e04950af6a349456aa5237dc682e2da2034780adffe242d603e2ad1653eb8
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073434Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 59f87cd1f3b048e72411c775bb1c80c7bea3287c1c0ba712a3bcfe5c84d18abe
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073458Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1601590034c9aa40373c939b94267fbeddc72ae5b0f15de48f380cba97d1b965
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073480Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 25c03d9bda1e63a093fb60ce4f43cf648fd4667df90e814c1a447437a3383da9
- evidence_id: report-28
  kind: prior_review
  reference: reports/yaml_record_review/20260921T083439Z-ACETOBACTERIUM_SUBMARINUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073503Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1f5db491b2f11f287acd60655a5b0b44466da08a39cbd2a57fb467bf31ea2610
- evidence_id: report-29
  kind: prior_review
  reference: reports/yaml_record_review/20260921T131114Z-anoxic_medium_for_strain_acbe2_1.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073524Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 84e487ca27d245977a3572b823e5d447a44bbb8daa8a8715e49b7084e880b07c
- evidence_id: report-30
  kind: prior_review
  reference: reports/yaml_record_review/20260921T230801Z-BN3_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073546Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f7b264f4b7f3aa84c40ec049d8d89f48d67f8bd0cb7f723e250de0ecdc068b0a
- evidence_id: report-31
  kind: prior_review
  reference: reports/yaml_record_review/20260921T231153Z-bn3_medium__59600ad0.md
  locator: Complete report
  accessed_at: '2026-10-28T17:34:21.073567Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 9c4941a859f60a9fc2adc04147052815d6fcf04f9e0453326d98a5732260de19
- evidence_id: dep-Se
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
  locator: Explicit document_scopes in quantity inventory
  accessed_at: '2026-10-28T17:34:21.096342Z'
  support: context_only
  summary: Full dependency context read; scientific assessment is limited to the declared
    stock fields and ambiguous merged-water descriptor, excluding parent-medium quantities,
    receiving doses and other stocks.
  snapshot_sha256: 35c2b3264b82cf435135a02583fb7e004fe58bc46d6c0906db454950ea333cdc
- evidence_id: dep-vitamin
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
  locator: Explicit document_scopes in quantity inventory
  accessed_at: '2026-10-28T17:34:21.096377Z'
  support: context_only
  summary: Full dependency context read; scientific assessment is limited to the declared
    stock fields and ambiguous merged-water descriptor, excluding parent-medium quantities,
    receiving doses and other stocks.
  snapshot_sha256: 16bfd52c74b4968fb71d19de9eeec863417b8f1e5711a8e1413b7b0917cae25c
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _is_primary_section; _extract_primary_components; _parse_unit; _extract_preparation_steps
  accessed_at: '2026-10-28T17:34:21.101814Z'
  support: context_only
  summary: 'Current parser preserves stock stages and maps ml to ML_PER_L and l to
    L, unlike these old fields. Its primary-section predicate recognizes only unnamed/main-solution
    sections: in current M581, presence of main solution1/2 excludes named Solution
    A and Substrate from primary extraction. Static current-code finding only, not
    historical execution proof.'
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T17:34:21.101851Z'
  support: context_only
  summary: Current _merge_ingredient_group does not sum conflicting quantities; it
    retains the first and flags them. Historical water sums must not be attributed
    to unchanged current behavior.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-migration
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _resolve_solution; _migrate_media_file
  accessed_at: '2026-10-28T17:34:21.101875Z'
  support: context_only
  summary: Current _resolve_solution preserves existing concentration and creates
    referenced or empty stubs; _migrate_media_file moves detected solution rows and
    appends history. It does not repair the copied quantity basis.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/historical-reading.json
  accessed_at: '2026-10-28T17:34:21.105641Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 8f5813cbbc3c3b9b1d1c0115375925705dd86b5086b08f87cc4ea61c2df432bd
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T17:34:21.105716Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/complete-document-reader.json
  accessed_at: '2026-10-28T17:34:21.105889Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 7d2f4a4b1bc00b2780b78b9e5e4093b12d641acf38b6c068b645a125597295ec
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T17:34:21.105953Z'
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
  accessed_at: '2026-10-28T17:34:21.105996Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch073/record08/historical-current-object-joins.json
  accessed_at: '2026-10-28T17:34:21.106026Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 92fb50c5f5554092662398822d761faba35564cd5351cf8a6942af97ab8e2409
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T17:19:21.025383Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T17:19:22.812373Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T17:19:28.367230Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T17:19:26.898076Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T17:19:23.622990Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  accessed_at: '2026-10-28T17:19:29.224916Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T17:19:24.636330Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T17:19:24.410973Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi46756
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_46756
  accessed_at: '2026-10-28T17:19:25.825763Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi46756.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 4270cc705078ff2f1787f98b7dbcf05c96b1eccd333801a00cff01b855298a69
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  accessed_at: '2026-10-28T17:19:22.569046Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi234557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_234557
  accessed_at: '2026-10-28T17:19:22.765102Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi234557.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 44bd42cb5d9cb05f32e63af7ad9b22e47bf35b5d6712f2aaaf7e5717c6a9be93
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  accessed_at: '2026-10-28T17:19:21.759423Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi16526.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T17:19:27.404126Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T17:19:25.039275Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  accessed_at: '2026-10-28T17:19:27.706976Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  accessed_at: '2026-10-28T17:19:28.992862Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  accessed_at: '2026-10-28T17:19:25.639330Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi35696.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T17:19:25.468816Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  accessed_at: '2026-10-28T17:19:28.626261Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  accessed_at: '2026-10-28T17:19:26.271153Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64734
  accessed_at: '2026-10-28T17:19:27.167835Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi64734.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 95b7557b1867dcce37a69714dbad0a6a6a6c11c66dde39c6793a2307a7fb0e1c
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  accessed_at: '2026-10-28T17:19:20.911763Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi131361.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  accessed_at: '2026-10-28T17:19:27.058297Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi63939.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  accessed_at: '2026-10-28T17:19:24.229685Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi32145.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  accessed_at: '2026-10-28T17:19:21.108519Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  accessed_at: '2026-10-28T17:19:23.189753Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  accessed_at: '2026-10-28T17:19:23.420652Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  accessed_at: '2026-10-28T17:19:21.150849Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  accessed_at: '2026-10-28T17:19:26.185826Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  accessed_at: '2026-10-28T17:19:22.206136Z'
  locator: REVIEW_WORK/batch073/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:34:21.214077Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: f2f22026e114b38ef1c0394d4f896649ec7eceaf8eef1aa29b47a87959fec4ae
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:34:21.214163Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: c115849165de3c61e4dc16deb9bd32908346a1683c5be2ad7c8ed978c48c3dae
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:34:21.214268Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 9d78deadff24afaca144a6f330da744fd859df49cd616a08719b08e6d78718d1
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:34:21.214358Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 4bfafaa71dd166bff3629d610747c62f37c23a89abaee63e300fb37b17e13244
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:34:21.214427Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 1ee17fe276f0691bc8fb29d26a440cf99a9414e4805284ec728ebed73d4c0c40
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:34:21.214453Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 6925bc19105d80727ee6396f6129a334835767135caa625583631340d4834f51
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch073/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T17:34:21.214474Z'
  support: context_only
  summary: 'The scoped existing-claim authentication sidecar is empty: no attached
    claims are asserted or authenticated here. Historical source-object correspondence
    is documented separately by historical-object-joins.'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch073/record08/schema-result.json
  accessed_at: '2026-10-28T17:19:32.520227Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 93a8e1ae67ec13424fd944fea425b79b22bf406ec661ae9f5111c2882867d13a
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch073/record08/strict-result.json
  accessed_at: '2026-10-28T17:19:34.117328Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 9445741a29bb88c34674d26bbe1131638630283c94738cfdc23fc19423a52dda
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch073/record08/terms-result.json
  accessed_at: '2026-10-28T17:19:36.106240Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: aa271a322680fbc4c99ba5a1202a862887c31c135f7a8f21686e1bb998690928
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch073/record08/references-result.json
  accessed_at: '2026-10-28T17:19:37.013219Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 6c24a64b6b6dde7f1413f3db1bb7e00908c7da61b7ae1f14486a786aac750caf
assessments:
- assessment_id: identity
  area: identity
  topic: Exact selected and stock-source crosswalks
  outcome: supported
  summary: TOGO M581 identifies JCM576. JCM431/M431 contributes only Se/W stock, and
    JCM403/M401 only its vitamin/thiamine/B12 preparations. Neighboring historical
    Desulfatiferula and BN3 whole formulations remain comparison context.
  target_ids:
  - CultureMech:009977
  evidence_ids:
  - jcm576
  - currentTogo581
  - jcm431
  - jcm403
- assessment_id: classification
  area: consistency
  topic: Complex liquid formulation
  outcome: supported
  summary: The yeast-containing formulation supports complex, semi-defined and liquid
    classification. No organism growth claim is inferred.
  target_ids:
  - CultureMech:009977
  evidence_ids:
  - jcm576
  - currentTogo581
- assessment_id: native
  area: schema
  topic: Original diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed once, including zero reference
    checks. They do not resolve scientific unit/stage or chemical-form issues.
  target_ids:
  - CultureMech:009977
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 76 current concentration fields are covered by 50 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009977
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b073-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","quantity_field_count":76,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"961.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"961.0","unit":"G_PER_L"}},{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[0].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 960.0, 1.0]"},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[0].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 960.0, 1.0]"}],"decision":"correct","rationale":"The stored961
    G_PER_L sums960 mL main input and1 L SL12 input without converting units or preserving
    stages. Restore separate source volume inputs, with no measured-final-volume inference.","source_stage":"separate
    main and SL12 water inputs","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;960.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 960,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"7","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"7","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;7.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 7,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.15","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.15","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.15&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary and TOGO row specify1 mg resazurin, not1 G_PER_L. Preserve the source
    mass and stage before considering any concentration basis.","source_stage":"Solution
    A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
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
    redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl                                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"Na2SO4\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\":
    \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"HEPES","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.38","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"2.38","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> HEPES                                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.38&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"HEPES\",\n          \"volume\": 2.38,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001142\",\n          \"gmo_id\": \"GMO_001142\",\n          \"label\":
    \"HEPES\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Yeast extract (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numeric source batch mass is supported, but the local G_PER_L denominator is unverified:960
    mL input water plus later additions is not an explicit final-volume statement.
    Retain the mass as evidence; do not substitute the provider nominal1005 mL rates
    as experimental final-medium concentrations.","source_stage":"Solution A batch","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract (BD-Difco)                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\":
    \"GMO_001018\",\n          \"label\": \"Bacto &trade; Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves dissolved concentration unspecified. Retain that uncertainty
    while separately recording source gas-handling stages and the4:1 v/v atmosphere;
    a gas-phase ratio is not a dissolved mass concentration.","source_stage":"gas-handling
    context","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients, adjust pH to 7.5 and autoclave under
    a N2 atmosphere. After cooling, add the following stock solutions (filter--sterilized
    or *autoclaved) to the solution:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Sodium
    palmitate","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.8","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    primary specifies2.8 g substrate in a separately autoclaved stage. Its numeric
    mass is supported, but no independently measured final volume establishes the
    local G_PER_L basis.","source_stage":"separately prepared substrate","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium palmitate                                        </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.8&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Sodium palmitate\",\n          \"volume\": 2.8,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001651\",\n          \"gmo_id\": \"GMO_001651\",\n          \"label\":
    \"Sodium palmitate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves dissolved concentration unspecified. Retain that uncertainty
    while separately recording source gas-handling stages and the4:1 v/v atmosphere;
    a gas-phase ratio is not a dissolved mass concentration.","source_stage":"gas-handling
    context","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    7,\n      \"comment\": \"To complete the medium, combine Solution A and substrate
    in the culture vessels under a N2--CO2 (4:1, v/v) gas mixture and seal with butyl
    rubber stoppers. Finally, reduce the medium with 0.01 volume of 5% Na2S・9H2O solution
    (autoclaved and stored under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Nitrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves dissolved concentration unspecified. Retain that uncertainty
    while separately recording source gas-handling stages and the4:1 v/v atmosphere;
    a gas-phase ratio is not a dissolved mass concentration.","source_stage":"gas-handling
    context","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\":
    \"Nitrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    7,\n      \"comment\": \"To complete the medium, combine Solution A and substrate
    in the culture vessels under a N2--CO2 (4:1, v/v) gas mixture and seal with butyl
    rubber stoppers. Finally, reduce the medium with 0.01 volume of 5% Na2S・9H2O solution
    (autoclaved and stored under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Na2MoO4・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"18","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;18.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[1]","quote":"{\n          \"component_name\":
    \"Na2MoO4・2H2O\",\n          \"volume\": 18,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"300","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"300","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;300.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[2]","quote":"{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 300,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\":
    \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"FeSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[3]","quote":"{\n          \"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 1.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\":
    \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"MnCl2・4H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;50.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[4]","quote":"{\n          \"component_name\":
    \"MnCl2・4H2O\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\":
    \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"CoCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"190","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"NiCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[6]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"CuCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[7]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"42","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"42","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;42.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[8]","quote":"{\n          \"component_name\":
    \"ZnCl2\",\n          \"volume\": 42,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\":
    \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"EDTA・2Na","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the SL12 stock, not a direct receiving-medium ingredient. Preserve
    its exact source g or mg amount and1 L stock input water; seven mg entries must
    not become grams. Explicit provider stock g_l is distinct from an inferred receiving-medium
    concentration.","source_stage":"SL12 stock","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> EDTA&#183;2Na                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[4].items[9]","quote":"{\n          \"component_name\":
    \"EDTA・2Na\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001058\",\n          \"gmo_id\": \"GMO_001058\",\n          \"label\":
    \"Disodium EDTA\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Trace
    metal solution SL12 (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a liquid addition in mL at its named stage, not G_PER_L of a
    neat component. Restore the stock name/composition or exact scoped reference.
    No density or final-volume conversion is supported.","source_stage":"stock receiving
    dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Trace metal solution SL12 (see below)\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M581\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution SL12
    (see below)                 </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Selenite--tungstate
    solution (see Medium [M431])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a liquid addition in mL at its named stage, not G_PER_L of a
    neat component. Restore the stock name/composition or exact scoped reference.
    No density or final-volume conversion is supported.","source_stage":"stock receiving
    dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"Selenite--tungstate solution (see Medium [M431])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M431\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Selenite-tungstate solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=431\">431</a>)     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"8%
    NaHCO3 solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a liquid addition in mL at its named stage, not G_PER_L of a
    neat component. Restore the stock name/composition or exact scoped reference.
    No density or final-volume conversion is supported. Retain the printed stock percentage
    with its unspecified basis and the distinct sterilization marker.","source_stage":"stock
    receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\":
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
    UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"15%
    MgCl2・6H2O solution*","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a liquid addition in mL at its named stage, not G_PER_L of a
    neat component. Restore the stock name/composition or exact scoped reference.
    No density or final-volume conversion is supported. Retain the printed stock percentage
    with its unspecified basis and the distinct sterilization marker.","source_stage":"stock
    receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"15% MgCl2・6H2O solution*\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 15,\n          \"conc_unit\": \"%\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001286\",\n          \"gmo_id\": \"GMO_001286\",\n          \"label\":
    \"Magnesium chloride hexahydrate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> 15% MgCl<sub>2</sub>&#183;6H<sub>2</sub>O
    solution*                  </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Vitamin
    solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a liquid addition in mL at its named stage, not G_PER_L of a
    neat component. Restore the stock name/composition or exact scoped reference.
    No density or final-volume conversion is supported.","source_stage":"stock receiving
    dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"Vitamin solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin solution (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\">403</a>)                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Thiamine
    solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a liquid addition in mL at its named stage, not G_PER_L of a
    neat component. Restore the stock name/composition or exact scoped reference.
    No density or final-volume conversion is supported.","source_stage":"stock receiving
    dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"Thiamine solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\">403</a>)                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Vitamin
    B12 solution (see Medium [M401])","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[6].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a liquid addition in mL at its named stage, not G_PER_L of a
    neat component. Restore the stock name/composition or exact scoped reference.
    No density or final-volume conversion is supported.","source_stage":"stock receiving
    dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"Vitamin B12 solution (see Medium [M401])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M401\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>
    solution (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=403\">403</a>)       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Na2S・9H2O
    solutions","local_fields":[{"path":"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml","field_path":"solutions[7].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary gives0.01 volume of a5% Na2S nonahydrate stock, not an unconditional10
    mL or10 G_PER_L amount. Preserve its relative-volume basis and unspecified percentage
    basis; TOGO10 mL is a source-view normalization requiring reconciliation.","source_stage":"stock
    receiving dose","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
    \"Na2S・9H2O solutions\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\":
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
    UTF-8"},{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"exact
    text from ''To complete the medium,'' through ''Trace metal solution SL12:''","quote":"To
    complete the medium, combine Solution A and substrate in the culture vessels under
    a N\n2\n-CO\n2\n(4:1, v/v) gas mixture and seal with butyl rubber stoppers. Finally,
    reduce the medium with 0.01 volume of 5% Na\n2\nS·9H\n2\nO solution (autoclaved
    and stored under a N\n2\natmosphere).\nTrace metal solution SL12:","quote_basis":"derivative
    text"}]},{"quantity_id":"q32","label":"M431 Na2SeO3・5H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    input belongs to the Se/W stock only. Preserve the primary milligram selenium/tungsten
    amounts and0.4 g NaOH against1 L input water; local direct-medium G_PER_L does
    not preserve that stock boundary.","source_stage":"Se/W stock input","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML
    table row 30 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SeO<sub>3</sub>&#183;5H<sub>2</sub>O                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"M431
    Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    input belongs to the Se/W stock only. Preserve the primary milligram selenium/tungsten
    amounts and0.4 g NaOH against1 L input water; local direct-medium G_PER_L does
    not preserve that stock boundary.","source_stage":"Se/W stock input","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML
    table row 31 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>WO<sub>4</sub>&#183;2H<sub>2</sub>O                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"M431
    NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.4","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    input belongs to the Se/W stock only. Preserve the primary milligram selenium/tungsten
    amounts and0.4 g NaOH against1 L input water; local direct-medium G_PER_L does
    not preserve that stock boundary.","source_stage":"Se/W stock input","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\":
    \"NaOH\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\":
    \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML
    table row 29 (zero-based)","quote":"<TR><TD WIDTH=75%> NaOH                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.4&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"M431
    merged water","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"989.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml","field_path":"ingredients[11].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Merged 3 duplicates: 1.0, 987.0, 1.0]"}],"decision":"correct","rationale":"This
    shared989 G_PER_L descriptor combines three differently scoped water inputs. Only
    the Se/W1 L input is transferable here; split the descriptor with full parent
    curation and do not treat the whole989 as stock water.","source_stage":"ambiguous
    shared water with Se/W contribution","sources":[{"evidence_id":"currentTogo431","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M431","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo431.raw","raw_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","text_sha256":"e906db1342c998a25b7fc6a9b8e9168bed218838aefdb9ef9c8398251c3ec570","accessed_at":"2026-10-28T17:19:20.429435Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm431","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm431.raw","raw_sha256":"cf3d25eefdeb8835ce27a453e2afa44b0f6a3f1644beb36fa84937ca7c904c50","text_sha256":"ec3776552cd428886c0020385d5a22ebcaa47851d680ae031dc2d6e36fd14618","accessed_at":"2026-10-28T17:19:19.719886Z","locator":"HTML
    table row 32 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"M401
    Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\":
    \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"M401
    p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"4","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"p--Aminobenzoic acid\",\n          \"volume\": 4,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;4.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"M401
    Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"M401
    Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"M401
    Sodium phosphate buffer (10 mM, pH 7.1)","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup. Retain the explicit buffer
    molarity and pH, without inferring its individual phosphate-salt recipe.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"Sodium phosphate buffer (10 mM, pH 7.1)\",\n          \"volume\": 100,\n          \"unit\":
    \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001124\",\n          \"gmo_id\":
    \"GMO_001124\",\n          \"label\": \"Sodium phosphate buffer\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium phosphate buffer
    (10 mM, pH 7.1)               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"M401
    DL--Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
    \"DL--Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001936\",\n          \"gmo_id\": \"GMO_001936\",\n          \"label\":
    \"DL-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> DL-Calcium pantothenate                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"M401
    Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Thiamine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"M401
    Sodium phosphate buffer (25 mM, pH 3.4)","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup. Retain the explicit buffer
    molarity and pH, without inferring its individual phosphate-salt recipe.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"Sodium phosphate buffer (25 mM, pH 3.4)\",\n          \"volume\": 100,\n          \"unit\":
    \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001124\",\n          \"gmo_id\":
    \"GMO_001124\",\n          \"label\": \"Sodium phosphate buffer\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium phosphate buffer
    (25 mM, pH 3.4)               </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"M401
    Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"Preserve
    this exact input within its named vitamin, thiamine or B12 preparation; it is
    not a direct parent-medium G_PER_L entry. The source gives mg masses or mL buffer
    volumes, without an independently stated final makeup.","source_stage":"referenced
    vitamin/thiamine/B12 stock","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"M401
    merged water","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"101.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml","field_path":"ingredients[0].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 1.0, 100.0]"}],"decision":"correct","rationale":"The101
    G_PER_L descriptor combines parent1 L and B12-stock100 mL inputs. Only the B12
    water is in receiving-record scope; preserve it separately without transferring
    parent water.","source_stage":"B12 stock water contribution","sources":[{"evidence_id":"currentTogo401","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M401","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo401.raw","raw_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","text_sha256":"380cb064612f29e5a94e95b7c145b3bc13608fe38de5a6defa50cdcf2bc746f1","accessed_at":"2026-10-28T17:19:20.447939Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm403","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=403","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm403.raw","raw_sha256":"b28331b54771accff48da1b68077398dd7450ee8746eaf1aec1b4ef7a055bd61","text_sha256":"cd32fdd8ae744410a4d112306055f1db7be847bd5ddee0647b7500d6cdb56b93","accessed_at":"2026-10-28T17:19:19.716154Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Missing
    source preparation 1","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the exact main/stock/substrate stage, pH and atmosphere from this source instruction.
    The source gas ratio is not a dissolved concentration and relative reductant volume
    is not an unconditional mL dose.","source_stage":"source preparation controls","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients, adjust pH to 7.5 and autoclave under
    a N2 atmosphere. After cooling, add the following stock solutions (filter--sterilized
    or *autoclaved) to the solution:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Missing
    source preparation 2","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the exact main/stock/substrate stage, pH and atmosphere from this source instruction.
    The source gas ratio is not a dissolved concentration and relative reductant volume
    is not an unconditional mL dose.","source_stage":"source preparation controls","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"Autoclave in culture vessels.\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q48","label":"Missing source preparation 3","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the exact main/stock/substrate stage, pH and atmosphere from this source instruction.
    The source gas ratio is not a dissolved concentration and relative reductant volume
    is not an unconditional mL dose.","source_stage":"source preparation controls","sources":[{"evidence_id":"currentTogo581","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M581","raw_path":"REVIEW_WORK/batch073/source07-08-10/currentTogo581.raw","raw_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","text_sha256":"0b926f9b1aaf5b971c52b202631afa12b20c71a595e4b5b236a72e6b1f5e2bbd","accessed_at":"2026-10-28T17:19:20.397490Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    7,\n      \"comment\": \"To complete the medium, combine Solution A and substrate
    in the culture vessels under a N2--CO2 (4:1, v/v) gas mixture and seal with butyl
    rubber stoppers. Finally, reduce the medium with 0.01 volume of 5% Na2S・9H2O solution
    (autoclaved and stored under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"SL12
    input water","local_fields":[],"decision":"evidence_only","rationale":"The1 L
    is stock solvent input, not a separately stated final makeup.","source_stage":"SL12
    stock water","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"JCM
    default sterilization","local_fields":[],"decision":"evidence_only","rationale":"The
    source default121°C/15 min applies only where not otherwise stated; preserve the
    separate filter-sterilization and starred autoclave exceptions.","source_stage":"source
    default","sources":[{"evidence_id":"jcm576","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=576","raw_path":"REVIEW_WORK/batch073/source07-08-10/jcm576.raw","raw_sha256":"25afea3069bc76e6cfe1d37d763c6efe74eb056b062205a391a843653687e9b4","text_sha256":"471f0a32aa9ab09645365f31ea5fe3a4ec567cdc1e765389fc8ca8ea402d32f8","accessed_at":"2026-10-28T17:19:19.015593Z","locator":"exact
    text from ''Unless otherwise stated,'' through ''15 min.''","quote":"Unless otherwise
    stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative
    text"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFATIBACILLUS_OLEFINIVORANS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml":["ingredients[11]","ingredients[27]","ingredients[28]","ingredients[29]"],"data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml":["ingredients[0]","ingredients[17]","ingredients[18]","ingredients[19]","ingredients[20]","ingredients[21]","ingredients[22]","ingredients[23]","ingredients[24]","ingredients[25]"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Current exact asserted ontology objects and packaged MIM rows are assessed
    independently of supplied-form correspondence. Cobalt/nickel hydration contradicts
    two asserted terms. Source EDTA lacks a hydrate designation, so the anhydrous-specific
    term remains a specificity limit rather than a confirmed substitute. Vitamin B12
    is a broad class; no vitamer is inferred. Existing HEPES secondary membership
    and scoped DL-calcium legacy linkage need bounded catalog reconciliation, with
    separate presence and validity populations.
  target_ids:
  - CultureMech:009977
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: 'All thirteen historical report scopes were read through the lossless pool:
    three selected/direct-scope October reviews were source-unchecked, and dependency/sibling
    September findings are contextual evidence, not new source authentication. Current
    M431/M401 stock fields remain uncorrected in the scoped sections. Current cleanup
    no longer sums conflicts; current TOGO unit/stage handling and conservative formulation
    merging are credited while its named-section routing issue is demonstrated separately.'
  target_ids:
  - CultureMech:009977
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009977-stock-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Reconstruct source stages and source amount units
  description: The selected water sum combines main and SL12 inputs; resazurin1 mg
    and multiple SL12 mg inputs became G_PER_L, while eight liquid or relative-volume
    additions use mass units. Restore Solution A, separate substrate and named stocks
    without assuming final volume. Preserve the primary0.01-volume5% reductant instruction
    and explicitly reconcile TOGO10 mL. Resolve only M431 Se/W and M401 vitamin/thiamine/B12
    subsections; repair their scoped mg/mL fields and shared-water contributions without
    importing parent quantities.
  target_ids:
  - CultureMech:009977
  field_paths:
  - ingredients
  - solutions
  - data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml::ingredients[27]
  - data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml::ingredients[17]
  evidence_ids:
  - jcm576
  - currentTogo581
  - jcm431
  - currentTogo431
  - jcm403
  - currentTogo401
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M431_BN3_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    role: scoped dependency
- finding_id: f2
  issue_key: culturemech-009977-missing-preparation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Restore the omitted staged source preparation
  description: The record omits Solution A pH7.5 and its N2 treatment, post-cooling
    stock sterilization distinctions, separately treated substrate,4:1 N2/CO2 assembly
    and relative reductant step. Preserve these exact source stages and JCM default
    exceptions. VARIABLE gas placeholders need no invented dissolved concentrations.
  target_ids:
  - CultureMech:009977
  field_paths:
  - preparation_steps
  - ph_value
  - sterilization
  - ingredients[10]
  - ingredients[12]
  - ingredients[13]
  evidence_ids:
  - jcm576
  - currentTogo581
  - quantities
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-009977-hydrate-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve explicit cobalt and nickel hexahydrates
  description: SL12 CoCl2·6H2O and NiCl2·6H2O are asserted as anhydrous CHEBI35696
    and34887. Current exact53503 and53542 objects confirm distinct hydrated identities.
    Correct supplied-form correspondence without changing source masses or inferring
    unprinted hydrates for EDTA.
  target_ids:
  - CultureMech:009977
  field_paths:
  - ingredients[18].term
  - ingredients[19].term
  evidence_ids:
  - jcm576
  - chebi35696
  - chebi34887
  - chebi53503
  - chebi53542
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-009977-current-import-section
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Preserve named basal and substrate sections in the current importer
  description: Current _is_primary_section accepts only unnamed or main solution N
    sections. The inspected M581 payload has named Solution A and Substrate plus main
    solution1/2, so current _extract_primary_components selects the latter and skips
    the named basal/substrate sections. Repair that exact section-routing boundary
    while retaining current unit/stage improvements; do not rerun an importer or regenerate
    this medium until source fidelity is checked.
  target_ids:
  - CultureMech:009977
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - currentTogo581
  - writer-togo
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained source section parser
- finding_id: f5
  issue_key: culturemech-009977-evidence-catalog
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach claims and reconcile bounded catalog links
  description: No scoped selected or dependency quantity claims are attached. Preserve
    historical reports as earlier incomplete reviews and append exact new evidence
    after curation. Replace Unknown solution names with source-supported names. HEPES
    CHEBI46756 is active but its existing secondary slot has no exact packaged MIM
    row; scoped M401 retains legacy000926 for DL-calcium pantothenate. Resolve these
    catalog links without equating current absence with ontology obsolescence or replacing
    DL with a D-only term.
  target_ids:
  - CultureMech:009977
  field_paths:
  - evidence
  - solutions
  - ingredients[8].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml::ingredients[22].mediaingredientmech_term
  evidence_ids:
  - old-reports
  - old-claims
  - groundings
  - mim
  - mim-meta
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: The selected water sum combines main and SL12 inputs; resazurin1 mg
    and multiple SL12 mg inputs became G_PER_L, while eight liquid or relative-volume
    additions use mass units. Restore Solution A, separate substrate and named stocks
    without assuming final volume. Preserve the primary0.01-volume5% reductant instruction
    and explicitly reconcile TOGO10 mL. Resolve only M431 Se/W and M401 vitamin/thiamine/B12
    subsections; repair their scoped mg/mL fields and shared-water contributions without
    importing parent quantities.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009977
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
    role: maintained source
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
- action_id: a2
  description: The record omits Solution A pH7.5 and its N2 treatment, post-cooling
    stock sterilization distinctions, separately treated substrate,4:1 N2/CO2 assembly
    and relative reductant step. Preserve these exact source stages and JCM default
    exceptions. VARIABLE gas placeholders need no invented dissolved concentrations.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009977
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
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
  description: SL12 CoCl2·6H2O and NiCl2·6H2O are asserted as anhydrous CHEBI35696
    and34887. Current exact53503 and53542 objects confirm distinct hydrated identities.
    Correct supplied-form correspondence without changing source masses or inferring
    unprinted hydrates for EDTA.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009977
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
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
  description: Current _is_primary_section accepts only unnamed or main solution N
    sections. The inspected M581 payload has named Solution A and Substrate plus main
    solution1/2, so current _extract_primary_components selects the latter and skips
    the named basal/substrate sections. Repair that exact section-routing boundary
    while retaining current unit/stage improvements; do not rerun an importer or regenerate
    this medium until source fidelity is checked.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009977
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained source section parser
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: No scoped selected or dependency quantity claims are attached. Preserve
    historical reports as earlier incomplete reviews and append exact new evidence
    after curation. Replace Unknown solution names with source-supported names. HEPES
    CHEBI46756 is active but its existing secondary slot has no exact packaged MIM
    row; scoped M401 retains legacy000926 for DL-calcium pantothenate. Resolve these
    catalog links without equating current absence with ontology obsolescence or replacing
    DL with a D-only term.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009977
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M581_Desulfatibacillus_Olefinivorans_Medium.yaml
    role: maintained source
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
- M431 parent medium, other trace stock and receiving doses are excluded; M401 basal/trace
  recipe, growth conditions and receiving doses are excluded. Shared merged-water
  descriptors are assessed only to identify the relevant stock contribution and the
  need for separate parent reconciliation.
- The primary0.01-volume reductant instruction and provider/TOGO absolute normalizations
  remain distinct. Unspecified percentage bases, EDTA hydration and vitamin identities
  are not invented.
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
