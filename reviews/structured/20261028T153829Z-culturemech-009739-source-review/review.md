# Scientific review: Deferribacter Abyssi Medium

- Review: 20261028T153829Z-culturemech-009739-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T15:21:42.953461Z
- Finished UTC: 2026-10-28T15:38:29.558853Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact JCM365 identity is supported. Water and stock units, final-volume basis, missing stock definitions and preparation stages require maintained-owner curation; sulfur grounding describes an atom rather than the bulk reagent. Existing scoped stock repairs and attached claims are credited. All four original canonical checks passed, without establishing scientific correctness.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch071 index 10
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009739 | data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml | generated | deferribacter_abyssi_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009739 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009739 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009739 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009739 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact identity and scoped source crosswalk

identity: supported. Targets: CultureMech:009739.

TOGO M359 explicitly links JCM365, and current MediaDive J365 carries the matching identity and source. The generated record has one maintained owner. The cited species paper supplies bibliographic/environmental context, not an authenticated exact formulation or permission to add organism-growth assertions. JCM151 and JCM197 transfer only the explicitly referenced trace and vitamin sections.

### Complexity and physical state

consistency: supported. Targets: CultureMech:009739.

Yeast extract makes the formulation complex and partly defined. The source has no agar, supporting the liquid-medium classification; separately handled sulfur does not itself imply an agar medium. Local category bacterial does not certify strain growth.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009739.

