# Scientific review: CLOSTRIDIUM ACETATE 1 MEDIUM

- Review: 20261028T093723Z-culturemech-003124-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T09:30:17.876858Z
- Finished UTC: 2026-10-28T09:37:23.685308Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The JCM781 identity and existing preparation text are retained, but three stock aliquots, a nine-component trace stock and one nickel hydrate mapping require curation. Every current amount and source-only control is inventoried with explicit provider/primary basis limits; no recipes were edited.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch062 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003124 | data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml | generated | clostridium_acetate_1_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:003124 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:003124 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:003124 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:003124 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact JCM781 identity and dependency scope

identity: supported. Targets: CultureMech:003124.

The maintained JCM J781 owner is the sole declared generation contributor. The historical October5 report also nominated TOGO M811 as a candidate by identity/name; it is not a current generation owner and its formulation is not transferred. JCM439 is consulted only for the explicitly linked trace subsection.

### Classification and organism scope

scope: supported. Targets: CultureMech:003124.

The source contains yeast extract and is a liquid complex formulation. No specific strain or growth evidence is asserted by the reviewed primary texts; no organism association is created from the name.

### Native structural diagnostics

schema: supported. Targets: CultureMech:003124.

All four canonical checks returned zero; strict reports no errors and references checked zero entries. These diagnostics do not establish chemical form, recipe stage or source completeness.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:003124.

44 current concentration fields are covered by 29 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b062-quantity-inventory-v1","target":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","quantity_field_count":44,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.28222 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.28222,\n                        \"mmol_l\": 2.07384,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.28222 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.28222,\n                        \"mmol_l\": 1.62032,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; K&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.940734 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.940734,\n                        \"mmol_l\": 17.5871,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.940734 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.940734,\n                        \"mmol_l\": 16.0974,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.0940734 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0940734,\n                        \"mmol_l\": 1.26188,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KCl                                                     &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.0940734 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0940734,\n                        \"mmol_l\": 0.63989,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.470367 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.470367,\n                        \"mmol_l\": 2.31362,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.940734 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.940734,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"L-Cysteine HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.470367 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.470367,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; L-Cysteine&amp;#183;HCl&amp;#183;H&lt;sub&gt;2&lt;/sub&gt;O                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.000940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.000940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both local values equal the explicit provider g_l=0.000940734 rate. MediaDive declares volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions per liter. This is support for the provider's stated normalization only, not independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.000940734,\n                        \"mmol_l\": 0.0041046,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"NaHCO3 stock addition","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"Local 25 G_PER_L misrepresents the source's 25 ml stock addition. JCM explicitly introduces these additions as per liter after cooling. Preserve the *, 8% stock attribute separately: fructose 1 M is explicit; 8% bicarbonate and 5% sulfide lack a stated percentage basis. Do not infer a mass dose, stock density or final-medium concentration.","source_stage":"Post-cooling anaerobic stock additions","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution*                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;25.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 13,\n                        \"step\": \"Mix components thoroughly, distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Fructose stock addition","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"Local 20 G_PER_L misrepresents the source's 20 ml stock addition. JCM explicitly introduces these additions as per liter after cooling. Preserve the 1 M stock attribute separately: fructose 1 M is explicit; 8% bicarbonate and 5% sulfide lack a stated percentage basis. Do not infer a mass dose, stock density or final-medium concentration.","source_stage":"Post-cooling anaerobic stock additions","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Fructose\",\n                        \"compound_id\": 98,\n                        \"attribute\": \"1 M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1 M Fructose solution                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 13,\n                        \"step\": \"Mix components thoroughly, distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Na2S x 9 H2O stock addition","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"Local 8 G_PER_L misrepresents the source's 8 ml stock addition. JCM explicitly introduces these additions as per liter after cooling. Preserve the 5% stock attribute separately: fructose 1 M is explicit; 8% bicarbonate and 5% sulfide lack a stated percentage basis. Do not infer a mass dose, stock density or final-medium concentration.","source_stage":"Post-cooling anaerobic stock additions","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"attribute\": \"5%\",\n                        \"amount\": 8,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 13,\n                        \"step\": \"Mix components thoroughly, distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"HCl in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"12.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"12.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local 12.5 G_PER_L is a volume-to-mass error as well as a stage error: the trace-stock recipe specifies 12.5 ml HCl (25%). Percentage basis and density are unspecified; no mass conversion is justified.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 12.5,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; HCl (25%)                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;12.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"FeSO4 x 7 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=2.1, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 2.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.1,\n                        \"mmol_l\": 7.55355,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"H3BO3 in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=0.03, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 30,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.485123,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"MnCl2 x 4 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=0.1, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"CoCl2 x 6 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=0.19, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=0.024, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"CuCl2 x 2 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=0.002, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"ZnSO4 x 7 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.144","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.144","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=0.144, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 144,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.144,\n                        \"mmol_l\": 0.500763,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;144.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Na2MoO4 x 2 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The local value matches provider stock g_l=0.036, but is flattened into the main ingredient list. The source instead places this component in the trace stock added at 10 ml per J781 recipe batch. Preserve the original stock mass and provider-declared stock rate separately; 987 ml water plus acid input does not establish an independently measured final stock volume. No working concentration is calculated.","source_stage":"JCM439 trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Main water input","local_fields":[],"decision":"evidence_only","rationale":"Primary 1 L water / provider 1000 ml is an input amount omitted locally. It is not a final-volume measurement.","source_stage":"Main batch water","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Trace stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"J781 specifies 10 ml trace stock. The parent JCM439 receiving dose is excluded; no 1 ml transfer is made.","source_stage":"J781 trace-stock addition","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\"&gt;439&lt;/a&gt;)          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\": 4186,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Trace-stock water input","local_fields":[],"decision":"evidence_only","rationale":"987 ml water is a source input, not an explicit final-makeup instruction. Keep the HCl aliquot separate.","source_stage":"Trace-stock preparation","sources":[{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;987.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 987,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Existing distribution and anaerobic sequence","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix components thoroughly, distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):"},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"preparation_steps[0].description","stored":"Mix components thoroughly, distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter-sterilized):"}],"decision":"evidence_only","rationale":"Both local descriptions retain the 5 ml example, N2-CO2 4:1 v/v atmosphere, seal/autoclave sequence and post-cooling per-liter stock introduction. Credit this text; the missing stock descriptors prevent it from fully identifying the additions. No incubation or growth claim follows.","source_stage":"Current preparation text","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 13,\n                        \"step\": \"Mix components thoroughly, distribute the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave. After cooling, add per liter the following solutions from anaerobic stocks (autoclaved or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"JCM general sterilization default","local_fields":[],"decision":"evidence_only","rationale":"The catalog states a general default of 121°C for 15 min unless otherwise stated. Record it only with that conditional scope; it is not an independently validated stock-specific condition.","source_stage":"Conditional primary catalog default","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"Catalog general default before recipe","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q28","label":"Unspecified stock percentage bases","local_fields":[],"decision":"unsupported","rationale":"The printed 8%, 5% and 25% have no w/v, w/w or v/v qualifier in the exact sources. Their source labels are supported; selecting a percentage enum or deriving mass concentrations remains unsupported.","source_stage":"Stock strengths; unresolved basis","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution*                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;25.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 5% Na&lt;sub&gt;2&lt;/sub&gt;S&amp;#183;9H&lt;sub&gt;2&lt;/sub&gt;O solution                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;8.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; HCl (25%)                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;12.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Fructose stock molarity","local_fields":[],"decision":"evidence_only","rationale":"The source explicitly states 1 M fructose. Preserve this stock molarity and the separate receiving aliquot; do not substitute 20 g/L.","source_stage":"Fructose stock strength","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML table row 13 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 1 M Fructose solution                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;20.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:003124.

