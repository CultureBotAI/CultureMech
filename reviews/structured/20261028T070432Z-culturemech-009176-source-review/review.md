# Scientific review: Carboxydothermus Medium

- Review: 20261028T070432Z-culturemech-009176-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:51:16.968651Z
- Finished UTC: 2026-10-28T07:04:32.177575Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact source separates stocks and solvent inputs that remain flattened or mis-unitized locally. Resolve the wrong SL-11 linkage, restore source preparation and claim evidence, correct nickel form, and credit the valid standalone stock repairs.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch059 index 08
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009176 | data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml | generated | carboxydothermus_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009176 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009176 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009176 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009176 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact TOGO source and linked stock identities

identity: concern. Targets: CultureMech:009176.

The target and owner match M2609 and the full current TOGO API identifies DSM507. The initial guessed endpoint returned an HTML application shell and is not recipe evidence. The exact linked 5191 is authenticated as its own stock but conflicts with the recipe;5980 and34 are separately assessed.

### Classification and source-specific controls

representation: supported. Targets: CultureMech:009176.

The complex semi-defined liquid classification is compatible with the source yeast extract and chemical components. The record name and source variant notes do not establish any organism-growth claim.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009176.

95 current concentration fields are covered by 67 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b059-quantity-inventory-v1","target":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","quantity_field_count":95,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3100.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3100.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The encoded 3100 g/L sums water inputs from four different preparation stages. Retain 1000 mL main water,1000 mL trace-stock water,1000 mL vitamin-stock water and 100 mL sulfide-stock water separately as volumes. SL-11 explicitly makes up to 1000 mL; the other water entries do not themselves prove final volumes.","source_stage":"four separate solvent inputs","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed amount is a supported main-batch mass, but the existing G_PER_L requires a denominator not established by 1000 mL water input alone. The separate API uses declared1022 mL normalization; do not silently replace one interpretation with the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 11-11","quote":"Yeast extract                                            0.05         g","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed amount is a supported main-batch mass, but the existing G_PER_L requires a denominator not established by 1000 mL water input alone. The separate API uses declared1022 mL normalization; do not silently replace one interpretation with the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"CaCl2 x 2 H2O\",\n          \"volume\": 0.29,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 5-5","quote":"CaCl2 x 2 H2O                                            0.29         g","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed amount is a supported main-batch mass, but the existing G_PER_L requires a denominator not established by 1000 mL water input alone. The separate API uses declared1022 mL normalization; do not silently replace one interpretation with the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 7-7","quote":"KH2PO4                                                   0.33         g","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed amount is a supported main-batch mass, but the existing G_PER_L requires a denominator not established by 1000 mL water input alone. The separate API uses declared1022 mL normalization; do not silently replace one interpretation with the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 6-6","quote":"NH4Cl                                                    0.33         g","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.52","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.52","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed amount is a supported main-batch mass, but the existing G_PER_L requires a denominator not established by 1000 mL water input alone. The separate API uses declared1022 mL normalization; do not silently replace one interpretation with the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"MgCl2 x 6 H2O\",\n          \"volume\": 0.52,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 4-4","quote":"MgCl2 x 6 H2O                                            0.52         g","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed amount is a supported main-batch mass, but the existing G_PER_L requires a denominator not established by 1000 mL water input alone. The separate API uses declared1022 mL normalization; do not silently replace one interpretation with the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 3-3","quote":"KCl                                                      0.33         g","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The printed amount is a supported main-batch mass, but the existing G_PER_L requires a denominator not established by 1000 mL water input alone. The separate API uses declared1022 mL normalization; do not silently replace one interpretation with the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 10-10","quote":"NaHCO3                                                   1.00         g","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Keep the delivered gas amount unquantified. 100% identifies the nitrogen atmosphere, not a liquid ingredient concentration; re-scope this descriptor to preparation without inventing a gas dose.","source_stage":"preparation gas","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"N2\",\n          \"conc_value\": 100,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 16-23","quote":"1. Dissolve ingredients except bicarbonate, yeast extract, vitamins and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their\nvolume and autoclave. Add yeast extract, vitamins (sterilized by filtration) and sulfide from\nsterile anoxic stock solutions prepared under 100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nNeutralize the sodium sulfide with sterile H2SO4 (see medium 29). After completing the\nmedium adjust pH to 6.8-7.0.","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"36","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"36","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4 x 2 H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 60-60","quote":"Na2MoO4 x 2 H2O                                         36.00      mg","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 56-56","quote":"H3BO3                                                    6.00      mg","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"MnCl2 x 4 H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 55-55","quote":"MnCl2 x 4 H2O                                          100.00      mg","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"190","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"CoCl2 x 6 H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 57-57","quote":"CoCl2 x 6 H2O                                          190.00      mg","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"NiCl2 x 6 H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 59-59","quote":"NiCl2 x 6 H2O                                           24.00      mg","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"CuCl2 x 2 H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 58-58","quote":"CuCl2 x 2 H2O                                            2.00      mg","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"70","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"70","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 54-54","quote":"ZnCl2                                                   70.00      mg","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"FeCl2 x 4 H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 45-45","quote":"FeCl2 x 4 H2O                                             1.50        g","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"Na2-EDTA x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock makeup. The independently linked 5191 provider stock is not compositionally equivalent and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Na2-EDTA x 2 H2O\",\n          \"volume\": 5.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001148\",\n          \"gmo_id\": \"GMO_001148\",\n          \"label\": \"Disodium EDTA dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 44-44","quote":"Na2-EDTA x 2 H2O                                          5.20        g","quote_basis":"derivative text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"2 N NaOH","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The 2 N identifies titrant strength, while the amount added to adjust SL-11 pH is unquantified. Preserve that distinction and move it from main ingredients into the stock preparation.","source_stage":"SL-11 pH titration","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"2 N NaOH\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 70-70","quote":"Biotin                                                  20.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 78-78","quote":"p-Aminobenzoic acid                                     50.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"Thiamine-HCl","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"Thiamine-HCl\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 73-73","quote":"Thiamine HCl                                            50.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"Pyridoxine hydrochloride\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 72-72","quote":"Pyridoxine hydrochloride                               100.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q24","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 71-71","quote":"Folic acid                                              20.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 77-77","quote":"Vitamin B12                                              1.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q26","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 74-74","quote":"Riboflavin                                              50.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q27","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 75-75","quote":"Nicotinic acid                                          50.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q28","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\": \"(DL)-alpha-Lipoic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 79-79","quote":"(DL)-alpha-Lipoic acid                                  50.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q29","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source prints this mass in mg in the vitamin stock, whereas the selected records put the same number in main-medium G_PER_L. Restore the stock stage and source mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water input does not independently establish measured final volume.","source_stage":"Wolin vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\": \"Calcium D-(+)-pantothenate\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001940\",\n          \"gmo_id\": \"GMO_001940\",\n          \"label\": \"D-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 76-76","quote":"Calcium D-(+)-pantothenate                              50.00      mg","quote_basis":"derivative text"}]},{"quantity_id":"q30","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"The 3 g sodium sulfide nonahydrate is a stock-preparation mass, not 3 g/L of receiving medium. The explicit3% w/v stock label and provider30 g/L agree on stock strength; retain the separately stated 20 mL batch addition without assuming a receiving-litre denominator.","source_stage":"neutralized sulfide stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Na2S x 9 H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 84-86","quote":"Neutralized sulfide solution 3% (w/v) (from medium 28)\n   Na2S x 9 H2O                                             3.00        g\n   Distilled water                                        100.00       ml","quote_basis":"derivative text"},{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\": 54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"g\",\n                \"g_l\": 30,\n                \"mmol_l\": 124.905,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"2 M H2SO4","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The 2 M identifies sulfuric-acid titrant strength, not a quantified dose or main-medium concentration. Preserve the unquantified acid addition in sulfide-stock preparation.","source_stage":"sulfide pH titration","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\": \"2 M H2SO4\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001482\",\n          \"gmo_id\": \"GMO_001482\",\n          \"label\": \"Sulfuric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 88-92","quote":"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber\nseptum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and\nautoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to\nabout 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the\nbottle.","quote_basis":"derivative text"}]},{"quantity_id":"q32","label":"Na-resazurin solution (0.1% w/v)","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed volume, stock identity and any explicit w/v strength separately; do not infer ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Na-resazurin solution (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001453\",\n          \"gmo_id\": \"GMO_001453\",\n          \"label\": \"Sodium resazurin solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 9-9","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative text"}]},{"quantity_id":"q33","label":"Trace element solution SL-11","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed volume, stock identity and any explicit w/v strength separately; do not infer ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution SL-11\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2609\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 8-8","quote":"Trace element solution SL-11                             1.00        ml","quote_basis":"derivative text"}]},{"quantity_id":"q34","label":"Wolin's vitamin solution (10x)","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed volume, stock identity and any explicit w/v strength separately; do not infer ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Wolin's vitamin solution (10x)\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2609\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 12-12","quote":"Wolin's vitamin solution (10x)                           1.00        ml","quote_basis":"derivative text"}]},{"quantity_id":"q35","label":"Neutralized sulfide solution 3% (w/v)","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed volume, stock identity and any explicit w/v strength separately; do not infer ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"Neutralized sulfide solution 3% (w/v)\",\n          \"volume\": 20,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2609\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 13-13","quote":"Neutralized sulfide solution 3% (w/v)                   20.00        ml","quote_basis":"derivative text"}]},{"quantity_id":"q36","label":"solution5191 / Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[0].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\": \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"solution5191 / FeCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[1].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"solution5191 / ZnCl2","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[2].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"solution5191 / MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[3].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"solution5191 / H3BO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[4].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"solution5191 / CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[5].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"solution5191 / CuCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[6].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"solution5191 / NiCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[7].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[7]","quote":"{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"solution5191 / Na2MoO4 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[8].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[8]","quote":"{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"solution5191 / Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[9].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[9]","quote":"{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"solution5191 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The complete composition is present and independently sourced; the generic VARIABLE placeholder and incomplete-composition flag no longer describe missing recipe data. Retire only that redundant placeholder with append-only provenance, not the actual composition.","source_stage":"representation placeholder","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"$.data.recipe","quote":"\"recipe\": [","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"solution5980 / Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[0].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"solution5980 / Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[1].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\": 138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\": \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"solution5980 / Pyridoxine hydrochloride","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[2].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\": 519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"solution5980 / Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[3].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.148236,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"solution5980 / Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[4].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Riboflavin\",\n                \"compound_id\": 136,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"solution5980 / Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[5].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\": 6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\": 139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"solution5980 / Calcium D-(+)-pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[6].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\": 7,\n                \"compound\": \"Calcium D-(+)-pantothenate\",\n                \"compound_id\": 1512,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.209846,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"solution5980 / Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[7].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[7]","quote":"{\n                \"recipe_order\": 8,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\": 18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\": \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": 0.00073779,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q55","label":"solution5980 / p-Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[8].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[8]","quote":"{\n                \"recipe_order\": 9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\": 47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q56","label":"solution5980 / (DL)-alpha-Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[9].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[9]","quote":"{\n                \"recipe_order\": 10,\n                \"compound\": \"(DL)-alpha-Lipoic acid\",\n                \"compound_id\": 252,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\": \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q57","label":"solution5980 / Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[10].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The existing attached literal excerpt and exact historical digest match the current provider response. Retain the declared provider stock rate, or the supported1 L water input. This verifies that provider-specific assertion, not equivalence to another stock or its receiving-medium concentration.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[10]","quote":"{\n                \"recipe_order\": 11,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q58","label":"solution34 / Na2S x 9 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"composition[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The current source explicitly reports 30 g/L and3% w/v stock strength; attach exact evidence while retaining the source stock stage and original water input.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\": 54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"g\",\n                \"g_l\": 30,\n                \"mmol_l\": 124.905,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q59","label":"solution34 / Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"composition[1].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The source 100 mL water input is0.1 L;1000 PERCENT_V_V is not its meaning. Preserve an input volume, not final makeup.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q60","label":"solution34 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The complete composition is present and independently sourced; the generic VARIABLE placeholder and incomplete-composition flag no longer describe missing recipe data. Retire only that redundant placeholder with append-only provenance, not the actual composition.","source_stage":"representation placeholder","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"$.data.recipe","quote":"\"recipe\": [","quote_basis":"raw UTF-8"}]},{"quantity_id":"q61","label":"solution5191 preparation_notes","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"preparation_notes","stored":"Adjust pH to 6.0."}],"decision":"evidence_only","rationale":"Credit supported existing preparation and original stock-volume context. Numbers describe the stock, its vessel or process; they are not main-medium amounts or a measured receiving volume.","source_stage":"standalone stock metadata","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Adjust pH to 6.0.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q62","label":"solution34 preparation_notes","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"preparation_notes","stored":"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"Credit supported existing preparation and original stock-volume context. Numbers describe the stock, its vessel or process; they are not main-medium amounts or a measured receiving volume.","source_stage":"standalone stock metadata","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121\\u00b0C. After cooling to room temperature the pH is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q63","label":"Main gas, sterilization and final pH","local_fields":[],"decision":"evidence_only","rationale":"Preserve these exact source-only controls in their original scope. No dose is supplied for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth claim or override transfer to the unqualified target is inferred.","source_stage":"source-only preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 16-25","quote":"1. Dissolve ingredients except bicarbonate, yeast extract, vitamins and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type tubes or serum vials to 30% of their\nvolume and autoclave. Add yeast extract, vitamins (sterilized by filtration) and sulfide from\nsterile anoxic stock solutions prepared under 100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.\nNeutralize the sodium sulfide with sterile H2SO4 (see medium 29). After completing the\nmedium adjust pH to 6.8-7.0.\n2. Inoculated vessels are pressurized with sterile carbon monoxide gas to 2 bar\noverpressure.","quote_basis":"derivative text"}]},{"quantity_id":"q64","label":"SL-11 final makeup and titrant","local_fields":[],"decision":"evidence_only","rationale":"Preserve these exact source-only controls in their original scope. No dose is supplied for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth claim or override transfer to the unqualified target is inferred.","source_stage":"source-only preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q65","label":"Sulfide vessel, sterilization and titrant","local_fields":[],"decision":"evidence_only","rationale":"Preserve these exact source-only controls in their original scope. No dose is supplied for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth claim or override transfer to the unqualified target is inferred.","source_stage":"source-only preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 88-92","quote":"The sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber\nseptum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed and\nautoclaved for 15 min. at 121°C. After cooling to room temperature the pH is adjusted to\nabout 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe without opening the\nbottle.","quote_basis":"derivative text"}]},{"quantity_id":"q66","label":"Source-specific strain overrides","local_fields":[],"decision":"evidence_only","rationale":"Preserve these exact source-only controls in their original scope. No dose is supplied for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth claim or override transfer to the unqualified target is inferred.","source_stage":"source-only preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt lines 28-38","quote":"For DSM 12326: Supplement medium with 1.00 ml/l selenite-tungstate solution (see\nmedium 385).\nFor DSM 19011: Supplement medium with 0.20 g/l Na-lactate. Change gas phase to 100%\ncarbon monoxide prior to inoculation, but do not use excess pressure.\nFor DSM 21830: Adjust pH of complete medium to 6.0.\nFor DSM 22663: Supplement medium with 10.00 g/l sulfur and increase amount of yeast\nextract to 1.00 g/l. Sulfur is sterilized separately by steaming for 3 h on each of three\nsuccessive days.\nFor DSM 23698: Supplement medium with 2.00 g/l Na-pyruvate and omit sulfide. Adjust\nfinal pH of medium to 6.2. Change gas phase to 100% carbon monoxide prior to\ninoculation, but do not use excess pressure.","quote_basis":"derivative text"}]},{"quantity_id":"q67","label":"Provider declared volume","local_fields":[],"decision":"evidence_only","rationale":"The current API declares 1022 mL for its main solution. It is provider normalization, not an independently measured final volume and not permission to derive a new volume by summing every printed input.","source_stage":"provider normalization","sources":[{"evidence_id":"api507","reference":"https://mediadive.dsmz.de/rest/medium/507","raw_path":"REVIEW_WORK/batch059/source07-09/api507.raw","raw_sha256":"14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48","text_sha256":"14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48","accessed_at":"2026-10-28T06:51:39.443123Z","locator":"$.data.solutions[0].volume","quote":"\"volume\": 1022","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml":null,"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml":null,"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009176.

All actual CHEBI slots are joined to fresh exact non-obsolete OLS objects and the packaged current MIM rows. Nickel has a confirmed hexahydrate/anhydrous contradiction. EDTA dihydrate in the embedded recipe is distinguished from the unqualified5191 stock; its lack of hydrate wording is an uncertainty, not proof of anhydrous identity. Calcium D-pantothenate agrees with the D-configured 31345 object but lacks a selected secondary slot. Generic biotin does not independently establish stereochemistry; DL lipoic acid remains compatible with the non-stereospecific object. Provider compound IDs in all three exact stocks were joined to their actual recipe rows. No resazurin CHEBI slot is asserted in the selected empty solution descriptor.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:009176.

All nine exact historical reports and current histories, including the 5980 archived change objects, were read. Current 5191 and 5980 raw digests exactly match their original attached claims, authenticating the retained content without relabelling access dates. The historical 34 report has null g_l while current source explicitly reports 30; preserve that version difference. The corrected sidecar strips trailing locator annotations and rechecks all 23 historical objects. Prior5191/5980 water repairs and 5980 placeholder removal receive credit. Source 161 history snippets remain historical correspondence only; no new 161 recipe retrieval or validation is claimed. Current importer, migration and conservative merge behavior are evaluated only as present code. Twenty-one attached concentration snippets have both literal and exact-current-digest matches. The additional biotin claim citing medium161 remains outside current raw authentication.

## Findings

### f1: Source stock masses and addition volumes are encoded as main mass concentrations

major / open / confirmed; issue key: culturemech-009176-stock-units.

Both selected records flatten the trace, vitamin and sulfide stocks into main ingredients. Several source mg amounts are retained numerically as G_PER_L, and all four stock additions use G_PER_L despite being source mL volumes. Restore separate source stages, exact units and literal evidence. Main-batch masses themselves are supported, but their current per-litre denominator remains unverified. Current TOGO code already separates named sections; a historical flattening claim is not attributed to its current body.

### f2: Water inputs are summed across stages and one stock remains a percentage

major / open / confirmed; issue key: culturemech-009176-water-stages.

The selected 3100 G_PER_L combines four distinct solvent inputs. Restore their separate volumes. The linked sulfide stock still represents100 mL as 1000 PERCENT_V_V; correct that to the input-volume meaning. Credit the already repaired1 L water entries in 5191 and 5980. Only the embedded DSM SL-11 explicitly makes up to 1000 mL.

### f3: The linked SL-11 stock is not the printed recipe stock

major / open / confirmed; issue key: culturemech-009176-sl11-identity.

The target links provider solution 5191, whose authenticated source contains 6 g boric acid and unqualified Na2-EDTA. The TOGO and DSM507 embedded stock instead has 6 mg boric acid and EDTA dihydrate, with explicit final makeup; current API identifies that embedded stock as 1474. Resolve the target reference against the exact recipe. Do not overwrite the correctly evidenced 5191 provider formulation or transfer its 6 g boric-acid quantity into this medium.

### f4: Source preparation and pH are missing while titrants appear as main ingredients

major / open / confirmed; issue key: culturemech-009176-preparation.

Neither selected record preserves the staged gas handling, filtration, final pH or carbon-monoxide overpressure. Nitrogen,2 N NaOH and2 M sulfuric acid are flattened as main descriptors; their delivered amounts remain unquantified. Restore the exact source controls with distinct main, trace-stock and sulfide-stock scope, credit the existing standalone sulfide preparation, and retain named strain overrides separately. No unspecified autoclave time, titrant dose or growth association is added.

### f5: Nickel hexahydrate is asserted as anhydrous nickel dichloride

major / open / confirmed; issue key: culturemech-009176-nickel-hydrate.

The actual supplied hexahydrate conflicts with CHEBI:34887 in both selected primary/secondary slots and the linked 5191 chebi_term. CHEBI:53542 is the independently captured hexahydrate candidate. Correct only the actual asserted fields after form review; other source-form uncertainty is not converted into a wrong-ID claim.

### f6: Two complete linked stocks retain incomplete-composition placeholders

minor / open / confirmed; issue key: culturemech-009176-stale-placeholders.

The 5191 and34 stocks retain a generic ingredient placeholder and incomplete-composition flag despite populated, directly sourced composition. Retire those stale descriptors with append-only history; the prior 5980 placeholder cleanup receives credit. Reassess the target high-metal warning after correcting stock placement and units rather than declaring experimental toxicity.

### f7: A compatible calcium pantothenate primary lacks its secondary link

minor / open / confirmed; issue key: culturemech-009176-pantothenate-secondary.

CHEBI:31345 has the current D-configured object compatible with source calcium D-pantothenate. The selected descriptors lack their secondary MIM slot despite a current packaged row; assess that linkage separately from stock repair.

## Recommended Actions And Acceptance Checks

### a1

Both selected records flatten the trace, vitamin and sulfide stocks into main ingredients. Several source mg amounts are retained numerically as G_PER_L, and all four stock additions use G_PER_L despite being source mL volumes. Restore separate source stages, exact units and literal evidence. Main-batch masses themselves are supported, but their current per-litre denominator remains unverified. Current TOGO code already separates named sections; a historical flattening claim is not attributed to its current body.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The selected 3100 G_PER_L combines four distinct solvent inputs. Restore their separate volumes. The linked sulfide stock still represents100 mL as 1000 PERCENT_V_V; correct that to the input-volume meaning. Credit the already repaired1 L water entries in 5191 and 5980. Only the embedded DSM SL-11 explicitly makes up to 1000 mL.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The target links provider solution 5191, whose authenticated source contains 6 g boric acid and unqualified Na2-EDTA. The TOGO and DSM507 embedded stock instead has 6 mg boric acid and EDTA dihydrate, with explicit final makeup; current API identifies that embedded stock as 1474. Resolve the target reference against the exact recipe. Do not overwrite the correctly evidenced 5191 provider formulation or transfer its 6 g boric-acid quantity into this medium.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Neither selected record preserves the staged gas handling, filtration, final pH or carbon-monoxide overpressure. Nitrogen,2 N NaOH and2 M sulfuric acid are flattened as main descriptors; their delivered amounts remain unquantified. Restore the exact source controls with distinct main, trace-stock and sulfide-stock scope, credit the existing standalone sulfide preparation, and retain named strain overrides separately. No unspecified autoclave time, titrant dose or growth association is added.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The actual supplied hexahydrate conflicts with CHEBI:34887 in both selected primary/secondary slots and the linked 5191 chebi_term. CHEBI:53542 is the independently captured hexahydrate candidate. Correct only the actual asserted fields after form review; other source-form uncertainty is not converted into a wrong-ID claim.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

The 5191 and34 stocks retain a generic ingredient placeholder and incomplete-composition flag despite populated, directly sourced composition. Retire those stale descriptors with append-only history; the prior 5980 placeholder cleanup receives credit. Reassess the target high-metal warning after correcting stock placement and units rather than declaring experimental toxicity.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a7

CHEBI:31345 has the current D-configured object compatible with source calcium D-pantothenate. The selected descriptors lack their secondary MIM slot despite a current packaged row; assess that linkage separately from stock repair.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| togo2609Api | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609; REVIEW_WORK/batch059/source07-09/togo2609Api.json; exact original raw/text/hash/time metadata | context_only | Exact TOGO M2609 JSON route; earlier /api/medium/M2609 returned only the website shell and remains preserved as unusable recipe evidence. |
| dsm507 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf; REVIEW_WORK/batch059/source07-09/dsm507.json; exact original raw/text/hash/time metadata | context_only | Exact primary medium and its printed stock/preparation subsections; named strain variations remain separate and do not establish generic growth. |
| api507 | https://mediadive.dsmz.de/rest/medium/507; REVIEW_WORK/batch059/source07-09/api507.json; exact original raw/text/hash/time metadata | context_only | Exact current provider identity and declared amounts/basis; provider volume is not independently measured final volume. |
| solution5191 | https://mediadive.dsmz.de/rest/solution/5191; REVIEW_WORK/batch059/source07-09/solution5191.json; exact original raw/text/hash/time metadata | context_only | Exact asserted provider stock identity and stock-stage quantity support only; no receiving-medium normalization inferred. |
| solution5980 | https://mediadive.dsmz.de/rest/solution/5980; REVIEW_WORK/batch059/source07-09/solution5980.json; exact original raw/text/hash/time metadata | context_only | Exact asserted provider stock identity and stock-stage quantity support only; no receiving-medium normalization inferred. |
| solution34 | https://mediadive.dsmz.de/rest/solution/34; REVIEW_WORK/batch059/source07-09/solution34.json; exact original raw/text/hash/time metadata | context_only | Exact asserted provider stock identity and stock-stage quantity support only; no receiving-medium normalization inferred. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch059/source07-09/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch059/source07-09/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734; REVIEW_WORK/batch059/source07-09/chebi64734.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64758; REVIEW_WORK/batch059/source07-09/chebi64758.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch059/source07-09/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch059/source07-09/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch059/source07-09/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| target | data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/records/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_5980_Wolin_s_vitamin_solution_10x.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-29 | reports/yaml_record_review/20260922T034856Z-CARBOXYDOTHERMUS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| dep-sl | data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml; Complete file | context_only | Complete linked stock, including current composition, attached claims, preparation and history; source identity compared before any transfer. |
| dep-vit | data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml; Complete file | context_only | Complete linked stock, including current composition, attached claims, preparation and history; source identity compared before any transfer. |
| dep-sulfide | data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml; Complete file | context_only | Complete linked stock, including current composition, attached claims, preparation and history; source identity compared before any transfer. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit | context_only | Current parser reads only the primary recipe, separates referenced solutions and percentage/ml additions, and preserves their source attributes. It prefers explicit g_l but otherwise maps bare mass/volume units to per-litre schema units. This credits existing stage handling without certifying a source final volume or historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current duplicate cleanup collapses identical values but flags conflicting values without summing. Earlier sums require source-stage curation; do not rerun cleanup as a substitute for scientific reconciliation. |
| historical-reading | REVIEW_WORK/batch059/record08/historical-reading.json; Complete report cell pool and exact current-source object joins | context_only | Complete report text read through exact duplicate pooling; old conclusions separately assessed. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components, _solution_from_item, _parse_unit, _extract_ph, _extract_preparation_steps, _convert_to_culturemech | context_only | Current conversion separates named source sections, maps mass/volume units, preserves solution identity and comments, and reads pH from the top-level field. The fresh API puts pH inside meta. Existing flat records are not evidence that the current converter still deliberately flattens all sections. Bare-unit mapping does not establish final-volume denominators. |
| writer-migration | scripts/migrate_solutions_from_ingredients.py; _resolve_solution and ingredient migration loop | context_only | Current migration resolves solution names through a single-ID name dictionary and copies concentration unchanged. Name matching does not authenticate equivalent composition or receiving-volume basis; no historical execution is inferred. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch059/source07-09/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch059/source07-09/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch059/source07-09/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch059/source07-09/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch059/source07-09/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch059/source07-09/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch059/source07-09/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997; REVIEW_WORK/batch059/source07-09/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch059/source07-09/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch059/source07-09/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch059/source07-09/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch059/source07-09/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch059/source07-09/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch059/source07-09/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch059/source07-09/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch059/source07-09/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch059/source07-09/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch059/source07-09/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch059/source07-09/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch059/source07-09/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch059/source07-09/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch059/source07-09/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch059/source07-09/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact ontology ID/label/definition/formula; neither recipe amounts nor growth support. |
| quantities | REVIEW_WORK/batch059/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch059/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch059/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch059/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch059/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch059/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch059/record08/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch059/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch059/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch059/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch059/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Current canonical checks validate encoded structure/labels; zero reference checks do not verify external source claims.
- All primary PDF pages were read visually as well as in their complete extracted text. Current source status, retrieval times and complete raw/text bytes remain in the capture catalog.
- The initial guessed TOGO endpoint capture is preserved as an unusable HTML shell in the source catalog; only the exact documented API is used for formulation support.
- Current source5191 and embedded 1474 are deliberately not treated as interchangeable. No new standalone 1474 YAML is created or silently selected.
- The old report linked an additional October 9 applied-record report outside the native input set; that outside file is not assessed. The current inspected 5980 history and its exact retained claims are assessed.
- The 3% w/v sulfide and 0.1% w/v resazurin labels state mass/volume stock strengths. Gas percentages and vessel fill fraction are different dimensions and are not liquid concentrations.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T070432Z-culturemech-009176-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Carboxydothermus Medium'
started_at: '2026-10-28T06:51:16.968651Z'
finished_at: '2026-10-28T07:04:32.177575Z'
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
summary: The exact source separates stocks and solvent inputs that remain flattened
  or mis-unitized locally. Resolve the wrong SL-11 linkage, restore source preparation
  and claim evidence, correct nickel form, and credit the valid standalone stock repairs.
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
  - path: data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
    sha256: 1632fa0a66a2486b0d2e949943b4676f10461e8ee23e6c66651357e526312bfd
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    sha256: 8dddad4735138a6f4dcf90387b4eb555f7b6098a3def56465d433d36a17dca62
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml
    sha256: ca019e7b638322b2013234ff001f4908a14e210c1962889a65bd535fc6d50bc6
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    sha256: 815892ebecf9cc2d1aa27e305c6ff73f6ab4183707b143e17f7f7e5c7e09ff0e
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
    sha256: b8b5efd085ffa7d0f4e3da6ccf82c0de49b364082867d531beefa757fa3c5950
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/plan.json
    sha256: c1d7b6e777a4761b79c3781f469e9c0f12bad85d7972e397d35afe228bbf8078
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/records/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml.md
    sha256: 86aa18c8854ef299cb5fb25d4b35e49a195e84accb6a1a9081926461b3397b2c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/plan.json
    sha256: 8b48afea717d9dd21cbd91fa1d7dff8b329d3ba973435a466ec236b436b8240c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml.md
    sha256: e224029355c2393dbb43a16772f11795f987da334fa788450c4b2c28bbd31ee1
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_5980_Wolin_s_vitamin_solution_10x.md
    sha256: f2fe262502bc7b014e102df78f0d05196f15c28c02908757d89ab110de98be56
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.md
    sha256: 2bfe3bff31d14d1f4a63488af4fe9d16eff3f4b55380907a2bba2c0044c7faee
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.md
    sha256: f0e50819d7ba3631a8220183c65d43db5d099a4c97a7aacbfcd735fb10e43657
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.md
    sha256: 097e8314e5e88365722356178f176a3f9f194bb79b5208940cf1d9a58aaed1a4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.md
    sha256: c1b3a38110cb267d5c959d25a95890b1d2e60cab9789e5f329576a5df7444cfd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.md
    sha256: 22e4d09decbfb67f326989cc36b747521220cf6a03747698257efdd00c8609d4
    role: context
  - path: reports/yaml_record_review/20260922T034856Z-CARBOXYDOTHERMUS_MEDIUM.md
    sha256: db2e0b51b00e62d08febb64f9d664b85700f13e5d04f13545491fe8b8b496063
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
  - path: scripts/repair_komodo_507_carboxydothermus_score10.py
    sha256: d33ce935e5f4621b68f2e8c3e351b4d0ec7e63caccc73918d5e43a38d7161582
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
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
  selection: Authoritative batch059 index 08
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009176
targets:
- target_id: CultureMech:009176
  path: data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
  label: carboxydothermus_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
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
  - CultureMech:009176
  command: just validate-schema data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
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
  - CultureMech:009176
  command: just validate-strict data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
    --out REVIEW_WORK/batch059/record08/strict.tsv --workers 1 --quiet
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
  - CultureMech:009176
  command: just validate-terms data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
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
  - CultureMech:009176
  command: just validate-references data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: togo2609Api
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609
  accessed_at: '2026-10-28T06:52:29.071094Z'
  locator: REVIEW_WORK/batch059/source07-09/togo2609Api.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact TOGO M2609 JSON route; earlier /api/medium/M2609 returned only the
    website shell and remains preserved as unusable recipe evidence.
  snapshot_sha256: 6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62
- evidence_id: dsm507
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf
  accessed_at: '2026-10-28T06:51:39.624958Z'
  locator: REVIEW_WORK/batch059/source07-09/dsm507.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact primary medium and its printed stock/preparation subsections; named
    strain variations remain separate and do not establish generic growth.
  snapshot_sha256: 47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4
- evidence_id: api507
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/507
  accessed_at: '2026-10-28T06:51:39.443123Z'
  locator: REVIEW_WORK/batch059/source07-09/api507.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current provider identity and declared amounts/basis; provider volume
    is not independently measured final volume.
  snapshot_sha256: 14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48
- evidence_id: solution5191
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5191
  accessed_at: '2026-10-28T06:51:40.289160Z'
  locator: REVIEW_WORK/batch059/source07-09/solution5191.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact asserted provider stock identity and stock-stage quantity support
    only; no receiving-medium normalization inferred.
  snapshot_sha256: a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0
- evidence_id: solution5980
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5980
  accessed_at: '2026-10-28T06:51:40.279623Z'
  locator: REVIEW_WORK/batch059/source07-09/solution5980.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact asserted provider stock identity and stock-stage quantity support
    only; no receiving-medium normalization inferred.
  snapshot_sha256: 2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c
- evidence_id: solution34
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/34
  accessed_at: '2026-10-28T06:51:40.279771Z'
  locator: REVIEW_WORK/batch059/source07-09/solution34.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact asserted provider stock identity and stock-stage quantity support
    only; no receiving-medium normalization inferred.
  snapshot_sha256: 33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T06:51:42.869820Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T06:51:43.468678Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734
  accessed_at: '2026-10-28T06:51:43.579559Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi64734.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 4afcce140f81023fe7e21d1081a51e76eb83b0d89e158079ef5be695df2388ec
- evidence_id: chebi64758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64758
  accessed_at: '2026-10-28T06:51:43.812472Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi64758.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 326b128326745296132512f9e618ef60c9c3230252a9dac3a75db92f8caa3156
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T06:51:42.245938Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T06:51:41.086967Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T06:51:40.953073Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi16494.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:03:19.287729Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 1632fa0a66a2486b0d2e949943b4676f10461e8ee23e6c66651357e526312bfd
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:03:19.287902Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 8dddad4735138a6f4dcf90387b4eb555f7b6098a3def56465d433d36a17dca62
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T07:03:19.287934Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T07:03:19.288268Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T07:03:19.288293Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T07:03:19.288317Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T07:03:19.288348Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: c1d7b6e777a4761b79c3781f469e9c0f12bad85d7972e397d35afe228bbf8078
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-0000-0500/records/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.290273Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 86aa18c8854ef299cb5fb25d4b35e49a195e84accb6a1a9081926461b3397b2c
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T07:03:19.290307Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 8b48afea717d9dd21cbd91fa1d7dff8b329d3ba973435a466ec236b436b8240c
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3500-4000/records/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292788Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: e224029355c2393dbb43a16772f11795f987da334fa788450c4b2c28bbd31ee1
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-stocks/mediadive_5980_Wolin_s_vitamin_solution_10x.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292826Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f2fe262502bc7b014e102df78f0d05196f15c28c02908757d89ab110de98be56
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292855Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2bfe3bff31d14d1f4a63488af4fe9d16eff3f4b55380907a2bba2c0044c7faee
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292884Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: f0e50819d7ba3631a8220183c65d43db5d099a4c97a7aacbfcd735fb10e43657
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292910Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 097e8314e5e88365722356178f176a3f9f194bb79b5208940cf1d9a58aaed1a4
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292932Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: c1b3a38110cb267d5c959d25a95890b1d2e60cab9789e5f329576a5df7444cfd
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292956Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 22e4d09decbfb67f326989cc36b747521220cf6a03747698257efdd00c8609d4
- evidence_id: report-29
  kind: prior_review
  reference: reports/yaml_record_review/20260922T034856Z-CARBOXYDOTHERMUS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T07:03:19.292977Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: db2e0b51b00e62d08febb64f9d664b85700f13e5d04f13545491fe8b8b496063
- evidence_id: dep-sl
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:03:19.299388Z'
  support: context_only
  summary: Complete linked stock, including current composition, attached claims,
    preparation and history; source identity compared before any transfer.
  snapshot_sha256: 815892ebecf9cc2d1aa27e305c6ff73f6ab4183707b143e17f7f7e5c7e09ff0e
- evidence_id: dep-vit
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:03:19.318264Z'
  support: context_only
  summary: Complete linked stock, including current composition, attached claims,
    preparation and history; source identity compared before any transfer.
  snapshot_sha256: b8b5efd085ffa7d0f4e3da6ccf82c0de49b364082867d531beefa757fa3c5950
- evidence_id: dep-sulfide
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml
  locator: Complete file
  accessed_at: '2026-10-28T07:03:19.319655Z'
  support: context_only
  summary: Complete linked stock, including current composition, attached claims,
    preparation and history; source identity compared before any transfer.
  snapshot_sha256: ca019e7b638322b2013234ff001f4908a14e210c1962889a65bd535fc6d50bc6
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _parse_api_solutions, _normalize_unit
  accessed_at: '2026-10-28T07:03:19.319685Z'
  support: context_only
  summary: Current parser reads only the primary recipe, separates referenced solutions
    and percentage/ml additions, and preserves their source attributes. It prefers
    explicit g_l but otherwise maps bare mass/volume units to per-litre schema units.
    This credits existing stage handling without certifying a source final volume
    or historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T07:03:19.319723Z'
  support: context_only
  summary: Current duplicate cleanup collapses identical values but flags conflicting
    values without summing. Earlier sums require source-stage curation; do not rerun
    cleanup as a substitute for scientific reconciliation.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: historical-reading
  kind: prior_review
  reference: REVIEW_WORK/batch059/record08/historical-reading.json
  locator: Complete report cell pool and exact current-source object joins
  accessed_at: '2026-10-28T07:03:19.369987Z'
  support: context_only
  summary: Complete report text read through exact duplicate pooling; old conclusions
    separately assessed.
  snapshot_sha256: ad7be9aacbe9cbedbd834ece28eed75b753f2ae164eb4ae0de25b6ad7c44ee22
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components, _solution_from_item, _parse_unit, _extract_ph,
    _extract_preparation_steps, _convert_to_culturemech
  accessed_at: '2026-10-28T07:03:19.370950Z'
  support: context_only
  summary: Current conversion separates named source sections, maps mass/volume units,
    preserves solution identity and comments, and reads pH from the top-level field.
    The fresh API puts pH inside meta. Existing flat records are not evidence that
    the current converter still deliberately flattens all sections. Bare-unit mapping
    does not establish final-volume denominators.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-migration
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _resolve_solution and ingredient migration loop
  accessed_at: '2026-10-28T07:03:19.370999Z'
  support: context_only
  summary: Current migration resolves solution names through a single-ID name dictionary
    and copies concentration unchanged. Name matching does not authenticate equivalent
    composition or receiving-volume basis; no historical execution is inferred.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T06:51:40.810661Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T06:51:44.192971Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T06:51:43.517218Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T06:51:42.216507Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T06:51:44.702578Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T06:51:42.616651Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi32588.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T06:51:42.273272Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi32139.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997
  accessed_at: '2026-10-28T06:51:41.658654Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: c4f240d59927c0f5c6c8d29c14830d0f278cfeabc4ed924be5c2b6bbe1039c05
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T06:51:44.103080Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T06:51:42.837479Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T06:51:44.859904Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T06:51:43.468865Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T06:51:44.725430Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T06:51:42.935053Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T06:51:44.403128Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi86249.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T06:51:41.732561Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T06:51:42.911648Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T06:51:42.015654Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T06:51:41.647007Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T06:51:41.413603Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T06:51:41.015362Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T06:51:40.977277Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T06:51:44.118684Z'
  locator: REVIEW_WORK/batch059/source07-09/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ontology ID/label/definition/formula; neither recipe amounts nor
    growth support.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch059/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:04:32.177569Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 3c55b24498b7d1970f3935257dd94b217aebf7080e8db694dd1b6ab90cfd1368
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch059/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:03:19.524429Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 9123352eb3a9934f5fb3d8900e4a40d781ebcceae40bc4e59bf60f18906dafc9
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch059/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:03:19.524612Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 951440b63015b00d7fcc09a61528a47ddd84a561fb7ab1557c891169ca00195b
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch059/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:03:19.524757Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 705e2abcdcd721c0071cd8403cadcf21206d966a9fb4d4fd7d8723861ff637b7
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch059/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:03:19.524880Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: f9dea4fdeda6d815d011a7ab4fc5d93b7576c7d2f66c66e0bb91d043183fd031
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch059/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:03:19.524930Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 312638a1e692b51a5a54944eed8920413ea6ccd7fe767492578b6e6702cd74fd
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch059/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T07:03:19.524959Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: d2eeef09824e4f20cd0dc628b9fcc738109183529e2b0b685753f31f6eb41ea6
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch059/record08/schema-result.json
  accessed_at: '2026-10-28T06:51:17.999179Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 9687acb8859ffc7eee3d851b969c49c0c362dc5b82593875137f472298929730
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch059/record08/strict-result.json
  accessed_at: '2026-10-28T06:51:18.926335Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 1c9b14d97dc3ff89f809ff89efe330c31d96531433b07e0d6c15e47b558982de
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch059/record08/terms-result.json
  accessed_at: '2026-10-28T06:51:19.935360Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 3500ad44c168e33421aab6bab1143da3ccdaac3a189928ba613092fc90de1ac6
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch059/record08/references-result.json
  accessed_at: '2026-10-28T06:51:20.676452Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 53e96947b68dd86fc8abe4380417a1747f88b230eaccfffedaf3e258cdb1158a
assessments:
- assessment_id: identity
  area: identity
  topic: Exact TOGO source and linked stock identities
  outcome: concern
  summary: The target and owner match M2609 and the full current TOGO API identifies
    DSM507. The initial guessed endpoint returned an HTML application shell and is
    not recipe evidence. The exact linked 5191 is authenticated as its own stock but
    conflicts with the recipe;5980 and34 are separately assessed.
  target_ids:
  - CultureMech:009176
  evidence_ids:
  - togo2609Api
  - dsm507
  - solution5191
  - solution5980
  - solution34
  - target
  - owner
- assessment_id: classification
  area: representation
  topic: Classification and source-specific controls
  outcome: supported
  summary: The complex semi-defined liquid classification is compatible with the source
    yeast extract and chemical components. The record name and source variant notes
    do not establish any organism-growth claim.
  target_ids:
  - CultureMech:009176
  evidence_ids:
  - togo2609Api
  - dsm507
  - target
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 95 current concentration fields are covered by 67 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009176
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b059-quantity-inventory-v1","target":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","quantity_field_count":95,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3100.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3100.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    encoded 3100 g/L sums water inputs from four different preparation stages. Retain
    1000 mL main water,1000 mL trace-stock water,1000 mL vitamin-stock water and 100
    mL sulfide-stock water separately as volumes. SL-11 explicitly makes up to 1000
    mL; the other water entries do not themselves prove final volumes.","source_stage":"four
    separate solvent inputs","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"Yeast
    extract","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed amount is a supported main-batch mass, but the existing G_PER_L requires
    a denominator not established by 1000 mL water input alone. The separate API uses
    declared1022 mL normalization; do not silently replace one interpretation with
    the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 11-11","quote":"Yeast extract                                            0.05         g","quote_basis":"derivative
    text"}]},{"quantity_id":"q3","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.29","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed amount is a supported main-batch mass, but the existing G_PER_L requires
    a denominator not established by 1000 mL water input alone. The separate API uses
    declared1022 mL normalization; do not silently replace one interpretation with
    the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"CaCl2 x 2 H2O\",\n          \"volume\": 0.29,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 5-5","quote":"CaCl2 x 2 H2O                                            0.29         g","quote_basis":"derivative
    text"}]},{"quantity_id":"q4","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed amount is a supported main-batch mass, but the existing G_PER_L requires
    a denominator not established by 1000 mL water input alone. The separate API uses
    declared1022 mL normalization; do not silently replace one interpretation with
    the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 7-7","quote":"KH2PO4                                                   0.33         g","quote_basis":"derivative
    text"}]},{"quantity_id":"q5","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed amount is a supported main-batch mass, but the existing G_PER_L requires
    a denominator not established by 1000 mL water input alone. The separate API uses
    declared1022 mL normalization; do not silently replace one interpretation with
    the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 6-6","quote":"NH4Cl                                                    0.33         g","quote_basis":"derivative
    text"}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.52","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.52","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed amount is a supported main-batch mass, but the existing G_PER_L requires
    a denominator not established by 1000 mL water input alone. The separate API uses
    declared1022 mL normalization; do not silently replace one interpretation with
    the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"MgCl2 x 6 H2O\",\n          \"volume\": 0.52,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 4-4","quote":"MgCl2 x 6 H2O                                            0.52         g","quote_basis":"derivative
    text"}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed amount is a supported main-batch mass, but the existing G_PER_L requires
    a denominator not established by 1000 mL water input alone. The separate API uses
    declared1022 mL normalization; do not silently replace one interpretation with
    the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\":
    \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 3-3","quote":"KCl                                                      0.33         g","quote_basis":"derivative
    text"}]},{"quantity_id":"q8","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    printed amount is a supported main-batch mass, but the existing G_PER_L requires
    a denominator not established by 1000 mL water input alone. The separate API uses
    declared1022 mL normalization; do not silently replace one interpretation with
    the other.","source_stage":"main batch mass","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"NaHCO3\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\":
    \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 10-10","quote":"NaHCO3                                                   1.00         g","quote_basis":"derivative
    text"}]},{"quantity_id":"q9","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Keep
    the delivered gas amount unquantified. 100% identifies the nitrogen atmosphere,
    not a liquid ingredient concentration; re-scope this descriptor to preparation
    without inventing a gas dose.","source_stage":"preparation gas","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"conc_value\": 100,\n          \"conc_unit\": \"%\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\":
    \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\":
    \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 16-23","quote":"1. Dissolve ingredients except bicarbonate, yeast extract,
    vitamins and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to
    make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials to 30% of their\nvolume and autoclave. Add yeast extract,
    vitamins (sterilized by filtration) and sulfide from\nsterile anoxic stock solutions
    prepared under 100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock
    solution prepared under 80% N2 and 20% CO2 gas mixture.\nNeutralize the sodium
    sulfide with sterile H2SO4 (see medium 29). After completing the\nmedium adjust
    pH to 6.8-7.0.","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"36","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"36","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"Na2MoO4 x 2 H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 60-60","quote":"Na2MoO4 x 2 H2O                                         36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q11","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 56-56","quote":"H3BO3                                                    6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q12","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"MnCl2 x 4 H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\":
    \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 55-55","quote":"MnCl2 x 4 H2O                                          100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q13","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"190","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"CoCl2 x 6 H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 57-57","quote":"CoCl2 x 6 H2O                                          190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q14","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
    \"NiCl2 x 6 H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\":
    \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 59-59","quote":"NiCl2 x 6 H2O                                           24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q15","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
    \"CuCl2 x 2 H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\":
    \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 58-58","quote":"CuCl2 x 2 H2O                                            2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q16","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"70","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"70","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 54-54","quote":"ZnCl2                                                   70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q17","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
    \"FeCl2 x 4 H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\":
    \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 45-45","quote":"FeCl2 x 4 H2O                                             1.50        g","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"Na2-EDTA x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    belongs to the embedded SL-11 stock, not the main ingredients. Preserve the exact
    printed mass and hydrate; convert mg to g only within this explicit 1000 mL final-stock
    makeup. The independently linked 5191 provider stock is not compositionally equivalent
    and must not be silently substituted.","source_stage":"embedded SL-11 stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
    \"Na2-EDTA x 2 H2O\",\n          \"volume\": 5.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001148\",\n          \"gmo_id\": \"GMO_001148\",\n          \"label\":
    \"Disodium EDTA dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 44-44","quote":"Na2-EDTA x 2 H2O                                          5.20        g","quote_basis":"derivative
    text"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q19","label":"2 N NaOH","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    2 N identifies titrant strength, while the amount added to adjust SL-11 pH is
    unquantified. Preserve that distinction and move it from main ingredients into
    the stock preparation.","source_stage":"SL-11 pH titration","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
    \"2 N NaOH\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"N\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\":
    \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q20","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\":
    \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 70-70","quote":"Biotin                                                  20.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q21","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 78-78","quote":"p-Aminobenzoic acid                                     50.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q22","label":"Thiamine-HCl","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"Thiamine-HCl\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 73-73","quote":"Thiamine HCl                                            50.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q23","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"Pyridoxine hydrochloride\",\n          \"volume\": 100,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\":
    \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 72-72","quote":"Pyridoxine hydrochloride                               100.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q24","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\":
    \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 71-71","quote":"Folic acid                                              20.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q25","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 77-77","quote":"Vitamin B12                                              1.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q26","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\":
    \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 74-74","quote":"Riboflavin                                              50.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q27","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 75-75","quote":"Nicotinic acid                                          50.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q28","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\":
    \"(DL)-alpha-Lipoic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\":
    \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 79-79","quote":"(DL)-alpha-Lipoic acid                                  50.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q29","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source prints this mass in mg in the vitamin stock, whereas the selected records
    put the same number in main-medium G_PER_L. Restore the stock stage and source
    mass/unit; current solution 5980 separately declares stock g_l. Its1000 mL water
    input does not independently establish measured final volume.","source_stage":"Wolin
    vitamin stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\":
    \"Calcium D-(+)-pantothenate\",\n          \"volume\": 50,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001940\",\n          \"gmo_id\":
    \"GMO_001940\",\n          \"label\": \"D-Calcium pantothenate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\":
    \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 76-76","quote":"Calcium D-(+)-pantothenate                              50.00      mg","quote_basis":"derivative
    text"}]},{"quantity_id":"q30","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    3 g sodium sulfide nonahydrate is a stock-preparation mass, not 3 g/L of receiving
    medium. The explicit3% w/v stock label and provider30 g/L agree on stock strength;
    retain the separately stated 20 mL batch addition without assuming a receiving-litre
    denominator.","source_stage":"neutralized sulfide stock","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
    \"Na2S x 9 H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\":
    \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 84-86","quote":"Neutralized sulfide solution 3% (w/v) (from medium 28)\n   Na2S
    x 9 H2O                                             3.00        g\n   Distilled
    water                                        100.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\":
    54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\":
    \"g\",\n                \"g_l\": 30,\n                \"mmol_l\": 124.905,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"2
    M H2SO4","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    2 M identifies sulfuric-acid titrant strength, not a quantified dose or main-medium
    concentration. Preserve the unquantified acid addition in sulfide-stock preparation.","source_stage":"sulfide
    pH titration","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\":
    \"2 M H2SO4\",\n          \"conc_value\": 2,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001482\",\n          \"gmo_id\": \"GMO_001482\",\n          \"label\":
    \"Sulfuric acid solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 88-92","quote":"The sulfide solution is prepared in a 250 ml screw-capped
    bottle with a butyl rubber\nseptum and a magnetic stirrer. The solution is bubbled
    with nitrogen gas, closed and\nautoclaved for 15 min. at 121°C. After cooling
    to room temperature the pH is adjusted to\nabout 7.0 by adding of sterile 2 M
    H2SO4 drop-wise with a syringe without opening the\nbottle.","quote_basis":"derivative
    text"}]},{"quantity_id":"q32","label":"Na-resazurin solution (0.1% w/v)","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed
    volume, stock identity and any explicit w/v strength separately; do not infer
    ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Na-resazurin solution (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001453\",\n          \"gmo_id\": \"GMO_001453\",\n          \"label\":
    \"Sodium resazurin solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent
    redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 9-9","quote":"Sodium resazurin (0.1% w/v)                              0.50        ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q33","label":"Trace element solution SL-11","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed
    volume, stock identity and any explicit w/v strength separately; do not infer
    ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution SL-11\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M2609\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 8-8","quote":"Trace element solution SL-11                             1.00        ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q34","label":"Wolin''s vitamin solution (10x)","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed
    volume, stock identity and any explicit w/v strength separately; do not infer
    ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Wolin''s vitamin solution (10x)\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M2609\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 12-12","quote":"Wolin''s vitamin solution (10x)                           1.00        ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q35","label":"Neutralized sulfide solution 3% (w/v)","local_fields":[{"path":"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a batch volume in mL, not the encoded G_PER_L. Preserve the printed
    volume, stock identity and any explicit w/v strength separately; do not infer
    ML_PER_L from water input alone.","source_stage":"stock addition to main batch","sources":[{"evidence_id":"togo2609Api","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2609","raw_path":"REVIEW_WORK/batch059/source07-09/togo2609Api.raw","raw_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","text_sha256":"6d602132f9c4cf0d3dd2f61401dfdd1226c77cb42e3f8d6b06403e77b1ed5f62","accessed_at":"2026-10-28T06:52:29.071094Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"Neutralized sulfide solution 3% (w/v)\",\n          \"volume\": 20,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M2609\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 13-13","quote":"Neutralized sulfide solution 3% (w/v)                   20.00        ml","quote_basis":"derivative
    text"}]},{"quantity_id":"q36","label":"solution5191 / Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[0].concentration","stored":{"value":"5.2","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\":
    34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5.2,\n                \"unit\":
    \"g\",\n                \"g_l\": 5.2,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"solution5191
    / FeCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[1].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\":
    260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"solution5191
    / ZnCl2","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[2].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\":
    64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"solution5191
    / MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[3].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"solution5191
    / H3BO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[4].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"g\",\n                \"g_l\": 6,\n                \"mmol_l\": 97.0246,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"solution5191
    / CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[5].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"solution5191
    / CuCl2 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[6].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\":
    7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\":
    39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"solution5191
    / NiCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[7].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[7]","quote":"{\n                \"recipe_order\":
    8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\":
    40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"solution5191
    / Na2MoO4 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[8].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[8]","quote":"{\n                \"recipe_order\":
    9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"solution5191
    / Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"composition[9].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.recipe[9]","quote":"{\n                \"recipe_order\":
    10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"solution5191
    placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The
    complete composition is present and independently sourced; the generic VARIABLE
    placeholder and incomplete-composition flag no longer describe missing recipe
    data. Retire only that redundant placeholder with append-only provenance, not
    the actual composition.","source_stage":"representation placeholder","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"$.data.recipe","quote":"\"recipe\":
    [","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"solution5980 / Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[0].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0818632,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"solution5980
    / Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[1].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Folic acid\",\n                \"compound_id\":
    138,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 20,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.02,\n                \"mmol_l\": 0.0453104,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"solution5980
    / Pyridoxine hydrochloride","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[2].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Pyridoxine hydrochloride\",\n                \"compound_id\":
    519,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.486287,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"solution5980
    / Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[3].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.148236,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"solution5980
    / Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[4].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Riboflavin\",\n                \"compound_id\":
    136,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.132837,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"solution5980
    / Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[5].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"Nicotinic acid\",\n                \"compound_id\":
    139,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.406141,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"solution5980
    / Calcium D-(+)-pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[6].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\":
    7,\n                \"compound\": \"Calcium D-(+)-pantothenate\",\n                \"compound_id\":
    1512,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.209846,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q54","label":"solution5980
    / Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[7].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[7]","quote":"{\n                \"recipe_order\":
    8,\n                \"compound\": \"Vitamin B12\",\n                \"compound_id\":
    18,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.001,\n                \"mmol_l\": 0.00073779,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q55","label":"solution5980
    / p-Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[8].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[8]","quote":"{\n                \"recipe_order\":
    9,\n                \"compound\": \"p-Aminobenzoic acid\",\n                \"compound_id\":
    47,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.364591,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q56","label":"solution5980
    / (DL)-alpha-Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[9].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[9]","quote":"{\n                \"recipe_order\":
    10,\n                \"compound\": \"(DL)-alpha-Lipoic acid\",\n                \"compound_id\":
    252,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 50,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.05,\n                \"mmol_l\": 0.24233,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q57","label":"solution5980
    / Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml","field_path":"composition[10].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"The
    existing attached literal excerpt and exact historical digest match the current
    provider response. Retain the declared provider stock rate, or the supported1
    L water input. This verifies that provider-specific assertion, not equivalence
    to another stock or its receiving-medium concentration.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution5980","reference":"https://mediadive.dsmz.de/rest/solution/5980","raw_path":"REVIEW_WORK/batch059/source07-09/solution5980.raw","raw_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","text_sha256":"2fe24a83c789ebc28eb97268a788cabd1316ae131baaea269df79019a14f992c","accessed_at":"2026-10-28T06:51:40.279623Z","locator":"data.recipe[10]","quote":"{\n                \"recipe_order\":
    11,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q58","label":"solution34
    / Na2S x 9 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"composition[0].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    current source explicitly reports 30 g/L and3% w/v stock strength; attach exact
    evidence while retaining the source stock stage and original water input.","source_stage":"standalone
    provider stock","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\":
    54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\":
    \"g\",\n                \"g_l\": 30,\n                \"mmol_l\": 124.905,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q59","label":"solution34
    / Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"composition[1].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The
    source 100 mL water input is0.1 L;1000 PERCENT_V_V is not its meaning. Preserve
    an input volume, not final makeup.","source_stage":"standalone provider stock","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q60","label":"solution34
    placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The
    complete composition is present and independently sourced; the generic VARIABLE
    placeholder and incomplete-composition flag no longer describe missing recipe
    data. Retire only that redundant placeholder with append-only provenance, not
    the actual composition.","source_stage":"representation placeholder","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"$.data.recipe","quote":"\"recipe\":
    [","quote_basis":"raw UTF-8"}]},{"quantity_id":"q61","label":"solution5191 preparation_notes","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml","field_path":"preparation_notes","stored":"Adjust
    pH to 6.0."}],"decision":"evidence_only","rationale":"Credit supported existing
    preparation and original stock-volume context. Numbers describe the stock, its
    vessel or process; they are not main-medium amounts or a measured receiving volume.","source_stage":"standalone
    stock metadata","sources":[{"evidence_id":"solution5191","reference":"https://mediadive.dsmz.de/rest/solution/5191","raw_path":"REVIEW_WORK/batch059/source07-09/solution5191.raw","raw_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","text_sha256":"a73424d1a717b3254fb032150130d22c0a664eee607ba102824f7ac3996f90a0","accessed_at":"2026-10-28T06:51:40.289160Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Adjust pH to 6.0.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q62","label":"solution34 preparation_notes","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml","field_path":"preparation_notes","stored":"The
    sulfide solution is prepared in a 250 ml screw-capped bottle with a butyl rubber
    septum and a magnetic stirrer. The solution is bubbled with nitrogen gas, closed
    and autoclaved for 15 min. at 121°C. After cooling to room temperature the pH
    is adjusted to about 7.0 by adding of sterile 2 M H2SO4 drop-wise with a syringe
    without opening the bottle.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"Credit
    supported existing preparation and original stock-volume context. Numbers describe
    the stock, its vessel or process; they are not main-medium amounts or a measured
    receiving volume.","source_stage":"standalone stock metadata","sources":[{"evidence_id":"solution34","reference":"https://mediadive.dsmz.de/rest/solution/34","raw_path":"REVIEW_WORK/batch059/source07-09/solution34.raw","raw_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","text_sha256":"33aab3917e55872514b7dd527ff05bfa4cb65d4b77da12b8118bcf69f285cd93","accessed_at":"2026-10-28T06:51:40.279771Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"The sulfide solution is prepared in a 250 ml
    screw-capped bottle with a butyl rubber septum and a magnetic stirrer. The solution
    is bubbled with nitrogen gas, closed and autoclaved for 15 min. at 121\\u00b0C.
    After cooling to room temperature the pH is adjusted to about 7.0 by adding of
    sterile 2 M H2SO4 drop-wise with a syringe without opening the bottle.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q63","label":"Main gas, sterilization and final pH","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    these exact source-only controls in their original scope. No dose is supplied
    for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth
    claim or override transfer to the unqualified target is inferred.","source_stage":"source-only
    preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 16-25","quote":"1. Dissolve ingredients except bicarbonate, yeast extract,
    vitamins and sulfide, then\nsparge medium with 100% N2 gas for 30 - 45 min to
    make it anoxic. Dispense medium\nunder same gas atmosphere into anoxic Hungate-type
    tubes or serum vials to 30% of their\nvolume and autoclave. Add yeast extract,
    vitamins (sterilized by filtration) and sulfide from\nsterile anoxic stock solutions
    prepared under 100% N2 gas atmosphere and bicarbonate\nfrom a sterile anoxic stock
    solution prepared under 80% N2 and 20% CO2 gas mixture.\nNeutralize the sodium
    sulfide with sterile H2SO4 (see medium 29). After completing the\nmedium adjust
    pH to 6.8-7.0.\n2. Inoculated vessels are pressurized with sterile carbon monoxide
    gas to 2 bar\noverpressure.","quote_basis":"derivative text"}]},{"quantity_id":"q64","label":"SL-11
    final makeup and titrant","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    these exact source-only controls in their original scope. No dose is supplied
    for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth
    claim or override transfer to the unqualified target is inferred.","source_stage":"source-only
    preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 63-65","quote":"Dissolve EDTA in 800 ml distilled water, adjust pH to 7
    using 2 N NaOH and add ferrous\nchloride. After ferrous chloride has dissolved
    add other compounds. Finally adjust pH to 6.0\nand bring volume to 1000 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q65","label":"Sulfide vessel, sterilization and titrant","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    these exact source-only controls in their original scope. No dose is supplied
    for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth
    claim or override transfer to the unqualified target is inferred.","source_stage":"source-only
    preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 88-92","quote":"The sulfide solution is prepared in a 250 ml screw-capped
    bottle with a butyl rubber\nseptum and a magnetic stirrer. The solution is bubbled
    with nitrogen gas, closed and\nautoclaved for 15 min. at 121°C. After cooling
    to room temperature the pH is adjusted to\nabout 7.0 by adding of sterile 2 M
    H2SO4 drop-wise with a syringe without opening the\nbottle.","quote_basis":"derivative
    text"}]},{"quantity_id":"q66","label":"Source-specific strain overrides","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    these exact source-only controls in their original scope. No dose is supplied
    for pH titrants. The base recipe and named strain overrides are distinct; no organism-growth
    claim or override transfer to the unqualified target is inferred.","source_stage":"source-only
    preparation/variant scope","sources":[{"evidence_id":"dsm507","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium507.pdf","raw_path":"REVIEW_WORK/batch059/source07-09/dsm507.raw","raw_sha256":"47846e07593b3c276652aaa3c6cd4936af8a55a53bb3fdaeaf9201b28a3acee4","text_sha256":"57c3837279b9fc31f941c69687d227c3e4b840e94adc49a002f023334d8865b7","accessed_at":"2026-10-28T06:51:39.624958Z","locator":"dsm507.txt
    lines 28-38","quote":"For DSM 12326: Supplement medium with 1.00 ml/l selenite-tungstate
    solution (see\nmedium 385).\nFor DSM 19011: Supplement medium with 0.20 g/l Na-lactate.
    Change gas phase to 100%\ncarbon monoxide prior to inoculation, but do not use
    excess pressure.\nFor DSM 21830: Adjust pH of complete medium to 6.0.\nFor DSM
    22663: Supplement medium with 10.00 g/l sulfur and increase amount of yeast\nextract
    to 1.00 g/l. Sulfur is sterilized separately by steaming for 3 h on each of three\nsuccessive
    days.\nFor DSM 23698: Supplement medium with 2.00 g/l Na-pyruvate and omit sulfide.
    Adjust\nfinal pH of medium to 6.2. Change gas phase to 100% carbon monoxide prior
    to\ninoculation, but do not use excess pressure.","quote_basis":"derivative text"}]},{"quantity_id":"q67","label":"Provider
    declared volume","local_fields":[],"decision":"evidence_only","rationale":"The
    current API declares 1022 mL for its main solution. It is provider normalization,
    not an independently measured final volume and not permission to derive a new
    volume by summing every printed input.","source_stage":"provider normalization","sources":[{"evidence_id":"api507","reference":"https://mediadive.dsmz.de/rest/medium/507","raw_path":"REVIEW_WORK/batch059/source07-09/api507.raw","raw_sha256":"14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48","text_sha256":"14e751ef4c3a1bdc5f4815b520f2cf050e5ff7c461148d10cd7cccbfa93d4e48","accessed_at":"2026-10-28T06:51:39.443123Z","locator":"$.data.solutions[0].volume","quote":"\"volume\":
    1022","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CARBOXYDOTHERMUS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml":null,"data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml":null,"data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All actual CHEBI slots are joined to fresh exact non-obsolete OLS objects
    and the packaged current MIM rows. Nickel has a confirmed hexahydrate/anhydrous
    contradiction. EDTA dihydrate in the embedded recipe is distinguished from the
    unqualified5191 stock; its lack of hydrate wording is an uncertainty, not proof
    of anhydrous identity. Calcium D-pantothenate agrees with the D-configured 31345
    object but lacks a selected secondary slot. Generic biotin does not independently
    establish stereochemistry; DL lipoic acid remains compatible with the non-stereospecific
    object. Provider compound IDs in all three exact stocks were joined to their actual
    recipe rows. No resazurin CHEBI slot is asserted in the selected empty solution
    descriptor.
  target_ids:
  - CultureMech:009176
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All nine exact historical reports and current histories, including the
    5980 archived change objects, were read. Current 5191 and 5980 raw digests exactly
    match their original attached claims, authenticating the retained content without
    relabelling access dates. The historical 34 report has null g_l while current
    source explicitly reports 30; preserve that version difference. The corrected
    sidecar strips trailing locator annotations and rechecks all 23 historical objects.
    Prior5191/5980 water repairs and 5980 placeholder removal receive credit. Source
    161 history snippets remain historical correspondence only; no new 161 recipe
    retrieval or validation is claimed. Current importer, migration and conservative
    merge behavior are evaluated only as present code. Twenty-one attached concentration
    snippets have both literal and exact-current-digest matches. The additional biotin
    claim citing medium161 remains outside current raw authentication.
  target_ids:
  - CultureMech:009176
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009176-stock-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Source stock masses and addition volumes are encoded as main mass concentrations
  description: Both selected records flatten the trace, vitamin and sulfide stocks
    into main ingredients. Several source mg amounts are retained numerically as G_PER_L,
    and all four stock additions use G_PER_L despite being source mL volumes. Restore
    separate source stages, exact units and literal evidence. Main-batch masses themselves
    are supported, but their current per-litre denominator remains unverified. Current
    TOGO code already separates named sections; a historical flattening claim is not
    attributed to its current body.
  target_ids:
  - CultureMech:009176
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - togo2609Api
  - dsm507
  - api507
  - writer-togo
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-009176-water-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Water inputs are summed across stages and one stock remains a percentage
  description: The selected 3100 G_PER_L combines four distinct solvent inputs. Restore
    their separate volumes. The linked sulfide stock still represents100 mL as 1000
    PERCENT_V_V; correct that to the input-volume meaning. Credit the already repaired1
    L water entries in 5191 and 5980. Only the embedded DSM SL-11 explicitly makes
    up to 1000 mL.
  target_ids:
  - CultureMech:009176
  field_paths:
  - ingredients[0].concentration
  - data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml::composition[1].concentration
  evidence_ids:
  - togo2609Api
  - dsm507
  - dep-sl
  - dep-vit
  - dep-sulfide
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml
    role: scoped dependency
- finding_id: f3
  issue_key: culturemech-009176-sl11-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The linked SL-11 stock is not the printed recipe stock
  description: The target links provider solution 5191, whose authenticated source
    contains 6 g boric acid and unqualified Na2-EDTA. The TOGO and DSM507 embedded
    stock instead has 6 mg boric acid and EDTA dihydrate, with explicit final makeup;
    current API identifies that embedded stock as 1474. Resolve the target reference
    against the exact recipe. Do not overwrite the correctly evidenced 5191 provider
    formulation or transfer its 6 g boric-acid quantity into this medium.
  target_ids:
  - CultureMech:009176
  field_paths:
  - solutions[1].term
  - data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml::composition
  evidence_ids:
  - togo2609Api
  - dsm507
  - api507
  - solution5191
  - dep-sl
  - writer-migration
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: scoped dependency
- finding_id: f4
  issue_key: culturemech-009176-preparation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Source preparation and pH are missing while titrants appear as main ingredients
  description: Neither selected record preserves the staged gas handling, filtration,
    final pH or carbon-monoxide overpressure. Nitrogen,2 N NaOH and2 M sulfuric acid
    are flattened as main descriptors; their delivered amounts remain unquantified.
    Restore the exact source controls with distinct main, trace-stock and sulfide-stock
    scope, credit the existing standalone sulfide preparation, and retain named strain
    overrides separately. No unspecified autoclave time, titrant dose or growth association
    is added.
  target_ids:
  - CultureMech:009176
  field_paths:
  - ingredients[8]
  - ingredients[18]
  - ingredients[30]
  - preparation_steps
  - ph_value
  evidence_ids:
  - togo2609Api
  - dsm507
  - solution34
  - writer-togo
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-009176-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is asserted as anhydrous nickel dichloride
  description: The actual supplied hexahydrate conflicts with CHEBI:34887 in both
    selected primary/secondary slots and the linked 5191 chebi_term. CHEBI:53542 is
    the independently captured hexahydrate candidate. Correct only the actual asserted
    fields after form review; other source-form uncertainty is not converted into
    a wrong-ID claim.
  target_ids:
  - CultureMech:009176
  field_paths:
  - ingredients[13].term
  - ingredients[13].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml::composition[7].chebi_term
  evidence_ids:
  - togo2609Api
  - solution5191
  - chebi34887
  - chebi53542
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: scoped dependency
- finding_id: f6
  issue_key: culturemech-009176-stale-placeholders
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Two complete linked stocks retain incomplete-composition placeholders
  description: The 5191 and34 stocks retain a generic ingredient placeholder and incomplete-composition
    flag despite populated, directly sourced composition. Retire those stale descriptors
    with append-only history; the prior 5980 placeholder cleanup receives credit.
    Reassess the target high-metal warning after correcting stock placement and units
    rather than declaring experimental toxicity.
  target_ids:
  - CultureMech:009176
  field_paths:
  - data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml::data_quality_flags
  - data_quality_flags
  evidence_ids:
  - dep-sl
  - dep-vit
  - dep-sulfide
  - solution5191
  - solution34
  rule_id: review-yaml-record/completeness
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml
    role: scoped dependency
- finding_id: f7
  issue_key: culturemech-009176-pantothenate-secondary
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: A compatible calcium pantothenate primary lacks its secondary link
  description: CHEBI:31345 has the current D-configured object compatible with source
    calcium D-pantothenate. The selected descriptors lack their secondary MIM slot
    despite a current packaged row; assess that linkage separately from stock repair.
  target_ids:
  - CultureMech:009176
  field_paths:
  - ingredients[28]
  evidence_ids:
  - chebi31345
  - mim
  - togo2609Api
  rule_id: review-yaml-record/grounding
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: Both selected records flatten the trace, vitamin and sulfide stocks
    into main ingredients. Several source mg amounts are retained numerically as G_PER_L,
    and all four stock additions use G_PER_L despite being source mL volumes. Restore
    separate source stages, exact units and literal evidence. Main-batch masses themselves
    are supported, but their current per-litre denominator remains unverified. Current
    TOGO code already separates named sections; a historical flattening claim is not
    attributed to its current body.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009176
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
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
  description: The selected 3100 G_PER_L combines four distinct solvent inputs. Restore
    their separate volumes. The linked sulfide stock still represents100 mL as 1000
    PERCENT_V_V; correct that to the input-volume meaning. Credit the already repaired1
    L water entries in 5191 and 5980. Only the embedded DSM SL-11 explicitly makes
    up to 1000 mL.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009176
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5980_Wolin_s_vitamin_solution_10x.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml
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
  description: The target links provider solution 5191, whose authenticated source
    contains 6 g boric acid and unqualified Na2-EDTA. The TOGO and DSM507 embedded
    stock instead has 6 mg boric acid and EDTA dihydrate, with explicit final makeup;
    current API identifies that embedded stock as 1474. Resolve the target reference
    against the exact recipe. Do not overwrite the correctly evidenced 5191 provider
    formulation or transfer its 6 g boric-acid quantity into this medium.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009176
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
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
  description: Neither selected record preserves the staged gas handling, filtration,
    final pH or carbon-monoxide overpressure. Nitrogen,2 N NaOH and2 M sulfuric acid
    are flattened as main descriptors; their delivered amounts remain unquantified.
    Restore the exact source controls with distinct main, trace-stock and sulfide-stock
    scope, credit the existing standalone sulfide preparation, and retain named strain
    overrides separately. No unspecified autoclave time, titrant dose or growth association
    is added.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009176
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
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
  description: The actual supplied hexahydrate conflicts with CHEBI:34887 in both
    selected primary/secondary slots and the linked 5191 chebi_term. CHEBI:53542 is
    the independently captured hexahydrate candidate. Correct only the actual asserted
    fields after form review; other source-form uncertainty is not converted into
    a wrong-ID claim.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009176
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
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
  description: The 5191 and34 stocks retain a generic ingredient placeholder and incomplete-composition
    flag despite populated, directly sourced composition. Retire those stale descriptors
    with append-only history; the prior 5980 placeholder cleanup receives credit.
    Reassess the target high-metal warning after correcting stock placement and units
    rather than declaring experimental toxicity.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009176
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_5191_Trace_element_solution_SL-11.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml
    role: scoped dependency
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a7
  description: CHEBI:31345 has the current D-configured object compatible with source
    calcium D-pantothenate. The selected descriptors lack their secondary MIM slot
    despite a current packaged row; assess that linkage separately from stock repair.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:009176
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2609_Carboxydothermus_Medium.yaml
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
- Current canonical checks validate encoded structure/labels; zero reference checks
  do not verify external source claims.
- All primary PDF pages were read visually as well as in their complete extracted
  text. Current source status, retrieval times and complete raw/text bytes remain
  in the capture catalog.
- The initial guessed TOGO endpoint capture is preserved as an unusable HTML shell
  in the source catalog; only the exact documented API is used for formulation support.
- Current source5191 and embedded 1474 are deliberately not treated as interchangeable.
  No new standalone 1474 YAML is created or silently selected.
- The old report linked an additional October 9 applied-record report outside the
  native input set; that outside file is not assessed. The current inspected 5980
  history and its exact retained claims are assessed.
- The 3% w/v sulfide and 0.1% w/v resazurin labels state mass/volume stock strengths.
  Gas percentages and vessel fill fraction are different dimensions and are not liquid
  concentrations.
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