30 current concentration fields are covered by 46 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b071-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","quantity_field_count":30,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact input is 1 L water (provider 1000 ml), not 1 G_PER_L. Restore the input-volume unit L. The listed water is not proof of final medium make-up.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=29.4118 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 30,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 30,\n                        \"unit\": \"g\",\n                        \"g_l\": 29.4118,\n                        \"mmol_l\": 503.281,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion. This component is separately autoclaved and added, not included in the initial autoclaved mixture.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\": 2.20066,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\": 2.37739,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\": 6.04841,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion. This component is separately autoclaved and added, not included in the initial autoclaved mixture.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\": 1.59137,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Na2S・9H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=0.490196 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion. This is the receiving-batch contribution, distinct from the separately prepared neutralized 5% reagent; percent basis and stock addition volume remain unspecified.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"Na2S・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.490196,\n                        \"mmol_l\": 2.04094,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.33&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\": 4.33976,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Sodium acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=2.94118 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sodium acetate                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"Sodium acetate\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\": \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\": 731,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.94118,\n                        \"mmol_l\": 35.8549,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Sulfur","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=9.80392 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion. Sulfur is prepared separately; a bulk sulfur reagent is not an isolated sulfur atom.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Sulfur                                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Sulfur\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001062\",\n          \"gmo_id\": \"GMO_001062\",\n          \"label\": \"Sulfur powder\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\": 80,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.80392,\n                        \"mmol_l\": 305.704,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Yeast extract (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The literal source batch amount is supported, but neither primary nor TOGO establishes final make-up. MediaDive explicitly reports its different g_l=0.0980392 on declared volume 1020 ml. That provider normalization is not an independently measured final volume and does not support the local bare G_PER_L value. Preserve the exact input mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0980392,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Nitrogen placeholder","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully leaves gas quantity unquantified. The source specifies an atmosphere, not dissolved nitrogen concentration or gas dose. Retain the placeholder if needed while restoring gas-handling context; do not turn it into a numeric concentration.","source_stage":"Gas atmosphere, not dissolved quantity","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Trace minerals (see Medium [M142])","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source adds 10 ml of this exact stock per receiving batch, equal to 0.01 L as a volume. The stored 10 G_PER_L is wrong in dimension. Neither a dose per final litre nor a stock concentration follows from this amount.","source_stage":"Receiving stock addition","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace minerals (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=151\"&gt;151&lt;/a&gt;)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"solution\": \"Trace minerals\",\n                        \"solution_id\": 3804,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Trace vitamins (see Medium [M190])","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source adds 10 ml of this exact stock per receiving batch, equal to 0.01 L as a volume. The stored 10 G_PER_L is wrong in dimension. Neither a dose per final litre nor a stock concentration follows from this amount.","source_stage":"Receiving stock addition","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace vitamins (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\"&gt;197&lt;/a&gt;)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Distilled water retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Collapsed 2 identical duplicates: 1.0, 1.0]\n\nSource water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. Water remains an explicit 1 L input, not a verified final stock volume.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 32 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"MgSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 3.5, 3.0]\n\nSource batch input: 3 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"NaCl retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 13.85, 1.0]\n\nSource batch input: 1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"CaCl2・2H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"Na2MoO4・2H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 31 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"H3BO3 retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 15.0, 0.01]\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 30 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"FeSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"ZnSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"CuSO4・5H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 28 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\": \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"CoSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001050\",\n          \"gmo_id\": \"GMO_001050\",\n          \"label\": \"Cobalt(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.645178,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Nitrilotriacetic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Mineral source; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nitrilotriacetic acid                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"MnSO4・xH2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[11].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium. Source x/n hydrate is unspecified; no fixed hydration number or molar conversion is inferred.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[11]","quote":"{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"AlK(SO4)2 retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[12].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML table row 29 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; AlK(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[12]","quote":"{\n          \"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001088\",\n          \"gmo_id\": \"GMO_001088\",\n          \"label\": \"Aluminum potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2\",\n                        \"compound_id\": 1015,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0387289,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Distilled water retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 981.0, 1.0, 1.0]\n\nSource water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. Water remains an explicit 1 L input, not a verified final stock volume.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Biotin retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"p--Aminobenzoic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Thiamine・HCl retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Calcium pantothenate retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium. Generic calcium pantothenate does not establish the D stereochemistry of the asserted ontology term; amount authentication does not recertify that specificity.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Pyridoxine・HCl retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Folic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Vitamin B12 retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Riboflavin retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Nicotinic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Lipoic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The retained batch-input note and its existing literal claim match exact current raw bytes, including the attached historical digest. The original access event is not newly recovered. The source batch mass remains in notes; absence of an unsupported G_PER_L assertion is credited. Explicit provider g_l is confined to its stock normalization, not transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Unquantified KOH retained note","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].solutions[0].notes","stored":"Role: Mineral source; Properties: Defined component, Solution\n\npH-adjustment reagent; no fixed dose is specified. Normality is not converted to molarity."}],"decision":"verified","rationale":"The exact additional root-attached excerpt authenticates this retained claim against the same current raw digest. KOH is a pH-adjustment reagent with no fixed amount; no concentration is invented.","source_stage":"Trace stock preparation","sources":[{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[13]","quote":"{\n          \"component_name\": \"KOH solution\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Retained trace pH and order","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].preparation_notes","stored":"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."}],"decision":"verified","rationale":"The exact additional root-attached excerpt authenticates this retained claim against the same current raw digest. The 6.5 adjustment precedes mineral addition and final stock pH 7.0. These are stock-only controls, not receiving-medium pH.","source_stage":"Trace stock preparation","sources":[{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"comments[1].comment","quote":"\"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.\"","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"jcm151.txt lines 203-203","quote":"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution.      Then proceed to add minerals.   Adjust final pH to 7.0.","quote_basis":"derivative text"}]},{"quantity_id":"q41","label":"Initial pH","local_fields":[],"decision":"evidence_only","rationale":"The source specifies pH 6.5 before autoclaving; later readjustment is conditional, not a new range.","source_stage":"Source-only receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO, sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO under a N\n2\natmosphere. Dispense the medium into culture vessels containing sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q42","label":"Separate calcium and magnesium treatment","local_fields":[],"decision":"evidence_only","rationale":"Exclude these two reagents from the initial mixture, sterilize separately and then add them; no unstated stock volume or strength is invented.","source_stage":"Source-only receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO, sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO under a N\n2\natmosphere. Dispense the medium into culture vessels containing sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q43","label":"Sulfur steam schedule","local_fields":[],"decision":"evidence_only","rationale":"The printed 3 h on each of 3 successive days belongs to sulfur steam treatment. No steam temperature or 121-degree sulfur autoclave claim is inferred.","source_stage":"Source-only receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO, sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO under a N\n2\natmosphere. Dispense the medium into culture vessels containing sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q44","label":"Sulfide stock label","local_fields":[],"decision":"evidence_only","rationale":"Neutralized 5% sodium sulfide nonahydrate is prepared separately. Percent basis and receiving addition volume are unstated; preserve the literal label without percent-to-mass conversion.","source_stage":"Source-only receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO, sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO under a N\n2\natmosphere. Dispense the medium into culture vessels containing sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q45","label":"Atmosphere and sequence","local_fields":[],"decision":"evidence_only","rationale":"Nitrogen atmosphere, vessel sealing and delayed sterile sulfide addition are explicit preparation context. No gas dose, incubation temperature or growth outcome is inferred.","source_stage":"Source-only receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO, sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO under a N\n2\natmosphere. Dispense the medium into culture vessels containing sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q46","label":"Default autoclave statement","local_fields":[],"decision":"evidence_only","rationale":"JCM states 121 degrees C for 15 min unless otherwise specified. Credit this default only for the source autoclave steps; sulfur has its separate printed steam schedule.","source_stage":"Source default with explicit exceptions","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml":["solutions[1].preferred_term","solutions[1].composition","solutions[1].solutions","solutions[1].preparation_notes"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].preferred_term","solutions[1].composition"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009739.

Current exact active OLS IDs/labels and packaged MIM rows are all joined, including scoped stock forms. The confirmed supplied-form error is the sulfur atom grounding. M142 manganese sulfate x/n hydrate remains unspecified; its generic base-salt ID does not certify an anhydrous or fixed-hydrate reagent. Generic calcium pantothenate does not establish the D stereochemistry of CHEBI:31345, so no stereochemical replacement or mass conversion is asserted. Vitamin B12 class, non-stoichiometric mixtures and unspecified acetate hydrate are not silently specialized. Secondary-link presence is reported separately from current label/row agreement.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:009739.

Complete current target/owner histories, both scoped dependency histories and all 16 native historical reports were read losslessly. The 24 retained composition claims and two scoped additional root excerpts match current exact raw digests from the October repair; current retrieval times are not backdated. Older flattened/merged records and J261/M253 relationships are comparison or provenance only, not extra owners of this singleton target. Historic per-litre assumptions are not adopted. Current stock repairs, l-to-L handling, comment retention and conservative formulation matching are credited; no writer is replayed and current bodies are not historical execution proof.

## Findings

### f1: Input volumes and final concentration bases are misrepresented

major / open / confirmed; issue key: culturemech-009739-water-stock-units-basis.

Correct maintained water from 1 G_PER_L to its exact 1 L input and each 10 G_PER_L stock addition to the source 10 ml batch dose. Preserve main input masses without asserting an unestablished final litre. MediaDive declares volume 1020 ml and different g_l values; retain that provider basis as context rather than silently substituting it for measured final make-up. Regenerate only after owner curation.

### f2: Exact trace and vitamin definitions are not represented

major / open / confirmed; issue key: culturemech-009739-stock-resolution.

Resolve the trace and vitamin references to the exact assessed M142 trace and M190 vitamin subtrees, or preserve equivalent source-scoped definitions and provenance. Current compositions are empty and names remain Unknown solution. The current M142 trace composition agrees with JCM151; the retained stock repairs are credited, not overwritten. Exclude both parent media, their receiving doses and unrelated stock or preparation sections.

### f3: The defining preparation stages are absent

major / open / confirmed; issue key: culturemech-009739-preparation-stage-loss.

Restore the source initial pH, separate calcium/magnesium treatment, sulfur steam schedule, literal sulfide stock label, nitrogen handling and final addition sequence with their exact supporting claims. Keep unspecified percent basis, stock dose and final volume unresolved. Credit current importer comment retention and fix only demonstrated parser boundaries; do not import preparation from M142 or M190 parent media.

### f4: Bulk sulfur is grounded to an isolated sulfur atom

major / open / confirmed; issue key: culturemech-009739-bulk-sulfur-form.

The source uses a bulk sulfur reagent with separate handling. CHEBI:26833 is a sulfur atom, with atomic formula/structure, so the matching canonical label does not establish the supplied material. Reconcile both primary and secondary sulfur slots against a verified material-level term without inferring an unreported allotrope.

### f5: Maintained claims and stock names need explicit provenance

minor / open / confirmed; issue key: culturemech-009739-claim-and-placeholder-metadata.

Attach exact source claims to the selected maintained owner, including unchanged supported inputs and unresolved denominator boundaries. Credit all 24 existing scoped dependency ingredient claims and the two additional trace root excerpts. Replace existing Unknown solution placeholders with their demonstrated source names, including the scoped KOH descriptor, without inventing its quantity. Preserve prior history and append new events.

## Recommended Actions And Acceptance Checks

### a1

Correct maintained water from 1 G_PER_L to its exact 1 L input and each 10 G_PER_L stock addition to the source 10 ml batch dose. Preserve main input masses without asserting an unestablished final litre. MediaDive declares volume 1020 ml and different g_l values; retain that provider basis as context rather than silently substituting it for measured final make-up. Regenerate only after owner curation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Resolve the trace and vitamin references to the exact assessed M142 trace and M190 vitamin subtrees, or preserve equivalent source-scoped definitions and provenance. Current compositions are empty and names remain Unknown solution. The current M142 trace composition agrees with JCM151; the retained stock repairs are credited, not overwritten. Exclude both parent media, their receiving doses and unrelated stock or preparation sections.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Restore the source initial pH, separate calcium/magnesium treatment, sulfur steam schedule, literal sulfide stock label, nitrogen handling and final addition sequence with their exact supporting claims. Keep unspecified percent basis, stock dose and final volume unresolved. Credit current importer comment retention and fix only demonstrated parser boundaries; do not import preparation from M142 or M190 parent media.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The source uses a bulk sulfur reagent with separate handling. CHEBI:26833 is a sulfur atom, with atomic formula/structure, so the matching canonical label does not establish the supplied material. Reconcile both primary and secondary sulfur slots against a verified material-level term without inferring an unreported allotrope.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Attach exact source claims to the selected maintained owner, including unchanged supported inputs and unresolved denominator boundaries. Credit all 24 existing scoped dependency ingredient claims and the two additional trace root excerpts. Replace existing Unknown solution placeholders with their demonstrated source names, including the scoped KOH descriptor, without inventing its quantity. Preserve prior history and append new events.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| jcm365 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365; REVIEW_WORK/batch071/source07-08-10/jcm365.json; exact original raw/text/hash/time metadata | context_only | Exact named source or scoped dependency; bibliographic organism identity only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer. |
| jcm151 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; REVIEW_WORK/batch071/source07-08-10/jcm151.json; exact original raw/text/hash/time metadata | context_only | Exact named source or scoped dependency; bibliographic organism identity only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; REVIEW_WORK/batch071/source07-08-10/jcm197.json; exact original raw/text/hash/time metadata | context_only | Exact named source or scoped dependency; bibliographic organism identity only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer. |
| currentTogo359 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359; REVIEW_WORK/batch071/source07-08-10/currentTogo359.json; exact original raw/text/hash/time metadata | context_only | Exact current provider recipe; M142 trace and M190 vitamin subsection only are in scientific dependency scope. |
| currentTogo142 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; REVIEW_WORK/batch071/source07-08-10/currentTogo142.json; exact original raw/text/hash/time metadata | context_only | Exact current provider recipe; M142 trace and M190 vitamin subsection only are in scientific dependency scope. |
| currentTogo190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; REVIEW_WORK/batch071/source07-08-10/currentTogo190.json; exact original raw/text/hash/time metadata | context_only | Exact current provider recipe; M142 trace and M190 vitamin subsection only are in scientific dependency scope. |
| apiJ365 | https://mediadive.dsmz.de/rest/medium/J365; REVIEW_WORK/batch071/source07-08-10/apiJ365.json; exact original raw/text/hash/time metadata | context_only | Exact named source or scoped dependency; bibliographic organism identity only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer. |
| pmid13130062 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:13130062%20AND%20SRC:MED&amp;resultType=core&amp;format=json; REVIEW_WORK/batch071/source07-08-10/pmid13130062.json; exact original raw/text/hash/time metadata | context_only | Exact named source or scoped dependency; bibliographic organism identity only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer. |
| chebi26833 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833; REVIEW_WORK/batch071/source07-08-10/chebi26833.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; REVIEW_WORK/batch071/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-19 | reports/ingredient_concentration_curation/20261008-j261-variant/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261008-j261-variant/records/M142.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261008-j261-variant/records/M253.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-23 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M142.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__6ffabef8.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__a85c0932.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-32 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-33 | reports/yaml_record_review/20260921T134926Z-archaeoglobus_fulgidus_medium__01928dac.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-34 | reports/yaml_record_review/20260922T140946Z-deferribacter_abyssi_medium__f0deb53f.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-35 | reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-36 | reports/yaml_record_review/20260924T234748Z-pyrococcus_medium__a85c0932.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| trace-owner | data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml; solutions[1].composition; solutions[1].solutions; solutions[1].preparation_notes | context_only | Full record read; only trace composition, nested unquantified KOH and trace preparation are assessed. Parent doses, other stocks and main preparation are excluded. |
| vitamin-owner | data/normalized_yaml/bacterial/togo_medium_m190.yaml; solutions[1].composition | context_only | Full provenance read; only the vitamin composition is scientifically assessed. Parent receiving doses and all parent preparation are excluded. |
| writer-togo | src/culturemech/import/togo_importer.py; _parse_unit, _ingredient_from_item, _extract_preparation_steps, _extract_ph | context_only | Current _parse_unit already maps l to L and comment extraction retains preparation; stored defects are not evidence that those current behaviors are absent. Bare mass and ml mappings do not establish final volume. _extract_ph reads root ph, whereas the actual source puts ph under meta. |
| writer-migration | scripts/migrate_solutions_from_ingredients.py; SolutionMigrator: current index construction and migration functions | context_only | Current migration recognizes solution names, preserves old concentration when moving a descriptor, and creates empty composition stubs. Its name-index lookup is not a scientific verification of exact referenced stock scope. |
| writer-stock-repair | scripts/repair_jcm_stock_preparations.py; Review.leaf, stock, fill, stages, procedures; build; process | context_only | Current guarded source-specific Review.leaf/stock/fill/stages/procedures retain batch amounts without inferred final volume, place claim evidence and trace pH by stage. Existing M142/M190 repairs are independently credited against current exact raw bytes; this body is not rerun or proof of a historical execution. |
| writer-variant | scripts/repair_j261_variant.py; Review.relationship, Review.finish, build | context_only | Current relationship and finish preserve the parent formulation and append reciprocal variant provenance. That J261/M253 relationship is contextual to M142, not a replacement formulation or owner for this JCM365 target. |
| scoped-root-claims | REVIEW_WORK/batch071/record10/scoped-root-claim-authentication.json; Two exact additional root evidence excerpts | supports | Root evidence legitimately contains stock claims. Only the exact KOH and trace-pH excerpts are authenticated, excluding parent doses and procedures. |
| historical-reading | REVIEW_WORK/batch071/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch071/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch071/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch071/record10/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch071/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch071/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch071/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch071/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch071/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch071/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; REVIEW_WORK/batch071/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch071/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; REVIEW_WORK/batch071/source07-08-10/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; REVIEW_WORK/batch071/source07-08-10/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; REVIEW_WORK/batch071/source07-08-10/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch071/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch071/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; REVIEW_WORK/batch071/source07-08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; REVIEW_WORK/batch071/source07-08-10/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; REVIEW_WORK/batch071/source07-08-10/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; REVIEW_WORK/batch071/source07-08-10/chebi91244.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; REVIEW_WORK/batch071/source07-08-10/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; REVIEW_WORK/batch071/source07-08-10/chebi86360.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86463 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86463; REVIEW_WORK/batch071/source07-08-10/chebi86463.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; REVIEW_WORK/batch071/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; REVIEW_WORK/batch071/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; REVIEW_WORK/batch071/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; REVIEW_WORK/batch071/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; REVIEW_WORK/batch071/source07-08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; REVIEW_WORK/batch071/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; REVIEW_WORK/batch071/source07-08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; REVIEW_WORK/batch071/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; REVIEW_WORK/batch071/source07-08-10/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch071/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch071/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch071/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch071/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch071/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch071/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch071/record10/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch071/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch071/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch071/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch071/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- M142 scientific scope is only its trace subtree and trace preparation; M190 scope is only its vitamin composition. Parent receiving doses, basal amounts, other stocks and main preparation are unassessed and excluded from transfer.
- Only metadata/abstract context of PMID:13130062 was read, not the full paper. No exact formulation, strain-growth evidence or conditions are inferred from that paper.
- Exact sulfur material/allotrope, generic calcium-pantothenate stereochemistry, unspecified manganese hydration and sulfide percent basis remain unresolved; no chemical or final-volume conversions are proposed.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T153829Z-culturemech-009739-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Deferribacter Abyssi Medium'
started_at: '2026-10-28T15:21:42.953461Z'
finished_at: '2026-10-28T15:38:29.558853Z'
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
summary: Exact JCM365 identity is supported. Water and stock units, final-volume basis,
  missing stock definitions and preparation stages require maintained-owner curation;
  sulfur grounding describes an atom rather than the bulk reagent. Existing scoped
  stock repairs and attached claims are credited. All four original canonical checks
  passed, without establishing scientific correctness.
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
  - path: data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml
    sha256: 833f624b29e68b1d4de9eab4b3813f645f84c31efa609a4b2c0ba8032d7ed22f
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    sha256: 67aacbc03f71c5e0b382b0a92609b29d71bfb2d9b49e6efa9ae9b2a45c60a75f
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
  - path: reports/ingredient_concentration_curation/20261008-j261-variant/plan.json
    sha256: 6596fd242999001378304c512ae0e469c74b342c4ba975acec7c80052b746d78
    role: context
  - path: reports/ingredient_concentration_curation/20261008-j261-variant/records/M142.md
    sha256: 3005c0fe47be96230058f7eb8779d9915ff96ebf9de43f2ba476bb7e4f1ac75d
    role: context
  - path: reports/ingredient_concentration_curation/20261008-j261-variant/records/M253.md
    sha256: 8cb25cf38148de75110754cba1ce951746573c3fae7ed47c8169ea604e906f32
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
    sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M142.md
    sha256: 42adc98b2f24eef6d866f81a2cdc36eba868fbcf592695cd02c649cae404855b
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
    sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.md
    sha256: 8306a05efee0ff5f12e4dcb2cb216c6ebb6bb604a1812ecb1ceac85e6bc1a924
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.md
    sha256: a5df34589b23951552885d084fec0e99431831726d7bf07f53cc6374bc4965c2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__6ffabef8.md
    sha256: 83c8213491aaeb9764f15234d55e465b4ddadad00dc05bfaa93743419b3d9ea2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__a85c0932.md
    sha256: b7afb33e6091981790d7d02bd4e7a2ecfa11655363fc9ee42994a3b3b3e757ad
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
    sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.md
    sha256: 2819146dc7d90f64ef630274b9d757bd510220b222d429716fc29d878d82b1b9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.md
    sha256: 9375b6b75f872d37d8e44d342d6de57746c21933bb15636d8c56c3148203ac0e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
    role: context
  - path: reports/yaml_record_review/20260921T134926Z-archaeoglobus_fulgidus_medium__01928dac.md
    sha256: c8179ba605d1060447c97f02315b5a012f9d7ae79f3074424db8d223b428f46f
    role: context
  - path: reports/yaml_record_review/20260922T140946Z-deferribacter_abyssi_medium__f0deb53f.md
    sha256: 3d82a81889d66e484e28a2dc54110eac7576b1678d6ab7368788a4eaa5ecb51d
    role: context
  - path: reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md
    sha256: 6497a50f712e4169a8f7a7cf4ae62d97e909b6695d86b7c522679b8f08909d7f
    role: context
  - path: reports/yaml_record_review/20260924T234748Z-pyrococcus_medium__a85c0932.md
    sha256: 691813f42cb15ef4629fbe725324ec56b58ae4365e2913707be7cc2316503733
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
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_j261_variant.py
    sha256: 040fbe3cb823c3f4d15f344869a4a88cdb0605147ee1a0d30a9e161dcd132506
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
  selection: Authoritative batch071 index 10
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009739
targets:
- target_id: CultureMech:009739
  path: data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml
  label: deferribacter_abyssi_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
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
  - CultureMech:009739
  command: just validate-schema data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml
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
  - CultureMech:009739
  command: just validate-strict data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml
    --out REVIEW_WORK/batch071/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:009739
  command: just validate-terms data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml
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
  - CultureMech:009739
  command: just validate-references data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: jcm365
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365
  accessed_at: '2026-10-28T15:22:14.209227Z'
  locator: REVIEW_WORK/batch071/source07-08-10/jcm365.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact named source or scoped dependency; bibliographic organism identity
    only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer.
  snapshot_sha256: 3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0
- evidence_id: jcm151
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  accessed_at: '2026-10-28T15:22:14.201182Z'
  locator: REVIEW_WORK/batch071/source07-08-10/jcm151.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact named source or scoped dependency; bibliographic organism identity
    only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer.
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  accessed_at: '2026-10-28T15:22:14.209338Z'
  locator: REVIEW_WORK/batch071/source07-08-10/jcm197.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact named source or scoped dependency; bibliographic organism identity
    only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: currentTogo359
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359
  accessed_at: '2026-10-28T15:22:15.493451Z'
  locator: REVIEW_WORK/batch071/source07-08-10/currentTogo359.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact current provider recipe; M142 trace and M190 vitamin subsection only
    are in scientific dependency scope.
  snapshot_sha256: 0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16
- evidence_id: currentTogo142
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T15:22:15.579215Z'
  locator: REVIEW_WORK/batch071/source07-08-10/currentTogo142.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact current provider recipe; M142 trace and M190 vitamin subsection only
    are in scientific dependency scope.
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
- evidence_id: currentTogo190
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T15:22:16.140967Z'
  locator: REVIEW_WORK/batch071/source07-08-10/currentTogo190.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact current provider recipe; M142 trace and M190 vitamin subsection only
    are in scientific dependency scope.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: apiJ365
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J365
  accessed_at: '2026-10-28T15:22:14.912501Z'
  locator: REVIEW_WORK/batch071/source07-08-10/apiJ365.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact named source or scoped dependency; bibliographic organism identity
    only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer.
  snapshot_sha256: 6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8
- evidence_id: pmid13130062
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:13130062%20AND%20SRC:MED&resultType=core&format=json
  accessed_at: '2026-10-28T15:22:14.854185Z'
  locator: REVIEW_WORK/batch071/source07-08-10/pmid13130062.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact named source or scoped dependency; bibliographic organism identity
    only, no inferred target growth. JCM151 trace and JCM197 vitamins only may transfer.
  snapshot_sha256: b1a35163e5ad9c6358c9fada82004677702f709f14221fb7bae824957e1c07c4
- evidence_id: chebi26833
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26833
  accessed_at: '2026-10-28T15:22:17.418801Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi26833.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 34952547270a6bcbbfa3a3699082c8d5359e51d0f90518ab9ca5400494a8ae33
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  accessed_at: '2026-10-28T15:22:18.022779Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T15:38:29.401834Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 833f624b29e68b1d4de9eab4b3813f645f84c31efa609a4b2c0ba8032d7ed22f
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T15:38:29.401989Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 67aacbc03f71c5e0b382b0a92609b29d71bfb2d9b49e6efa9ae9b2a45c60a75f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T15:38:29.402011Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T15:38:29.402291Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T15:38:29.402313Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T15:38:29.402331Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-j261-variant/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T15:38:29.402354Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 6596fd242999001378304c512ae0e469c74b342c4ba975acec7c80052b746d78
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-j261-variant/records/M142.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.402688Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 3005c0fe47be96230058f7eb8779d9915ff96ebf9de43f2ba476bb7e4f1ac75d
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-j261-variant/records/M253.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.402709Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 8cb25cf38148de75110754cba1ce951746573c3fae7ed47c8169ea604e906f32
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T15:38:29.402758Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M142.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403123Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 42adc98b2f24eef6d866f81a2cdc36eba868fbcf592695cd02c649cae404855b
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403153Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403184Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 8306a05efee0ff5f12e4dcb2cb216c6ebb6bb604a1812ecb1ceac85e6bc1a924
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/deferribacter_abyssi_medium__f0deb53f.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403205Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: a5df34589b23951552885d084fec0e99431831726d7bf07f53cc6374bc4965c2
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__6ffabef8.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403225Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 83c8213491aaeb9764f15234d55e465b4ddadad00dc05bfaa93743419b3d9ea2
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__a85c0932.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403246Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: b7afb33e6091981790d7d02bd4e7a2ecfa11655363fc9ee42994a3b3b3e757ad
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403265Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403285Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 2819146dc7d90f64ef630274b9d757bd510220b222d429716fc29d878d82b1b9
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403309Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 9375b6b75f872d37d8e44d342d6de57746c21933bb15636d8c56c3148203ac0e
- evidence_id: report-32
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403331Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
- evidence_id: report-33
  kind: prior_review
  reference: reports/yaml_record_review/20260921T134926Z-archaeoglobus_fulgidus_medium__01928dac.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403350Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: c8179ba605d1060447c97f02315b5a012f9d7ae79f3074424db8d223b428f46f
- evidence_id: report-34
  kind: prior_review
  reference: reports/yaml_record_review/20260922T140946Z-deferribacter_abyssi_medium__f0deb53f.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403371Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 3d82a81889d66e484e28a2dc54110eac7576b1678d6ab7368788a4eaa5ecb51d
- evidence_id: report-35
  kind: prior_review
  reference: reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403390Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 6497a50f712e4169a8f7a7cf4ae62d97e909b6695d86b7c522679b8f08909d7f
- evidence_id: report-36
  kind: prior_review
  reference: reports/yaml_record_review/20260924T234748Z-pyrococcus_medium__a85c0932.md
  locator: Complete report
  accessed_at: '2026-10-28T15:38:29.403408Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 691813f42cb15ef4629fbe725324ec56b58ae4365e2913707be7cc2316503733
- evidence_id: trace-owner
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
  locator: solutions[1].composition; solutions[1].solutions; solutions[1].preparation_notes
  accessed_at: '2026-10-28T15:38:29.437411Z'
  support: context_only
  summary: Full record read; only trace composition, nested unquantified KOH and trace
    preparation are assessed. Parent doses, other stocks and main preparation are
    excluded.
  snapshot_sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
- evidence_id: vitamin-owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: solutions[1].composition
  accessed_at: '2026-10-28T15:38:29.437480Z'
  support: context_only
  summary: Full provenance read; only the vitamin composition is scientifically assessed.
    Parent receiving doses and all parent preparation are excluded.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _parse_unit, _ingredient_from_item, _extract_preparation_steps, _extract_ph
  accessed_at: '2026-10-28T15:38:29.437528Z'
  support: context_only
  summary: Current _parse_unit already maps l to L and comment extraction retains
    preparation; stored defects are not evidence that those current behaviors are
    absent. Bare mass and ml mappings do not establish final volume. _extract_ph reads
    root ph, whereas the actual source puts ph under meta.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-migration
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: 'SolutionMigrator: current index construction and migration functions'
  accessed_at: '2026-10-28T15:38:29.437564Z'
  support: context_only
  summary: Current migration recognizes solution names, preserves old concentration
    when moving a descriptor, and creates empty composition stubs. Its name-index
    lookup is not a scientific verification of exact referenced stock scope.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-stock-repair
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: Review.leaf, stock, fill, stages, procedures; build; process
  accessed_at: '2026-10-28T15:38:29.437589Z'
  support: context_only
  summary: Current guarded source-specific Review.leaf/stock/fill/stages/procedures
    retain batch amounts without inferred final volume, place claim evidence and trace
    pH by stage. Existing M142/M190 repairs are independently credited against current
    exact raw bytes; this body is not rerun or proof of a historical execution.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: writer-variant
  kind: record_content
  reference: scripts/repair_j261_variant.py
  locator: Review.relationship, Review.finish, build
  accessed_at: '2026-10-28T15:38:29.437617Z'
  support: context_only
  summary: Current relationship and finish preserve the parent formulation and append
    reciprocal variant provenance. That J261/M253 relationship is contextual to M142,
    not a replacement formulation or owner for this JCM365 target.
  snapshot_sha256: 040fbe3cb823c3f4d15f344869a4a88cdb0605147ee1a0d30a9e161dcd132506
- evidence_id: scoped-root-claims
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/scoped-root-claim-authentication.json
  accessed_at: '2026-10-28T15:38:29.454027Z'
  locator: Two exact additional root evidence excerpts
  support: supports
  summary: Root evidence legitimately contains stock claims. Only the exact KOH and
    trace-pH excerpts are authenticated, excluding parent doses and procedures.
  snapshot_sha256: 5beb94c489c2e5db99caf429f010cec88a8213017f19469d10467d93e027173f
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/historical-reading.json
  accessed_at: '2026-10-28T15:38:29.459186Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 709e8ae9bc10cd0e4133cce035838410d5bf5f5c00839712716efb26e175d5f2
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T15:38:29.459304Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 3fd4844f594ad18d2975e199d1335f7a52f6afa14c6e66390509d4cbc1bb1ca3
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/complete-document-reader.json
  accessed_at: '2026-10-28T15:38:29.459496Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: fcd45e12eb3ee93cc44371337526f467ac7ca8a316cdeb8f49125ff7780e6e77
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T15:38:29.459584Z'
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
  accessed_at: '2026-10-28T15:38:29.459619Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch071/record10/historical-current-object-joins.json
  accessed_at: '2026-10-28T15:38:29.459645Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: ea2f8cdb17a5d29c781957f5b3585700af4aa5a25f25d5356008609c8dacb489
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T15:22:16.114980Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T15:22:17.400490Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T15:22:19.436424Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T15:22:19.265681Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T15:22:18.012998Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  accessed_at: '2026-10-28T15:22:19.824223Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  accessed_at: '2026-10-28T15:22:19.401113Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T15:22:18.616026Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  accessed_at: '2026-10-28T15:22:18.626109Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi32954.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  accessed_at: '2026-10-28T15:22:16.929223Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  accessed_at: '2026-10-28T15:22:18.157648Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi31795.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T15:22:19.228285Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T15:22:18.732150Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  accessed_at: '2026-10-28T15:22:19.368301Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  accessed_at: '2026-10-28T15:22:18.198160Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  accessed_at: '2026-10-28T15:22:18.098033Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi31440.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi91244
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  accessed_at: '2026-10-28T15:22:20.005079Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi91244.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  accessed_at: '2026-10-28T15:22:18.763511Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi44557.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi86360
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  accessed_at: '2026-10-28T15:22:19.857529Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi86360.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: chebi86463
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86463
  accessed_at: '2026-10-28T15:22:20.042889Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi86463.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 59060418cddd95e8401be3d2518a69fbcd26a4f4e6f0597b2c8c03834a87812e
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  accessed_at: '2026-10-28T15:22:16.381970Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  accessed_at: '2026-10-28T15:22:17.554050Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  accessed_at: '2026-10-28T15:22:18.808854Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  accessed_at: '2026-10-28T15:22:17.595758Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  accessed_at: '2026-10-28T15:22:17.488913Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  accessed_at: '2026-10-28T15:22:16.800101Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  accessed_at: '2026-10-28T15:22:16.835127Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  accessed_at: '2026-10-28T15:22:16.326977Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  accessed_at: '2026-10-28T15:22:16.793529Z'
  locator: REVIEW_WORK/batch071/source07-08-10/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:38:29.556615Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: accfb61dc6b284d9eade47adc4b231b500ec9ef000bd386d276e1f3d355d6cc1
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:38:29.556710Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 158506675444157f61602400457806c1697067f13fc5dba24fc3ac1629e619ce
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:38:29.556826Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 1839bdbea3b79fa92cd9aadeb0854546685d69594b9e4e2b1aacc7f423f21046
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:38:29.556952Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 2e44737e8b6d5dba8eb642b0a27aab40a0199726ea3a100d4ccb87ac979ddac0
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:38:29.557068Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: cbeda7468cbaeaf4090ca39d967f8ba3b82f100109f44d69ee3e93370b5091ed
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:38:29.557103Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 09975fb3ff9617e8435da3871511d4ba7f6e25b5867d77bc0d1e9b723300c44f
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch071/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:38:29.557125Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 600d3174e829deab3f4e964b49a9c9385685a5dd379b58ef9561166f53af02e6
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch071/record10/schema-result.json
  accessed_at: '2026-10-28T15:21:43.976734Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 6bacdfdcf333f3f17e77c4cde765575d036502d0f9d1feb495e9e04226b95bf0
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch071/record10/strict-result.json
  accessed_at: '2026-10-28T15:21:44.923955Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 22ab6ba76be018aac6d275e9ff217bc433fdf6ca0f5f64b520f3696eb720daba
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch071/record10/terms-result.json
  accessed_at: '2026-10-28T15:21:45.995534Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: f453dc095c483ecdaedfb42061bc5b7b83ac3f5479da1c7c5221f19a67c33a7b
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch071/record10/references-result.json
  accessed_at: '2026-10-28T15:21:46.724116Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: dc337c556b12a7c851d578b21268f636003857847fade4a03b303bffbfc8a243
assessments:
- assessment_id: identity
  area: identity
  topic: Exact identity and scoped source crosswalk
  outcome: supported
  summary: TOGO M359 explicitly links JCM365, and current MediaDive J365 carries the
    matching identity and source. The generated record has one maintained owner. The
    cited species paper supplies bibliographic/environmental context, not an authenticated
    exact formulation or permission to add organism-growth assertions. JCM151 and
    JCM197 transfer only the explicitly referenced trace and vitamin sections.
  target_ids:
  - CultureMech:009739
  evidence_ids:
  - target
  - owner
  - jcm365
  - currentTogo359
  - apiJ365
  - pmid13130062
- assessment_id: classification
  area: consistency
  topic: Complexity and physical state
  outcome: supported
  summary: Yeast extract makes the formulation complex and partly defined. The source
    has no agar, supporting the liquid-medium classification; separately handled sulfur
    does not itself imply an agar medium. Local category bacterial does not certify
    strain growth.
  target_ids:
  - CultureMech:009739
  evidence_ids:
  - target
  - jcm365
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 30 current concentration fields are covered by 46 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009739
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b071-quantity-inventory-v1","target":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","quantity_field_count":30,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact input is 1 L water (provider 1000 ml), not 1 G_PER_L. Restore the input-volume
    unit L. The listed water is not proof of final medium make-up.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=29.4118 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 30,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 30,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 29.4118,\n                        \"mmol_l\":
    503.281,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion. This component
    is separately autoclaved and added, not included in the initial autoclaved mixture.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\":
    2.20066,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\":
    2.37739,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\":
    \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\":
    6.04841,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion. This component
    is separately autoclaved and added, not included in the initial autoclaved mixture.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\":
    1.59137,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Na2S・9H2O","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=0.490196 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion. This is the receiving-batch
    contribution, distinct from the separately prepared neutralized 5% reagent; percent
    basis and stock addition volume remain unspecified.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>S&#183;9H<sub>2</sub>O                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"Na2S・9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\":
    \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\":
    \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.490196,\n                        \"mmol_l\":
    2.04094,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=0.323529 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl                                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.33&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.323529,\n                        \"mmol_l\":
    4.33976,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Sodium acetate","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=2.94118 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Sodium acetate                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"Sodium acetate\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\":
    \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Sodium acetate\",\n                        \"compound_id\":
    731,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.94118,\n                        \"mmol_l\":
    35.8549,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Sulfur","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=9.80392 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion. Sulfur is prepared
    separately; a bulk sulfur reagent is not an isolated sulfur atom.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Sulfur                                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Sulfur\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001062\",\n          \"gmo_id\": \"GMO_001062\",\n          \"label\":
    \"Sulfur powder\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sulfur\",\n                        \"compound_id\":
    80,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 9.80392,\n                        \"mmol_l\":
    305.704,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Yeast
    extract (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    literal source batch amount is supported, but neither primary nor TOGO establishes
    final make-up. MediaDive explicitly reports its different g_l=0.0980392 on declared
    volume 1020 ml. That provider normalization is not an independently measured final
    volume and does not support the local bare G_PER_L value. Preserve the exact input
    mass and stage; do not adopt an invented final-rate conversion.","source_stage":"Receiving
    batch input; separate preparation where stated","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract (BD-Difco)                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\":
    \"GMO_001018\",\n          \"label\": \"Bacto &trade; Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.0980392,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"Nitrogen placeholder","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully leaves gas quantity unquantified. The source specifies an atmosphere,
    not dissolved nitrogen concentration or gas dose. Retain the placeholder if needed
    while restoring gas-handling context; do not turn it into a numeric concentration.","source_stage":"Gas
    atmosphere, not dissolved quantity","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Trace
    minerals (see Medium [M142])","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source adds 10 ml of this exact stock per receiving batch, equal to 0.01 L as
    a volume. The stored 10 G_PER_L is wrong in dimension. Neither a dose per final
    litre nor a stock concentration follows from this amount.","source_stage":"Receiving
    stock addition","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace minerals (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=151\">151</a>)                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"solution\": \"Trace minerals\",\n                        \"solution_id\":
    3804,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"Trace vitamins (see Medium [M190])","local_fields":[{"path":"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source adds 10 ml of this exact stock per receiving batch, equal to 0.01 L as
    a volume. The stored 10 G_PER_L is wrong in dimension. Neither a dose per final
    litre nor a stock concentration follows from this amount.","source_stage":"Receiving
    stock addition","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace vitamins (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\">197</a>)                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\":
    3861,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"Distilled water retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Collapsed 2 identical duplicates: 1.0, 1.0]\n\nSource water batch input: 1 L
    = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe
    the superseded flattened record."}],"decision":"verified","rationale":"The retained
    batch-input note and its existing literal claim match exact current raw bytes,
    including the attached historical digest. The original access event is not newly
    recovered. Water remains an explicit 1 L input, not a verified final stock volume.","source_stage":"Trace
    stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 32 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"MgSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 3.5, 3.0]\n\nSource batch input: 3 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The
    retained batch-input note and its existing literal claim match exact current raw
    bytes, including the attached historical digest. The original access event is
    not newly recovered. The source batch mass remains in notes; absence of an unsupported
    G_PER_L assertion is credited. Explicit provider g_l is confined to its stock
    normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\":
    \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q17","label":"NaCl retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 13.85, 1.0]\n\nSource batch input: 1 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The
    retained batch-input note and its existing literal claim match exact current raw
    bytes, including the attached historical digest. The original access event is
    not newly recovered. The source batch mass remains in notes; absence of an unsupported
    G_PER_L assertion is credited. Explicit provider g_l is confined to its stock
    normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q18","label":"CaCl2・2H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"Na2MoO4・2H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 31 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q20","label":"H3BO3 retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 15.0, 0.01]\n\nSource batch input: 0.01 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"The
    retained batch-input note and its existing literal claim match exact current raw
    bytes, including the attached historical digest. The original access event is
    not newly recovered. The source batch mass remains in notes; absence of an unsupported
    G_PER_L assertion is credited. Explicit provider g_l is confined to its stock
    normalization, not transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 30 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q21","label":"FeSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\":
    \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q22","label":"ZnSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
    \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\":
    \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.347752,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q23","label":"CuSO4・5H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 28 (zero-based)","quote":"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\":
    \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\":
    \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"CoSO4・7H2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> CoSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\":
    \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001050\",\n          \"gmo_id\": \"GMO_001050\",\n          \"label\":
    \"Cobalt(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.645178,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q25","label":"Nitrilotriacetic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Mineral source; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nitrilotriacetic acid                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\":
    \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\":
    \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"MnSO4・xH2O retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[11].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium. Source x/n hydrate is unspecified; no fixed hydration
    number or molar conversion is inferred.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> MnSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[11]","quote":"{\n          \"component_name\":
    \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\":
    \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\":
    1000,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"AlK(SO4)2
    retained stock input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[12].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Trace stock","sources":[{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"HTML
    table row 29 (zero-based)","quote":"<TR><TD WIDTH=75%> AlK(SO<sub>4</sub>)<sub>2</sub>                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[12]","quote":"{\n          \"component_name\":
    \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001088\",\n          \"gmo_id\": \"GMO_001088\",\n          \"label\":
    \"Aluminum potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2\",\n                        \"compound_id\":
    1015,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0387289,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Distilled water retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Merged 3 duplicates: 981.0, 1.0, 1.0]\n\nSource water batch input: 1 L = 1 L.
    This is not a measured final volume. Prior duplicate-collapse notes describe the
    superseded flattened record."}],"decision":"verified","rationale":"The retained
    batch-input note and its existing literal claim match exact current raw bytes,
    including the attached historical digest. The original access event is not newly
    recovered. Water remains an explicit 1 L input, not a verified final stock volume.","source_stage":"Vitamin
    stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"Biotin retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q30","label":"p--Aminobenzoic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q31","label":"Thiamine・HCl retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q32","label":"Calcium pantothenate retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium. Generic calcium pantothenate does not establish the
    D stereochemistry of the asserted ontology term; amount authentication does not
    recertify that specificity.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Calcium pantothenate                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0104925,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q33","label":"Pyridoxine・HCl retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q34","label":"Folic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Folic acid                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.00453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q35","label":"Vitamin B12 retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\":
    7.3779e-5,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q36","label":"Riboflavin retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> Riboflavin                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q37","label":"Nicotinic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.0406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q38","label":"Lipoic acid retained stock input","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"The retained batch-input
    note and its existing literal claim match exact current raw bytes, including the
    attached historical digest. The original access event is not newly recovered.
    The source batch mass remains in notes; absence of an unsupported G_PER_L assertion
    is credited. Explicit provider g_l is confined to its stock normalization, not
    transferred into the medium.","source_stage":"Vitamin stock","sources":[{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T15:22:14.209338Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Lipoic acid                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T15:22:16.140967Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\":
    368,\n                        \"amount\": 5,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\":
    0.024233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q39","label":"Unquantified KOH retained note","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].solutions[0].notes","stored":"Role:
    Mineral source; Properties: Defined component, Solution\n\npH-adjustment reagent;
    no fixed dose is specified. Normality is not converted to molarity."}],"decision":"verified","rationale":"The
    exact additional root-attached excerpt authenticates this retained claim against
    the same current raw digest. KOH is a pH-adjustment reagent with no fixed amount;
    no concentration is invented.","source_stage":"Trace stock preparation","sources":[{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"components[2].items[13]","quote":"{\n          \"component_name\":
    \"KOH solution\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\":
    \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Retained
    trace pH and order","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].preparation_notes","stored":"Dissolve
    nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to
    add minerals. Adjust final pH to 7.0."}],"decision":"verified","rationale":"The
    exact additional root-attached excerpt authenticates this retained claim against
    the same current raw digest. The 6.5 adjustment precedes mineral addition and
    final stock pH 7.0. These are stock-only controls, not receiving-medium pH.","source_stage":"Trace
    stock preparation","sources":[{"evidence_id":"currentTogo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T15:22:15.579215Z","locator":"comments[1].comment","quote":"\"Dissolve
    nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to
    add minerals. Adjust final pH to 7.0.\"","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T15:22:14.201182Z","locator":"jcm151.txt
    lines 203-203","quote":"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with
    KOH solution.      Then proceed to add minerals.   Adjust final pH to 7.0.","quote_basis":"derivative
    text"}]},{"quantity_id":"q41","label":"Initial pH","local_fields":[],"decision":"evidence_only","rationale":"The
    source specifies pH 6.5 before autoclaving; later readjustment is conditional,
    not a new range.","source_stage":"Source-only receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust
    pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and
    add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave
    neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture
    vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers.
    Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust
    pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt
    lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO,
    sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave
    CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur
    for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO
    under a N\n2\natmosphere. Dispense the medium into culture vessels containing
    sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior
    to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust
    pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q42","label":"Separate
    calcium and magnesium treatment","local_fields":[],"decision":"evidence_only","rationale":"Exclude
    these two reagents from the initial mixture, sterilize separately and then add
    them; no unstated stock volume or strength is invented.","source_stage":"Source-only
    receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust
    pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and
    add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave
    neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture
    vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers.
    Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust
    pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt
    lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO,
    sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave
    CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur
    for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO
    under a N\n2\natmosphere. Dispense the medium into culture vessels containing
    sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior
    to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust
    pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q43","label":"Sulfur
    steam schedule","local_fields":[],"decision":"evidence_only","rationale":"The
    printed 3 h on each of 3 successive days belongs to sulfur steam treatment. No
    steam temperature or 121-degree sulfur autoclave claim is inferred.","source_stage":"Source-only
    receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust
    pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and
    add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave
    neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture
    vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers.
    Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust
    pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt
    lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO,
    sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave
    CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur
    for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO
    under a N\n2\natmosphere. Dispense the medium into culture vessels containing
    sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior
    to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust
    pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q44","label":"Sulfide
    stock label","local_fields":[],"decision":"evidence_only","rationale":"Neutralized
    5% sodium sulfide nonahydrate is prepared separately. Percent basis and receiving
    addition volume are unstated; preserve the literal label without percent-to-mass
    conversion.","source_stage":"Source-only receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust
    pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and
    add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave
    neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture
    vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers.
    Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust
    pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt
    lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO,
    sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave
    CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur
    for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO
    under a N\n2\natmosphere. Dispense the medium into culture vessels containing
    sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior
    to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust
    pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q45","label":"Atmosphere
    and sequence","local_fields":[],"decision":"evidence_only","rationale":"Nitrogen
    atmosphere, vessel sealing and delayed sterile sulfide addition are explicit preparation
    context. No gas dose, incubation temperature or growth outcome is inferred.","source_stage":"Source-only
    receiving-medium preparation","sources":[{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ365","reference":"https://mediadive.dsmz.de/rest/medium/J365","raw_path":"REVIEW_WORK/batch071/source07-08-10/apiJ365.raw","raw_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","text_sha256":"6f2774f73ab6efd5729a5a4ccd040342271a0306365b63f5ec13cffdcf966db8","accessed_at":"2026-10-28T15:22:14.912501Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Mix ingredients except CaCl2 x 2H2O, MgCl2 x 6H2O, sulfur and Na2S x 9H2O, adjust
    pH to 6.5 and autoclave. Separately autoclave CaCl2 x 2H2O and MgCl2 x 6H2O and
    add to the medium. Steam sulfur for 3 hr on each of 3 successive days. Autoclave
    neutralized 5% Na2S x 9H2O under a N2 atmosphere. Dispense the medium into culture
    vessels containing sulfur under a N2 atmosphere, and seal with butyl rubber stoppers.
    Prior to inoculation, add the sterile Na2S x 9H2O solution to the medium and readjust
    pH, if necessary.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt
    lines 66-98","quote":"Mix ingredients except CaCl\n2\n·2H\n2\nO, MgCl\n2\n·6H\n2\nO,
    sulfur and Na\n2\nS·9H\n2\nO, adjust pH to 6.5 and autoclave.  Separately autoclave
    CaCl\n2\n·2H\n2\nO and MgCl\n2\n·6H\n2\nO and add to the medium.  Steam sulfur
    for 3 hr on each of 3 successive days.   Autoclave neutralized 5% Na\n2\nS·9H\n2\nO
    under a N\n2\natmosphere. Dispense the medium into culture vessels containing
    sulfur under a N\n2\natmosphere, and seal with butyl rubber stoppers.   Prior
    to inoculation, add the sterile Na\n2\nS·9H\n2\nO solution to the medium and readjust
    pH, if necessary.","quote_basis":"derivative text"}]},{"quantity_id":"q46","label":"Default
    autoclave statement","local_fields":[],"decision":"evidence_only","rationale":"JCM
    states 121 degrees C for 15 min unless otherwise specified. Credit this default
    only for the source autoclave steps; sulfur has its separate printed steam schedule.","source_stage":"Source
    default with explicit exceptions","sources":[{"evidence_id":"jcm365","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=365","raw_path":"REVIEW_WORK/batch071/source07-08-10/jcm365.raw","raw_sha256":"3c8f8f90432c39c39829f07e4e13126bc6037eaa3a989bc9e173d8d0df6299a0","text_sha256":"0c10eacb8073b50e57875c35811006358019de3eac1293d4b9113b056ac30f56","accessed_at":"2026-10-28T15:22:14.209227Z","locator":"jcm365.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"currentTogo359","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M359","raw_path":"REVIEW_WORK/batch071/source07-08-10/currentTogo359.raw","raw_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","text_sha256":"0ca5b6a84d97a5e7dadec590f430309184cdc2bc32882cafd6fe28b89fe56c16","accessed_at":"2026-10-28T15:22:15.493451Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix ingredients except CaCl2・2H2O, MgCl2・6H2O, sulfur
    and Na2S・9H2O, adjust pH to 6.5 and autoclave. Separately autoclave CaCl2・2H2O
    and MgCl2・6H2O and add to the medium. Steam sulfur for 3 hr on each of 3 successive
    days. Autoclave neutralized 5% Na2S・9H2O under a N2 atmosphere. Dispense the medium
    into culture vessels containing sulfur under a N2 atmosphere, and seal with butyl
    rubber stoppers. Prior to inoculation, add the sterile Na2S・9H2O solution to the
    medium and readjust pH, if necessary.\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DEFERRIBACTER_ABYSSI_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml":["solutions[1].preferred_term","solutions[1].composition","solutions[1].solutions","solutions[1].preparation_notes"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].preferred_term","solutions[1].composition"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Current exact active OLS IDs/labels and packaged MIM rows are all joined,
    including scoped stock forms. The confirmed supplied-form error is the sulfur
    atom grounding. M142 manganese sulfate x/n hydrate remains unspecified; its generic
    base-salt ID does not certify an anhydrous or fixed-hydrate reagent. Generic calcium
    pantothenate does not establish the D stereochemistry of CHEBI:31345, so no stereochemical
    replacement or mass conversion is asserted. Vitamin B12 class, non-stoichiometric
    mixtures and unspecified acetate hydrate are not silently specialized. Secondary-link
    presence is reported separately from current label/row agreement.
  target_ids:
  - CultureMech:009739
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: Complete current target/owner histories, both scoped dependency histories
    and all 16 native historical reports were read losslessly. The 24 retained composition
    claims and two scoped additional root excerpts match current exact raw digests
    from the October repair; current retrieval times are not backdated. Older flattened/merged
    records and J261/M253 relationships are comparison or provenance only, not extra
    owners of this singleton target. Historic per-litre assumptions are not adopted.
    Current stock repairs, l-to-L handling, comment retention and conservative formulation
    matching are credited; no writer is replayed and current bodies are not historical
    execution proof.
  target_ids:
  - CultureMech:009739
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009739-water-stock-units-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Input volumes and final concentration bases are misrepresented
  description: Correct maintained water from 1 G_PER_L to its exact 1 L input and
    each 10 G_PER_L stock addition to the source 10 ml batch dose. Preserve main input
    masses without asserting an unestablished final litre. MediaDive declares volume
    1020 ml and different g_l values; retain that provider basis as context rather
    than silently substituting it for measured final make-up. Regenerate only after
    owner curation.
  target_ids:
  - CultureMech:009739
  field_paths:
  - ingredients
  - solutions[0].concentration
  - solutions[1].concentration
  evidence_ids:
  - jcm365
  - currentTogo359
  - apiJ365
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-009739-stock-resolution
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Exact trace and vitamin definitions are not represented
  description: Resolve the trace and vitamin references to the exact assessed M142
    trace and M190 vitamin subtrees, or preserve equivalent source-scoped definitions
    and provenance. Current compositions are empty and names remain Unknown solution.
    The current M142 trace composition agrees with JCM151; the retained stock repairs
    are credited, not overwritten. Exclude both parent media, their receiving doses
    and unrelated stock or preparation sections.
  target_ids:
  - CultureMech:009739
  field_paths:
  - solutions[0].composition
  - solutions[1].composition
  - solutions[0].name
  - solutions[1].name
  evidence_ids:
  - jcm365
  - jcm151
  - jcm197
  - currentTogo142
  - currentTogo190
  - trace-owner
  - vitamin-owner
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-009739-preparation-stage-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The defining preparation stages are absent
  description: Restore the source initial pH, separate calcium/magnesium treatment,
    sulfur steam schedule, literal sulfide stock label, nitrogen handling and final
    addition sequence with their exact supporting claims. Keep unspecified percent
    basis, stock dose and final volume unresolved. Credit current importer comment
    retention and fix only demonstrated parser boundaries; do not import preparation
    from M142 or M190 parent media.
  target_ids:
  - CultureMech:009739
  field_paths:
  - preparation_steps
  - ph_value
  - sterilization
  evidence_ids:
  - jcm365
  - currentTogo359
  - apiJ365
  - writer-togo
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: 'P2-equivalent custom preparation-scope finding: missing material
    separation, handling sequence and source controls are substantial completeness
    issues, despite passing native shape checks.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-009739-bulk-sulfur-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Bulk sulfur is grounded to an isolated sulfur atom
  description: The source uses a bulk sulfur reagent with separate handling. CHEBI:26833
    is a sulfur atom, with atomic formula/structure, so the matching canonical label
    does not establish the supplied material. Reconcile both primary and secondary
    sulfur slots against a verified material-level term without inferring an unreported
    allotrope.
  target_ids:
  - CultureMech:009739
  field_paths:
  - ingredients[9].term
  - ingredients[9].mediaingredientmech_chebi_term
  evidence_ids:
  - jcm365
  - currentTogo359
  - chebi26833
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-009739-claim-and-placeholder-metadata
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Maintained claims and stock names need explicit provenance
  description: Attach exact source claims to the selected maintained owner, including
    unchanged supported inputs and unresolved denominator boundaries. Credit all 24
    existing scoped dependency ingredient claims and the two additional trace root
    excerpts. Replace existing Unknown solution placeholders with their demonstrated
    source names, including the scoped KOH descriptor, without inventing its quantity.
    Preserve prior history and append new events.
  target_ids:
  - CultureMech:009739
  field_paths:
  - evidence
  - ingredients
  - solutions
  - data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml::solutions[1].solutions[0].name
  evidence_ids:
  - jcm365
  - currentTogo359
  - old-claims
  - scoped-root-claims
  - writer-stock-repair
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: Correct maintained water from 1 G_PER_L to its exact 1 L input and
    each 10 G_PER_L stock addition to the source 10 ml batch dose. Preserve main input
    masses without asserting an unestablished final litre. MediaDive declares volume
    1020 ml and different g_l values; retain that provider basis as context rather
    than silently substituting it for measured final make-up. Regenerate only after
    owner curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009739
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
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
  description: Resolve the trace and vitamin references to the exact assessed M142
    trace and M190 vitamin subtrees, or preserve equivalent source-scoped definitions
    and provenance. Current compositions are empty and names remain Unknown solution.
    The current M142 trace composition agrees with JCM151; the retained stock repairs
    are credited, not overwritten. Exclude both parent media, their receiving doses
    and unrelated stock or preparation sections.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009739
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
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
  description: Restore the source initial pH, separate calcium/magnesium treatment,
    sulfur steam schedule, literal sulfide stock label, nitrogen handling and final
    addition sequence with their exact supporting claims. Keep unspecified percent
    basis, stock dose and final volume unresolved. Credit current importer comment
    retention and fix only demonstrated parser boundaries; do not import preparation
    from M142 or M190 parent media.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009739
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
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
  description: The source uses a bulk sulfur reagent with separate handling. CHEBI:26833
    is a sulfur atom, with atomic formula/structure, so the matching canonical label
    does not establish the supplied material. Reconcile both primary and secondary
    sulfur slots against a verified material-level term without inferring an unreported
    allotrope.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009739
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: Attach exact source claims to the selected maintained owner, including
    unchanged supported inputs and unresolved denominator boundaries. Credit all 24
    existing scoped dependency ingredient claims and the two additional trace root
    excerpts. Replace existing Unknown solution placeholders with their demonstrated
    source names, including the scoped KOH descriptor, without inventing its quantity.
    Preserve prior history and append new events.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009739
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M359_Deferribacter_Abyssi_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
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
- M142 scientific scope is only its trace subtree and trace preparation; M190 scope
  is only its vitamin composition. Parent receiving doses, basal amounts, other stocks
  and main preparation are unassessed and excluded from transfer.
- Only metadata/abstract context of PMID:13130062 was read, not the full paper. No
  exact formulation, strain-growth evidence or conditions are inferred from that paper.
- Exact sulfur material/allotrope, generic calcium-pantothenate stereochemistry, unspecified
  manganese hydration and sulfide percent basis remain unresolved; no chemical or
  final-volume conversions are proposed.
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
