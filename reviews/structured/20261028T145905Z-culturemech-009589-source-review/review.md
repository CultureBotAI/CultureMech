# Scientific review: Chemically defined medium

- Review: 20261028T145905Z-culturemech-009589-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T14:32:28.463787Z
- Finished UTC: 2026-10-28T14:59:05.030387Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact M3118 target retains severe stock flattening and unit defects, wrong generic-name dependency links, missing preparation and supplied-form mismatches. Eight dependency solute claims are authenticated and unchanged. Primary formulation access is incomplete; source-table claims and unresolved volume/form boundaries are explicit.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch070 index 01
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009589 | data/merge_yaml/merged/Chemically_defined_medium.yaml | generated | chemically_defined_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009589 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009589 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009589 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009589 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and linked-stock identities

identity: concern. Targets: CultureMech:009589.

The one-owner target is exact TOGO M3118. PMC6744853 independently identifies Thermodesulfobium acidiphilum 3127-1T and quotes the same defined-medium context, referring to Frolov 2017. DSM/LPSN identity is environmental and does not make DSM 901a equivalent. MediaDive 6187 and 6241 are different stocks despite generic names.

### Classification and unsupported flags

representation: concern. Targets: CultureMech:009589.

COMPLEX/UNDEFINED conflicts with the explicitly chemically defined source and its enumerated chemicals. Liquid state is consistent; no universal growth claim is inferred. The high_metal flag needs reassessment after undoing the inflated stock quantities.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009589.