All asserted CHEBI objects resolve with current canonical labels, and the exact packaged MIM row joins are inventoried. The nickel hexahydrate source contradicts anhydrous CHEBI:34887 despite label agreement. Other hydrates are form-consistent with the inspected primary names; generic fructose remains generic, yeast extract has no fabricated pure-chemical ID, and a chemical ID does not define a stock percentage basis.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:003124.

The October5 reports were explicit unverified inventories; the October7 J781 report left all 22 concentration fields unchanged because stock topology required source-specific work. Its source rows can be compared to the fresh payload without claiming historical execution. Current primary-only MediaDive parsing and conservative formulation merging are credited, with the molar-only stock and conditional volume normalization boundaries retained.

## Findings

### f1: Three stock aliquots are represented as direct mass concentrations

major / open / confirmed; issue key: culturemech-003124-stock-volume-as-mass.

Reconcile ingredients[10:13] against the exact JCM781 post-cooling stock additions: the three printed ml amounts are currently labelled G_PER_L. Restore separate stock descriptors, source-explicit fructose molarity and scoped receiving doses; preserve unresolved percentage bases. The current importer recognizes percent-labelled ml stocks but not the molar-only fructose attribute, so audit that remaining parser boundary rather than claiming all current imports still flatten every stock.

### f2: Trace-stock components and acid aliquot are flattened into the medium

major / open / confirmed; issue key: culturemech-003124-trace-stock-flattening.

Move the nine trace-stock components out of direct main-medium concentrations and retain the source-specific trace composition, 10 ml receiving dose and separate water/acid input basis. HCl 12.5 ml at unspecified-basis 25% cannot be 12.5 g/L. Do not import the JCM439 parent basal formulation, its receiving dose, or an inferred final volume.

### f3: Nickel hexahydrate is keyed to anhydrous nickel dichloride

major / open / confirmed; issue key: culturemech-003124-nickel-hydrate.

The supplied NiCl2·6H2O at ingredients[18] has CHEBI:34887 (Cl2Ni) in both primary and secondary slots. Fresh OLS CHEBI:53542 explicitly describes nickel chloride hexahydrate and provides the six-water formula. Curate both affected slots after source-form reconciliation; a matching current label or MIM row does not resolve the hydrate mismatch.

