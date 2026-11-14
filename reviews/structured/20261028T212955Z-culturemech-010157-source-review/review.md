# Scientific review: Desulfosporosinus Acidiphilus Medium

- Review: 20261028T212955Z-culturemech-010157-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:57:41.171927Z
- Finished UTC: 2026-10-28T21:29:55.422407Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The two main provider rates and repaired dependency batch claims are supported. The selected documents need water/stock-stage separation, six liquid-dose corrections, sourced preparation and the scoped nickel supplied-form fix; selected primary access remains incomplete.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch078 index 10
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010157 | data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml | generated | desulfosporosinus_acidiphilus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:010157 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:010157 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:010157 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:010157 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Selected identity and available source versions

identity: concern. Targets: CultureMech:010157.

TOGO M751 and J728 identify JCM728 and agree on the named main/HBS/trace/Ni-Se-W scopes. Current JCM728 returns HTTP200 Nothing found, so primary selected-recipe recovery is incomplete. JCM151 and244 corroborate only their named stock tables; complete parent recipes and their receiving doses are excluded.

### Complex liquid classification

consistency: supported. Targets: CultureMech:010157.

The source includes defined salts and a small yeast-extract contribution, supporting the actual COMPLEX/SEMI_DEFINED liquid classification. No growth claim follows from the organism or medium name.

### Original required diagnostics

schema: supported. Targets: CultureMech:010157.

The original four diagnostics all exited 0. The additive inspection preserves every original input and adds only two current repair writers; no canonical check was repeated.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:010157.