81 current concentration fields are covered by 52 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b070-quantity-inventory-v1","target":"data/merge_yaml/merged/Chemically_defined_medium.yaml","quantity_field_count":81,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1002.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1002.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 1002 G_PER_L sums numerals from 1 L main water, 1000 ml trace-stock water and 1 L vitamin-stock water. The units and solution-stage bases differ; this is neither a total water volume nor a final-medium mass concentration. Keep the three source water inputs separate.","source_stage":"main and two separate stock batches","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The stored 1002 G_PER_L sums numerals from 1 L main water, 1000 ml trace-stock water and 1 L vitamin-stock water. The units and solution-stage bases differ; this is neither a total water volume nor a final-medium mass concentration. Keep the three source water inputs separate."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The stored 1002 G_PER_L sums numerals from 1 L main water, 1000 ml trace-stock water and 1 L vitamin-stock water. The units and solution-stage bases differ; this is neither a total water volume nor a final-medium mass concentration. Keep the three source water inputs separate."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source supports 0.33 g of KH2PO4 in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of KH2PO4 in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of KH2PO4 in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source supports 0.33 g of NH4Cl in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of NH4Cl in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of NH4Cl in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q4","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Source reports 1 mg resazurin, not 1 g/L. Preserve the exact mass and unresolved final-volume basis; do not silently turn the source input water into a final-volume instruction.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","decision":"conflict","rationale":"Source reports 1 mg resazurin, not 1 g/L. Preserve the exact mass and unresolved final-volume basis; do not silently turn the source input water into a final-volume instruction."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","decision":"conflict","rationale":"Source reports 1 mg resazurin, not 1 g/L. Preserve the exact mass and unresolved final-volume basis; do not silently turn the source input water into a final-volume instruction."}]},{"quantity_id":"q5","label":"Na2S.9H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source supports 0.5 g of Na2S.9H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"Na2S.9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The source supports 0.5 g of Na2S.9H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The source supports 0.5 g of Na2S.9H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source supports 0.33 g of KCl in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of KCl in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of KCl in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q7","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.8","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source supports 2.8 g of Na2SO4 in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"Na2SO4\",\n          \"volume\": 2.8,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The source supports 2.8 g of Na2SO4 in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The source supports 2.8 g of Na2SO4 in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q8","label":"CaCl2.6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source supports 0.33 g of CaCl2.6H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"CaCl2.6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001163\",\n          \"gmo_id\": \"GMO_001163\",\n          \"label\": \"Calcium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of CaCl2.6H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of CaCl2.6H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q9","label":"MgCl2.2H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The source supports 0.33 g of MgCl2.2H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"MgCl2.2H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001266\",\n          \"gmo_id\": \"GMO_001266\",\n          \"label\": \"Magnesium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of MgCl2.2H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The source supports 0.33 g of MgCl2.2H2O in the main batch. Its 1 L water input is not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q10","label":"3 M HCl","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The 3 M acid strength is explicit but its added amount is not. VARIABLE is an unquantified dose marker, not a measured concentration; retain 3 M stock identity and the source pH context.","source_stage":"adjustment reagent or gas headspace","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"3 M HCl\",\n          \"conc_value\": 3,\n          \"conc_unit\": \"M\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"To adjust the pH of the medium to 4.8, 3 M HCl was added.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","decision":"not_quantified","rationale":"The 3 M acid strength is explicit but its added amount is not. VARIABLE is an unquantified dose marker, not a measured concentration; retain 3 M stock identity and the source pH context."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","decision":"not_quantified","rationale":"The 3 M acid strength is explicit but its added amount is not. VARIABLE is an unquantified dose marker, not a measured concentration; retain 3 M stock identity and the source pH context."}]},{"quantity_id":"q11","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The gas identity is supported, but no dissolved-medium concentration is quantified. VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context, which belong to preparation rather than mass concentration.","source_stage":"adjustment reagent or gas headspace","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\": 6,\n      \"comment\": \"The medium was dispensed in 5 ml portions into 17 ml Hungate tubes; the head space was filled with H2/CO2 (4 : 1, 151.9 kPa).\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","decision":"not_quantified","rationale":"The gas identity is supported, but no dissolved-medium concentration is quantified. VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context, which belong to preparation rather than mass concentration."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","decision":"not_quantified","rationale":"The gas identity is supported, but no dissolved-medium concentration is quantified. VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context, which belong to preparation rather than mass concentration."}]},{"quantity_id":"q12","label":"Hydrogen gas","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The gas identity is supported, but no dissolved-medium concentration is quantified. VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context, which belong to preparation rather than mass concentration.","source_stage":"adjustment reagent or gas headspace","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\": \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\": \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\": 6,\n      \"comment\": \"The medium was dispensed in 5 ml portions into 17 ml Hungate tubes; the head space was filled with H2/CO2 (4 : 1, 151.9 kPa).\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","decision":"not_quantified","rationale":"The gas identity is supported, but no dissolved-medium concentration is quantified. VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context, which belong to preparation rather than mass concentration."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","decision":"not_quantified","rationale":"The gas identity is supported, but no dissolved-medium concentration is quantified. VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context, which belong to preparation rather than mass concentration."}]},{"quantity_id":"q13","label":"Na2MoO4 × H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 24 mg of Na2MoO4 × H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4 × H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The source reports 24 mg of Na2MoO4 × H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The source reports 24 mg of Na2MoO4 × H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q14","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 6 mg of H3BO3 in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The source reports 6 mg of H3BO3 in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The source reports 6 mg of H3BO3 in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q15","label":"MnCl2 × 4H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"99","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"99","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 99 mg of MnCl2 × 4H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"MnCl2 × 4H2O\",\n          \"volume\": 99,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The source reports 99 mg of MnCl2 × 4H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The source reports 99 mg of MnCl2 × 4H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q16","label":"CoCl2 × 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"238","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"238","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 238 mg of CoCl2 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"CoCl2 × 6H2O\",\n          \"volume\": 238,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The source reports 238 mg of CoCl2 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The source reports 238 mg of CoCl2 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q17","label":"ZnSO4 × 7H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"144","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"144","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 144 mg of ZnSO4 × 7H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"ZnSO4 × 7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The source reports 144 mg of ZnSO4 × 7H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The source reports 144 mg of ZnSO4 × 7H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q18","label":"Na2WO4 × 2H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"33","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 33 mg of Na2WO4 × 2H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Na2WO4 × 2H2O\",\n          \"volume\": 33,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The source reports 33 mg of Na2WO4 × 2H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The source reports 33 mg of Na2WO4 × 2H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q19","label":"(NH4)2SO4FeSO4 × 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"748","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"748","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 748 mg of (NH4)2SO4FeSO4 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"(NH4)2SO4FeSO4 × 6H2O\",\n          \"volume\": 748,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001076\",\n          \"gmo_id\": \"GMO_001076\",\n          \"label\": \"Ammonium iron(II) sulfate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The source reports 748 mg of (NH4)2SO4FeSO4 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The source reports 748 mg of (NH4)2SO4FeSO4 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q20","label":"(NH4)2SO4NiSO4 × 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"395","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"395","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 395 mg of (NH4)2SO4NiSO4 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"(NH4)2SO4NiSO4 × 6H2O\",\n          \"volume\": 395,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001102\",\n          \"gmo_id\": \"GMO_001102\",\n          \"label\": \"Ammonium nickel(II) sulfate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The source reports 395 mg of (NH4)2SO4NiSO4 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The source reports 395 mg of (NH4)2SO4NiSO4 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q21","label":"Na2SeO4 × 5H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"94","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"94","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 94 mg of Na2SeO4 × 5H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Na2SeO4 × 5H2O\",\n          \"volume\": 94,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001603\",\n          \"gmo_id\": \"GMO_001603\",\n          \"label\": \"Sodium selenate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The source reports 94 mg of Na2SeO4 × 5H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The source reports 94 mg of Na2SeO4 × 5H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q22","label":"CuCl2 × 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"238","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"238","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 238 mg of CuCl2 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"CuCl2 × 6H2O\",\n          \"volume\": 238,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001755\",\n          \"gmo_id\": \"GMO_001755\",\n          \"label\": \"Copper(II) chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The source reports 238 mg of CuCl2 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The source reports 238 mg of CuCl2 × 6H2O in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q23","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 2 mg of Biotin in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The source reports 2 mg of Biotin in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The source reports 2 mg of Biotin in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q24","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 5 mg of p-Aminobenzoic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The source reports 5 mg of p-Aminobenzoic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The source reports 5 mg of p-Aminobenzoic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q25","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 10 mg of Pyridoxine hydrochloride in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"Pyridoxine hydrochloride\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The source reports 10 mg of Pyridoxine hydrochloride in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The source reports 10 mg of Pyridoxine hydrochloride in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q26","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 2 mg of Folic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The source reports 2 mg of Folic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The source reports 2 mg of Folic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q27","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 0.1 mg of Vitamin B12 in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The source reports 0.1 mg of Vitamin B12 in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The source reports 0.1 mg of Vitamin B12 in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q28","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 5 mg of Riboflavin in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The source reports 5 mg of Riboflavin in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The source reports 5 mg of Riboflavin in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q29","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 5 mg of Nicotinic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The source reports 5 mg of Nicotinic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The source reports 5 mg of Nicotinic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q30","label":"Thiamine","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 5 mg of Thiamine in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\": \"Thiamine\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001230\",\n          \"gmo_id\": \"GMO_001230\",\n          \"label\": \"Thiamine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The source reports 5 mg of Thiamine in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The source reports 5 mg of Thiamine in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q31","label":"Pantothenic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 5 mg of Pantothenic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\": \"Pantothenic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001616\",\n          \"gmo_id\": \"GMO_001616\",\n          \"label\": \"Pantothenic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The source reports 5 mg of Pantothenic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The source reports 5 mg of Pantothenic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q32","label":"Thioctic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source reports 5 mg of Thioctic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\": \"Thioctic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The source reports 5 mg of Thioctic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The source reports 5 mg of Thioctic acid in this stock batch, not the same numeral G_PER_L directly in the receiving medium. Retain the stock composition separately from its 1 ml addition; no final working concentration is calculated without all dilution bases."}]},{"quantity_id":"q33","label":"Trace element solution receiving dose","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition differs from the named MediaDive link, so neither a generic-name link nor the existing dependency amount can substitute for this stock.","source_stage":"M3118 stock addition","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition differs from the named MediaDive link, so neither a generic-name link nor the existing dependency amount can substitute for this stock."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition differs from the named MediaDive link, so neither a generic-name link nor the existing dependency amount can substitute for this stock."}]},{"quantity_id":"q34","label":"Vitamin solution receiving dose","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition differs from the named MediaDive link, so neither a generic-name link nor the existing dependency amount can substitute for this stock.","source_stage":"M3118 stock addition","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition differs from the named MediaDive link, so neither a generic-name link nor the existing dependency amount can substitute for this stock."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition differs from the named MediaDive link, so neither a generic-name link nor the existing dependency amount can substitute for this stock."}]},{"quantity_id":"q35","label":"solution6187 Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\": \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q36","label":"solution6187 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1000","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage. Retain the exact stock water input/make-up instruction without inventing a water fraction.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","decision":"conflict","rationale":"The source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage. Retain the exact stock water input/make-up instruction without inventing a water fraction."}]},{"quantity_id":"q37","label":"solution6187 FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.097","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\": 82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\": \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q38","label":"solution6187 MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"0.041","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\": \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q39","label":"solution6187 ZnCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q40","label":"solution6187 CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\": 7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q41","label":"solution6187 Na2MoO4 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\": 8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q42","label":"solution6187 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This is a schema-default placeholder, not an additional ingredient or an experimentally quantified variable. The complete provider composition is available; retain history while removing the phantom ingredient in later curation.","source_stage":"metadata placeholder","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This is a schema-default placeholder, not an additional ingredient or an experimentally quantified variable. The complete provider composition is available; retain history while removing the phantom ingredient in later curation."}]},{"quantity_id":"q43","label":"solution6187 retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","stored":"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing sequence:"}],"decision":"evidence_only","rationale":"The existing preparation wording agrees with the exact provider stock instructions; preserve it with root-level path-scoped evidence. It does not prescribe the selected medium dose.","source_stage":"standalone stock preparation","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The existing preparation wording agrees with the exact provider stock instructions; preserve it with root-level path-scoped evidence. It does not prescribe the selected medium dose."}]},{"quantity_id":"q44","label":"solution6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q45","label":"solution6241 Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The existing attached exact recipe object and claimed raw digest match the current capture. The provider-declared g_l equals the local value for this standalone stock only. This authenticates current content, not the original access event or a receiving-medium dose."}]},{"quantity_id":"q46","label":"solution6241 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Source gives 200 micrograms biotin and explicitly makes up to 100 ml. This supports 0.002 g/L (200 × 10^-6 g / 0.1 L), not local 2000 G_PER_L. This correction is confined to solution6241; it does not identify the selected M3118 vitamin stock.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","decision":"conflict","rationale":"Source gives 200 micrograms biotin and explicitly makes up to 100 ml. This supports 0.002 g/L (200 × 10^-6 g / 0.1 L), not local 2000 G_PER_L. This correction is confined to solution6241; it does not identify the selected M3118 vitamin stock."}]},{"quantity_id":"q47","label":"solution6241 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage. Retain the exact stock water input/make-up instruction without inventing a water fraction.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","decision":"conflict","rationale":"The source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage. Retain the exact stock water input/make-up instruction without inventing a water fraction."}]},{"quantity_id":"q48","label":"solution6241 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This is a schema-default placeholder, not an additional ingredient or an experimentally quantified variable. The complete provider composition is available; retain history while removing the phantom ingredient in later curation.","source_stage":"metadata placeholder","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This is a schema-default placeholder, not an additional ingredient or an experimentally quantified variable. The complete provider composition is available; retain history while removing the phantom ingredient in later curation."}]},{"quantity_id":"q49","label":"solution6241 retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The existing preparation wording agrees with the exact provider stock instructions; preserve it with root-level path-scoped evidence. It does not prescribe the selected medium dose.","source_stage":"standalone stock preparation","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The existing preparation wording agrees with the exact provider stock instructions; preserve it with root-level path-scoped evidence. It does not prescribe the selected medium dose."}]},{"quantity_id":"q50","label":"M3118 source-only context 0","local_fields":[],"decision":"evidence_only","rationale":"Exact source context absent from the local recipe; preserve its named-medium and stage boundary. The paper separately confirms organism/source identity, not every TOGO amount.","source_stage":"source-only preparation/identity","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 1,\n      \"comment\": \"T. acidiphilum was grown under anaerobic conditions on a chemically defined medium (20) with CO2 as the carbon source, H2 as the electron donor, and sulfate as the electron acceptor.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q51","label":"M3118 source-only context 3","local_fields":[],"decision":"evidence_only","rationale":"Exact source context absent from the local recipe; preserve its named-medium and stage boundary. The paper separately confirms organism/source identity, not every TOGO amount.","source_stage":"source-only preparation/identity","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"To adjust the pH of the medium to 4.8, 3 M HCl was added.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q52","label":"M3118 source-only context 4","local_fields":[],"decision":"evidence_only","rationale":"Exact source context absent from the local recipe; preserve its named-medium and stage boundary. The paper separately confirms organism/source identity, not every TOGO amount.","source_stage":"source-only preparation/identity","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\": 6,\n      \"comment\": \"The medium was dispensed in 5 ml portions into 17 ml Hungate tubes; the head space was filled with H2/CO2 (4 : 1, 151.9 kPa).\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/Chemically_defined_medium.yaml":null,"data/normalized_yaml/bacterial/chemically_defined_medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009589.

All asserted current ontology objects are nonobsolete and exact labels are inventoried. Confirmed hydrate/anhydrous mismatches and molybdate source conflict remain distinct from generic thioctic-acid stereochemical uncertainty. Correct calcium/magnesium hydrates, zinc sulfate hydrate, vitamin/B12 class and chloride identities are credited. No forced mapping is proposed for ungrounded double salts; legacy thiamine membership is only current-snapshot evidence, not historical validity.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:009589.

Complete six reports and selected parent objects were read. October 5 source-unchecked triage is superseded only by the present scoped source reads. October 7 attached concentration claims for 6187/6241 authenticate against equal raw bytes (six plus two); water/biotin/placeholder exclusions are retained as prior limits, not endorsed. Current TOGO separates named stocks and current cleanup no longer sums; the existing 1002 numeral is historical data, not proof of current writer execution. Naive dependency timestamps remain original and any verified provenance clarification must be appended.

## Findings

### f1: Restore local M3118 stock stages and units

major / open / confirmed; issue key: culturemech-009589-stock-unit-stage.

Separate the ten trace and ten vitamin stock components from direct main ingredients; restore their source mg amounts and separate water inputs. Preserve the 1 mg resazurin amount and two 1 ml stock additions. Resolve main-batch G_PER_L denominators before asserting final concentrations; input water does not prove final volume.

### f2: Replace unsupported generic-name stock links

major / open / confirmed; issue key: culturemech-009589-stock-reference-identity.

The M3118 trace stock is a ten-compound formulation, whereas linked 6187 is an EDTA/iron-based six-solute stock. M3118 vitamin stock has ten vitamins, whereas 6241 has three. Resolve the links to exact local M3118 stocks, retaining comparison evidence without transferring a dependency formula or dose.

### f3: Restore scoped pH and preparation evidence

major / open / confirmed; issue key: culturemech-009589-missing-preparation.

The source pH 4.8, acid-strength context, vessel/dispensing and gas headspace specifications are absent. Add only the exact supported M3118 preparation, with root evidence tied to its paths; no sterilization duration or main final volume is invented. Current parser reads root ph rather than meta.ph.

### f4: Reconcile supplied forms without guessing replacements

major / open / confirmed; issue key: culturemech-009589-supplied-forms.

Selected cobalt hexahydrate and copper hexahydrate names carry anhydrous chloride IDs; the molybdate formula says one water while TOGO label says dihydrate and the selected ID is anhydrous. Resolve that source conflict explicitly. Generic thioctic acid does not establish R-specific CHEBI:30314. In dependency 6187, composition[4].chebi_term is anhydrous CHEBI:49976 despite the six-water supplied name. Keep amount support distinct from chemical-form support.

### f5: Repair distinct dependency units and biotin

major / open / confirmed; issue key: culturemech-009589-dependency-quantity.

For solution 6241 only, source 200 micrograms biotin made up to 100 ml supports 0.002 g/L rather than 2000 G_PER_L. Both standalone stocks encode water as 1000 PERCENT_V_V and retain phantom placeholder ingredients. Preserve the eight authenticated attached solute claims and stock preparation notes; repair remaining fields only within these dependency identities.

### f6: Align defined-medium classification and evidence

minor / open / confirmed; issue key: culturemech-009589-classification.

After exact-stock reconciliation, classify this explicitly defined source consistently in medium_type/composition_type, reassess high_metal against corrected stages, replace Unknown solution names with exact source names and attach bibliography/claim evidence. Preserve the original history and append any verified correction event.

## Recommended Actions And Acceptance Checks

### a1

Separate the ten trace and ten vitamin stock components from direct main ingredients; restore their source mg amounts and separate water inputs. Preserve the 1 mg resazurin amount and two 1 ml stock additions. Resolve main-batch G_PER_L denominators before asserting final concentrations; input water does not prove final volume.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The M3118 trace stock is a ten-compound formulation, whereas linked 6187 is an EDTA/iron-based six-solute stock. M3118 vitamin stock has ten vitamins, whereas 6241 has three. Resolve the links to exact local M3118 stocks, retaining comparison evidence without transferring a dependency formula or dose.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The source pH 4.8, acid-strength context, vessel/dispensing and gas headspace specifications are absent. Add only the exact supported M3118 preparation, with root evidence tied to its paths; no sterilization duration or main final volume is invented. Current parser reads root ph rather than meta.ph.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Selected cobalt hexahydrate and copper hexahydrate names carry anhydrous chloride IDs; the molybdate formula says one water while TOGO label says dihydrate and the selected ID is anhydrous. Resolve that source conflict explicitly. Generic thioctic acid does not establish R-specific CHEBI:30314. In dependency 6187, composition[4].chebi_term is anhydrous CHEBI:49976 despite the six-water supplied name. Keep amount support distinct from chemical-form support.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

For solution 6241 only, source 200 micrograms biotin made up to 100 ml supports 0.002 g/L rather than 2000 G_PER_L. Both standalone stocks encode water as 1000 PERCENT_V_V and retain phantom placeholder ingredients. Preserve the eight authenticated attached solute claims and stock preparation notes; repair remaining fields only within these dependency identities.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

After exact-stock reconciliation, classify this explicitly defined source consistently in medium_type/composition_type, reassess high_metal against corrected stages, replace Unknown solution names with exact source names and attach bibliography/claim evidence. Preserve the original history and append any verified correction event.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| togo3118 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118; REVIEW_WORK/batch070/source01-03-preflight/togo3118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Exact selected-source identity preflight. Organism/source context screened before any operational assessment; no source transfer between variants. |
| solution6187 | https://mediadive.dsmz.de/rest/solution/6187; REVIEW_WORK/batch070/source01-03-supplement/solution6187.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; REVIEW_WORK/batch070/validation-authors/solution6241-metadata-adapter.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh batch070 shared exact provider solution 6241 capture, reused with original timestamps; comparison only to selected M3118 vitamin stock, not equivalent. |
| pmc6744853 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6744853/; REVIEW_WORK/batch070/source01-03-supplement/pmc6744853.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| pmcSI | https://pmc.ncbi.nlm.nih.gov/articles/instance/6744853/bin/pnas.1904225116.sapp.pdf; REVIEW_WORK/batch070/source01-primary-followup/pmcSI.json; exact original raw/text/hash/time metadata | unknown | Exact supplement URL returned HTTP200 browser-check HTML; no PDF or formulation recovered. |
| frolov2017 | https://doi.org/10.1099/ijsem.0.001745; REVIEW_WORK/batch070/source01-primary-followup/frolov2017.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Exact paper supplement and cited primary reference; assess only selected-medium formulation context. |
| dsm102892 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-102892; REVIEW_WORK/batch070/source01-03-supplement/dsm102892.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| lpsnacidiphilum | https://lpsn.dsmz.de/species/thermodesulfobium-acidiphilum; REVIEW_WORK/batch070/source01-03-supplement/lpsnacidiphilum.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/Chemically_defined_medium.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/chemically_defined_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-18 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Chemically_defined_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chemically_defined_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch070/record01/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch070/record01/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch070/record01/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _local_batch_volume_ml; _parse_unit; _extract_ph; _extract_preparation_steps | context_only | Current _extract_primary_components separates named local stocks; _solution_from_item retains a local stock without composition if its basis is insufficient. _parse_unit now maps mg to MG_PER_L and ml to ML_PER_L, but bare g still becomes G_PER_L and bare percent becomes PERCENT_W_V without independently proving final volume or percent basis. _extract_ph reads root ph, while these API payloads provide meta.ph. _extract_preparation_steps retains comments but labels any filter sentence FILTER_STERILIZE, which overstates ordinary cheesecloth filtration. These are current behaviors, not proof of historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| deptrace | data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml; Complete file | context_only | Whole referenced standalone solution audited as a distinct identity comparison, not the M3118 stock. |
| depvit | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Complete file | context_only | Whole referenced standalone solution audited as a distinct identity comparison, not the M3118 stock. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch070/source01-03-supplement/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch070/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch070/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch070/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch070/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch070/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch070/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi91243 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91243; REVIEW_WORK/batch070/source01-03-supplement/chebi91243.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131394 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131394; REVIEW_WORK/batch070/source01-03-supplement/chebi131394.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526; REVIEW_WORK/batch070/source01-03-supplement/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276; REVIEW_WORK/batch070/source01-03-supplement/chebi18276.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75215 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75215; REVIEW_WORK/batch070/source01-03-supplement/chebi75215.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch070/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch070/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696; REVIEW_WORK/batch070/source01-03-supplement/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch070/source01-03-supplement/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; REVIEW_WORK/batch070/source01-03-supplement/chebi63939.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49553 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49553; REVIEW_WORK/batch070/source01-03-supplement/chebi49553.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch070/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch070/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch070/source01-03-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch070/source01-03-supplement/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch070/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch070/source01-03-supplement/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch070/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi18385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18385; REVIEW_WORK/batch070/source01-03-supplement/chebi18385.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi7916 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:7916; REVIEW_WORK/batch070/source01-03-supplement/chebi7916.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30314 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30314; REVIEW_WORK/batch070/source01-03-supplement/chebi30314.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734; REVIEW_WORK/batch070/source01-03-supplement/chebi64734.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254; REVIEW_WORK/batch070/source01-03-supplement/chebi86254.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch070/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch070/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch070/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439; REVIEW_WORK/batch070/source01-03-supplement/chebi17439.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch070/source01-03-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch070/record01/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch070/record01/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch070/record01/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch070/record01/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch070/record01/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch070/record01/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch070/record01/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch070/record01/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch070/record01/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch070/record01/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch070/record01/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Full primary formulation behind Frolov2017 was unavailable: DOI returned403. The exact PMC supplement URL returned200 browser-check HTML, not a PDF. PMC main text independently corroborates identity/defined-medium use but does not authenticate every TOGO mass; these are explicitly database-level claims.
- The TOGO molybdate supplied formula and ontology label disagree. Copper hydrate notation and generic vitamin stereochemistry are preserved as unresolved source/form boundaries; no inferred molecular-weight conversions.
- Provider mmol_l fields are not certified here; quantities are evaluated using exact source masses, declared g_l, and explicit stock make-up where available.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T145905Z-culturemech-009589-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Chemically defined medium'
started_at: '2026-10-28T14:32:28.463787Z'
finished_at: '2026-10-28T14:59:05.030387Z'
reviewer:
  identity: Codex batch006_validation
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, exact
    captured sources, fresh scoped primary sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: The exact M3118 target retains severe stock flattening and unit defects,
  wrong generic-name dependency links, missing preparation and supplied-form mismatches.
  Eight dependency solute claims are authenticated and unchanged. Primary formulation
  access is incomplete; source-table claims and unresolved volume/form boundaries
  are explicit.
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
  - path: data/merge_yaml/merged/Chemically_defined_medium.yaml
    sha256: 9146a1ebece05eab9447eabf8b9636a74b2e72eaf40bdf6cac820f85b9aca6f6
    role: target
  - path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    sha256: 0fe41ed0f6f119b73c45b41c8974ba70c45a444117efa3e49c621d33e9736492
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md
    sha256: 51447d8fea765972d4344a448ea87c9dd84eb196a0e80dbacc00290a627b10cc
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
    sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Chemically_defined_medium.md
    sha256: 25e8a28e7a4c9d42c63b38f07c2c9be884a7c91d5c644af38ca52f25c78a6463
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chemically_defined_medium.md
    sha256: 23943b2d2b6e30c2e1d430e3909240011b5b2714a9b876d3b65b740ab23cb7d4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.md
    sha256: 2ec3be557e14096c1fdf3abb674976cd044d552f48bafa76fc3e52d15dddbd6c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
    sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
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
  selection: Authoritative batch070 index 01
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009589
targets:
- target_id: CultureMech:009589
  path: data/merge_yaml/merged/Chemically_defined_medium.yaml
  label: chemically_defined_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:009589
  command: just validate-schema data/merge_yaml/merged/Chemically_defined_medium.yaml
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
  - CultureMech:009589
  command: just validate-strict data/merge_yaml/merged/Chemically_defined_medium.yaml
    --out REVIEW_WORK/batch070/record01/strict.tsv --workers 1 --quiet
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
  - CultureMech:009589
  command: just validate-terms data/merge_yaml/merged/Chemically_defined_medium.yaml
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
  - CultureMech:009589
  command: just validate-references data/merge_yaml/merged/Chemically_defined_medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: togo3118
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118
  accessed_at: '2026-10-28T14:31:12.414346Z'
  locator: REVIEW_WORK/batch070/source01-03-preflight/togo3118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Exact selected-source identity preflight. Organism/source
    context screened before any operational assessment; no source transfer between
    variants.
  snapshot_sha256: 6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242
- evidence_id: solution6187
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6187
  accessed_at: '2026-10-28T14:35:51.544530Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/solution6187.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  accessed_at: '2026-10-28T14:32:10.413055Z'
  locator: REVIEW_WORK/batch070/validation-authors/solution6241-metadata-adapter.json;
    exact original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh batch070 shared exact provider solution 6241
    capture, reused with original timestamps; comparison only to selected M3118 vitamin
    stock, not equivalent.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: pmc6744853
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6744853/
  accessed_at: '2026-10-28T14:35:52.054928Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/pmc6744853.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f094b591acd9a0d58276c3d0f6de8acbe689c210c9d1705cc7bf48e3c757a391
- evidence_id: pmcSI
  kind: search
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/6744853/bin/pnas.1904225116.sapp.pdf
  accessed_at: '2026-10-28T14:37:24.424831Z'
  locator: REVIEW_WORK/batch070/source01-primary-followup/pmcSI.json; exact original
    raw/text/hash/time metadata
  support: unknown
  summary: Exact supplement URL returned HTTP200 browser-check HTML; no PDF or formulation
    recovered.
  snapshot_sha256: e8a0e5acba5b6c0deadc2a290bb821421b58abdc2b877bcade09dc5c859b5436
  search_scope: One exact PMC supplementary-file GET; original200 status and challenge
    body retained.
- evidence_id: frolov2017
  kind: search
  reference: https://doi.org/10.1099/ijsem.0.001745
  accessed_at: '2026-10-28T14:37:24.512785Z'
  locator: REVIEW_WORK/batch070/source01-primary-followup/frolov2017.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Exact paper supplement and cited primary reference;
    assess only selected-medium formulation context.
  snapshot_sha256: 2486be26994ac129cbd2d598dee459aca1dea42fe1b67dc71d271ad26a3a093f
  search_scope: One exact public GET of https://doi.org/10.1099/ijsem.0.001745; retained
    status 403. No exhaustive repository or literature absence claim.
- evidence_id: dsm102892
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-102892
  accessed_at: '2026-10-28T14:35:53.693720Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/dsm102892.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cbb02986ce7fa608437f57f41cd5f3c9abe472c047aa5fa2bef6f12ee9c70bc5
- evidence_id: lpsnacidiphilum
  kind: primary_source
  reference: https://lpsn.dsmz.de/species/thermodesulfobium-acidiphilum
  accessed_at: '2026-10-28T14:35:52.465234Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/lpsnacidiphilum.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5c2f9798eb7b9762d0404d93ce5ef9894988578e89fd8ff6a2698e0d630a885a
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Chemically_defined_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:41:27.278723Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 9146a1ebece05eab9447eabf8b9636a74b2e72eaf40bdf6cac820f85b9aca6f6
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:41:27.278879Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 0fe41ed0f6f119b73c45b41c8974ba70c45a444117efa3e49c621d33e9736492
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T14:41:27.278909Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T14:41:27.279202Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T14:41:27.279224Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T14:41:27.279244Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T14:41:27.279268Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T14:41:27.280046Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 51447d8fea765972d4344a448ea87c9dd84eb196a0e80dbacc00290a627b10cc
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T14:41:27.280072Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Chemically_defined_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T14:41:27.280093Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 25e8a28e7a4c9d42c63b38f07c2c9be884a7c91d5c644af38ca52f25c78a6463
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chemically_defined_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T14:41:27.280119Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 23943b2d2b6e30c2e1d430e3909240011b5b2714a9b876d3b65b740ab23cb7d4
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T14:41:27.280144Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2ec3be557e14096c1fdf3abb674976cd044d552f48bafa76fc3e52d15dddbd6c
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T14:41:27.280163Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/historical-reading.json
  accessed_at: '2026-10-28T14:41:27.280187Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 1892b82c5feb57daec6e4657edf00dec59db0f7dd66d678a69be9773404636ad
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T14:41:27.280411Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 4cb1505e7cd5a15bf3d1b323688aad54ca79000f1fbc4740c5a267f341849400
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/complete-document-reader.json
  accessed_at: '2026-10-28T14:41:27.280577Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 7218854d3bf759854a86be88e040d57c9babd528cb67685eebf4debedec1936b
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T14:41:27.280840Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _local_batch_volume_ml;
    _parse_unit; _extract_ph; _extract_preparation_steps
  accessed_at: '2026-10-28T14:41:27.280874Z'
  support: context_only
  summary: Current _extract_primary_components separates named local stocks; _solution_from_item
    retains a local stock without composition if its basis is insufficient. _parse_unit
    now maps mg to MG_PER_L and ml to ML_PER_L, but bare g still becomes G_PER_L and
    bare percent becomes PERCENT_W_V without independently proving final volume or
    percent basis. _extract_ph reads root ph, while these API payloads provide meta.ph.
    _extract_preparation_steps retains comments but labels any filter sentence FILTER_STERILIZE,
    which overstates ordinary cheesecloth filtration. These are current behaviors,
    not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: MediaQualityFixer._merge_ingredient_group
  accessed_at: '2026-10-28T14:41:27.280907Z'
  support: context_only
  summary: Current _merge_ingredient_group keeps identical duplicate amounts and flags
    disagreements; it no longer sums duplicate quantities. It cannot establish compatible
    stock/main bases or repair a historical flattened sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: deptrace
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:41:27.285192Z'
  support: context_only
  summary: Whole referenced standalone solution audited as a distinct identity comparison,
    not the M3118 stock.
  snapshot_sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
- evidence_id: depvit
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:41:27.287567Z'
  support: context_only
  summary: Whole referenced standalone solution audited as a distinct identity comparison,
    not the M3118 stock.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T14:35:53.489055Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi15377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T14:36:01.579507Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T14:35:59.076020Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T14:36:03.933227Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T14:36:02.807740Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T14:35:59.429374Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T14:35:59.079818Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi91243
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91243
  accessed_at: '2026-10-28T14:36:03.933437Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi91243.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d508c52dd058e80c32d74980d46164e7d251f95515482c415cce94b9eb197dcf
- evidence_id: chebi131394
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131394
  accessed_at: '2026-10-28T14:35:52.465071Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi131394.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1873667a81a0f4e32783ca14fbb2da202d7ee1ea2e843d762319662ee1e0cb9c
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526
  accessed_at: '2026-10-28T14:35:55.276961Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi16526.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1fc9ed85cc20ea796dc5884bab2961c0cb13288fec88089767d5ca0349e6ab66
- evidence_id: chebi18276
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276
  accessed_at: '2026-10-28T14:35:56.600607Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi18276.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e9495ec2aad65253b7f792e780c1610f9f12f2c0bb20e06c2526156d37b09ed7
- evidence_id: chebi75215
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75215
  accessed_at: '2026-10-28T14:36:02.602845Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi75215.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2b20066f2750e25b25f2d4bf8ef1ab632fd6c452500a39a7641bcd5f596377ab
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T14:35:59.940617Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T14:36:03.600790Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696
  accessed_at: '2026-10-28T14:36:00.083117Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi35696.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 22f49067d1405baa8e2bbd7c4405035d8663c69aa045b7bbacf363bb30729244
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T14:35:59.429084Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi32312.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  accessed_at: '2026-10-28T14:36:01.783499Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi63939.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 01f41117ab89dbd1d514a894850dc06afd5d95c0bee7fd89f7dfdb54c309c514
- evidence_id: chebi49553
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49553
  accessed_at: '2026-10-28T14:36:00.330545Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi49553.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d4660eb3bc066caef0e626b9b3bdf46ebaecdcf1779b4a75bfcd982f49bbc5b
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T14:35:54.718207Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T14:35:58.219685Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T14:35:58.766215Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi30961.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T14:35:58.708680Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi27470.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T14:35:55.881032Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi176843.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T14:35:54.920946Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi17015.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T14:35:54.593754Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi18385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18385
  accessed_at: '2026-10-28T14:35:56.587155Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi18385.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 8751d9fa71080919eb386ddec0f27d58a47ec857d1b3d11e5922a0c192a19516
- evidence_id: chebi7916
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:7916
  accessed_at: '2026-10-28T14:36:02.978556Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi7916.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cd669aeb8ae7305e679345b84cd598247eae09bfdc58c3b28dc30aa9e1a2066a
- evidence_id: chebi30314
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30314
  accessed_at: '2026-10-28T14:35:58.195908Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi30314.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c65311307ace44e29b902c93926f9a84f7fd601f7666e192d2af3dd18d4727e4
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734
  accessed_at: '2026-10-28T14:36:01.982045Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi64734.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4afcce140f81023fe7e21d1081a51e76eb83b0d89e158079ef5be695df2388ec
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254
  accessed_at: '2026-10-28T14:36:03.216831Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi86254.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: b3a79ee6d9359b7b827f6f87134bc166d84d3948ec20c54965c6e706aecde3a4
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T14:36:00.951037Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T14:36:01.271098Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T14:36:02.192806Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439
  accessed_at: '2026-10-28T14:35:55.775892Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi17439.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 71dca75ee64801424c519bde7667291decd3b97f0c4e46c3d9b9405fa04a71d4
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T14:36:00.330390Z'
  locator: REVIEW_WORK/batch070/source01-03-supplement/chebi49105.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch070 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:41:27.442526Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: c37741eb7a2d0796f142ada8a39bd89fc7f7542236265c4a590c9d7874d99a79
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:41:27.442626Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: c1e83de2d1cc7204e8e202f67eb7d5d7629c1b8cf40f5be3912ca7c6a17fb6d8
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:41:27.442750Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 53eb0bc2fda861b15429a169cf8d9eae03569e5157f2eb6c2b09d5f29b987db6
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:41:27.442823Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: ec45c620c1205885f3c1551becb42ba1d70ae5a6e3e28e8fa1a2c83eaf9894ae
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:41:27.442888Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 35df2336addddfdb0c39610c5c5eed2a3c599b93eef5b3791297f7c3934f9c72
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:41:27.442917Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: b7f26822e430d4f23c3ea2a23dceb27ed4de32a3b2b5e166dba416174eea606e
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch070/record01/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:41:27.442936Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: b5937fe8c7f8af2b68151130af19c5cf2428245078111b76e1d7651a2df0c5fd
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch070/record01/validate-schema.json
  accessed_at: '2026-10-28T14:32:29.527302Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: ca743dbc85c328ea499fe2c801d78e256d113812a50c78c68dbb7c3ffadfcc79
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch070/record01/validate-strict.json
  accessed_at: '2026-10-28T14:32:30.439024Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: e374b465bd6b992a49a6fbfbe0169c6ef2bab5ca7caebf2967479ab368e34fe4
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch070/record01/validate-terms.json
  accessed_at: '2026-10-28T14:32:31.443881Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 050f25a97e485d4b29f8ad0a05df4e1009870733d3967765784ded19b267148d
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch070/record01/validate-references.json
  accessed_at: '2026-10-28T14:32:32.175835Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: e003f8c618b094a65f62c87a0a03bdddc4b5e52358a17f9d7290a9614c83d24e
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and linked-stock identities
  outcome: concern
  summary: The one-owner target is exact TOGO M3118. PMC6744853 independently identifies
    Thermodesulfobium acidiphilum 3127-1T and quotes the same defined-medium context,
    referring to Frolov 2017. DSM/LPSN identity is environmental and does not make
    DSM 901a equivalent. MediaDive 6187 and 6241 are different stocks despite generic
    names.
  target_ids:
  - CultureMech:009589
  evidence_ids:
  - togo3118
  - pmc6744853
  - dsm102892
  - lpsnacidiphilum
  - deptrace
  - depvit
- assessment_id: classification
  area: representation
  topic: Classification and unsupported flags
  outcome: concern
  summary: COMPLEX/UNDEFINED conflicts with the explicitly chemically defined source
    and its enumerated chemicals. Liquid state is consistent; no universal growth
    claim is inferred. The high_metal flag needs reassessment after undoing the inflated
    stock quantities.
  target_ids:
  - CultureMech:009589
  evidence_ids:
  - togo3118
  - pmc6744853
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 81 current concentration fields are covered by 52 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009589
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b070-quantity-inventory-v1","target":"data/merge_yaml/merged/Chemically_defined_medium.yaml","quantity_field_count":81,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1002.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1002.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 1002 G_PER_L sums numerals from 1 L main water, 1000 ml trace-stock water
    and 1 L vitamin-stock water. The units and solution-stage bases differ; this is
    neither a total water volume nor a final-medium mass concentration. Keep the three
    source water inputs separate.","source_stage":"main and two separate stock batches","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The
    stored 1002 G_PER_L sums numerals from 1 L main water, 1000 ml trace-stock water
    and 1 L vitamin-stock water. The units and solution-stage bases differ; this is
    neither a total water volume nor a final-medium mass concentration. Keep the three
    source water inputs separate."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The
    stored 1002 G_PER_L sums numerals from 1 L main water, 1000 ml trace-stock water
    and 1 L vitamin-stock water. The units and solution-stage bases differ; this is
    neither a total water volume nor a final-medium mass concentration. Keep the three
    source water inputs separate."}]},{"quantity_id":"q2","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source supports 0.33 g of KH2PO4 in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main
    recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of KH2PO4 in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of KH2PO4 in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source supports 0.33 g of NH4Cl in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main
    recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of NH4Cl in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of NH4Cl in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q4","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Source
    reports 1 mg resazurin, not 1 g/L. Preserve the exact mass and unresolved final-volume
    basis; do not silently turn the source input water into a final-volume instruction.","source_stage":"main
    recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
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
    redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","decision":"conflict","rationale":"Source
    reports 1 mg resazurin, not 1 g/L. Preserve the exact mass and unresolved final-volume
    basis; do not silently turn the source input water into a final-volume instruction."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[3].concentration","decision":"conflict","rationale":"Source
    reports 1 mg resazurin, not 1 g/L. Preserve the exact mass and unresolved final-volume
    basis; do not silently turn the source input water into a final-volume instruction."}]},{"quantity_id":"q5","label":"Na2S.9H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source supports 0.5 g of Na2S.9H2O in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main
    recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"Na2S.9H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\":
    \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    source supports 0.5 g of Na2S.9H2O in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    source supports 0.5 g of Na2S.9H2O in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q6","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source supports 0.33 g of KCl in the main batch. Its 1 L water input is not an
    explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required
    denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main
    recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of KCl in the main batch. Its 1 L water input is not an
    explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required
    denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of KCl in the main batch. Its 1 L water input is not an
    explicit final-medium volume, so the unchanged G_PER_L assertion lacks the required
    denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q7","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2.8","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source supports 2.8 g of Na2SO4 in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced.","source_stage":"main
    recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"Na2SO4\",\n          \"volume\": 2.8,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\":
    \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    source supports 2.8 g of Na2SO4 in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    source supports 2.8 g of Na2SO4 in the main batch. Its 1 L water input is not
    an explicit final-medium volume, so the unchanged G_PER_L assertion lacks the
    required denominator. The source digits and supplied form are credited, not replaced."}]},{"quantity_id":"q8","label":"CaCl2.6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source supports 0.33 g of CaCl2.6H2O in the main batch. Its 1 L water input is
    not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks
    the required denominator. The source digits and supplied form are credited, not
    replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"CaCl2.6H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001163\",\n          \"gmo_id\": \"GMO_001163\",\n          \"label\":
    \"Calcium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of CaCl2.6H2O in the main batch. Its 1 L water input is
    not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks
    the required denominator. The source digits and supplied form are credited, not
    replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of CaCl2.6H2O in the main batch. Its 1 L water input is
    not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks
    the required denominator. The source digits and supplied form are credited, not
    replaced."}]},{"quantity_id":"q9","label":"MgCl2.2H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.33","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    source supports 0.33 g of MgCl2.2H2O in the main batch. Its 1 L water input is
    not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks
    the required denominator. The source digits and supplied form are credited, not
    replaced.","source_stage":"main recipe batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"MgCl2.2H2O\",\n          \"volume\": 0.33,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001266\",\n          \"gmo_id\": \"GMO_001266\",\n          \"label\":
    \"Magnesium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of MgCl2.2H2O in the main batch. Its 1 L water input is
    not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks
    the required denominator. The source digits and supplied form are credited, not
    replaced."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    source supports 0.33 g of MgCl2.2H2O in the main batch. Its 1 L water input is
    not an explicit final-medium volume, so the unchanged G_PER_L assertion lacks
    the required denominator. The source digits and supplied form are credited, not
    replaced."}]},{"quantity_id":"q10","label":"3 M HCl","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    3 M acid strength is explicit but its added amount is not. VARIABLE is an unquantified
    dose marker, not a measured concentration; retain 3 M stock identity and the source
    pH context.","source_stage":"adjustment reagent or gas headspace","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"3 M HCl\",\n          \"conc_value\": 3,\n          \"conc_unit\": \"M\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\":
    \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"To adjust the pH of the medium to 4.8, 3 M HCl was added.\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","decision":"not_quantified","rationale":"The
    3 M acid strength is explicit but its added amount is not. VARIABLE is an unquantified
    dose marker, not a measured concentration; retain 3 M stock identity and the source
    pH context."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[9].concentration","decision":"not_quantified","rationale":"The
    3 M acid strength is explicit but its added amount is not. VARIABLE is an unquantified
    dose marker, not a measured concentration; retain 3 M stock identity and the source
    pH context."}]},{"quantity_id":"q11","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    gas identity is supported, but no dissolved-medium concentration is quantified.
    VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context,
    which belong to preparation rather than mass concentration.","source_stage":"adjustment
    reagent or gas headspace","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\":
    6,\n      \"comment\": \"The medium was dispensed in 5 ml portions into 17 ml
    Hungate tubes; the head space was filled with H2/CO2 (4 : 1, 151.9 kPa).\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","decision":"not_quantified","rationale":"The
    gas identity is supported, but no dissolved-medium concentration is quantified.
    VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context,
    which belong to preparation rather than mass concentration."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[10].concentration","decision":"not_quantified","rationale":"The
    gas identity is supported, but no dissolved-medium concentration is quantified.
    VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context,
    which belong to preparation rather than mass concentration."}]},{"quantity_id":"q12","label":"Hydrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    gas identity is supported, but no dissolved-medium concentration is quantified.
    VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context,
    which belong to preparation rather than mass concentration.","source_stage":"adjustment
    reagent or gas headspace","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\":
    \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\":
    \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\":
    6,\n      \"comment\": \"The medium was dispensed in 5 ml portions into 17 ml
    Hungate tubes; the head space was filled with H2/CO2 (4 : 1, 151.9 kPa).\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","decision":"not_quantified","rationale":"The
    gas identity is supported, but no dissolved-medium concentration is quantified.
    VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context,
    which belong to preparation rather than mass concentration."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[11].concentration","decision":"not_quantified","rationale":"The
    gas identity is supported, but no dissolved-medium concentration is quantified.
    VARIABLE must not obscure the explicit headspace ratio/pressure and vessel context,
    which belong to preparation rather than mass concentration."}]},{"quantity_id":"q13","label":"Na2MoO4
    × H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"24","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"24","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 24 mg of Na2MoO4 × H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"Na2MoO4 × H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    source reports 24 mg of Na2MoO4 × H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"The
    source reports 24 mg of Na2MoO4 × H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q14","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"6","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 6 mg of H3BO3 in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    source reports 6 mg of H3BO3 in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"The
    source reports 6 mg of H3BO3 in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."}]},{"quantity_id":"q15","label":"MnCl2 × 4H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"99","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"99","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 99 mg of MnCl2 × 4H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"MnCl2 × 4H2O\",\n          \"volume\": 99,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\":
    \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    source reports 99 mg of MnCl2 × 4H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"The
    source reports 99 mg of MnCl2 × 4H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q16","label":"CoCl2 × 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"238","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"238","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 238 mg of CoCl2 × 6H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"CoCl2 × 6H2O\",\n          \"volume\": 238,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    source reports 238 mg of CoCl2 × 6H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"The
    source reports 238 mg of CoCl2 × 6H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q17","label":"ZnSO4 × 7H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"144","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"144","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 144 mg of ZnSO4 × 7H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
    \"ZnSO4 × 7H2O\",\n          \"volume\": 144,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\":
    \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    source reports 144 mg of ZnSO4 × 7H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"The
    source reports 144 mg of ZnSO4 × 7H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q18","label":"Na2WO4 × 2H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"33","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"33","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 33 mg of Na2WO4 × 2H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
    \"Na2WO4 × 2H2O\",\n          \"volume\": 33,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\":
    \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    source reports 33 mg of Na2WO4 × 2H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"The
    source reports 33 mg of Na2WO4 × 2H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q19","label":"(NH4)2SO4FeSO4 × 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"748","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"748","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 748 mg of (NH4)2SO4FeSO4 × 6H2O in this stock batch, not the same
    numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
    \"(NH4)2SO4FeSO4 × 6H2O\",\n          \"volume\": 748,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001076\",\n          \"gmo_id\": \"GMO_001076\",\n          \"label\":
    \"Ammonium iron(II) sulfate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    source reports 748 mg of (NH4)2SO4FeSO4 × 6H2O in this stock batch, not the same
    numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"The
    source reports 748 mg of (NH4)2SO4FeSO4 × 6H2O in this stock batch, not the same
    numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases."}]},{"quantity_id":"q20","label":"(NH4)2SO4NiSO4 ×
    6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"395","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"395","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 395 mg of (NH4)2SO4NiSO4 × 6H2O in this stock batch, not the same
    numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
    \"(NH4)2SO4NiSO4 × 6H2O\",\n          \"volume\": 395,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001102\",\n          \"gmo_id\": \"GMO_001102\",\n          \"label\":
    \"Ammonium nickel(II) sulfate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    source reports 395 mg of (NH4)2SO4NiSO4 × 6H2O in this stock batch, not the same
    numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"The
    source reports 395 mg of (NH4)2SO4NiSO4 × 6H2O in this stock batch, not the same
    numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases."}]},{"quantity_id":"q21","label":"Na2SeO4 × 5H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"94","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"94","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 94 mg of Na2SeO4 × 5H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
    \"Na2SeO4 × 5H2O\",\n          \"volume\": 94,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001603\",\n          \"gmo_id\": \"GMO_001603\",\n          \"label\":
    \"Sodium selenate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    source reports 94 mg of Na2SeO4 × 5H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"The
    source reports 94 mg of Na2SeO4 × 5H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q22","label":"CuCl2 × 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"238","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"238","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 238 mg of CuCl2 × 6H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"trace stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
    \"CuCl2 × 6H2O\",\n          \"volume\": 238,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001755\",\n          \"gmo_id\": \"GMO_001755\",\n          \"label\":
    \"Copper(II) chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    source reports 238 mg of CuCl2 × 6H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"The
    source reports 238 mg of CuCl2 × 6H2O in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q23","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 2 mg of Biotin in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    source reports 2 mg of Biotin in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"The
    source reports 2 mg of Biotin in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."}]},{"quantity_id":"q24","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 5 mg of p-Aminobenzoic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of p-Aminobenzoic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[23].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of p-Aminobenzoic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q25","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 10 mg of Pyridoxine hydrochloride in this stock batch, not the
    same numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"Pyridoxine hydrochloride\",\n          \"volume\": 10,\n          \"unit\":
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
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    source reports 10 mg of Pyridoxine hydrochloride in this stock batch, not the
    same numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[24].concentration","decision":"conflict","rationale":"The
    source reports 10 mg of Pyridoxine hydrochloride in this stock batch, not the
    same numeral G_PER_L directly in the receiving medium. Retain the stock composition
    separately from its 1 ml addition; no final working concentration is calculated
    without all dilution bases."}]},{"quantity_id":"q26","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 2 mg of Folic acid in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    source reports 2 mg of Folic acid in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[25].concentration","decision":"conflict","rationale":"The
    source reports 2 mg of Folic acid in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."}]},{"quantity_id":"q27","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 0.1 mg of Vitamin B12 in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    source reports 0.1 mg of Vitamin B12 in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[26].concentration","decision":"conflict","rationale":"The
    source reports 0.1 mg of Vitamin B12 in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q28","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 5 mg of Riboflavin in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Riboflavin in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[27].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Riboflavin in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."}]},{"quantity_id":"q29","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 5 mg of Nicotinic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Nicotinic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[28].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Nicotinic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q30","label":"Thiamine","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 5 mg of Thiamine in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\":
    \"Thiamine\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001230\",\n          \"gmo_id\": \"GMO_001230\",\n          \"label\":
    \"Thiamine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Thiamine in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[29].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Thiamine in this stock batch, not the same numeral G_PER_L
    directly in the receiving medium. Retain the stock composition separately from
    its 1 ml addition; no final working concentration is calculated without all dilution
    bases."}]},{"quantity_id":"q31","label":"Pantothenic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 5 mg of Pantothenic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\":
    \"Pantothenic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001616\",\n          \"gmo_id\": \"GMO_001616\",\n          \"label\":
    \"Pantothenic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Pantothenic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[30].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Pantothenic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q32","label":"Thioctic acid","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source reports 5 mg of Thioctic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases.","source_stage":"vitamin stock batch","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\":
    \"Thioctic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\":
    \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Thioctic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"ingredients[31].concentration","decision":"conflict","rationale":"The
    source reports 5 mg of Thioctic acid in this stock batch, not the same numeral
    G_PER_L directly in the receiving medium. Retain the stock composition separately
    from its 1 ml addition; no final working concentration is calculated without all
    dilution bases."}]},{"quantity_id":"q33","label":"Trace element solution receiving
    dose","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition
    differs from the named MediaDive link, so neither a generic-name link nor the
    existing dependency amount can substitute for this stock.","source_stage":"M3118
    stock addition","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Trace element solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The
    exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition
    differs from the named MediaDive link, so neither a generic-name link nor the
    existing dependency amount can substitute for this stock."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The
    exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition
    differs from the named MediaDive link, so neither a generic-name link nor the
    existing dependency amount can substitute for this stock."}]},{"quantity_id":"q34","label":"Vitamin
    solution receiving dose","local_fields":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition
    differs from the named MediaDive link, so neither a generic-name link nor the
    existing dependency amount can substitute for this stock.","source_stage":"M3118
    stock addition","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M3118\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Chemically_defined_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The
    exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition
    differs from the named MediaDive link, so neither a generic-name link nor the
    existing dependency amount can substitute for this stock."},{"path":"data/normalized_yaml/bacterial/chemically_defined_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"The
    exact M3118 stock addition is 1 ml, not 1 G_PER_L. Its local TOGO composition
    differs from the named MediaDive link, so neither a generic-name link nor the
    existing dependency amount can substitute for this stock."}]},{"quantity_id":"q35","label":"solution6187
    Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\":
    34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q36","label":"solution6187 Distilled
    water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1000","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The
    source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage.
    Retain the exact stock water input/make-up instruction without inventing a water
    fraction.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","decision":"conflict","rationale":"The
    source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage.
    Retain the exact stock water input/make-up instruction without inventing a water
    fraction."}]},{"quantity_id":"q37","label":"solution6187 FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.097","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\":
    82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q38","label":"solution6187 MnCl2
    x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"0.041","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q39","label":"solution6187 ZnCl2
    x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\":
    2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q40","label":"solution6187 CoCl2
    x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\":
    7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q41","label":"solution6187 Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\":
    8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q42","label":"solution6187 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This
    is a schema-default placeholder, not an additional ingredient or an experimentally
    quantified variable. The complete provider composition is available; retain history
    while removing the phantom ingredient in later curation.","source_stage":"metadata
    placeholder","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This
    is a schema-default placeholder, not an additional ingredient or an experimentally
    quantified variable. The complete provider composition is available; retain history
    while removing the phantom ingredient in later curation."}]},{"quantity_id":"q43","label":"solution6187
    retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","stored":"Add
    to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing
    sequence:"}],"decision":"evidence_only","rationale":"The existing preparation
    wording agrees with the exact provider stock instructions; preserve it with root-level
    path-scoped evidence. It does not prescribe the selected medium dose.","source_stage":"standalone
    stock preparation","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch070/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T14:35:51.544530Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The
    existing preparation wording agrees with the exact provider stock instructions;
    preserve it with root-level path-scoped evidence. It does not prescribe the selected
    medium dose."}]},{"quantity_id":"q44","label":"solution6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\":
    847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q45","label":"solution6241 Thiamine
    HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The
    existing attached exact recipe object and claimed raw digest match the current
    capture. The provider-declared g_l equals the local value for this standalone
    stock only. This authenticates current content, not the original access event
    or a receiving-medium dose."}]},{"quantity_id":"q46","label":"solution6241 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"Source
    gives 200 micrograms biotin and explicitly makes up to 100 ml. This supports 0.002
    g/L (200 × 10^-6 g / 0.1 L), not local 2000 G_PER_L. This correction is confined
    to solution6241; it does not identify the selected M3118 vitamin stock.","source_stage":"distinct
    standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","decision":"conflict","rationale":"Source
    gives 200 micrograms biotin and explicitly makes up to 100 ml. This supports 0.002
    g/L (200 × 10^-6 g / 0.1 L), not local 2000 G_PER_L. This correction is confined
    to solution6241; it does not identify the selected M3118 vitamin stock."}]},{"quantity_id":"q47","label":"solution6241
    Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The
    source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage.
    Retain the exact stock water input/make-up instruction without inventing a water
    fraction.","source_stage":"distinct standalone stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","decision":"conflict","rationale":"The
    source water amount is in ml; the local PERCENT_V_V numeral is not a valid percentage.
    Retain the exact stock water input/make-up instruction without inventing a water
    fraction."}]},{"quantity_id":"q48","label":"solution6241 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This
    is a schema-default placeholder, not an additional ingredient or an experimentally
    quantified variable. The complete provider composition is available; retain history
    while removing the phantom ingredient in later curation.","source_stage":"metadata
    placeholder","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This
    is a schema-default placeholder, not an additional ingredient or an experimentally
    quantified variable. The complete provider composition is available; retain history
    while removing the phantom ingredient in later curation."}]},{"quantity_id":"q49","label":"solution6241
    retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make
    up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The
    existing preparation wording agrees with the exact provider stock instructions;
    preserve it with root-level path-scoped evidence. It does not prescribe the selected
    medium dose.","source_stage":"standalone stock preparation","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch070/record05/sources/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T14:32:10.413055Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The
    existing preparation wording agrees with the exact provider stock instructions;
    preserve it with root-level path-scoped evidence. It does not prescribe the selected
    medium dose."}]},{"quantity_id":"q50","label":"M3118 source-only context 0","local_fields":[],"decision":"evidence_only","rationale":"Exact
    source context absent from the local recipe; preserve its named-medium and stage
    boundary. The paper separately confirms organism/source identity, not every TOGO
    amount.","source_stage":"source-only preparation/identity","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    1,\n      \"comment\": \"T. acidiphilum was grown under anaerobic conditions on
    a chemically defined medium (20) with CO2 as the carbon source, H2 as the electron
    donor, and sulfate as the electron acceptor.\"\n    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q51","label":"M3118
    source-only context 3","local_fields":[],"decision":"evidence_only","rationale":"Exact
    source context absent from the local recipe; preserve its named-medium and stage
    boundary. The paper separately confirms organism/source identity, not every TOGO
    amount.","source_stage":"source-only preparation/identity","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"To adjust the pH of the medium to 4.8, 3 M HCl was added.\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q52","label":"M3118 source-only
    context 4","local_fields":[],"decision":"evidence_only","rationale":"Exact source
    context absent from the local recipe; preserve its named-medium and stage boundary.
    The paper separately confirms organism/source identity, not every TOGO amount.","source_stage":"source-only
    preparation/identity","sources":[{"evidence_id":"togo3118","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3118","raw_path":"REVIEW_WORK/batch070/source01-03-preflight/togo3118.bin","raw_sha256":"6629d5ccd0d7b876b8f74de07735bed9e8b82cd70d7dd12176a425b221c8b242","text_sha256":"1a825bbac38019d248aa2ab4273c04b7f85c99f9c02f90a2ef696ec84ce8a287","accessed_at":"2026-10-28T14:31:12.414346Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\":
    6,\n      \"comment\": \"The medium was dispensed in 5 ml portions into 17 ml
    Hungate tubes; the head space was filled with H2/CO2 (4 : 1, 151.9 kPa).\"\n    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/Chemically_defined_medium.yaml":null,"data/normalized_yaml/bacterial/chemically_defined_medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted current ontology objects are nonobsolete and exact labels
    are inventoried. Confirmed hydrate/anhydrous mismatches and molybdate source conflict
    remain distinct from generic thioctic-acid stereochemical uncertainty. Correct
    calcium/magnesium hydrates, zinc sulfate hydrate, vitamin/B12 class and chloride
    identities are credited. No forced mapping is proposed for ungrounded double salts;
    legacy thiamine membership is only current-snapshot evidence, not historical validity.
  target_ids:
  - CultureMech:009589
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: Complete six reports and selected parent objects were read. October 5 source-unchecked
    triage is superseded only by the present scoped source reads. October 7 attached
    concentration claims for 6187/6241 authenticate against equal raw bytes (six plus
    two); water/biotin/placeholder exclusions are retained as prior limits, not endorsed.
    Current TOGO separates named stocks and current cleanup no longer sums; the existing
    1002 numeral is historical data, not proof of current writer execution. Naive
    dependency timestamps remain original and any verified provenance clarification
    must be appended.
  target_ids:
  - CultureMech:009589
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009589-stock-unit-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore local M3118 stock stages and units
  description: Separate the ten trace and ten vitamin stock components from direct
    main ingredients; restore their source mg amounts and separate water inputs. Preserve
    the 1 mg resazurin amount and two 1 ml stock additions. Resolve main-batch G_PER_L
    denominators before asserting final concentrations; input water does not prove
    final volume.
  target_ids:
  - CultureMech:009589
  field_paths:
  - ingredients
  - solutions[0].concentration
  - solutions[1].concentration
  evidence_ids:
  - togo3118
  - writer-togo
  - writer-cleanup
  rule_id: review-yaml-record/quantity-unit-and-stock-stage
  native_severity: P2
  normalization_reason: 'Custom quantity and solution-stage rule: the documented unit
    and stock/main-stage discrepancies materially change the represented formulation,
    so severity is major. This does not redefine native P2.3, which addresses physical-state
    mismatch.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-009589-stock-reference-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Replace unsupported generic-name stock links
  description: The M3118 trace stock is a ten-compound formulation, whereas linked
    6187 is an EDTA/iron-based six-solute stock. M3118 vitamin stock has ten vitamins,
    whereas 6241 has three. Resolve the links to exact local M3118 stocks, retaining
    comparison evidence without transferring a dependency formula or dose.
  target_ids:
  - CultureMech:009589
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[0].notes
  - solutions[1].notes
  evidence_ids:
  - togo3118
  - solution6187
  - solution6241
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-009589-missing-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Restore scoped pH and preparation evidence
  description: The source pH 4.8, acid-strength context, vessel/dispensing and gas
    headspace specifications are absent. Add only the exact supported M3118 preparation,
    with root evidence tied to its paths; no sterilization duration or main final
    volume is invented. Current parser reads root ph rather than meta.ph.
  target_ids:
  - CultureMech:009589
  field_paths:
  - ph_value
  - preparation_steps
  - evidence
  evidence_ids:
  - togo3118
  - writer-togo
  rule_id: review-yaml-record/preparation-context
  native_severity: P3
  normalization_reason: Native missing-preparation/pH concerns are normalized to major
    because the source-specific staged preparation is absent, not merely an optional
    annotation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-009589-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile supplied forms without guessing replacements
  description: Selected cobalt hexahydrate and copper hexahydrate names carry anhydrous
    chloride IDs; the molybdate formula says one water while TOGO label says dihydrate
    and the selected ID is anhydrous. Resolve that source conflict explicitly. Generic
    thioctic acid does not establish R-specific CHEBI:30314. In dependency 6187, composition[4].chebi_term
    is anhydrous CHEBI:49976 despite the six-water supplied name. Keep amount support
    distinct from chemical-form support.
  target_ids:
  - CultureMech:009589
  field_paths:
  - ingredients[12].term
  - ingredients[15].term
  - ingredients[21].term
  - ingredients[31].term
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::composition[4].chebi_term
  - ingredients[31].mediaingredientmech_chebi_term
  evidence_ids:
  - togo3118
  - solution6187
  - chebi75215
  - chebi35696
  - chebi49553
  - chebi30314
  - chebi49976
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
- finding_id: f5
  issue_key: culturemech-009589-dependency-quantity
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Repair distinct dependency units and biotin
  description: For solution 6241 only, source 200 micrograms biotin made up to 100
    ml supports 0.002 g/L rather than 2000 G_PER_L. Both standalone stocks encode
    water as 1000 PERCENT_V_V and retain phantom placeholder ingredients. Preserve
    the eight authenticated attached solute claims and stock preparation notes; repair
    remaining fields only within these dependency identities.
  target_ids:
  - CultureMech:009589
  field_paths:
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[2].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[3].concentration
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::composition[1].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::ingredients[0]
  evidence_ids:
  - solution6241
  - solution6187
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
- finding_id: f6
  issue_key: culturemech-009589-classification
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Align defined-medium classification and evidence
  description: After exact-stock reconciliation, classify this explicitly defined
    source consistently in medium_type/composition_type, reassess high_metal against
    corrected stages, replace Unknown solution names with exact source names and attach
    bibliography/claim evidence. Preserve the original history and append any verified
    correction event.
  target_ids:
  - CultureMech:009589
  field_paths:
  - medium_type
  - composition_type
  - high_metal
  - solutions[0].name
  - solutions[1].name
  - references
  - evidence
  evidence_ids:
  - togo3118
  - pmc6744853
  rule_id: review-yaml-record/classification-and-metadata
  native_severity: P2
  normalization_reason: Custom defined-medium classification and metadata rule; normalized
    minor because source identity and the chemical inventory are retained, while material
    quantitative defects are separately reported. This is distinct from native P2.4,
    which addresses file category versus target organisms.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: Separate the ten trace and ten vitamin stock components from direct
    main ingredients; restore their source mg amounts and separate water inputs. Preserve
    the 1 mg resazurin amount and two 1 ml stock additions. Resolve main-batch G_PER_L
    denominators before asserting final concentrations; input water does not prove
    final volume.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009589
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
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
  description: The M3118 trace stock is a ten-compound formulation, whereas linked
    6187 is an EDTA/iron-based six-solute stock. M3118 vitamin stock has ten vitamins,
    whereas 6241 has three. Resolve the links to exact local M3118 stocks, retaining
    comparison evidence without transferring a dependency formula or dose.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009589
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
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
  description: The source pH 4.8, acid-strength context, vessel/dispensing and gas
    headspace specifications are absent. Add only the exact supported M3118 preparation,
    with root evidence tied to its paths; no sterilization duration or main final
    volume is invented. Current parser reads root ph rather than meta.ph.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009589
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
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
  description: Selected cobalt hexahydrate and copper hexahydrate names carry anhydrous
    chloride IDs; the molybdate formula says one water while TOGO label says dihydrate
    and the selected ID is anhydrous. Resolve that source conflict explicitly. Generic
    thioctic acid does not establish R-specific CHEBI:30314. In dependency 6187, composition[4].chebi_term
    is anhydrous CHEBI:49976 despite the six-water supplied name. Keep amount support
    distinct from chemical-form support.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009589
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
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
  description: For solution 6241 only, source 200 micrograms biotin made up to 100
    ml supports 0.002 g/L rather than 2000 G_PER_L. Both standalone stocks encode
    water as 1000 PERCENT_V_V and retain phantom placeholder ingredients. Preserve
    the eight authenticated attached solute claims and stock preparation notes; repair
    remaining fields only within these dependency identities.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009589
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
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
  description: After exact-stock reconciliation, classify this explicitly defined
    source consistently in medium_type/composition_type, reassess high_metal against
    corrected stages, replace Unknown solution names with exact source names and attach
    bibliography/claim evidence. Preserve the original history and append any verified
    correction event.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009589
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chemically_defined_medium.yaml
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
- 'Full primary formulation behind Frolov2017 was unavailable: DOI returned403. The
  exact PMC supplement URL returned200 browser-check HTML, not a PDF. PMC main text
  independently corroborates identity/defined-medium use but does not authenticate
  every TOGO mass; these are explicitly database-level claims.'
- The TOGO molybdate supplied formula and ontology label disagree. Copper hydrate
  notation and generic vitamin stereochemistry are preserved as unresolved source/form
  boundaries; no inferred molecular-weight conversions.
- Provider mmol_l fields are not certified here; quantities are evaluated using exact
  source masses, declared g_l, and explicit stock make-up where available.
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