### f4: Source basis and omitted water controls need explicit evidence

minor / open / confirmed; issue key: culturemech-003124-source-evidence-and-controls.

Attach exact source-stage evidence and restore input-water context when curating the stock topology. Retain the existing anaerobic preparation text and qualify the JCM general sterilization default rather than inventing stock conditions. Explain the provider 1063 ml normalization separately from the primary initial water and per-liter additions; no new pH or strain-growth assertion is supported.

## Recommended Actions And Acceptance Checks

### a1

Reconcile ingredients[10:13] against the exact JCM781 post-cooling stock additions: the three printed ml amounts are currently labelled G_PER_L. Restore separate stock descriptors, source-explicit fructose molarity and scoped receiving doses; preserve unresolved percentage bases. The current importer recognizes percent-labelled ml stocks but not the molar-only fructose attribute, so audit that remaining parser boundary rather than claiming all current imports still flatten every stock.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Move the nine trace-stock components out of direct main-medium concentrations and retain the source-specific trace composition, 10 ml receiving dose and separate water/acid input basis. HCl 12.5 ml at unspecified-basis 25% cannot be 12.5 g/L. Do not import the JCM439 parent basal formulation, its receiving dose, or an inferred final volume.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The supplied NiCl2·6H2O at ingredients[18] has CHEBI:34887 (Cl2Ni) in both primary and secondary slots. Fresh OLS CHEBI:53542 explicitly describes nickel chloride hexahydrate and provides the six-water formula. Curate both affected slots after source-form reconciliation; a matching current label or MIM row does not resolve the hydrate mismatch.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Attach exact source-stage evidence and restore input-water context when curating the stock topology. Retain the existing anaerobic preparation text and qualify the JCM general sterilization default rather than inventing stock conditions. Explain the provider 1063 ml normalization separately from the primary initial water and per-liter additions; no new pH or strain-growth assertion is supported.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| apiJ781 | https://mediadive.dsmz.de/rest/medium/J781; REVIEW_WORK/batch062/source07-09/apiJ781.json; exact original raw/text/hash/time metadata | context_only | Exact selected source identity and complete source stages; inspect organism context before operational assessment. KOMODO catalog is identity only. |
| jcm781HTML | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781; REVIEW_WORK/batch062/source07-09/jcm781HTML.json; exact original raw/text/hash/time metadata | context_only | Exact current source catalog from selected record or attached historical literal hyperlink. Prior guessed PDF404 preserved separately; no automatic retry. |
| jcm439HTML | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439; REVIEW_WORK/batch062/source07-09/jcm439HTML.json; exact original raw/text/hash/time metadata | context_only | Exact literal linked source: JCM439 trace-element subsection only, excluding parent basal recipe and receiving dose; KOMODO411 historical catalog hyperlink identity only. |
| jcm781 | https://www.jcm.riken.jp/medium/medium/JCM781.pdf; REVIEW_WORK/batch062/source07-09/jcm781.json; exact original raw/text/hash/time metadata | context_only | Exact selected source identity and complete source stages; inspect organism context before operational assessment. KOMODO catalog is identity only. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch062/source07-09/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| target | data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/clostridium_acetate_1_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-19 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_acetate_1_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch062/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch062/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch062/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit, _parse_preparation_steps | context_only | Current _parse_api_composition reads the primary solution only; _is_api_stock_addition recognizes solution_id or percent-labelled ml rows. Molar-only stock attributes are outside that predicate; preparation steps are pooled across solutions. Current code is not proof of historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; merge_duplicate_ingredients and _merge_ingredient_group | context_only | Current _merge_ingredient_group no longer sums disagreeing duplicate concentrations; keeps first and flags conflicts. Historical summed notes remain separate evidence. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch062/source07-09/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch062/source07-09/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch062/source07-09/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch062/source07-09/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch062/source07-09/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch062/source07-09/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch062/source07-09/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248; REVIEW_WORK/batch062/source07-09/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch062/source07-09/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch062/source07-09/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi28757 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28757; REVIEW_WORK/batch062/source07-09/chebi28757.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch062/source07-09/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch062/source07-09/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; REVIEW_WORK/batch062/source07-09/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch062/source07-09/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch062/source07-09/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch062/source07-09/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch062/source07-09/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch062/source07-09/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch062/source07-09/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch062/source07-09/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| quantities | REVIEW_WORK/batch062/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch062/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch062/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch062/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch062/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch062/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch062/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch062/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch062/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch062/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch062/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The two guessed /medium/medium/JCM*.pdf URLs were not source evidence: each returned 404 and remains preserved. The exact existing-record JCM781 catalog URL returned usable HTML.
- Only the trace subsection of JCM439 is evidence for this record; parent nutrients, other stocks, receiving doses and organism context are excluded.
- No numerical final-medium concentrations are derived from 1063 ml, the 1 L water input, or the printed percent stock labels. Unknown author/publication year metadata remains unknown.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T093723Z-culturemech-003124-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CLOSTRIDIUM ACETATE 1 MEDIUM'
started_at: '2026-10-28T09:30:17.876858Z'
finished_at: '2026-10-28T09:37:23.685308Z'
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
summary: The JCM781 identity and existing preparation text are retained, but three
  stock aliquots, a nine-component trace stock and one nickel hydrate mapping require
  curation. Every current amount and source-only control is inventoried with explicit
  provider/primary basis limits; no recipes were edited.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml
    sha256: 77066892e1fde1cd08d4f6d02eecd65cf97b341aa00924fee83b6d0a64b9da19
    role: target
  - path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
    sha256: 3f096deab4738d46bbaa0e4bfa7b35fe13dcf502be71e43eb242cd9b8c9f7e7d
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/clostridium_acetate_1_medium.yaml.md
    sha256: d9b5a642e2a43bc6b954ccc7defb3ffae331f7d520b2ffcc6ae76723b6a88189
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.md
    sha256: cd6b6585c1b1339e91ca8c25b6db3fa1f9ef26ef3de9f341da88a68dd8d9dd8f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_acetate_1_medium.md
    sha256: 91f72e47fe325c7589ac4b3ddde4e9f17386132cab1cd6fa0d7bbeb8a69b47f9
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
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_dsmz489_stocks.py
    sha256: 0e86a9b273b82de1adf556a1d300f215da3ea64b84fc7eaadc10f77ea79d190e
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
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
  selection: Authoritative batch062 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003124