36 current concentration fields are covered by 39 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b078-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","quantity_field_count":36,"decisions":[{"quantity_id":"q1","label":"Separate main and HBS water inputs","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"940.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"940.0","unit":"G_PER_L"}},{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[0].notes","stored":"Role: Solvating media; Properties: Defined component, Simple component, Inorganic compound [Merged 2 duplicates: 939.0, 1.0]"},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[0].notes","stored":"Role: Solvating media; Properties: Defined component, Simple component, Inorganic compound [Merged 2 duplicates: 939.0, 1.0]"}],"decision":"correct","rationale":"The local 940 g/L is a duplicate sum of 939 ml main water and 1 L HBS water, combining distinct stages and source units. Preserve each native water input separately; neither input alone establishes measured final volume.","source_stage":"Main versus HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 939,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 939,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider explicitly declares this unchanged g/L rate. Credit its normalization separately from the native batch amount; the 1000 ml provider volume is not independent measurement of final volume. No attached current claim exists in the selected documents.","source_stage":"Main solution","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"K2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.87","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.87","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The exact main-solution provider explicitly declares this unchanged g/L rate. Credit its normalization separately from the native batch amount; the 1000 ml provider volume is not independent measurement of final volume. No attached current claim exists in the selected documents.","source_stage":"Main solution","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"K2SO4\",\n          \"volume\": 0.87,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001173\",\n          \"gmo_id\": \"GMO_001173\",\n          \"label\": \"Potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"K2SO4\",\n                        \"compound_id\": 382,\n                        \"amount\": 0.87,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.87,\n                        \"mmol_l\": 4.99254,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"H2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The source does not specify a fixed amount or dissolved concentration. Retain the truthful VARIABLE placeholder; the separately missing pH adjustment or nitrogen-atmosphere instruction does not supply a numeric ingredient concentration.","source_stage":"Main unquantified reagent or atmosphere","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"H2SO4\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001482\",\n          \"gmo_id\": \"GMO_001482\",\n          \"label\": \"Sulfuric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix thoroughly, adjust to pH 5.5 with H2SO4 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add the following solutions (filter--sterilized) to the medium:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The source does not specify a fixed amount or dissolved concentration. Retain the truthful VARIABLE placeholder; the separately missing pH adjustment or nitrogen-atmosphere instruction does not supply a numeric ingredient concentration.","source_stage":"Main unquantified reagent or atmosphere","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix thoroughly, adjust to pH 5.5 with H2SO4 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add the following solutions (filter--sterilized) to the medium:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"MgSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider explicitly supports this rate only within HBS stock. Restore that named stock boundary and its distinct water input; the current root placement incorrectly represents stock strength as a main-medium ingredient concentration. No final-medium dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 25,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\": 101.43,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider explicitly supports this rate only within HBS stock. Restore that named stock boundary and its distinct water input; the current root placement incorrectly represents stock strength as a main-medium ingredient concentration. No final-medium dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\": 10,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 14.3533,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider explicitly supports this rate only within HBS stock. Restore that named stock boundary and its distinct water input; the current root placement incorrectly represents stock strength as a main-medium ingredient concentration. No final-medium dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"KCl\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 33.5345,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"(NH4)2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"22.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"22.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider explicitly supports this rate only within HBS stock. Restore that named stock boundary and its distinct water input; the current root placement incorrectly represents stock strength as a main-medium ingredient concentration. No final-medium dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"(NH4)2SO4\",\n          \"volume\": 22.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\": \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 22.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 22.5,\n                        \"mmol_l\": 170.274,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3.3","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider explicitly supports this rate only within HBS stock. Restore that named stock boundary and its distinct water input; the current root placement incorrectly represents stock strength as a main-medium ingredient concentration. No final-medium dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Na2SO4\",\n          \"volume\": 3.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.3,\n                        \"mmol_l\": 23.2329,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Ca(NO3)2・4H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.7","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.7","unit":"G_PER_L"}}],"decision":"correct","rationale":"The provider explicitly supports this rate only within HBS stock. Restore that named stock boundary and its distinct water input; the current root placement incorrectly represents stock strength as a main-medium ingredient concentration. No final-medium dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Ca(NO3)2・4H2O\",\n          \"volume\": 0.7,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001116\",\n          \"gmo_id\": \"GMO_001116\",\n          \"label\": \"Calcium nitrate tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\": 213,\n                        \"amount\": 0.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.7,\n                        \"mmol_l\": 2.96423,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"HBS solution (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source gives this addition in ml, while the local descriptor records the same numeral in G_PER_L. Restore the batch volume and preserve exact stock identity and composition separately. A receiving-medium dose does not equal the parent record dose or prove a final-volume denominator.","source_stage":"Main receives named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"HBS solution (see below)\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M751\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"solution\": \"HBS solution\",\n                        \"solution_id\": 4653,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Trace minerals (see Medium [M142])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source gives this addition in ml, while the local descriptor records the same numeral in G_PER_L. Restore the batch volume and preserve exact stock identity and composition separately. A receiving-medium dose does not equal the parent record dose or prove a final-volume denominator.","source_stage":"Main receives named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Trace minerals\",\n                        \"solution_id\": 3804,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"Ni-Se-W solution (see Medium [M236])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source gives this addition in ml, while the local descriptor records the same numeral in G_PER_L. Restore the batch volume and preserve exact stock identity and composition separately. A receiving-medium dose does not equal the parent record dose or prove a final-volume denominator.","source_stage":"Main receives named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"Ni-Se-W solution (see Medium [M236])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M236\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Ni-Se-W solution\",\n                        \"solution_id\": 3927,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"1 M ZnSO4 solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"7","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"7","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source gives this addition in ml, while the local descriptor records the same numeral in G_PER_L. Restore the batch volume and preserve exact stock identity and composition separately. A receiving-medium dose does not equal the parent record dose or prove a final-volume denominator. Its explicit molar strength remains distinct from addition volume; do not infer a hydrate or mass conversion. Retain the later filter-sterilized addition stage.","source_stage":"Main receives named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"1 M ZnSO4 solution\",\n          \"volume\": 7,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001277\",\n          \"gmo_id\": \"GMO_001277\",\n          \"label\": \"Zinc sulfate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"ZnSO4\",\n                        \"compound_id\": 441,\n                        \"attribute\": \"1 M\",\n                        \"amount\": 7,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"10 mM FeSO4 solution (pH 2.0)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source gives this addition in ml, while the local descriptor records the same numeral in G_PER_L. Restore the batch volume and preserve exact stock identity and composition separately. A receiving-medium dose does not equal the parent record dose or prove a final-volume denominator. Its explicit molar strength remains distinct from addition volume; do not infer a hydrate or mass conversion. Retain the later filter-sterilized addition stage.","source_stage":"Main receives named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"10 mM FeSO4 solution (pH 2.0)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\": \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"FeSO4\",\n                        \"compound_id\": 595,\n                        \"attribute\": \"pH 2.0, 10 mM\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"1 M Glycerol solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"4","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source gives this addition in ml, while the local descriptor records the same numeral in G_PER_L. Restore the batch volume and preserve exact stock identity and composition separately. A receiving-medium dose does not equal the parent record dose or prove a final-volume denominator. Its explicit molar strength remains distinct from addition volume; do not infer a hydrate or mass conversion. Retain the later filter-sterilized addition stage.","source_stage":"Main receives named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"1 M Glycerol solution\",\n          \"volume\": 4,\n          \"unit\": \"ml\",\n          \"conc_value\": 1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001466\",\n          \"gmo_id\": \"GMO_001466\",\n          \"label\": \"Glycerol solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Glycerol\",\n                        \"compound_id\": 72,\n                        \"attribute\": \"1 M\",\n                        \"amount\": 4,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Collapsed 2 identical duplicates: 1.0, 1.0]\n\nSource water batch input: 1 L = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe the superseded flattened record."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 32 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"MgSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 3.5, 3.0]\n\nSource batch input: 3 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"NaCl","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 13.85, 1.0]\n\nSource batch input: 1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"CaCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 31 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component [Merged 2 duplicates: 15.0, 0.01]\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 30 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"FeSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"ZnSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 27 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"CuSO4・5H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\": \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 28 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;5H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"CoSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.1 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\": \"CoSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001050\",\n          \"gmo_id\": \"GMO_001050\",\n          \"label\": \"Cobalt(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;7H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.645178,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Mineral source; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nitrilotriacetic acid                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"MnSO4・xH2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[11].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation. The printed hydrate variable remains unspecified; no fixed water count is assigned.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[11]","quote":"{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnSO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;&lt;I&gt;x&lt;/I&gt;H&lt;sub&gt;2&lt;/sub&gt;O                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"AlK(SO4)2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[12].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.01 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[12]","quote":"{\n          \"component_name\": \"AlK(SO4)2\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001088\",\n          \"gmo_id\": \"GMO_001088\",\n          \"label\": \"Aluminum potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML table row 29 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; AlK(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.01&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2\",\n                        \"compound_id\": 1015,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0387289,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[0].notes","stored":"Role: Solvating media; Properties: Inorganic compound, Defined component, Simple component [Merged 3 duplicates: 500.0, 1.0, 1.0]\n\nSource water batch input: 1 L = 1 L. This is not a measured final volume.\n\nThe earlier duplicate-summing note is superseded: it combined separate preparation scopes and source units. This node carries only the batch input at the cited source row; other occurrences are separate scoped ingredients."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 25 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 25,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;25.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 25,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.192903,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;WO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0303168,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Na2SeO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 0.3 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"Na2SeO3\",\n          \"volume\": 0.3,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001093\",\n          \"gmo_id\": \"GMO_001093\",\n          \"label\": \"Sodium selenite\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;3&lt;/sub&gt;                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.3&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SeO3\",\n                        \"compound_id\": 699,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"(NH4)2Ni(SO4)2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"(NH4)2Ni(SO4)2・6H2O\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001102\",\n          \"gmo_id\": \"GMO_001102\",\n          \"label\": \"Ammonium nickel(II) sulfate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; (NH&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;Ni(SO&lt;sub&gt;4&lt;/sub&gt;)&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"(NH4)2Ni(SO4)2 x 6 H2O\",\n                        \"compound_id\": 739,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\": 5.06346,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Na2SeO4","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit the retained batch input and its existing attached literal source claim, authenticated against unchanged current provider raw bytes. Historical duplicate notes are superseded by the explicit scoped repair. Water is a batch input; retained mass notes do not assert a measured final-volume concentration. The current J728 provider also declares a stock rate, which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Na2SeO4\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001602\",\n          \"gmo_id\": \"GMO_001602\",\n          \"label\": \"Sodium selenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;SeO&lt;sub&gt;4&lt;/sub&gt;                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2SeO4\",\n                        \"compound_id\": 375,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0529241,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Retained trace-stock pH preparation","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].preparation_notes","stored":"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0."}],"decision":"verified","rationale":"The retained pH 6.5 then 7.0 method belongs only to the trace-mineral stock and is explicitly supported by an additional excerpt in the existing root evidence. Preserve it; no receiving-medium pH or fixed titrant dose is inferred.","source_stage":"Trace minerals preparation","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].steps[0]","quote":"{\n                        \"step\": \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"jcm151.txt lines 203-203","quote":"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution.      Then proceed to add minerals.   Adjust final pH to 7.0.","quote_basis":"derivative text"}]},{"quantity_id":"q38","label":"Unquantified KOH titrant","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].solutions[0].notes","stored":"Role: Mineral source; Properties: Defined component, Solution\n\npH-adjustment reagent; no fixed dose is specified. Normality is not converted to molarity."}],"decision":"verified","rationale":"The retained stock-only titrant note and absent fixed quantity agree with the current source and existing root additional excerpt. The source supplies no numeric strength; the placeholder name is a separate minor metadata defect.","source_stage":"Trace minerals titration","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[13]","quote":"{\n          \"component_name\": \"KOH solution\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Missing main pH and staged preparation","local_fields":[],"decision":"correct","rationale":"Restore source-supported main pH 5.5, nitrogen autoclave atmosphere, cooling, then aseptic anaerobic additions of the three filter-sterilized solutions. Preserve FeSO4 stock pH 2.0 separately. No autoclave temperature/time is supplied by the available selected source, and no JCM151/244 default is transferred.","source_stage":"Main versus later additions","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix thoroughly, adjust to pH 5.5 with H2SO4 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add the following solutions (filter--sterilized) to the medium:\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\": 7,\n                        \"step\": \"Mix thoroughly, adjust to pH 5.5 with H2SO4 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically add the following solutions (filter-sterilized) to the medium: \"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"10 mM FeSO4 solution (pH 2.0)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\": \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml":["solutions[1].composition","solutions[1].solutions","solutions[1].preparation_notes","solutions[1].preferred_term","solutions[1].name"],"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml":["solutions[2].composition","solutions[2].preferred_term","solutions[2].name"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:010157.

All asserted slots and current exact MIM/OLS objects were checked. The selected magnesium heptahydrate primary is correct and no secondary slot is asserted there. Scoped nickel hexahydrate uses anhydrous nickel identity. Other explicitly supplied hydrates, NTA and selenium salts were assessed separately. The trace manganese hydrate variable remains unresolved; current catalog spelling/status is not proof of supplied form.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:010157.

The complete historical report and selected-parent reading is supplied by the pinned root contribution, including current M142/M236 history and root evidence. The author independently checked the current sources, every in-scope quantity and supplied form, existing scoped excerpts, and current importer/repair bodies. Current equal raw content authenticates the exact excerpt, not the original retrieval event. Prior repairs correctly retain separate batch notes and water inputs; those current fixes are credited, while old parent-wide recommendations are not automatically adopted.

## Findings

### f1: Restore stock boundaries and separate water stages

major / open / confirmed; issue key: culturemech-010157-stock-stage-water.

The selected target and owner combine 939 ml main water with 1 L HBS water as 940 g/L and flatten six HBS stock components into main ingredients. Preserve the provider-supported HBS rates under their stock and keep both water inputs separate. The repaired M142 and M236 stock definitions already retain correct batch inputs with evidence and must not be re-flattened.

### f2: Represent six liquid additions as volumes

major / open / confirmed; issue key: culturemech-010157-stock-dose-units.

All six named solution descriptors encode ml addition numerals as G_PER_L and have empty compositions. Restore exact source-specific stock references or scoped compositions and native receiving-batch volumes; retain the separate 1 M zinc sulfate, 10 mM iron sulfate and 1 M glycerol strengths without hydrate guesses or inferred mass conversions.

### f3: Restore main preparation and separate stock controls

major / open / confirmed; issue key: culturemech-010157-preparation-scope.

The available exact TOGO and J728 sources specify main pH 5.5 and staged sterilization/addition, but the selected documents retain none of that procedure. Preserve the already supported trace-stock pH 6.5 then 7.0 and the separate iron-stock pH 2.0; neither is the final-medium pH. Retain VARIABLE H2SO4 and nitrogen placeholders as unquantified, independently of restoring the method.

### f4: Resolve the scoped nickel hexahydrate identity

major / open / confirmed; issue key: culturemech-010157-nickel-hydrate.

The Ni-Se-W dependency source and preferred term specify nickel chloride hexahydrate, but its primary CHEBI:34887 identifies anhydrous nickel dichloride. Current CHEBI:53542 explicitly includes six waters. Reconcile this exact dependency slot while preserving the already supported 25 mg batch note.

### f5: Complete source claims, stock names and unresolved hydrate scope

minor / open / confirmed; issue key: culturemech-010157-metadata-claims-and-hydrate.

Attach exact selected-medium claims while preserving the authenticated dependency claims. Replace the six selected Unknown solution names, supply the missing scoped M142 trace name, and replace the nested KOH and M236 Ni-Se-W placeholder names using their existing source-specific preferred terms. Keep the trace manganese xH2O hydrate unspecified; its generic manganese sulfate identifier does not establish a fixed hydrate and no molecular conversion is warranted.

## Recommended Actions And Acceptance Checks

### a1

The selected target and owner combine 939 ml main water with 1 L HBS water as 940 g/L and flatten six HBS stock components into main ingredients. Preserve the provider-supported HBS rates under their stock and keep both water inputs separate. The repaired M142 and M236 stock definitions already retain correct batch inputs with evidence and must not be re-flattened.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

All six named solution descriptors encode ml addition numerals as G_PER_L and have empty compositions. Restore exact source-specific stock references or scoped compositions and native receiving-batch volumes; retain the separate 1 M zinc sulfate, 10 mM iron sulfate and 1 M glycerol strengths without hydrate guesses or inferred mass conversions.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The available exact TOGO and J728 sources specify main pH 5.5 and staged sterilization/addition, but the selected documents retain none of that procedure. Preserve the already supported trace-stock pH 6.5 then 7.0 and the separate iron-stock pH 2.0; neither is the final-medium pH. Retain VARIABLE H2SO4 and nitrogen placeholders as unquantified, independently of restoring the method.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The Ni-Se-W dependency source and preferred term specify nickel chloride hexahydrate, but its primary CHEBI:34887 identifies anhydrous nickel dichloride. Current CHEBI:53542 explicitly includes six waters. Reconcile this exact dependency slot while preserving the already supported 25 mg batch note.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Attach exact selected-medium claims while preserving the authenticated dependency claims. Replace the six selected Unknown solution names, supply the missing scoped M142 trace name, and replace the nested KOH and M236 Ni-Se-W placeholder names using their existing source-specific preferred terms. Keep the trace manganese xH2O hydrate unspecified; its generic manganese sulfate identifier does not establish a fixed hydrate and no molecular conversion is warranted.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| togo751 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751; REVIEW_WORK/batch078/source07-08-10/togo751.json; exact original raw/text/hash/time metadata | context_only | Exact provider source M751; selected M751 full scope, M142 trace and M236 Ni-Se-W only. |
| apiJ728 | https://mediadive.dsmz.de/rest/medium/J728; REVIEW_WORK/batch078/source07-08-10/apiJ728.json; exact original raw/text/hash/time metadata | context_only | Current JCM728 provider representation is compared separately to primary/source quantities. |
| jcm728 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=728; REVIEW_WORK/batch078/source07-08-10/jcm728.json; exact original raw/text/hash/time metadata | context_only | Exact selected JCM728 request returned HTTP200 Nothing found; no selected primary recipe was recovered. |
| togo142 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142; REVIEW_WORK/batch078/source07-08-10/togo142.json; exact original raw/text/hash/time metadata | context_only | Exact current M142 provider source; only the Trace minerals subsection and preparation are in scientific scope. |
| jcm151 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151; REVIEW_WORK/batch078/source07-08-10/jcm151.json; exact original raw/text/hash/time metadata | context_only | Complete current JCM151 source read; only its Trace minerals table and stock preparation transfer to the M751 dependency scope. |
| togo236 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236; REVIEW_WORK/batch078/source07-08-10/togo236.json; exact original raw/text/hash/time metadata | context_only | Exact current M236 provider source; only the Ni-Se-W subsection is in scientific scope. |
| jcm244 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244; REVIEW_WORK/batch078/source07-08-10/jcm244.json; exact original raw/text/hash/time metadata | context_only | Complete current JCM244 source read; only its Ni-Se-W table transfers to the M751 dependency scope. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch078/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-19 | reports/ingredient_concentration_curation/20261008-j261-variant/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261008-j261-variant/records/M142.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261008-j261-variant/records/M253.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-23 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M142.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_curation/20261008-reducing-stages/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-25 | reports/ingredient_concentration_curation/20261008-reducing-stages/records/M236.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__6ffabef8.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__a85c0932.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/stetteria_medium__0a06dac3.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/stetteria_medium__87ed999a.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-32 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-33 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-34 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-35 | reports/yaml_record_review/20260921T134926Z-archaeoglobus_fulgidus_medium__01928dac.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-36 | reports/yaml_record_review/20260922T195126Z-desulfosporosinus_acidiphilus_medium__0c10268a.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-37 | reports/yaml_record_review/20260923T165029Z-jcm_medium_no_244.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-38 | reports/yaml_record_review/20260924T234748Z-pyrococcus_medium__a85c0932.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-39 | reports/yaml_record_review/20260925T073134Z-stetteria_medium__0a06dac3.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch078/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch078/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch078/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch078/record10/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| writer-togo | src/culturemech/import/togo_importer.py; Full lines 229-869; extraction, solution, preparation, unit and pH methods | context_only | Current _extract_primary_components keeps named stock sections distinct and _solution_from_item retains their reference, but molar conc_value/conc_unit are not structured. Bare ml normalization and root-only pH parsing require source-stage care; current code does not establish historical execution. |
| writer-stock-repair | scripts/repair_jcm_stock_preparations.py; Complete current body | context_only | Current guarded M142 repair preserves supported batch inputs and trace-only preparation claims; no live repair was run. |
| writer-reducing | scripts/repair_reducing_stages.py; Complete current body; sources, Review.stock/formulate/finish and process | context_only | Current M236 source graph separates Ni-Se-W stock components and named source excerpts; finish creates this repair output and records an event, not scientific validation of retained chemical identifiers. |
| writer-shared-repair | scripts/repair_methanogen_stock_boundaries.py; Complete current body; Review.claim/descriptor/finish and process | context_only | The shared claim method validates literal source excerpts and appends additional excerpts for an existing reference; descriptor distinguishes native batch volume from explicit per-litre prescription. Its guarded process checks frozen before/output bytes. These current methods are not replayed historical execution. |
| scoped-html-claims | REVIEW_WORK/batch078/record10/existing-html-claim-authentication.json; Complete artifact | context_only | Existing JCM244 component excerpts separately match normalized current HTML; raw digest equality is separately recorded. |
| writer-read-addendum | REVIEW_WORK/batch078/record10/author-current-writer-addendum.json; Complete artifact | context_only | Exact current TOGO full extraction methods and complete two added repair-writer bodies read; prior global reader is retained unchanged. |
| root-history-contribution | REVIEW_WORK/batch078/record10/root-provenance-contribution-20261028.json; Complete bounded root contribution and direct pins | context_only | Root independently read complete reports, exact selected parent rows and current M142/M236 histories/root evidence; source/quantity/form and current two added writer scopes were read by this author. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; REVIEW_WORK/batch078/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32036; REVIEW_WORK/batch078/source07-08-10/chebi32036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836; REVIEW_WORK/batch078/source07-08-10/chebi26836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; REVIEW_WORK/batch078/source07-08-10/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; REVIEW_WORK/batch078/source07-08-10/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; REVIEW_WORK/batch078/source07-08-10/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; REVIEW_WORK/batch078/source07-08-10/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946; REVIEW_WORK/batch078/source07-08-10/chebi62946.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch078/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86159 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159; REVIEW_WORK/batch078/source07-08-10/chebi86159.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch078/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch078/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch078/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch078/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; REVIEW_WORK/batch078/source07-08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; REVIEW_WORK/batch078/source07-08-10/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; REVIEW_WORK/batch078/source07-08-10/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; REVIEW_WORK/batch078/source07-08-10/chebi91244.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; REVIEW_WORK/batch078/source07-08-10/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360; REVIEW_WORK/batch078/source07-08-10/chebi86360.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86463 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86463; REVIEW_WORK/batch078/source07-08-10/chebi86463.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch078/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; REVIEW_WORK/batch078/source07-08-10/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi48843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843; REVIEW_WORK/batch078/source07-08-10/chebi48843.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149; REVIEW_WORK/batch078/source07-08-10/chebi86149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775; REVIEW_WORK/batch078/source07-08-10/chebi77775.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch078/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch078/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch078/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch078/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch078/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch078/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch078/record10/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch078/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch078/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch078/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch078/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- The exact current JCM728 route returns HTTP200 Nothing found; no original selected recipe was recovered. TOGO M751 and J728 are separately identified provider evidence, not substitutes silently labelled as that primary.
- M142 coverage is only trace composition, nested KOH and trace preparation; M236 coverage is only Ni-Se-W composition. Their full current provenance is read, but parent receiving doses, other ingredients and cultivation procedures are excluded.
- The JCM151/244 general autoclave defaults are not transferred to the unavailable selected JCM728 recipe. Fixed stock hydrates or density are not inferred from molar labels.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T212955Z-culturemech-010157-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Desulfosporosinus Acidiphilus Medium'
started_at: '2026-10-28T20:57:41.171927Z'
finished_at: '2026-10-28T21:29:55.422407Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: The two main provider rates and repaired dependency batch claims are supported.
  The selected documents need water/stock-stage separation, six liquid-dose corrections,
  sourced preparation and the scoped nickel supplied-form fix; selected primary access
  remains incomplete.
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
  - path: data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml
    sha256: 93d5a5918b049290e6d6111d32dab38b9a0eb4b5155bc9596a9c724b96894dc0
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    sha256: 290433e6204999b98296f516fb77589d6df2c07e922d780683ae0ed53353844d
    role: context
  - path: data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml
    sha256: 896b03b57a4d9f36bab8fb2e36f7daf634aea74dfeb264676540f08f1d7e712f
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    sha256: 8f97519904c7ec55054b3e06be0b7d0d14528521824a0e30206f5fecac7833aa
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
  - path: reports/ingredient_concentration_curation/20261008-reducing-stages/plan.json
    sha256: 7262df2869246a849e11ab6eca57475a6163a346abd31e5c50a0ed8865fc0edf
    role: context
  - path: reports/ingredient_concentration_curation/20261008-reducing-stages/records/M236.md
    sha256: 89c67d9d489a74e3ffcddb35fce9f3a26eab3099e4a19f8f595a9e5c41b5e5e6
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.md
    sha256: 78147c6528e0368dc355246ecfe8b1504e2d89b1bb63a77add906ec286cdd313
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.md
    sha256: fdc94cf985da6217a496a4960033148b91b059477a39a2daeabb6d2a13500f40
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__6ffabef8.md
    sha256: 83c8213491aaeb9764f15234d55e465b4ddadad00dc05bfaa93743419b3d9ea2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__a85c0932.md
    sha256: b7afb33e6091981790d7d02bd4e7a2ecfa11655363fc9ee42994a3b3b3e757ad
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/stetteria_medium__0a06dac3.md
    sha256: a582736badb07bb5ad08fe04551c58f61c8bcd1c441e9825aa861facc41e36a1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/stetteria_medium__87ed999a.md
    sha256: 1dac54ee407cad8e61c2f1638856eb079271b1a6767beb364aa6aeea6f4f0896
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.md
    sha256: 2819146dc7d90f64ef630274b9d757bd510220b222d429716fc29d878d82b1b9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.md
    sha256: d7cb69aa18b8ba621fb353ddd4fe26c89b6b97c552be374ffba6080d652e9b0c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.md
    sha256: 27ff9317c0c7429a7da291fe13aff12f337669101e3aba43ff95a6117fd6a411
    role: context
  - path: reports/yaml_record_review/20260921T134926Z-archaeoglobus_fulgidus_medium__01928dac.md
    sha256: c8179ba605d1060447c97f02315b5a012f9d7ae79f3074424db8d223b428f46f
    role: context
  - path: reports/yaml_record_review/20260922T195126Z-desulfosporosinus_acidiphilus_medium__0c10268a.md
    sha256: 197d7d5af8fc9564d24e6d1636d61cdeba5873624f68a65ddd36cfadfa7ee059
    role: context
  - path: reports/yaml_record_review/20260923T165029Z-jcm_medium_no_244.md
    sha256: 173f5ea3e4b1dc3870c6d48db9c3e35248407145fd627824dcf520b228b4f43f
    role: context
  - path: reports/yaml_record_review/20260924T234748Z-pyrococcus_medium__a85c0932.md
    sha256: 691813f42cb15ef4629fbe725324ec56b58ae4365e2913707be7cc2316503733
    role: context
  - path: reports/yaml_record_review/20260925T073134Z-stetteria_medium__0a06dac3.md
    sha256: 41bfa56ac9bcb89736aff2e979209ee5c11e63d715a748fe6a67d25add61860a
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
  - path: scripts/fetch_komodo_base_volumes.py
    sha256: 9dad49c380422b2e7d3f40b4ff713d59360d22f6eec9b55068e050099cb9cffa
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
  - path: scripts/repair_methanogen_stock_boundaries.py
    sha256: 8d4d32c7dc3cb2586242a188f958087482df3aff553d1dbc468c422eddb037ba
    role: context
  - path: scripts/repair_reducing_stages.py
    sha256: 8fd71c0218edcf91dc6dba0804cc703d4a21141c258a46f7f4aa27460eccfc49
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
  selection: Authoritative batch078 index 10
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010157
targets:
- target_id: CultureMech:010157
  path: data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml
  label: desulfosporosinus_acidiphilus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
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
  - CultureMech:010157
  command: just validate-schema data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml
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
  - CultureMech:010157
  command: just validate-strict data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml
    --out REVIEW_WORK/batch078/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:010157
  command: just validate-terms data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml
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
  - CultureMech:010157
  command: just validate-references data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: togo751
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751
  accessed_at: '2026-10-28T20:57:52.100670Z'
  locator: REVIEW_WORK/batch078/source07-08-10/togo751.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact provider source M751; selected M751 full scope, M142 trace and M236
    Ni-Se-W only.
  snapshot_sha256: 5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9
- evidence_id: apiJ728
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J728
  accessed_at: '2026-10-28T20:57:52.577177Z'
  locator: REVIEW_WORK/batch078/source07-08-10/apiJ728.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Current JCM728 provider representation is compared separately to primary/source
    quantities.
  snapshot_sha256: 8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37
- evidence_id: jcm728
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=728
  accessed_at: '2026-10-28T20:57:51.422627Z'
  locator: REVIEW_WORK/batch078/source07-08-10/jcm728.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected JCM728 request returned HTTP200 Nothing found; no selected
    primary recipe was recovered.
  snapshot_sha256: 4cc4a1acf27b21290d8c3d89f2952623cc42bfd0c21ff3b7cb1a80cb661db982
- evidence_id: togo142
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142
  accessed_at: '2026-10-28T20:57:52.796420Z'
  locator: REVIEW_WORK/batch078/source07-08-10/togo142.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current M142 provider source; only the Trace minerals subsection
    and preparation are in scientific scope.
  snapshot_sha256: 610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33
- evidence_id: jcm151
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151
  accessed_at: '2026-10-28T20:57:52.009118Z'
  locator: REVIEW_WORK/batch078/source07-08-10/jcm151.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Complete current JCM151 source read; only its Trace minerals table and
    stock preparation transfer to the M751 dependency scope.
  snapshot_sha256: 6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7
- evidence_id: togo236
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236
  accessed_at: '2026-10-28T20:57:52.815582Z'
  locator: REVIEW_WORK/batch078/source07-08-10/togo236.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current M236 provider source; only the Ni-Se-W subsection is in scientific
    scope.
  snapshot_sha256: 22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68
- evidence_id: jcm244
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244
  accessed_at: '2026-10-28T20:57:52.009069Z'
  locator: REVIEW_WORK/batch078/source07-08-10/jcm244.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Complete current JCM244 source read; only its Ni-Se-W table transfers to
    the M751 dependency scope.
  snapshot_sha256: 112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T20:57:55.582950Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T21:12:41.400387Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 93d5a5918b049290e6d6111d32dab38b9a0eb4b5155bc9596a9c724b96894dc0
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T21:12:41.400576Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 8f97519904c7ec55054b3e06be0b7d0d14528521824a0e30206f5fecac7833aa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T21:12:41.400607Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T21:12:41.400895Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T21:12:41.400918Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T21:12:41.400939Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-j261-variant/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:12:41.400963Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 6596fd242999001378304c512ae0e469c74b342c4ba975acec7c80052b746d78
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-j261-variant/records/M142.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.401309Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 3005c0fe47be96230058f7eb8779d9915ff96ebf9de43f2ba476bb7e4f1ac75d
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-j261-variant/records/M253.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.401331Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 8cb25cf38148de75110754cba1ce951746573c3fae7ed47c8169ea604e906f32
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:12:41.401381Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 00113dc0b556486b52084f2508b061b9a188423d479f8aa102511ec55074ebd5
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M142.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.401753Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 42adc98b2f24eef6d866f81a2cdc36eba868fbcf592695cd02c649cae404855b
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-reducing-stages/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:12:41.401783Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 7262df2869246a849e11ab6eca57475a6163a346abd31e5c50a0ed8865fc0edf
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-reducing-stages/records/M236.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402354Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 89c67d9d489a74e3ffcddb35fce9f3a26eab3099e4a19f8f595a9e5c41b5e5e6
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402402Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 78147c6528e0368dc355246ecfe8b1504e2d89b1bb63a77add906ec286cdd313
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfosporosinus_acidiphilus_medium__0c10268a.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402425Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: fdc94cf985da6217a496a4960033148b91b059477a39a2daeabb6d2a13500f40
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__6ffabef8.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402446Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 83c8213491aaeb9764f15234d55e465b4ddadad00dc05bfaa93743419b3d9ea2
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/pyrococcus_medium__a85c0932.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402466Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: b7afb33e6091981790d7d02bd4e7a2ecfa11655363fc9ee42994a3b3b3e757ad
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/stetteria_medium__0a06dac3.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402486Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: a582736badb07bb5ad08fe04551c58f61c8bcd1c441e9825aa861facc41e36a1
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/stetteria_medium__87ed999a.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402509Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 1dac54ee407cad8e61c2f1638856eb079271b1a6767beb364aa6aeea6f4f0896
- evidence_id: report-32
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402529Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 2819146dc7d90f64ef630274b9d757bd510220b222d429716fc29d878d82b1b9
- evidence_id: report-33
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402550Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d7cb69aa18b8ba621fb353ddd4fe26c89b6b97c552be374ffba6080d652e9b0c
- evidence_id: report-34
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402570Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 27ff9317c0c7429a7da291fe13aff12f337669101e3aba43ff95a6117fd6a411
- evidence_id: report-35
  kind: prior_review
  reference: reports/yaml_record_review/20260921T134926Z-archaeoglobus_fulgidus_medium__01928dac.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402590Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: c8179ba605d1060447c97f02315b5a012f9d7ae79f3074424db8d223b428f46f
- evidence_id: report-36
  kind: prior_review
  reference: reports/yaml_record_review/20260922T195126Z-desulfosporosinus_acidiphilus_medium__0c10268a.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402611Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 197d7d5af8fc9564d24e6d1636d61cdeba5873624f68a65ddd36cfadfa7ee059
- evidence_id: report-37
  kind: prior_review
  reference: reports/yaml_record_review/20260923T165029Z-jcm_medium_no_244.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402631Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 173f5ea3e4b1dc3870c6d48db9c3e35248407145fd627824dcf520b228b4f43f
- evidence_id: report-38
  kind: prior_review
  reference: reports/yaml_record_review/20260924T234748Z-pyrococcus_medium__a85c0932.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402650Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 691813f42cb15ef4629fbe725324ec56b58ae4365e2913707be7cc2316503733
- evidence_id: report-39
  kind: prior_review
  reference: reports/yaml_record_review/20260925T073134Z-stetteria_medium__0a06dac3.md
  locator: Complete report
  accessed_at: '2026-10-28T21:12:41.402672Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 41bfa56ac9bcb89736aff2e979209ee5c11e63d715a748fe6a67d25add61860a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/historical-reading.json
  accessed_at: '2026-10-28T21:12:41.474719Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: bde361f5bba1eb9b4d1ce4d4f2516a03188df61349b7e9f21ed2d070e66d5834
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:12:41.474864Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 9408c601b83c54a545cb4ebe0d9be69e0397fc45f75bb0dffb1813ef20acbea9
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/complete-document-reader.json
  accessed_at: '2026-10-28T21:12:41.475107Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: ce455cc6fc7a37d98035de1ab2d52ce3a2791b593d8e42189ec67926584f99fb
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T21:12:41.475237Z'
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
  accessed_at: '2026-10-28T21:12:41.475273Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch078/record10/historical-current-object-joins.json
  accessed_at: '2026-10-28T21:12:41.475299Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: ce836d4e544a31ef3d22e8916a7bba10880d370a0672837d9b14a65d7aa06f25
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Full lines 229-869; extraction, solution, preparation, unit and pH methods
  accessed_at: '2026-10-28T21:12:41.475411Z'
  support: context_only
  summary: Current _extract_primary_components keeps named stock sections distinct
    and _solution_from_item retains their reference, but molar conc_value/conc_unit
    are not structured. Bare ml normalization and root-only pH parsing require source-stage
    care; current code does not establish historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-stock-repair
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: Complete current body
  accessed_at: '2026-10-28T21:12:41.475443Z'
  support: context_only
  summary: Current guarded M142 repair preserves supported batch inputs and trace-only
    preparation claims; no live repair was run.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: writer-reducing
  kind: record_content
  reference: scripts/repair_reducing_stages.py
  locator: Complete current body; sources, Review.stock/formulate/finish and process
  accessed_at: '2026-10-28T21:12:41.475473Z'
  support: context_only
  summary: Current M236 source graph separates Ni-Se-W stock components and named
    source excerpts; finish creates this repair output and records an event, not scientific
    validation of retained chemical identifiers.
  snapshot_sha256: 8fd71c0218edcf91dc6dba0804cc703d4a21141c258a46f7f4aa27460eccfc49
- evidence_id: writer-shared-repair
  kind: record_content
  reference: scripts/repair_methanogen_stock_boundaries.py
  locator: Complete current body; Review.claim/descriptor/finish and process
  accessed_at: '2026-10-28T21:12:41.475501Z'
  support: context_only
  summary: The shared claim method validates literal source excerpts and appends additional
    excerpts for an existing reference; descriptor distinguishes native batch volume
    from explicit per-litre prescription. Its guarded process checks frozen before/output
    bytes. These current methods are not replayed historical execution.
  snapshot_sha256: 8d4d32c7dc3cb2586242a188f958087482df3aff553d1dbc468c422eddb037ba
- evidence_id: scoped-html-claims
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/existing-html-claim-authentication.json
  accessed_at: '2026-10-28T21:12:41.475532Z'
  locator: Complete artifact
  support: context_only
  summary: Existing JCM244 component excerpts separately match normalized current
    HTML; raw digest equality is separately recorded.
  snapshot_sha256: f6a905f89845b22e605bdf929b7a7b0c6c8f833d90c4561393e9e4238549b940
- evidence_id: writer-read-addendum
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/author-current-writer-addendum.json
  accessed_at: '2026-10-28T21:12:41.475552Z'
  locator: Complete artifact
  support: context_only
  summary: Exact current TOGO full extraction methods and complete two added repair-writer
    bodies read; prior global reader is retained unchanged.
  snapshot_sha256: 075e231821b8d1831c829a40563ec7d61cfde8f65aa64f6632661a56f42d45d6
- evidence_id: root-history-contribution
  kind: prior_review
  reference: REVIEW_WORK/batch078/record10/root-provenance-contribution-20261028.json
  accessed_at: '2026-10-28T21:12:41.475708Z'
  locator: Complete bounded root contribution and direct pins
  support: context_only
  summary: Root independently read complete reports, exact selected parent rows and
    current M142/M236 histories/root evidence; source/quantity/form and current two
    added writer scopes were read by this author.
  snapshot_sha256: 51056578513681fcd4d6a703ac4bdb1c0ffd7fda1176da99f176292756c71fc6
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  accessed_at: '2026-10-28T20:57:52.805335Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi32036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32036
  accessed_at: '2026-10-28T20:57:54.002024Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi32036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0e2a526c994d512b314d090b5acbd8acbc65a9f998ac0d292d8756f2b97de777
- evidence_id: chebi26836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26836
  accessed_at: '2026-10-28T20:57:53.415675Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi26836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 19e202cd697eed2be3130d5b0b29cc0c1d18575ad103110877303ee678779737
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  accessed_at: '2026-10-28T20:57:53.331265Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  accessed_at: '2026-10-28T20:57:54.006206Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi31795.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  accessed_at: '2026-10-28T20:57:52.741596Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  accessed_at: '2026-10-28T20:57:54.528493Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_62946
  accessed_at: '2026-10-28T20:57:55.765820Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi62946.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 10c25b481047a1fdfbc201104ecc06b15b32d5e72319beed5133e5d5693bede5
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T20:57:54.037990Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi86159
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86159
  accessed_at: '2026-10-28T20:57:56.949932Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86159.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d2b0e9caef5876c00ed00136113d600d34a071b137bdd8c661c734ad5435682f
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T20:57:53.394246Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T20:57:56.790414Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T20:57:56.189397Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T20:57:54.626226Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  accessed_at: '2026-10-28T20:57:56.363819Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  accessed_at: '2026-10-28T20:57:54.373367Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  accessed_at: '2026-10-28T20:57:53.946843Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi31440.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi91244
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  accessed_at: '2026-10-28T20:57:57.984864Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi91244.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  accessed_at: '2026-10-28T20:57:54.983491Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi44557.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi86360
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86360
  accessed_at: '2026-10-28T20:57:57.392345Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86360.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee3b60385f389c4eeb301cfe59996112ffa9c3c135268559b79e91810a14932b
- evidence_id: chebi86463
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86463
  accessed_at: '2026-10-28T20:57:57.638587Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86463.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 59060418cddd95e8401be3d2518a69fbcd26a4f4e6f0597b2c8c03834a87812e
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T20:57:54.649502Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  accessed_at: '2026-10-28T20:57:55.840293Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi63939.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi48843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_48843
  accessed_at: '2026-10-28T20:57:55.165408Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi48843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f8b54c90292c3ea1c215cbb96e7b9302304ba97f07c586c66f09b6689b9f2d91
- evidence_id: chebi86149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86149
  accessed_at: '2026-10-28T20:57:56.453246Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 930d93c33f6115f19153868ae36f0153b69406fd555708237a7ccccfb010cd97
- evidence_id: chebi77775
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_77775
  accessed_at: '2026-10-28T20:57:56.443251Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi77775.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: a1a4ab87bbf08908fef7df53a788a85d9f6eee32350f082895e0563d6344c908
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:12:41.565875Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: dd51c269ef7fba1aa105ec58b9e9c7ceaa5c7e40fc58b77daade2d2d1c37996a
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:12:41.565957Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: c5ca9f85a7896d34134136faf22e1b53f9883f4b1842ba30fe198c7fe029d630
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:12:41.566052Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 668ce13079ed75ab2d17fca7ad6d6d0fd5c91ae65deba2f81fc34de6b662c246
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:12:41.566219Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: af8eb017518687b2d24761f4b9725112d2b99a1e634eeea6aa5660b7200addce
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:12:41.566383Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 192ec13cbedb79f8ffa0b761168fd57653b3765da63557522ad97c8b1608748b
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:12:41.566432Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: c12a7be0ea6de23776920c305a0d96a7ad59a7809881f2d0cd7847416e7bd323
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch078/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:12:41.566454Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 44204dea073cc5cddbb83116b781d9f15bb861c551510f16c3d594ccb4109b54
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch078/record10/schema-result.json
  accessed_at: '2026-10-28T20:57:42.214301Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 4d70622fc10d9ebaf7d340e20cd2f64ba0a81ed680d61bc9d39e7683dbd9b49e
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch078/record10/strict-result.json
  accessed_at: '2026-10-28T20:57:43.271691Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: b9d35c996550bfa5c79452ef9f64833df56f8a1ae0a6ee11ecdca5ca837c03f1
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch078/record10/terms-result.json
  accessed_at: '2026-10-28T20:57:44.367728Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 55231e9104e6d68ba43b6b6e25eff3e7b42456c0ac0059f060daeb494685766d
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch078/record10/references-result.json
  accessed_at: '2026-10-28T20:57:45.093129Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 4a74cffe35f51b8b59f9b2280e81ca4b25457960787f4f2d7ef023b84b94e41e
assessments:
- assessment_id: identity
  area: identity
  topic: Selected identity and available source versions
  outcome: concern
  summary: TOGO M751 and J728 identify JCM728 and agree on the named main/HBS/trace/Ni-Se-W
    scopes. Current JCM728 returns HTTP200 Nothing found, so primary selected-recipe
    recovery is incomplete. JCM151 and244 corroborate only their named stock tables;
    complete parent recipes and their receiving doses are excluded.
  target_ids:
  - CultureMech:010157
  evidence_ids:
  - togo751
  - apiJ728
  - jcm728
  - jcm151
  - jcm244
  - target
  - owner
- assessment_id: classification
  area: consistency
  topic: Complex liquid classification
  outcome: supported
  summary: The source includes defined salts and a small yeast-extract contribution,
    supporting the actual COMPLEX/SEMI_DEFINED liquid classification. No growth claim
    follows from the organism or medium name.
  target_ids:
  - CultureMech:010157
  evidence_ids:
  - togo751
  - apiJ728
  - target
  - owner
- assessment_id: schema
  area: schema
  topic: Original required diagnostics
  outcome: supported
  summary: The original four diagnostics all exited 0. The additive inspection preserves
    every original input and adds only two current repair writers; no canonical check
    was repeated.
  target_ids:
  - CultureMech:010157
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
  - writer-reducing
  - writer-shared-repair
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 36 current concentration fields are covered by 39 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:010157
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b078-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","quantity_field_count":36,"decisions":[{"quantity_id":"q1","label":"Separate
    main and HBS water inputs","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"940.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"940.0","unit":"G_PER_L"}},{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[0].notes","stored":"Role:
    Solvating media; Properties: Defined component, Simple component, Inorganic compound
    [Merged 2 duplicates: 939.0, 1.0]"},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[0].notes","stored":"Role:
    Solvating media; Properties: Defined component, Simple component, Inorganic compound
    [Merged 2 duplicates: 939.0, 1.0]"}],"decision":"correct","rationale":"The local
    940 g/L is a duplicate sum of 939 ml main water and 1 L HBS water, combining distinct
    stages and source units. Preserve each native water input separately; neither
    input alone establishes measured final volume.","source_stage":"Main versus HBS
    stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 939,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 939,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider explicitly declares this unchanged g/L rate. Credit
    its normalization separately from the native batch amount; the 1000 ml provider
    volume is not independent measurement of final volume. No attached current claim
    exists in the selected documents.","source_stage":"Main solution","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"K2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.87","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.87","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    exact main-solution provider explicitly declares this unchanged g/L rate. Credit
    its normalization separately from the native batch amount; the 1000 ml provider
    volume is not independent measurement of final volume. No attached current claim
    exists in the selected documents.","source_stage":"Main solution","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"K2SO4\",\n          \"volume\": 0.87,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001173\",\n          \"gmo_id\": \"GMO_001173\",\n          \"label\":
    \"Potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"K2SO4\",\n                        \"compound_id\":
    382,\n                        \"amount\": 0.87,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.87,\n                        \"mmol_l\":
    4.99254,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"H2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The
    source does not specify a fixed amount or dissolved concentration. Retain the
    truthful VARIABLE placeholder; the separately missing pH adjustment or nitrogen-atmosphere
    instruction does not supply a numeric ingredient concentration.","source_stage":"Main
    unquantified reagent or atmosphere","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"H2SO4\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001482\",\n          \"gmo_id\":
    \"GMO_001482\",\n          \"label\": \"Sulfuric acid solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix thoroughly, adjust to pH 5.5 with H2SO4 and autoclave
    under a N2 atmosphere. After cooling, aseptically and anaerobically add the following
    solutions (filter--sterilized) to the medium:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"The
    source does not specify a fixed amount or dissolved concentration. Retain the
    truthful VARIABLE placeholder; the separately missing pH adjustment or nitrogen-atmosphere
    instruction does not supply a numeric ingredient concentration.","source_stage":"Main
    unquantified reagent or atmosphere","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix thoroughly, adjust to pH 5.5 with H2SO4 and autoclave
    under a N2 atmosphere. After cooling, aseptically and anaerobically add the following
    solutions (filter--sterilized) to the medium:\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"MgSO4・7H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"25","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider explicitly supports this rate only within HBS stock. Restore that named
    stock boundary and its distinct water input; the current root placement incorrectly
    represents stock strength as a main-medium ingredient concentration. No final-medium
    dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"MgSO4・7H2O\",\n          \"volume\": 25,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\":
    \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 25,\n                        \"mmol_l\":
    101.43,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider explicitly supports this rate only within HBS stock. Restore that named
    stock boundary and its distinct water input; the current root placement incorrectly
    represents stock strength as a main-medium ingredient concentration. No final-medium
    dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"K2HPO4\",\n                        \"compound_id\":
    10,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    14.3533,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider explicitly supports this rate only within HBS stock. Restore that named
    stock boundary and its distinct water input; the current root placement incorrectly
    represents stock strength as a main-medium ingredient concentration. No final-medium
    dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    33.5345,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"(NH4)2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"22.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"22.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider explicitly supports this rate only within HBS stock. Restore that named
    stock boundary and its distinct water input; the current root placement incorrectly
    represents stock strength as a main-medium ingredient concentration. No final-medium
    dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"(NH4)2SO4\",\n          \"volume\": 22.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001030\",\n          \"gmo_id\": \"GMO_001030\",\n          \"label\":
    \"Ammonium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\":
    27,\n                        \"amount\": 22.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 22.5,\n                        \"mmol_l\":
    170.274,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3.3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3.3","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider explicitly supports this rate only within HBS stock. Restore that named
    stock boundary and its distinct water input; the current root placement incorrectly
    represents stock strength as a main-medium ingredient concentration. No final-medium
    dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Na2SO4\",\n          \"volume\": 3.3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\":
    \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.3,\n                        \"mmol_l\":
    23.2329,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"Ca(NO3)2・4H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.7","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.7","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    provider explicitly supports this rate only within HBS stock. Restore that named
    stock boundary and its distinct water input; the current root placement incorrectly
    represents stock strength as a main-medium ingredient concentration. No final-medium
    dilution is inferred.","source_stage":"HBS stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Ca(NO3)2・4H2O\",\n          \"volume\": 0.7,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001116\",\n          \"gmo_id\": \"GMO_001116\",\n          \"label\":
    \"Calcium nitrate tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Ca(NO3)2 x 4 H2O\",\n                        \"compound_id\":
    213,\n                        \"amount\": 0.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.7,\n                        \"mmol_l\":
    2.96423,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q12","label":"HBS solution (see below)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source gives this addition in ml, while the local descriptor records the same
    numeral in G_PER_L. Restore the batch volume and preserve exact stock identity
    and composition separately. A receiving-medium dose does not equal the parent
    record dose or prove a final-volume denominator.","source_stage":"Main receives
    named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"HBS solution (see below)\",\n          \"volume\": 20,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M751\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"HBS solution\",\n                        \"solution_id\":
    4653,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"Trace minerals (see Medium [M142])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source gives this addition in ml, while the local descriptor records the same
    numeral in G_PER_L. Restore the batch volume and preserve exact stock identity
    and composition separately. A receiving-medium dose does not equal the parent
    record dose or prove a final-volume denominator.","source_stage":"Main receives
    named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"Trace minerals (see Medium [M142])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M142\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Trace minerals\",\n                        \"solution_id\":
    3804,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"Ni-Se-W solution (see Medium [M236])","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source gives this addition in ml, while the local descriptor records the same
    numeral in G_PER_L. Restore the batch volume and preserve exact stock identity
    and composition separately. A receiving-medium dose does not equal the parent
    record dose or prove a final-volume denominator.","source_stage":"Main receives
    named stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"Ni-Se-W solution (see Medium [M236])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M236\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Ni-Se-W solution\",\n                        \"solution_id\":
    3927,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"1 M ZnSO4 solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"7","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"7","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source gives this addition in ml, while the local descriptor records the same
    numeral in G_PER_L. Restore the batch volume and preserve exact stock identity
    and composition separately. A receiving-medium dose does not equal the parent
    record dose or prove a final-volume denominator. Its explicit molar strength remains
    distinct from addition volume; do not infer a hydrate or mass conversion. Retain
    the later filter-sterilized addition stage.","source_stage":"Main receives named
    stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"1 M ZnSO4 solution\",\n          \"volume\": 7,\n          \"unit\": \"ml\",\n          \"conc_value\":
    1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001277\",\n          \"gmo_id\":
    \"GMO_001277\",\n          \"label\": \"Zinc sulfate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"ZnSO4\",\n                        \"compound_id\":
    441,\n                        \"attribute\": \"1 M\",\n                        \"amount\":
    7,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"10
    mM FeSO4 solution (pH 2.0)","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[4].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source gives this addition in ml, while the local descriptor records the same
    numeral in G_PER_L. Restore the batch volume and preserve exact stock identity
    and composition separately. A receiving-medium dose does not equal the parent
    record dose or prove a final-volume denominator. Its explicit molar strength remains
    distinct from addition volume; do not infer a hydrate or mass conversion. Retain
    the later filter-sterilized addition stage.","source_stage":"Main receives named
    stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"10 mM FeSO4 solution (pH 2.0)\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\":
    \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"FeSO4\",\n                        \"compound_id\":
    595,\n                        \"attribute\": \"pH 2.0, 10 mM\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"1
    M Glycerol solution","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml","field_path":"solutions[5].concentration","stored":{"value":"4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"4","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source gives this addition in ml, while the local descriptor records the same
    numeral in G_PER_L. Restore the batch volume and preserve exact stock identity
    and composition separately. A receiving-medium dose does not equal the parent
    record dose or prove a final-volume denominator. Its explicit molar strength remains
    distinct from addition volume; do not infer a hydrate or mass conversion. Retain
    the later filter-sterilized addition stage.","source_stage":"Main receives named
    stock","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"1 M Glycerol solution\",\n          \"volume\": 4,\n          \"unit\": \"ml\",\n          \"conc_value\":
    1,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001466\",\n          \"gmo_id\":
    \"GMO_001466\",\n          \"label\": \"Glycerol solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Glycerol\",\n                        \"compound_id\":
    72,\n                        \"attribute\": \"1 M\",\n                        \"amount\":
    4,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"Distilled
    water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[0].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Collapsed 2 identical duplicates: 1.0, 1.0]\n\nSource water batch input: 1 L
    = 1 L. This is not a measured final volume. Prior duplicate-collapse notes describe
    the superseded flattened record."}],"decision":"verified","rationale":"Credit
    the retained batch input and its existing attached literal source claim, authenticated
    against unchanged current provider raw bytes. Historical duplicate notes are superseded
    by the explicit scoped repair. Water is a batch input; retained mass notes do
    not assert a measured final-volume concentration. The current J728 provider also
    declares a stock rate, which does not invalidate this conservative batch-note
    representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 32 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"MgSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 3.5, 3.0]\n\nSource batch input: 3 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit
    the retained batch input and its existing attached literal source claim, authenticated
    against unchanged current provider raw bytes. Historical duplicate notes are superseded
    by the explicit scoped repair. Water is a batch input; retained mass notes do
    not assert a measured final-volume concentration. The current J728 provider also
    declares a stock rate, which does not invalidate this conservative batch-note
    representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> MgSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q20","label":"NaCl","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 13.85, 1.0]\n\nSource batch input: 1 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit
    the retained batch input and its existing attached literal source claim, authenticated
    against unchanged current provider raw bytes. Historical duplicate notes are superseded
    by the explicit scoped repair. Water is a batch input; retained mass notes do
    not assert a measured final-volume concentration. The current J728 provider also
    declares a stock rate, which does not invalidate this conservative batch-note
    representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q21","label":"CaCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q22","label":"Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 31 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q23","label":"H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component
    [Merged 2 duplicates: 15.0, 0.01]\n\nSource batch input: 0.01 g. Final preparation
    volume is not independently established; the unsupported g/L assertion is withdrawn,
    not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit
    the retained batch input and its existing attached literal source claim, authenticated
    against unchanged current provider raw bytes. Historical duplicate notes are superseded
    by the explicit scoped repair. Water is a batch input; retained mass notes do
    not assert a measured final-volume concentration. The current J728 provider also
    declares a stock rate, which does not invalidate this conservative batch-note
    representation.","source_stage":"Trace minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 30 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"FeSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> FeSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q25","label":"ZnSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 27 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.347752,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"CuSO4・5H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 28 (zero-based)","quote":"<TR><TD WIDTH=75%> CuSO<sub>4</sub>&#183;5H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"CoSO4・7H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> CoSO<sub>4</sub>&#183;7H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.645178,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Mineral source; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nitrilotriacetic acid                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"MnSO4・xH2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[11].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation. The printed
    hydrate variable remains unspecified; no fixed water count is assigned.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[11]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> MnSO<sub>4</sub>&#183;<I>x</I>H<sub>2</sub>O                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\":
    1000,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"AlK(SO4)2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].composition[12].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.01 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Trace
    minerals only","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[12]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"HTML
    table row 29 (zero-based)","quote":"<TR><TD WIDTH=75%> AlK(SO<sub>4</sub>)<sub>2</sub>                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.01&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2\",\n                        \"compound_id\":
    1015,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0387289,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q31","label":"Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[0].concentration","stored":{"value":"1","unit":"L"}},{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[0].notes","stored":"Role:
    Solvating media; Properties: Inorganic compound, Defined component, Simple component
    [Merged 3 duplicates: 500.0, 1.0, 1.0]\n\nSource water batch input: 1 L = 1 L.
    This is not a measured final volume.\n\nThe earlier duplicate-summing note is
    superseded: it combined separate preparation scopes and source units. This node
    carries only the batch input at the cited source row; other occurrences are separate
    scoped ingredients."}],"decision":"verified","rationale":"Credit the retained
    batch input and its existing attached literal source claim, authenticated against
    unchanged current provider raw bytes. Historical duplicate notes are superseded
    by the explicit scoped repair. Water is a batch input; retained mass notes do
    not assert a measured final-volume concentration. The current J728 provider also
    declares a stock rate, which does not invalidate this conservative batch-note
    representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q32","label":"NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 25 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W
    only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"NiCl2・6H2O\",\n          \"volume\": 25,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\":
    \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;25.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 25,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\":
    0.192903,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q33","label":"Na2WO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[2].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W
    only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"Na2WO4・2H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\":
    \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>WO<sub>4</sub>&#183;2H<sub>2</sub>O                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0303168,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q34","label":"Na2SeO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[3].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 0.3 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W
    only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"Na2SeO3\",\n          \"volume\": 0.3,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001093\",\n          \"gmo_id\": \"GMO_001093\",\n          \"label\":
    \"Sodium selenite\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SeO<sub>3</sub>                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.3&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2SeO3\",\n                        \"compound_id\":
    699,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"(NH4)2Ni(SO4)2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[4].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 2 g. Final preparation volume is not independently established; the
    unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Credit
    the retained batch input and its existing attached literal source claim, authenticated
    against unchanged current provider raw bytes. Historical duplicate notes are superseded
    by the explicit scoped repair. Water is a batch input; retained mass notes do
    not assert a measured final-volume concentration. The current J728 provider also
    declares a stock rate, which does not invalidate this conservative batch-note
    representation.","source_stage":"Ni-Se-W only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"(NH4)2Ni(SO4)2・6H2O\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001102\",\n          \"gmo_id\": \"GMO_001102\",\n          \"label\":
    \"Ammonium nickel(II) sulfate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> (NH<sub>4</sub>)<sub>2</sub>Ni(SO<sub>4</sub>)<sub>2</sub>&#183;6H<sub>2</sub>O                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"(NH4)2Ni(SO4)2 x 6 H2O\",\n                        \"compound_id\":
    739,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"mmol_l\":
    5.06346,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q36","label":"Na2SeO4","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml","field_path":"solutions[2].composition[5].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Credit the retained batch
    input and its existing attached literal source claim, authenticated against unchanged
    current provider raw bytes. Historical duplicate notes are superseded by the explicit
    scoped repair. Water is a batch input; retained mass notes do not assert a measured
    final-volume concentration. The current J728 provider also declares a stock rate,
    which does not invalidate this conservative batch-note representation.","source_stage":"Ni-Se-W
    only","sources":[{"evidence_id":"togo236","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M236","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo236.raw","raw_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","text_sha256":"22033637522251f2e6d6f1eb0d048bd092a0894eb2636e6eb127102af6822d68","accessed_at":"2026-10-28T20:57:52.815582Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Na2SeO4\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001602\",\n          \"gmo_id\": \"GMO_001602\",\n          \"label\":
    \"Sodium selenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm244","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=244","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm244.raw","raw_sha256":"112072cc87d6839b575287734b39edcce1bd55c1660d8b221ccc679d496ae97e","text_sha256":"164dad6002b36e30356a9e70a389335cd873a33f747a5139f9df039d4cde6eb4","accessed_at":"2026-10-28T20:57:52.009069Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>SeO<sub>4</sub>                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[3].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Na2SeO4\",\n                        \"compound_id\":
    375,\n                        \"amount\": 10,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0529241,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q37","label":"Retained trace-stock pH preparation","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].preparation_notes","stored":"Dissolve
    nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then proceed to
    add minerals. Adjust final pH to 7.0."}],"decision":"verified","rationale":"The
    retained pH 6.5 then 7.0 method belongs only to the trace-mineral stock and is
    explicitly supported by an additional excerpt in the existing root evidence. Preserve
    it; no receiving-medium pH or fixed titrant dose is inferred.","source_stage":"Trace
    minerals preparation","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with
    KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[2].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH solution. Then
    proceed to add minerals. Adjust final pH to 7.0.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm151","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151","raw_path":"REVIEW_WORK/batch078/source07-08-10/jcm151.raw","raw_sha256":"6cfac0ff9954839eabcdf17884480ce9ea76646da8cbfac0ca0d92ac393584d7","text_sha256":"3365c558faa5ecbd13048774769862f1bdbcae3d9d8925d147bd81ce66c38aa6","accessed_at":"2026-10-28T20:57:52.009118Z","locator":"jcm151.txt
    lines 203-203","quote":"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with
    KOH solution.      Then proceed to add minerals.   Adjust final pH to 7.0.","quote_basis":"derivative
    text"}]},{"quantity_id":"q38","label":"Unquantified KOH titrant","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml","field_path":"solutions[1].solutions[0].notes","stored":"Role:
    Mineral source; Properties: Defined component, Solution\n\npH-adjustment reagent;
    no fixed dose is specified. Normality is not converted to molarity."}],"decision":"verified","rationale":"The
    retained stock-only titrant note and absent fixed quantity agree with the current
    source and existing root additional excerpt. The source supplies no numeric strength;
    the placeholder name is a separate minor metadata defect.","source_stage":"Trace
    minerals titration","sources":[{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"components[2].items[13]","quote":"{\n          \"component_name\":
    \"KOH solution\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\":
    \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo142","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M142","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo142.raw","raw_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","text_sha256":"610b8b81872be555185d912ce93fed547485e0b9f3a1c1ee14fe4c6fc0e14c33","accessed_at":"2026-10-28T20:57:52.796420Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with
    KOH solution. Then proceed to add minerals. Adjust final pH to 7.0.\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q39","label":"Missing main pH and staged preparation","local_fields":[],"decision":"correct","rationale":"Restore
    source-supported main pH 5.5, nitrogen autoclave atmosphere, cooling, then aseptic
    anaerobic additions of the three filter-sterilized solutions. Preserve FeSO4 stock
    pH 2.0 separately. No autoclave temperature/time is supplied by the available
    selected source, and no JCM151/244 default is transferred.","source_stage":"Main
    versus later additions","sources":[{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Mix thoroughly, adjust to pH 5.5 with H2SO4 and autoclave
    under a N2 atmosphere. After cooling, aseptically and anaerobically add the following
    solutions (filter--sterilized) to the medium:\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ728","reference":"https://mediadive.dsmz.de/rest/medium/J728","raw_path":"REVIEW_WORK/batch078/source07-08-10/apiJ728.raw","raw_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","text_sha256":"8671a1f3a641d7ea84a3c971adbf5740bd57b49c8d85123957162432aa108f37","accessed_at":"2026-10-28T20:57:52.577177Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"step\": \"Mix thoroughly, adjust to pH 5.5 with
    H2SO4 and autoclave under a N2 atmosphere. After cooling, aseptically and anaerobically
    add the following solutions (filter-sterilized) to the medium: \"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo751","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M751","raw_path":"REVIEW_WORK/batch078/source07-08-10/togo751.raw","raw_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","text_sha256":"5c544ff412ca6d1d01d435ab7f2957390680884eba5641c7777bd84c70d5d4d9","accessed_at":"2026-10-28T20:57:52.100670Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"10 mM FeSO4 solution (pH 2.0)\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 10,\n          \"conc_unit\": \"mM\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001393\",\n          \"gmo_id\": \"GMO_001393\",\n          \"label\":
    \"Iron(II) sulfate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOSPOROSINUS_ACIDIPHILUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml":["solutions[1].composition","solutions[1].solutions","solutions[1].preparation_notes","solutions[1].preferred_term","solutions[1].name"],"data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml":["solutions[2].composition","solutions[2].preferred_term","solutions[2].name"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted slots and current exact MIM/OLS objects were checked. The
    selected magnesium heptahydrate primary is correct and no secondary slot is asserted
    there. Scoped nickel hexahydrate uses anhydrous nickel identity. Other explicitly
    supplied hydrates, NTA and selenium salts were assessed separately. The trace
    manganese hydrate variable remains unresolved; current catalog spelling/status
    is not proof of supplied form.
  target_ids:
  - CultureMech:010157
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: The complete historical report and selected-parent reading is supplied
    by the pinned root contribution, including current M142/M236 history and root
    evidence. The author independently checked the current sources, every in-scope
    quantity and supplied form, existing scoped excerpts, and current importer/repair
    bodies. Current equal raw content authenticates the exact excerpt, not the original
    retrieval event. Prior repairs correctly retain separate batch notes and water
    inputs; those current fixes are credited, while old parent-wide recommendations
    are not automatically adopted.
  target_ids:
  - CultureMech:010157
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - historical-object-joins
  - writer-mediadive
  - writer-formulation
  - writer-merger
  - historical-selected-parent-rows
  - root-history-contribution
  - writer-stock-repair
  - writer-reducing
  - writer-shared-repair
  - writer-togo
  - writer-read-addendum
  - scoped-html-claims
findings:
- finding_id: f1
  issue_key: culturemech-010157-stock-stage-water
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore stock boundaries and separate water stages
  description: The selected target and owner combine 939 ml main water with 1 L HBS
    water as 940 g/L and flatten six HBS stock components into main ingredients. Preserve
    the provider-supported HBS rates under their stock and keep both water inputs
    separate. The repaired M142 and M236 stock definitions already retain correct
    batch inputs with evidence and must not be re-flattened.
  target_ids:
  - CultureMech:010157
  field_paths:
  - ingredients[0]
  - ingredients[5]
  - ingredients[6]
  - ingredients[7]
  - ingredients[8]
  - ingredients[9]
  - ingredients[10]
  - solutions[0].composition
  evidence_ids:
  - togo751
  - apiJ728
  - quantities
  - writer-togo
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-010157-stock-dose-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Represent six liquid additions as volumes
  description: All six named solution descriptors encode ml addition numerals as G_PER_L
    and have empty compositions. Restore exact source-specific stock references or
    scoped compositions and native receiving-batch volumes; retain the separate 1
    M zinc sulfate, 10 mM iron sulfate and 1 M glycerol strengths without hydrate
    guesses or inferred mass conversions.
  target_ids:
  - CultureMech:010157
  field_paths:
  - solutions[0].concentration
  - solutions[1].concentration
  - solutions[2].concentration
  - solutions[3].concentration
  - solutions[4].concentration
  - solutions[5].concentration
  evidence_ids:
  - togo751
  - apiJ728
  - quantities
  - writer-togo
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-010157-preparation-scope
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Restore main preparation and separate stock controls
  description: The available exact TOGO and J728 sources specify main pH 5.5 and staged
    sterilization/addition, but the selected documents retain none of that procedure.
    Preserve the already supported trace-stock pH 6.5 then 7.0 and the separate iron-stock
    pH 2.0; neither is the final-medium pH. Retain VARIABLE H2SO4 and nitrogen placeholders
    as unquantified, independently of restoring the method.
  target_ids:
  - CultureMech:010157
  field_paths:
  - preparation_steps
  - ph_value
  evidence_ids:
  - togo751
  - apiJ728
  - old-claims
  - quantities
  - writer-togo
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material omission of explicitly sourced preparation-stage
    and pH context; the quantity placeholders themselves are not fixed concentrations.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-010157-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the scoped nickel hexahydrate identity
  description: The Ni-Se-W dependency source and preferred term specify nickel chloride
    hexahydrate, but its primary CHEBI:34887 identifies anhydrous nickel dichloride.
    Current CHEBI:53542 explicitly includes six waters. Reconcile this exact dependency
    slot while preserving the already supported 25 mg batch note.
  target_ids:
  - CultureMech:010157
  field_paths:
  - data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml::solutions[2].composition[1].term
  evidence_ids:
  - togo236
  - jcm244
  - chebi34887
  - chebi53542
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml
    role: scoped dependency
- finding_id: f5
  issue_key: culturemech-010157-metadata-claims-and-hydrate
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Complete source claims, stock names and unresolved hydrate scope
  description: Attach exact selected-medium claims while preserving the authenticated
    dependency claims. Replace the six selected Unknown solution names, supply the
    missing scoped M142 trace name, and replace the nested KOH and M236 Ni-Se-W placeholder
    names using their existing source-specific preferred terms. Keep the trace manganese
    xH2O hydrate unspecified; its generic manganese sulfate identifier does not establish
    a fixed hydrate and no molecular conversion is warranted.
  target_ids:
  - CultureMech:010157
  field_paths:
  - solutions
  - data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml::solutions[1].name
  - data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml::solutions[1].solutions[0].name
  - data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml::solutions[1].composition[11].term
  - data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml::solutions[2].name
  evidence_ids:
  - old-claims
  - scoped-html-claims
  - groundings
  - togo751
  - togo142
  - togo236
  rule_id: review-yaml-record/completeness
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: The selected target and owner combine 939 ml main water with 1 L HBS
    water as 940 g/L and flatten six HBS stock components into main ingredients. Preserve
    the provider-supported HBS rates under their stock and keep both water inputs
    separate. The repaired M142 and M236 stock definitions already retain correct
    batch inputs with evidence and must not be re-flattened.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010157
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
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
  description: All six named solution descriptors encode ml addition numerals as G_PER_L
    and have empty compositions. Restore exact source-specific stock references or
    scoped compositions and native receiving-batch volumes; retain the separate 1
    M zinc sulfate, 10 mM iron sulfate and 1 M glycerol strengths without hydrate
    guesses or inferred mass conversions.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010157
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
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
  description: The available exact TOGO and J728 sources specify main pH 5.5 and staged
    sterilization/addition, but the selected documents retain none of that procedure.
    Preserve the already supported trace-stock pH 6.5 then 7.0 and the separate iron-stock
    pH 2.0; neither is the final-medium pH. Retain VARIABLE H2SO4 and nitrogen placeholders
    as unquantified, independently of restoring the method.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010157
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
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
  description: The Ni-Se-W dependency source and preferred term specify nickel chloride
    hexahydrate, but its primary CHEBI:34887 identifies anhydrous nickel dichloride.
    Current CHEBI:53542 explicitly includes six waters. Reconcile this exact dependency
    slot while preserving the already supported 25 mg batch note.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010157
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml
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
  description: Attach exact selected-medium claims while preserving the authenticated
    dependency claims. Replace the six selected Unknown solution names, supply the
    missing scoped M142 trace name, and replace the nested KOH and M236 Ni-Se-W placeholder
    names using their existing source-specific preferred terms. Keep the trace manganese
    xH2O hydrate unspecified; its generic manganese sulfate identifier does not establish
    a fixed hydrate and no molecular conversion is warranted.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010157
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M751_Desulfosporosinus_Acidiphilus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M142_Pyrococcus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M236_Stetteria_Medium.yaml
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
- The exact current JCM728 route returns HTTP200 Nothing found; no original selected
  recipe was recovered. TOGO M751 and J728 are separately identified provider evidence,
  not substitutes silently labelled as that primary.
- M142 coverage is only trace composition, nested KOH and trace preparation; M236
  coverage is only Ni-Se-W composition. Their full current provenance is read, but
  parent receiving doses, other ingredients and cultivation procedures are excluded.
- The JCM151/244 general autoclave defaults are not transferred to the unavailable
  selected JCM728 recipe. Fixed stock hydrates or density are not inferred from molar
  labels.
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