targets:
- target_id: CultureMech:003124
  path: data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml
  label: clostridium_acetate_1_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
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
  - CultureMech:003124
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml
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
  - CultureMech:003124
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml
    --out REVIEW_WORK/batch062/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:003124
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml
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
  - CultureMech:003124
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: apiJ781
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J781
  accessed_at: '2026-10-28T09:30:19.508803Z'
  locator: REVIEW_WORK/batch062/source07-09/apiJ781.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected source identity and complete source stages; inspect organism
    context before operational assessment. KOMODO catalog is identity only.
  snapshot_sha256: 7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab
- evidence_id: jcm781HTML
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781
  accessed_at: '2026-10-28T09:31:21.664270Z'
  locator: REVIEW_WORK/batch062/source07-09/jcm781HTML.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current source catalog from selected record or attached historical
    literal hyperlink. Prior guessed PDF404 preserved separately; no automatic retry.
  snapshot_sha256: 8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2
- evidence_id: jcm439HTML
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439
  accessed_at: '2026-10-28T09:33:09.184119Z'
  locator: REVIEW_WORK/batch062/source07-09/jcm439HTML.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 'Exact literal linked source: JCM439 trace-element subsection only, excluding
    parent basal recipe and receiving dose; KOMODO411 historical catalog hyperlink
    identity only.'
  snapshot_sha256: 2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda
- evidence_id: jcm781
  kind: search
  reference: https://www.jcm.riken.jp/medium/medium/JCM781.pdf
  accessed_at: '2026-10-28T09:30:19.681826Z'
  locator: REVIEW_WORK/batch062/source07-09/jcm781.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected source identity and complete source stages; inspect organism
    context before operational assessment. KOMODO catalog is identity only.
  snapshot_sha256: 81328808599f42cf0913bb061fee2ee27ca61954b0eaae5647371a6667c73ac5
  search_scope: One exact public GET of https://www.jcm.riken.jp/medium/medium/JCM781.pdf;
    retained status 404. No exhaustive repository or literature absence claim.
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T09:30:22.610738Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T09:37:23.590882Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 77066892e1fde1cd08d4f6d02eecd65cf97b341aa00924fee83b6d0a64b9da19
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T09:37:23.591057Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 3f096deab4738d46bbaa0e4bfa7b35fe13dcf502be71e43eb242cd9b8c9f7e7d
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T09:37:23.591088Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T09:37:23.591394Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T09:37:23.591419Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T09:37:23.591441Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T09:37:23.591467Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1db6b2b69fb7a9a131c95c22d837d6a4c5f10dab810921069496169a06d6f5c2
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000/records/bacterial/clostridium_acetate_1_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T09:37:23.596473Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d9b5a642e2a43bc6b954ccc7defb3ffae331f7d520b2ffcc6ae76723b6a88189
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T09:37:23.596525Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: cd6b6585c1b1339e91ca8c25b6db3fa1f9ef26ef3de9f341da88a68dd8d9dd8f
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_acetate_1_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T09:37:23.596553Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 91f72e47fe325c7589ac4b3ddde4e9f17386132cab1cd6fa0d7bbeb8a69b47f9
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/historical-reading.json
  accessed_at: '2026-10-28T09:37:23.596588Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 6ee6ce0b222ee88689eaca0372eb4cac0cd209f0fc5fcb93ccb0e42012379c1c
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T09:37:23.596861Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 5e363d90ecc34c20573594e99f71456ca5985bfd201a65fa108397be6cfe7175
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/complete-document-reader.json
  accessed_at: '2026-10-28T09:37:23.597021Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 24a9a0e4dbe177fff612ab275bced99b7ce0bab4457ba39027b68163bc27ae58
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit,
    _parse_preparation_steps
  accessed_at: '2026-10-28T09:37:23.597166Z'
  support: context_only
  summary: Current _parse_api_composition reads the primary solution only; _is_api_stock_addition
    recognizes solution_id or percent-labelled ml rows. Molar-only stock attributes
    are outside that predicate; preparation steps are pooled across solutions. Current
    code is not proof of historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: merge_duplicate_ingredients and _merge_ingredient_group
  accessed_at: '2026-10-28T09:37:23.597208Z'
  support: context_only
  summary: Current _merge_ingredient_group no longer sums disagreeing duplicate concentrations;
    keeps first and flags conflicts. Historical summed notes remain separate evidence.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T09:37:23.597236Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T09:30:22.703175Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T09:30:20.502208Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T09:30:21.182328Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T09:30:20.892628Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T09:30:21.546017Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T09:30:23.244782Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T09:30:23.395210Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248
  accessed_at: '2026-10-28T09:30:23.852060Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi91248.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: d0959ac455ece32a6e94c13fd8e592403109201b6c61144dccfe0d58f1916380
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T09:30:23.822472Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T09:30:21.394985Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi28757
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28757
  accessed_at: '2026-10-28T09:30:20.802191Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi28757.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: da80fa1ea13ae90516654464b6144104ea9be1b1e341046d241a44f8dae748e9
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T09:30:23.224504Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T09:30:20.778858Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi17883.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  accessed_at: '2026-10-28T09:30:22.877311Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T09:30:22.236112Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T09:30:23.467622Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T09:30:22.177923Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T09:30:22.024101Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T09:30:23.333661Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T09:30:21.398233Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T09:30:22.793529Z'
  locator: REVIEW_WORK/batch062/source07-09/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:37:23.683716Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: a09f604bf09e2d7ebd95c3b796319c275ebe50d6ee651dc76d458309f972af5e
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:37:23.683785Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: c03b634ec93dc76824b88c92b8e78328f2d0d93e5d88f29c817b8f760dc94949
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:37:23.683887Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 1936c9f3e1457a424d6d416c2b0bd49e1ea96a9ecee8f8b3ec290ef9f2fe88f0
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:37:23.683929Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: b368ee9fd69adce9df587604c3ab3b959636f192cfc8e0233cf410abf862c105
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:37:23.683973Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 50f549e3857b82b52fc4a9a0829b701d81cb79852a5efb0976c501a211d1cb87
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:37:23.683993Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 9b7977c12a5638519db44bb6a06ec4d9caca861392fcc84e2f145856fe5dce67
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch062/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T09:37:23.684011Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch062/record07/schema-result.json
  accessed_at: '2026-10-28T09:30:18.911382Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 64c1019330b7e1a796e36b9eaddb1c9cf7be210c1eada9869dba097a83a15b5f
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch062/record07/strict-result.json
  accessed_at: '2026-10-28T09:30:19.816078Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 7d7ca620372f51aa7d6153367a4bb819604d2256611f597277c3002e600dff18
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch062/record07/terms-result.json
  accessed_at: '2026-10-28T09:30:20.818482Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 9ccfc9b9e2af14f869d8b5d3ec947badd410df3eae4aba8bdfc667b74eaf5ddc
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch062/record07/references-result.json
  accessed_at: '2026-10-28T09:30:21.541696Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 7fbd3ae24c2f908adc86ff0306b5cff4e89d4b678091534d52fdcc6dd2e2d938
assessments:
- assessment_id: identity
  area: identity
  topic: Exact JCM781 identity and dependency scope
  outcome: supported
  summary: The maintained JCM J781 owner is the sole declared generation contributor.
    The historical October5 report also nominated TOGO M811 as a candidate by identity/name;
    it is not a current generation owner and its formulation is not transferred. JCM439
    is consulted only for the explicitly linked trace subsection.
  target_ids:
  - CultureMech:003124
  evidence_ids:
  - target
  - owner
  - jcm781HTML
  - historical-reading
- assessment_id: classification
  area: scope
  topic: Classification and organism scope
  outcome: supported
  summary: The source contains yeast extract and is a liquid complex formulation.
    No specific strain or growth evidence is asserted by the reviewed primary texts;
    no organism association is created from the name.
  target_ids:
  - CultureMech:003124
  evidence_ids:
  - apiJ781
  - jcm781HTML
  - target
- assessment_id: native
  area: schema
  topic: Native structural diagnostics
  outcome: supported
  summary: All four canonical checks returned zero; strict reports no errors and references
    checked zero entries. These diagnostics do not establish chemical form, recipe
    stage or source completeness.
  target_ids:
  - CultureMech:003124
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 44 current concentration fields are covered by 29 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:003124
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b062-quantity-inventory-v1","target":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","quantity_field_count":44,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.28222 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.28222,\n                        \"mmol_l\":
    2.07384,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.28222","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.28222 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.28222,\n                        \"mmol_l\":
    1.62032,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> K<sub>2</sub>HPO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.940734 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.940734,\n                        \"mmol_l\":
    17.5871,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.940734 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.940734,\n                        \"mmol_l\":
    16.0974,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.0940734 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0940734,\n                        \"mmol_l\":
    1.26188,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> KCl                                                     </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"CaCl2
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.0940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.0940734 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0940734,\n                        \"mmol_l\":
    0.63989,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"MgCl2
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.470367 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.470367,\n                        \"mmol_l\":
    2.31362,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Yeast
    extract","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.940734 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.940734,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"L-Cysteine
    HCl x H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.470367","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.470367 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.470367,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> L-Cysteine&#183;HCl&#183;H<sub>2</sub>O                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.000940734","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.000940734","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"Both
    local values equal the explicit provider g_l=0.000940734 rate. MediaDive declares
    volume 1063 ml, whereas JCM prints an initial 1 L water input and later additions
    per liter. This is support for the provider''s stated normalization only, not
    independently measured final volume. No concentration evidence is currently attached.","source_stage":"Provider
    main-solution normalization versus primary batch input","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.000940734,\n                        \"mmol_l\":
    0.0041046,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"NaHCO3
    stock addition","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"Local
    25 G_PER_L misrepresents the source''s 25 ml stock addition. JCM explicitly introduces
    these additions as per liter after cooling. Preserve the *, 8% stock attribute
    separately: fructose 1 M is explicit; 8% bicarbonate and 5% sulfide lack a stated
    percentage basis. Do not infer a mass dose, stock density or final-medium concentration.","source_stage":"Post-cooling
    anaerobic stock additions","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"attribute\": \"*, 8%\",\n                        \"amount\":
    25,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution*                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;25.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"step\": \"Mix components thoroughly, distribute
    the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes)
    under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave.
    After cooling, add per liter the following solutions from anaerobic stocks (autoclaved
    or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"Fructose
    stock addition","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"Local
    20 G_PER_L misrepresents the source''s 20 ml stock addition. JCM explicitly introduces
    these additions as per liter after cooling. Preserve the 1 M stock attribute separately:
    fructose 1 M is explicit; 8% bicarbonate and 5% sulfide lack a stated percentage
    basis. Do not infer a mass dose, stock density or final-medium concentration.","source_stage":"Post-cooling
    anaerobic stock additions","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Fructose\",\n                        \"compound_id\":
    98,\n                        \"attribute\": \"1 M\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> 1 M Fructose solution                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"step\": \"Mix components thoroughly, distribute
    the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes)
    under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave.
    After cooling, add per liter the following solutions from anaerobic stocks (autoclaved
    or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Na2S
    x 9 H2O stock addition","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"8","unit":"G_PER_L"}}],"decision":"correct","rationale":"Local
    8 G_PER_L misrepresents the source''s 8 ml stock addition. JCM explicitly introduces
    these additions as per liter after cooling. Preserve the 5% stock attribute separately:
    fructose 1 M is explicit; 8% bicarbonate and 5% sulfide lack a stated percentage
    basis. Do not infer a mass dose, stock density or final-medium concentration.","source_stage":"Post-cooling
    anaerobic stock additions","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[14]","quote":"{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"attribute\": \"5%\",\n                        \"amount\":
    8,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution                      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"step\": \"Mix components thoroughly, distribute
    the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes)
    under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave.
    After cooling, add per liter the following solutions from anaerobic stocks (autoclaved
    or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"HCl
    in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"12.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"12.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local 12.5 G_PER_L is a volume-to-mass error as well as a stage error: the trace-stock
    recipe specifies 12.5 ml HCl (25%). Percentage basis and density are unspecified;
    no mass conversion is justified.","source_stage":"JCM439 trace subsection only,
    received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    12.5,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> HCl (25%)                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;12.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"FeSO4
    x 7 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=2.1, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 2.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.1,\n                        \"mmol_l\":
    7.55355,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"H3BO3
    in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=0.03, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 30,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.485123,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"MnCl2
    x 4 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=0.1, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"CoCl2
    x 6 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=0.19, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"NiCl2
    x 6 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=0.024, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"CuCl2
    x 2 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=0.002, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"ZnSO4
    x 7 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.144","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.144","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=0.144, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 144,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.144,\n                        \"mmol_l\":
    0.500763,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;144.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Na2MoO4
    x 2 H2O in trace stock","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    local value matches provider stock g_l=0.036, but is flattened into the main ingredient
    list. The source instead places this component in the trace stock added at 10
    ml per J781 recipe batch. Preserve the original stock mass and provider-declared
    stock rate separately; 987 ml water plus acid input does not establish an independently
    measured final stock volume. No working concentration is calculated.","source_stage":"JCM439
    trace subsection only, received by J781","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Main
    water input","local_fields":[],"decision":"evidence_only","rationale":"Primary
    1 L water / provider 1000 ml is an input amount omitted locally. It is not a final-volume
    measurement.","source_stage":"Main batch water","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"Trace stock receiving dose","local_fields":[],"decision":"evidence_only","rationale":"J781
    specifies 10 ml trace stock. The parent JCM439 receiving dose is excluded; no
    1 ml transfer is made.","source_stage":"J781 trace-stock addition","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution (see
    Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=439\">439</a>)          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution\",\n                        \"solution_id\":
    4186,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q25","label":"Trace-stock water input","local_fields":[],"decision":"evidence_only","rationale":"987
    ml water is a source input, not an explicit final-makeup instruction. Keep the
    HCl aliquot separate.","source_stage":"Trace-stock preparation","sources":[{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;987.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 987,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"Existing distribution and anaerobic sequence","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml","field_path":"preparation_steps[0].description","stored":"Mix
    components thoroughly, distribute the medium into culture vessels (e.g., 5 ml
    of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal
    with butyl rubber stoppers and autoclave. After cooling, add per liter the following
    solutions from anaerobic stocks (autoclaved or *filter-sterilized):"},{"path":"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml","field_path":"preparation_steps[0].description","stored":"Mix
    components thoroughly, distribute the medium into culture vessels (e.g., 5 ml
    of the medium in the Hungate tubes) under a N2-CO2 (4:1, v/v) gas mixture, seal
    with butyl rubber stoppers and autoclave. After cooling, add per liter the following
    solutions from anaerobic stocks (autoclaved or *filter-sterilized):"}],"decision":"evidence_only","rationale":"Both
    local descriptions retain the 5 ml example, N2-CO2 4:1 v/v atmosphere, seal/autoclave
    sequence and post-cooling per-liter stock introduction. Credit this text; the
    missing stock descriptors prevent it from fully identifying the additions. No
    incubation or growth claim follows.","source_stage":"Current preparation text","sources":[{"evidence_id":"apiJ781","reference":"https://mediadive.dsmz.de/rest/medium/J781","raw_path":"REVIEW_WORK/batch062/source07-09/apiJ781.raw","raw_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","text_sha256":"7aabd1ca2c331ea790335f2f844684eb67d39c54625aca6b753fd2fb87dd69ab","accessed_at":"2026-10-28T09:30:19.508803Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"step\": \"Mix components thoroughly, distribute
    the medium into culture vessels (e.g., 5 ml of the medium in the Hungate tubes)
    under a N2-CO2 (4:1, v/v) gas mixture, seal with butyl rubber stoppers and autoclave.
    After cooling, add per liter the following solutions from anaerobic stocks (autoclaved
    or *filter-sterilized): \"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"JCM
    general sterilization default","local_fields":[],"decision":"evidence_only","rationale":"The
    catalog states a general default of 121°C for 15 min unless otherwise stated.
    Record it only with that conditional scope; it is not an independently validated
    stock-specific condition.","source_stage":"Conditional primary catalog default","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"Catalog
    general default before recipe","quote":"Unless otherwise stated, sterilize media
    by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]},{"quantity_id":"q28","label":"Unspecified
    stock percentage bases","local_fields":[],"decision":"unsupported","rationale":"The
    printed 8%, 5% and 25% have no w/v, w/w or v/v qualifier in the exact sources.
    Their source labels are supported; selecting a percentage enum or deriving mass
    concentrations remains unsupported.","source_stage":"Stock strengths; unresolved
    basis","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution*                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;25.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> 5% Na<sub>2</sub>S&#183;9H<sub>2</sub>O
    solution                      </TD><TD WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;8.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm439HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=439","raw_path":"REVIEW_WORK/batch062/source07-09/jcm439HTML.raw","raw_sha256":"2a71115d17d54beb8454d4106e93dd60364885a914eee9d1c434ee15f510ceda","text_sha256":"1cb6dcf404652697fb71246848f47bed1b9abd92350ab91eab0db68140e2623d","accessed_at":"2026-10-28T09:33:09.184119Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> HCl (25%)                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;12.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Fructose
    stock molarity","local_fields":[],"decision":"evidence_only","rationale":"The
    source explicitly states 1 M fructose. Preserve this stock molarity and the separate
    receiving aliquot; do not substitute 20 g/L.","source_stage":"Fructose stock strength","sources":[{"evidence_id":"jcm781HTML","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=781","raw_path":"REVIEW_WORK/batch062/source07-09/jcm781HTML.raw","raw_sha256":"8149d6df2136fecbe5dd960768f990663a5be474d75f962e4a1dbe608e6f55d2","text_sha256":"637b1f0c1ed79a5d425bb56dafe0bc6f2a16e31e67cd54aa56ea934d15829174","accessed_at":"2026-10-28T09:31:21.664270Z","locator":"HTML
    table row 13 (zero-based)","quote":"<TR><TD WIDTH=75%> 1 M Fructose solution                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;20.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CLOSTRIDIUM_ACETATE_1_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted CHEBI objects resolve with current canonical labels, and the
    exact packaged MIM row joins are inventoried. The nickel hexahydrate source contradicts
    anhydrous CHEBI:34887 despite label agreement. Other hydrates are form-consistent
    with the inspected primary names; generic fructose remains generic, yeast extract
    has no fabricated pure-chemical ID, and a chemical ID does not define a stock
    percentage basis.
  target_ids:
  - CultureMech:003124
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: The October5 reports were explicit unverified inventories; the October7
    J781 report left all 22 concentration fields unchanged because stock topology
    required source-specific work. Its source rows can be compared to the fresh payload
    without claiming historical execution. Current primary-only MediaDive parsing
    and conservative formulation merging are credited, with the molar-only stock and
    conditional volume normalization boundaries retained.
  target_ids:
  - CultureMech:003124
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-003124-stock-volume-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Three stock aliquots are represented as direct mass concentrations
  description: 'Reconcile ingredients[10:13] against the exact JCM781 post-cooling
    stock additions: the three printed ml amounts are currently labelled G_PER_L.
    Restore separate stock descriptors, source-explicit fructose molarity and scoped
    receiving doses; preserve unresolved percentage bases. The current importer recognizes
    percent-labelled ml stocks but not the molar-only fructose attribute, so audit
    that remaining parser boundary rather than claiming all current imports still
    flatten every stock.'
  target_ids:
  - CultureMech:003124
  field_paths:
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - solutions
  evidence_ids:
  - apiJ781
  - jcm781HTML
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-003124-trace-stock-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Trace-stock components and acid aliquot are flattened into the medium
  description: Move the nine trace-stock components out of direct main-medium concentrations
    and retain the source-specific trace composition, 10 ml receiving dose and separate
    water/acid input basis. HCl 12.5 ml at unspecified-basis 25% cannot be 12.5 g/L.
    Do not import the JCM439 parent basal formulation, its receiving dose, or an inferred
    final volume.
  target_ids:
  - CultureMech:003124
  field_paths:
  - ingredients[13:22]
  - solutions
  evidence_ids:
  - apiJ781
  - jcm781HTML
  - jcm439HTML
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-003124-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is keyed to anhydrous nickel dichloride
  description: The supplied NiCl2·6H2O at ingredients[18] has CHEBI:34887 (Cl2Ni)
    in both primary and secondary slots. Fresh OLS CHEBI:53542 explicitly describes
    nickel chloride hexahydrate and provides the six-water formula. Curate both affected
    slots after source-form reconciliation; a matching current label or MIM row does
    not resolve the hydrate mismatch.
  target_ids:
  - CultureMech:003124
  field_paths:
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - apiJ781
  - jcm439HTML
  - chebi34887
  - chebi53542
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-003124-source-evidence-and-controls
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source basis and omitted water controls need explicit evidence
  description: Attach exact source-stage evidence and restore input-water context
    when curating the stock topology. Retain the existing anaerobic preparation text
    and qualify the JCM general sterilization default rather than inventing stock
    conditions. Explain the provider 1063 ml normalization separately from the primary
    initial water and per-liter additions; no new pH or strain-growth assertion is
    supported.
  target_ids:
  - CultureMech:003124
  field_paths:
  - ingredients
  - preparation_steps
  - references
  evidence_ids:
  - apiJ781
  - jcm781HTML
  - quantities
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: 'Reconcile ingredients[10:13] against the exact JCM781 post-cooling
    stock additions: the three printed ml amounts are currently labelled G_PER_L.
    Restore separate stock descriptors, source-explicit fructose molarity and scoped
    receiving doses; preserve unresolved percentage bases. The current importer recognizes
    percent-labelled ml stocks but not the molar-only fructose attribute, so audit
    that remaining parser boundary rather than claiming all current imports still
    flatten every stock.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003124
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
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
  description: Move the nine trace-stock components out of direct main-medium concentrations
    and retain the source-specific trace composition, 10 ml receiving dose and separate
    water/acid input basis. HCl 12.5 ml at unspecified-basis 25% cannot be 12.5 g/L.
    Do not import the JCM439 parent basal formulation, its receiving dose, or an inferred
    final volume.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003124
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
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
  description: The supplied NiCl2·6H2O at ingredients[18] has CHEBI:34887 (Cl2Ni)
    in both primary and secondary slots. Fresh OLS CHEBI:53542 explicitly describes
    nickel chloride hexahydrate and provides the six-water formula. Curate both affected
    slots after source-form reconciliation; a matching current label or MIM row does
    not resolve the hydrate mismatch.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003124
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
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
  description: Attach exact source-stage evidence and restore input-water context
    when curating the stock topology. Retain the existing anaerobic preparation text
    and qualify the JCM general sterilization default rather than inventing stock
    conditions. Explain the provider 1063 ml normalization separately from the primary
    initial water and per-liter additions; no new pH or strain-growth assertion is
    supported.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003124
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_acetate_1_medium.yaml
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
- 'The two guessed /medium/medium/JCM*.pdf URLs were not source evidence: each returned
  404 and remains preserved. The exact existing-record JCM781 catalog URL returned
  usable HTML.'
- Only the trace subsection of JCM439 is evidence for this record; parent nutrients,
  other stocks, receiving doses and organism context are excluded.
- No numerical final-medium concentrations are derived from 1063 ml, the 1 L water
  input, or the printed percent stock labels. Unknown author/publication year metadata
  remains unknown.
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
