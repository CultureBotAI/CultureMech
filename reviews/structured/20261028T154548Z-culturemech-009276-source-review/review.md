# Scientific review: Clostridium medium

- Review: 20261028T154548Z-culturemech-009276-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T15:21:54.200316Z
- Finished UTC: 2026-10-28T15:45:48.806767Z
- Reviewer: Codex batch006_validation (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ATCC 591 supports the local two-batch recipe, but flattened stock amounts, incompatible water arithmetic, wrong units and four unrelated stock links materially misrepresent it. Missing staged preparation and supplied-form mismatches require curation; thirteen authenticated standalone claims remain credited without transferring their formulations.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch071 index 03
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009276 | data/merge_yaml/merged/Clostridium_medium.yaml | generated | clostridium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009276 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009276 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009276 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009276 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact ATCC 591 and four misleading namesake stocks

identity: concern. Targets: CultureMech:009276.

The complete primary ATCC 591 and TOGO M2726 agree on the local two-batch recipe, nine-component trace stock and seven-vitamin stock. All four linked MediaDive identifiers resolve to different formulations; names alone do not establish equivalence. No organism or strain growth claim is inferred.

### Complex liquid representation

representation: supported. Targets: CultureMech:009276.

Peptone supports complex/undefined classification. The primary contains no agar and the selected liquid state is consistent. Generic medium identity does not establish a pathogen-specific use or universal growth.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009276.

74 current concentration fields are covered by 54 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b071-quantity-inventory-v1","target":"data/merge_yaml/merged/Clostridium_medium.yaml","quantity_field_count":74,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1077.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1077.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The stored 1077 G_PER_L adds the numerals 600 ml, 376 ml, 1 L and 100 ml from four different batches. Both units and solution-stage bases differ. Preserve the two receiving batches and two stock water inputs separately; no final volume follows from that sum.","source_stage":"four distinct water inputs","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 600,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 376,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 6-6","quote":"Distilled water............600.0 ml","quote_basis":"derivative text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 16-16","quote":"Distilled water........................376.0 ml","quote_basis":"derivative text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 31-31","quote":"Distilled water..............1.0 L","quote_basis":"derivative text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 41-41","quote":"Distilled water............100.0 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The stored 1077 G_PER_L adds the numerals 600 ml, 376 ml, 1 L and 100 ml from four different batches. Both units and solution-stage bases differ. Preserve the two receiving batches and two stock water inputs separately; no final volume follows from that sum."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The stored 1077 G_PER_L adds the numerals 600 ml, 376 ml, 1 L and 100 ml from four different batches. Both units and solution-stage bases differ. Preserve the two receiving batches and two stock water inputs separately; no final volume follows from that sum."}]},{"quantity_id":"q2","label":"Peptone","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium.","source_stage":"Solution 1","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Peptone\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_000012\",\n          \"gmo_id\": \"GMO_000012\",\n          \"label\": \"Peptone\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 5-5","quote":"Peptone......................5.0 g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."}]},{"quantity_id":"q3","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 12-12","quote":"K2HPO4 ..................................10.0 g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."}]},{"quantity_id":"q4","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 13-13","quote":"NaHCO3 ..................................20.0 g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."}]},{"quantity_id":"q5","label":"Fructose","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"Fructose\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001123\",\n          \"gmo_id\": \"GMO_001123\",\n          \"label\": \"D-Fructose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 11-11","quote":"Fructose................................10.0 g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."}]},{"quantity_id":"q6","label":"Sodium thioglycollate","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.75","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"Sodium thioglycollate\",\n          \"volume\": 0.75,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001132\",\n          \"gmo_id\": \"GMO_001132\",\n          \"label\": \"Sodium thioglycolate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 18-18","quote":"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust pH to 8.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit final-medium denominator. Preserve Solution 1 versus Solution 2 membership and the exact supplied material; the source does not instruct final make-up of the combined medium."}]},{"quantity_id":"q7","label":"CO2","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE truthfully retains unquantified CO2 gassing, not a dissolved concentration.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"CO2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 18-18","quote":"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust pH to 8.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully retains unquantified CO2 gassing, not a dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"VARIABLE truthfully retains unquantified CO2 gassing, not a dissolved concentration."}]},{"quantity_id":"q8","label":"Na2MoO4 . 2H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4 . 2H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 30-30","quote":"Na2MoO4 . 2H2O................3.0 mg","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[7].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[7].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q9","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 26-26","quote":"H3BO3 ........................0.03 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[8].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[8].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q10","label":"FeSO4 . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\": \"FeSO4 . 7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 23-23","quote":"FeSO4 . 7H2O .................0.2 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[9].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[9].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q11","label":"MnCl2 . 4H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[4]","quote":"{\n          \"component_name\": \"MnCl2 . 4H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 25-25","quote":"MnCl2 . 4H2O .................3.0 mg","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[10].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[10].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q12","label":"CoCl2 . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[5]","quote":"{\n          \"component_name\": \"CoCl2 . 6H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 27-27","quote":"CoCl2 . 6H2O .................0.02 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q13","label":"NiCl2 . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[6]","quote":"{\n          \"component_name\": \"NiCl2 . 6H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 29-29","quote":"NiCl2 . 6H2O .................2.0 mg","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q14","label":"ZnSO4 . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[7]","quote":"{\n          \"component_name\": \"ZnSO4 . 7H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 24-24","quote":"ZnSO4 . 7H2O .................0.01 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q15","label":"CuCl2 . 2H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[8]","quote":"{\n          \"component_name\": \"CuCl2 . 2H2O\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 28-28","quote":"CuCl2 . 2H2O ................ 1.0 mg","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q16","label":"EDTA","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[9]","quote":"{\n          \"component_name\": \"EDTA\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001237\",\n          \"gmo_id\": \"GMO_001237\",\n          \"label\": \"EDTA\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 22-22","quote":"EDTA.........................0.5 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"This is a trace-stock component, not a direct receiving-medium amount. Preserve its exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition to Solution 2. The unchanged root numeral G_PER_L both loses stock membership and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q17","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 40-40","quote":"Biotin.......................1.0 mg","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."}]},{"quantity_id":"q18","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[2]","quote":"{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 39-39","quote":"p-Aminobenzoic acid..........5.0 mg","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."}]},{"quantity_id":"q19","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[3]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 38-38","quote":"Vitamin B12..................2.0 mg","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."}]},{"quantity_id":"q20","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[4]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 35-35","quote":"Nicotinic acid...............0.05 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."}]},{"quantity_id":"q21","label":"Thiamine","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[5]","quote":"{\n          \"component_name\": \"Thiamine\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001230\",\n          \"gmo_id\": \"GMO_001230\",\n          \"label\": \"Thiamine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 34-34","quote":"Thiamine.....................0.1 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."}]},{"quantity_id":"q22","label":"Pantothenic acid","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[6]","quote":"{\n          \"component_name\": \"Pantothenic acid\",\n          \"volume\": 0.025,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001616\",\n          \"gmo_id\": \"GMO_001616\",\n          \"label\": \"Pantothenic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 36-36","quote":"Pantothenic acid.............0.025 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."}]},{"quantity_id":"q23","label":"Pyridoxine","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[7]","quote":"{\n          \"component_name\": \"Pyridoxine\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001632\",\n          \"gmo_id\": \"GMO_001632\",\n          \"label\": \"Pyridoxine\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 37-37","quote":"Pyridoxine...................0.05 g","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"This belongs to the seven-vitamin stock with a 100 ml water input and a separate 14 ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred from input water."}]},{"quantity_id":"q24","label":"Solution 1","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"600","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"600","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source describes Solution 1 with 600 ml input water; 600 G_PER_L is not that volume. Keep this local peptone batch, not the namesake FeNa-EDTA/Na2-EDTA stock 6108.","source_stage":"local batch or receiving-stock addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Solution 1\",\n          \"volume\": 600,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 6-6","quote":"Distilled water............600.0 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The source describes Solution 1 with 600 ml input water; 600 G_PER_L is not that volume. Keep this local peptone batch, not the namesake FeNa-EDTA/Na2-EDTA stock 6108."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The source describes Solution 1 with 600 ml input water; 600 G_PER_L is not that volume. Keep this local peptone batch, not the namesake FeNa-EDTA/Na2-EDTA stock 6108."}]},{"quantity_id":"q25","label":"Solution 2","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"400","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"400","unit":"G_PER_L"}}],"decision":"conflict","rationale":"TOGO labels this batch 400 ml, equal to 376 ml water plus the 10 ml and 14 ml additions. That input-volume sum is not an explicit final-volume instruction and is not 400 G_PER_L. Keep the source Solution 2 instead of unrelated stock 6109.","source_stage":"local batch or receiving-stock addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Solution 2\",\n          \"volume\": 400,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 16-16","quote":"Distilled water........................376.0 ml","quote_basis":"derivative text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"TOGO labels this batch 400 ml, equal to 376 ml water plus the 10 ml and 14 ml additions. That input-volume sum is not an explicit final-volume instruction and is not 400 G_PER_L. Keep the source Solution 2 instead of unrelated stock 6109."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"TOGO labels this batch 400 ml, equal to 376 ml water plus the 10 ml and 14 ml additions. That input-volume sum is not an explicit final-volume instruction and is not 400 G_PER_L. Keep the source Solution 2 instead of unrelated stock 6109."}]},{"quantity_id":"q26","label":"Trace Element Solution","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L. The exact local ATCC table differs from the linked standalone namesake; no stock composition transfer is justified.","source_stage":"local batch or receiving-stock addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 14-14","quote":"Trace Element Solution (see below)......10.0 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[2].concentration","decision":"conflict","rationale":"The source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L. The exact local ATCC table differs from the linked standalone namesake; no stock composition transfer is justified."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[2].concentration","decision":"conflict","rationale":"The source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L. The exact local ATCC table differs from the linked standalone namesake; no stock composition transfer is justified."}]},{"quantity_id":"q27","label":"Vitamin Solution","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"14","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"14","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L. The exact local ATCC table differs from the linked standalone namesake; no stock composition transfer is justified.","source_stage":"local batch or receiving-stock addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 15-15","quote":"Vitamin Solution (see below)............14.0 ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[3].concentration","decision":"conflict","rationale":"The source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L. The exact local ATCC table differs from the linked standalone namesake; no stock composition transfer is justified."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[3].concentration","decision":"conflict","rationale":"The source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L. The exact local ATCC table differs from the linked standalone namesake; no stock composition transfer is justified."}]},{"quantity_id":"q28","label":"6108 FeNa-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[0].concentration","stored":{"value":"2.25","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6108","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"FeNa-EDTA\",\n                \"compound_id\": 1230,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.45,\n                \"unit\": \"g\",\n                \"g_l\": 2.25,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q29","label":"6108 Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[1].concentration","stored":{"value":"2.25","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6108","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.45,\n                \"unit\": \"g\",\n                \"g_l\": 2.25,\n                \"mmol_l\": 6.69233,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q30","label":"6108 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact.","source_stage":"standalone structural placeholder","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"$.data.name","quote":"\"name\": \"Solution 1\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact."}]},{"quantity_id":"q31","label":"6108 existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"preparation_notes","stored":"Original volume: 200 mL"}],"decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence.","source_stage":"standalone preparation context","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"$.data.volume","quote":"\"volume\": 200","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q32","label":"6109 H3BO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[0].concentration","stored":{"value":"2.48","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6109","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.496,\n                \"unit\": \"g\",\n                \"g_l\": 2.48,\n                \"mmol_l\": 40.1035,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q33","label":"6109 MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[1].concentration","stored":{"value":"1.39","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6109","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.278,\n                \"unit\": \"g\",\n                \"g_l\": 1.39,\n                \"mmol_l\": 7.02357,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q34","label":"6109 (NH4)6Mo7O24 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6109","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"(NH4)6Mo7O24 x 4 H2O\",\n                \"compound_id\": 120,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\": \"g\",\n                \"g_l\": 1,\n                \"mmol_l\": 0.809153,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q35","label":"6109 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact.","source_stage":"standalone structural placeholder","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"$.data.name","quote":"\"name\": \"Solution 2\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact."}]},{"quantity_id":"q36","label":"6109 existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"preparation_notes","stored":"Original volume: 200 mL"}],"decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence.","source_stage":"standalone preparation context","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"$.data.volume","quote":"\"volume\": 200","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q37","label":"6187 Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\": \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q38","label":"6187 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1000","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The source specifies a 1000 ml water input, not 1000 percent. Preserve the input volume and stated ordered additions; no measured final-volume or water percentage is implied.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","decision":"conflict","rationale":"The source specifies a 1000 ml water input, not 1000 percent. Preserve the input volume and stated ordered additions; no measured final-volume or water percentage is implied."}]},{"quantity_id":"q39","label":"6187 FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.097","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\": 82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\": \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q40","label":"6187 MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"0.041","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\": \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q41","label":"6187 ZnCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q42","label":"6187 CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\": 7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q43","label":"6187 Na2MoO4 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\": 8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q44","label":"6187 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact.","source_stage":"standalone structural placeholder","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"$.data.name","quote":"\"name\": \"Trace element solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact."}]},{"quantity_id":"q45","label":"6187 existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","stored":"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing sequence:"}],"decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence.","source_stage":"standalone preparation context","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"$.data.volume","quote":"\"volume\": 1000","quote_basis":"raw UTF-8"},{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q46","label":"6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q47","label":"6241 Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The current raw object, claimed digest, exact compound and provider-declared g_l authenticate the existing field claim. This support is confined to this standalone stock and does not establish equivalence to ATCC 591 or recover the original access event. Provider mmol_l is not endorsed."}]},{"quantity_id":"q48","label":"6241 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The source gives 200 micrograms biotin and explicitly says make up to 100 ml: 0.0002 g / 0.1 L = 0.002 g/L in this stock, not 2000 G_PER_L. This corrected source-based rate is confined to distinct stock 6241, never substituted for the ATCC seven-vitamin stock.","source_stage":"distinct standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","decision":"conflict","rationale":"The source gives 200 micrograms biotin and explicitly says make up to 100 ml: 0.0002 g / 0.1 L = 0.002 g/L in this stock, not 2000 G_PER_L. This corrected source-based rate is confined to distinct stock 6241, never substituted for the ATCC seven-vitamin stock."}]},{"quantity_id":"q49","label":"6241 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The source says make up to 100 ml with water, not 1000 percent. Preserve that final stock make-up instruction without inventing a water volume fraction.","source_stage":"distinct standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","decision":"conflict","rationale":"The source says make up to 100 ml with water, not 1000 percent. Preserve that final stock make-up instruction without inventing a water volume fraction."}]},{"quantity_id":"q50","label":"6241 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact.","source_stage":"standalone structural placeholder","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"$.data.name","quote":"\"name\": \"Vitamin solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This is a schema placeholder, not a scientific ingredient or an amount. The real composition and supported claims must remain intact."}]},{"quantity_id":"q51","label":"6241 existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence.","source_stage":"standalone preparation context","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"$.data.volume","quote":"\"volume\": 100","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The numeric note matches the declared provider volume or exact preparation. Preserve the distinction between original provider volume, input water and explicit make-up. It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q52","label":"Source-only staged preparation 0","local_fields":[],"decision":"evidence_only","rationale":"Retain Solution 1 autoclaving separately from Solution 2 gassing, thioglycollate addition, pH 8.0 and filtration before aseptic combination. ATCC 591 gives no autoclave temperature or duration; unrelated page defaults are not transferred.","source_stage":"ATCC 591 source-only preparation","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Aseptically combine Solutions 1 and 2.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 19-19","quote":"Filter-sterilize. Aseptically combine Solutions 1 and 2.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q53","label":"Source-only staged preparation 2","local_fields":[],"decision":"evidence_only","rationale":"Retain Solution 1 autoclaving separately from Solution 2 gassing, thioglycollate addition, pH 8.0 and filtration before aseptic combination. ATCC 591 gives no autoclave temperature or duration; unrelated page defaults are not transferred.","source_stage":"ATCC 591 source-only preparation","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 5,\n      \"comment\": \"Autoclave.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 8-8","quote":"Autoclave.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q54","label":"Source-only staged preparation 4","local_fields":[],"decision":"evidence_only","rationale":"Retain Solution 1 autoclaving separately from Solution 2 gassing, thioglycollate addition, pH 8.0 and filtration before aseptic combination. ATCC 591 gives no autoclave temperature or duration; unrelated page defaults are not transferred.","source_stage":"ATCC 591 source-only preparation","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\": 8,\n      \"comment\": \"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust pH to 8.0. Filter-sterilize.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 18-18","quote":"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust pH to 8.0.","quote_basis":"derivative text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt lines 19-19","quote":"Filter-sterilize. Aseptically combine Solutions 1 and 2.","quote_basis":"derivative text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/Clostridium_medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml":null,"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml":null,"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009276.

All current ontology slots and packaged MIM rows are checked. Sodium thioglycolate, sulfate hydrates, molybdate dihydrate and the generic vitamin B12 class are consistent. Cobalt/nickel/zinc hydrate mismatches are separated from the unverified fructose anomer assertion. CHEBI:91249 is ammonium orthomolybdate and does not represent stock 6109 ammonium heptamolybdate tetrahydrate; thiamine versus thiamine hydrochloride remains source-specific. Current absence of legacy 000898 does not establish historical invalidity.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:009276.

All ten complete reports and all four exact selected parent rows were read. Thirteen existing direct-stock solute claims match current literal raw objects and claimed digests; original retrieval events are not reconstructed. Earlier water/biotin exclusions remain explicit and are now resolved only where exact source text supports the decision. Current TOGO code separates stocks and current cleanup no longer sums duplicates; these observations are not proof of historical execution. Current singleton merge copies the existing owner, preserving rather than scientifically repairing its defects.

## Findings

### f1: Separate local batches, stocks and units

major / open / confirmed; issue key: culturemech-009276-unit-and-solution-stage.

Undo the incompatible water-numeral sum and preserve the exact source batch masses, milligram units and millilitre stock additions. Move trace and vitamin amounts back to their source stages rather than treating them as direct final-medium G_PER_L. Preserve CO2 VARIABLE as truthful unquantified gas context.

### f2: Resolve all four stocks to the actual local formulations

major / open / confirmed; issue key: culturemech-009276-stock-identity.

Replace namesake links 6108/6109/6187/6241 only after representing the exact ATCC 591 local batches and stock tables. Existing standalone concentration claims remain valid in their own stock scope; none authenticates these selected-medium links.

### f3: Retain the separate preparation stages and literal evidence

major / open / confirmed; issue key: culturemech-009276-preparation-and-evidence.

Add the missing pH 8.0 and full scoped preparation: Solution 1 autoclaving versus Solution 2 gas, reductant and filtration before combination. Do not invent an autoclave temperature/duration or final volume. Attach ingredient evidence and root-level scoped solution/preparation evidence; replace Unknown solution names using the actual local identities.

### f4: Correct errors within the distinct standalone stocks

major / open / confirmed; issue key: culturemech-009276-comparison-stock-units.

For stock 6241, the source explicitly supports 200 micrograms biotin made up to 100 ml, or 0.002 g/L, not 2000 g/L. Its water is a final make-up instruction; stock 6187 water is an input. Neither is 1000 percent. Resolve the four placeholder ingredients while retaining all thirteen authenticated direct-solute claims and avoiding transfer into ATCC 591.

### f5: Reconcile hydrate and stereochemical assertions

major / open / confirmed; issue key: culturemech-009276-supplied-forms.

Selected cobalt and nickel hexahydrates carry anhydrous CHEBI:35696 and CHEBI:34887. Distinct stock 6187 zinc hexahydrate carries anhydrous CHEBI:49976 at composition[4].chebi_term; stock 6109 ammonium heptamolybdate tetrahydrate is incorrectly linked to CHEBI:91249 ammonium orthomolybdate (2:1 ammonium:molybdate). Verify and reconcile those supplied forms without changing supported mass claims. Generic fructose does not authenticate beta-D-fructofuranose in either selected primary or secondary slot; retain that specificity as unverified.

### f6: Retain exact historical context without rewriting original events

minor / open / confirmed; issue key: culturemech-009276-historical-metadata.

The four standalone stocks retain naive timestamps in their earlier quality/category events. Preserve these original bytes; append verified time context only if original provenance is recovered. The current MIM snapshot does not contain legacy MediaIngredientMech:000898; that present-day lookup is not proof that the old link was historically invalid.

## Recommended Actions And Acceptance Checks

### a1

Undo the incompatible water-numeral sum and preserve the exact source batch masses, milligram units and millilitre stock additions. Move trace and vitamin amounts back to their source stages rather than treating them as direct final-medium G_PER_L. Preserve CO2 VARIABLE as truthful unquantified gas context.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Replace namesake links 6108/6109/6187/6241 only after representing the exact ATCC 591 local batches and stock tables. Existing standalone concentration claims remain valid in their own stock scope; none authenticates these selected-medium links.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Add the missing pH 8.0 and full scoped preparation: Solution 1 autoclaving versus Solution 2 gas, reductant and filtration before combination. Do not invent an autoclave temperature/duration or final volume. Attach ingredient evidence and root-level scoped solution/preparation evidence; replace Unknown solution names using the actual local identities.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

For stock 6241, the source explicitly supports 200 micrograms biotin made up to 100 ml, or 0.002 g/L, not 2000 g/L. Its water is a final make-up instruction; stock 6187 water is an input. Neither is 1000 percent. Resolve the four placeholder ingredients while retaining all thirteen authenticated direct-solute claims and avoiding transfer into ATCC 591.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Selected cobalt and nickel hexahydrates carry anhydrous CHEBI:35696 and CHEBI:34887. Distinct stock 6187 zinc hexahydrate carries anhydrous CHEBI:49976 at composition[4].chebi_term; stock 6109 ammonium heptamolybdate tetrahydrate is incorrectly linked to CHEBI:91249 ammonium orthomolybdate (2:1 ammonium:molybdate). Verify and reconcile those supplied forms without changing supported mass claims. Generic fructose does not authenticate beta-D-fructofuranose in either selected primary or secondary slot; retain that specificity as unverified.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

The four standalone stocks retain naive timestamps in their earlier quality/category events. Preserve these original bytes; append verified time context only if original provenance is recovered. The current MIM snapshot does not contain legacy MediaIngredientMech:000898; that present-day lookup is not proof that the old link was historically invalid.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| togo2726 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726; REVIEW_WORK/batch071/source01-03-preflight/togo2726.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Exact selected-source identity preflight. Organism/source context screened before any operational assessment; no source transfer between variants. |
| atccClostridium | https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx; REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Exact selected-source identity preflight. Organism/source context screened before any operational assessment; no source transfer between variants. |
| solution6108 | https://mediadive.dsmz.de/rest/solution/6108; REVIEW_WORK/batch071/source01-03-supplement/solution6108.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| solution6109 | https://mediadive.dsmz.de/rest/solution/6109; REVIEW_WORK/batch071/source01-03-supplement/solution6109.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| solution6187 | https://mediadive.dsmz.de/rest/solution/6187; REVIEW_WORK/batch071/source01-03-supplement/solution6187.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; REVIEW_WORK/batch071/source01-03-supplement/solution6241.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/Clostridium_medium.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6108_Solution_1.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6109_Solution_2.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6108_Solution_1.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6109_Solution_2.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch071/record03/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch071/record03/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch071/record03/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components; _solution_from_item; _local_batch_volume_ml; _parse_unit; _extract_ph; _extract_preparation_steps | context_only | Current _extract_primary_components separates named local stocks; _solution_from_item retains a local stock without composition if its basis is insufficient. _parse_unit now maps mg to MG_PER_L and ml to ML_PER_L, but bare g still becomes G_PER_L and bare percent becomes PERCENT_W_V without independently proving final volume or percent basis. _extract_ph reads root ph, while these API payloads provide meta.ph. _extract_preparation_steps retains comments but its classifier checks autoclave before filtration and does not split mixed-process paragraphs. These are current behaviors, not proof of historical execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| dep6108 | data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml; Complete record | context_only | Whole distinct standalone record, including its own source claims and preparation; no equivalence to the ATCC 591 local stock is inferred. |
| dep6109 | data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml; Complete record | context_only | Whole distinct standalone record, including its own source claims and preparation; no equivalence to the ATCC 591 local stock is inferred. |
| dep6187 | data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml; Complete record | context_only | Whole distinct standalone record, including its own source claims and preparation; no equivalence to the ATCC 591 local stock is inferred. |
| dep6241 | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Complete record | context_only | Whole distinct standalone record, including its own source claims and preparation; no equivalence to the ATCC 591 local stock is inferred. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch071/source01-03-supplement/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch071/source01-03-supplement/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139; REVIEW_WORK/batch071/source01-03-supplement/chebi32139.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi28645 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28645; REVIEW_WORK/batch071/source01-03-supplement/chebi28645.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86481 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86481; REVIEW_WORK/batch071/source01-03-supplement/chebi86481.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526; REVIEW_WORK/batch071/source01-03-supplement/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch071/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch071/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; REVIEW_WORK/batch071/source01-03-supplement/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch071/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696; REVIEW_WORK/batch071/source01-03-supplement/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch071/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch071/source01-03-supplement/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch071/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:4735; REVIEW_WORK/batch071/source01-03-supplement/chebi4735.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch071/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch071/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch071/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch071/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi18385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18385; REVIEW_WORK/batch071/source01-03-supplement/chebi18385.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi7916 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:7916; REVIEW_WORK/batch071/source01-03-supplement/chebi7916.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16709 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16709; REVIEW_WORK/batch071/source01-03-supplement/chebi16709.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734; REVIEW_WORK/batch071/source01-03-supplement/chebi64734.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi91249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91249; REVIEW_WORK/batch071/source01-03-supplement/chebi91249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254; REVIEW_WORK/batch071/source01-03-supplement/chebi86254.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch071/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch071/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439; REVIEW_WORK/batch071/source01-03-supplement/chebi17439.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch071/source01-03-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch071/record03/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch071/record03/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch071/record03/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch071/record03/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch071/record03/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch071/record03/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch071/record03/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch071/record03/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch071/record03/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch071/record03/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch071/record03/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- ATCC 591 does not specify a measured final medium volume, final stock make-up for its own tables, or autoclave temperature/duration. No such values are borrowed from other sources.
- The four standalone stocks are reviewed independently because they are linked, but their valid source claims never establish equivalence to the ATCC local stocks.
- Provider mmol_l conversions are not certified; direct concentration credit uses exact declared g_l and explicit mass/final-make-up text only.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T154548Z-culturemech-009276-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Clostridium medium'
started_at: '2026-10-28T15:21:54.200316Z'
finished_at: '2026-10-28T15:45:48.806767Z'
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
summary: ATCC 591 supports the local two-batch recipe, but flattened stock amounts,
  incompatible water arithmetic, wrong units and four unrelated stock links materially
  misrepresent it. Missing staged preparation and supplied-form mismatches require
  curation; thirteen authenticated standalone claims remain credited without transferring
  their formulations.
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
  - path: data/merge_yaml/merged/Clostridium_medium.yaml
    sha256: 39e85994ab4d5c7d90454fb7e28ca4cf1b3a856f92f89fa90545bb892a9038b6
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    sha256: 0f9670b25c42e64abe7a3bc0b292a90a3624c36b7f3d5c078d4ce867c7d8b8b8
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
    sha256: 56d60c4e40bae68d41fd01929401539310e1de16699acc56006d663ea1c0693a
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    sha256: e77c0621012111c7f76ac3804b809d1f8f1a190a3b7fcc85b5ff85bcc6ef0323
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6108_Solution_1.yaml.md
    sha256: aa496483fbf67d6fe6d1ace7e94591a48659d046833334b997235ff18bda7423
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6109_Solution_2.yaml.md
    sha256: e76d0e6d0ec1963df814ebb945a09e7d611ab4579d3978d47a79e6f00d61a97b
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md
    sha256: 51447d8fea765972d4344a448ea87c9dd84eb196a0e80dbacc00290a627b10cc
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
    sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_medium.md
    sha256: 2d456417d50f00f68a2123494d7c6c12be45567147add467394321fffbd60db7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.md
    sha256: 751b182239f426effc18870274c78bfcd93004ba14ff578ec503ddff5a0f03b2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6108_Solution_1.md
    sha256: 8f70e8b9076dbebc692dd7138db5c73182816a8d138b57eb0557c47a41e51358
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6109_Solution_2.md
    sha256: 88444ea5485a75e325d26d81953a6e522b6e107d83a98f1334028d46fab6f875
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
  selection: Authoritative batch071 index 03
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009276
targets:
- target_id: CultureMech:009276
  path: data/merge_yaml/merged/Clostridium_medium.yaml
  label: clostridium_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:009276
  command: just validate-schema data/merge_yaml/merged/Clostridium_medium.yaml
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
  - CultureMech:009276
  command: just validate-strict data/merge_yaml/merged/Clostridium_medium.yaml --out
    REVIEW_WORK/batch071/record03/strict.tsv --workers 1 --quiet
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
  - CultureMech:009276
  command: just validate-terms data/merge_yaml/merged/Clostridium_medium.yaml
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
  - CultureMech:009276
  command: just validate-references data/merge_yaml/merged/Clostridium_medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: togo2726
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726
  accessed_at: '2026-10-28T15:20:21.188559Z'
  locator: REVIEW_WORK/batch071/source01-03-preflight/togo2726.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Exact selected-source identity preflight. Organism/source
    context screened before any operational assessment; no source transfer between
    variants.
  snapshot_sha256: 2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b
- evidence_id: atccClostridium
  kind: primary_source
  reference: https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx
  accessed_at: '2026-10-28T15:20:22.109787Z'
  locator: REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Exact selected-source identity preflight. Organism/source
    context screened before any operational assessment; no source transfer between
    variants.
  snapshot_sha256: 72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f
- evidence_id: solution6108
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6108
  accessed_at: '2026-10-28T15:22:22.755043Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/solution6108.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd
- evidence_id: solution6109
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6109
  accessed_at: '2026-10-28T15:22:23.083841Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/solution6109.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630
- evidence_id: solution6187
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6187
  accessed_at: '2026-10-28T15:22:23.161776Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/solution6187.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  accessed_at: '2026-10-28T15:22:23.264363Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/solution6241.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Clostridium_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T15:45:48.643968Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 39e85994ab4d5c7d90454fb7e28ca4cf1b3a856f92f89fa90545bb892a9038b6
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T15:45:48.644115Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 0f9670b25c42e64abe7a3bc0b292a90a3624c36b7f3d5c078d4ce867c7d8b8b8
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T15:45:48.644140Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T15:45:48.644432Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T15:45:48.644455Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T15:45:48.644475Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T15:45:48.644499Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6108_Solution_1.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645299Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: aa496483fbf67d6fe6d1ace7e94591a48659d046833334b997235ff18bda7423
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6109_Solution_2.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645324Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: e76d0e6d0ec1963df814ebb945a09e7d611ab4579d3978d47a79e6f00d61a97b
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645345Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 51447d8fea765972d4344a448ea87c9dd84eb196a0e80dbacc00290a627b10cc
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645368Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645388Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2d456417d50f00f68a2123494d7c6c12be45567147add467394321fffbd60db7
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645411Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 751b182239f426effc18870274c78bfcd93004ba14ff578ec503ddff5a0f03b2
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6108_Solution_1.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645432Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8f70e8b9076dbebc692dd7138db5c73182816a8d138b57eb0557c47a41e51358
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6109_Solution_2.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645452Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 88444ea5485a75e325d26d81953a6e522b6e107d83a98f1334028d46fab6f875
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645471Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 2ec3be557e14096c1fdf3abb674976cd044d552f48bafa76fc3e52d15dddbd6c
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T15:45:48.645493Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/historical-reading.json
  accessed_at: '2026-10-28T15:45:48.645517Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 9d023b2e8f76bdb9972f024b3c3b7a79b0ced8c993dd85bb89eaf082b5d05d85
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T15:45:48.645729Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 2e17943f30144eb025c558bcab6147751357c0633587b01800365ac185b591d1
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/complete-document-reader.json
  accessed_at: '2026-10-28T15:45:48.645887Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: ab3df0791371a5ecb8bd4f3e946bf2057bcdbfb7aa6db2903e77ed299992d3d6
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T15:45:48.646095Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components; _solution_from_item; _local_batch_volume_ml;
    _parse_unit; _extract_ph; _extract_preparation_steps
  accessed_at: '2026-10-28T15:45:48.646118Z'
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
  accessed_at: '2026-10-28T15:45:48.646147Z'
  support: context_only
  summary: Current _merge_ingredient_group keeps identical duplicate amounts and flags
    disagreements; it no longer sums duplicate quantities. It cannot establish compatible
    stock/main bases or repair a historical flattened sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: dep6108
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
  locator: Complete record
  accessed_at: '2026-10-28T15:45:48.654600Z'
  support: context_only
  summary: Whole distinct standalone record, including its own source claims and preparation;
    no equivalence to the ATCC 591 local stock is inferred.
  snapshot_sha256: 56d60c4e40bae68d41fd01929401539310e1de16699acc56006d663ea1c0693a
- evidence_id: dep6109
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
  locator: Complete record
  accessed_at: '2026-10-28T15:45:48.662441Z'
  support: context_only
  summary: Whole distinct standalone record, including its own source claims and preparation;
    no equivalence to the ATCC 591 local stock is inferred.
  snapshot_sha256: e77c0621012111c7f76ac3804b809d1f8f1a190a3b7fcc85b5ff85bcc6ef0323
- evidence_id: dep6187
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
  locator: Complete record
  accessed_at: '2026-10-28T15:45:48.672307Z'
  support: context_only
  summary: Whole distinct standalone record, including its own source claims and preparation;
    no equivalence to the ATCC 591 local stock is inferred.
  snapshot_sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
- evidence_id: dep6241
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Complete record
  accessed_at: '2026-10-28T15:45:48.680601Z'
  support: context_only
  summary: Whole distinct standalone record, including its own source claims and preparation;
    no equivalence to the ATCC 591 local stock is inferred.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T15:22:23.721558Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi15377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T15:22:23.382736Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi131527.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32139
  accessed_at: '2026-10-28T15:22:28.672406Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi32139.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 51709e2510736d0b63369147b10ec6ffe80d5d5c3a40605381de9b3ed78634c3
- evidence_id: chebi28645
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:28645
  accessed_at: '2026-10-28T15:22:27.201457Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi28645.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c14cd257b73dc0bd70aaf02cc24991479f6e1a57964169ac9be65d4981ffabcd
- evidence_id: chebi86481
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86481
  accessed_at: '2026-10-28T15:22:35.018587Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi86481.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 79f61c13d4412cc84b2297080689dcd9af21ef84dd46bed94617955191de53a6
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526
  accessed_at: '2026-10-28T15:22:24.592685Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi16526.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1fc9ed85cc20ea796dc5884bab2961c0cb13288fec88089767d5ca0349e6ab66
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T15:22:32.709049Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T15:22:29.628698Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  accessed_at: '2026-10-28T15:22:33.006153Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi75836.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T15:22:34.829157Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696
  accessed_at: '2026-10-28T15:22:30.558845Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi35696.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 22f49067d1405baa8e2bbd7c4405035d8663c69aa045b7bbacf363bb30729244
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T15:22:30.247758Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T15:22:29.154133Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi32312.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T15:22:34.329794Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi4735
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:4735
  accessed_at: '2026-10-28T15:22:30.914237Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi4735.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cbb8a2d2fd80b7e771711746d09aee7aaf9a8ac2dabc853617c1c08b49db4908
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T15:22:24.390247Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T15:22:27.734877Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T15:22:25.635324Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi176843.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T15:22:24.192226Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi18385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18385
  accessed_at: '2026-10-28T15:22:26.198461Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi18385.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 8751d9fa71080919eb386ddec0f27d58a47ec857d1b3d11e5922a0c192a19516
- evidence_id: chebi7916
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:7916
  accessed_at: '2026-10-28T15:22:33.623394Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi7916.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cd669aeb8ae7305e679345b84cd598247eae09bfdc58c3b28dc30aa9e1a2066a
- evidence_id: chebi16709
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16709
  accessed_at: '2026-10-28T15:22:24.670251Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi16709.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 19cc203510680cb0e4276a55e199a0730a31c5f8a1db3fa2b208d6aeaf1ab2a7
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734
  accessed_at: '2026-10-28T15:22:32.557745Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi64734.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4afcce140f81023fe7e21d1081a51e76eb83b0d89e158079ef5be695df2388ec
- evidence_id: chebi91249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91249
  accessed_at: '2026-10-28T15:22:35.522809Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi91249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3467507cd859066153a7fe667e2a73c627569bb275cc360729d9a8b15704e99
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254
  accessed_at: '2026-10-28T15:22:34.215104Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi86254.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: b3a79ee6d9359b7b827f6f87134bc166d84d3948ec20c54965c6e706aecde3a4
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T15:22:31.323766Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T15:22:31.841266Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439
  accessed_at: '2026-10-28T15:22:25.290356Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi17439.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 71dca75ee64801424c519bde7667291decd3b97f0c4e46c3d9b9405fa04a71d4
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T15:22:31.186068Z'
  locator: REVIEW_WORK/batch071/source01-03-supplement/chebi49105.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch071 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:45:48.804647Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 940e77fbec5580592f4115f95a949569308e96ea55ed455fcd07a113d1abba52
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:45:48.804761Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 2accbb9e4c434a061fb8aa70e7e57f8eaa345dddecd2d3ab0c68bceba9d1597e
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:45:48.804883Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: ece5783f0bd356da77b636f7b94db66607a62f7f6c2378016c30ca2fd078ced6
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:45:48.804962Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: c5daf818c310e2f52da5a2a6a6e1e7dc1fda219a502c52b667847554fdf18b20
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:45:48.805034Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 15ebacf9491658d8454d16a9c190cd76a7f69359c0bd6676ebc869c1d2996909
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:45:48.805066Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: abd95f54fd00bc71fa1b7f9db20af115bd03c7548da16d547c2ce9d713c85404
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch071/record03/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:45:48.805087Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: ec499eaa64f8ce20730a8ebfcf68e6ff1122380e4f0a992bf280893e7b3da4c7
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch071/record03/validate-schema.json
  accessed_at: '2026-10-28T15:21:55.220170Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 6e46f8aa2eb2b7553a89b7f5256967d072401c2a009d301a4ef2c8e2a5671513
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch071/record03/validate-strict.json
  accessed_at: '2026-10-28T15:21:56.136258Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 818eaff98818f9ef096bff85102e8883bdde02b5f543924c734053c13588bc88
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch071/record03/validate-terms.json
  accessed_at: '2026-10-28T15:21:57.151009Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 8ce3cf2229fa70e34dfa1649f84527fb4c92eb6c5d92610ec2785304f2fc2f12
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch071/record03/validate-references.json
  accessed_at: '2026-10-28T15:21:57.862925Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 0de09c59024914076d6cbe912d2bb64fa797d959dc14082bbcc9cb7a4cf72d36
assessments:
- assessment_id: identity
  area: identity
  topic: Exact ATCC 591 and four misleading namesake stocks
  outcome: concern
  summary: The complete primary ATCC 591 and TOGO M2726 agree on the local two-batch
    recipe, nine-component trace stock and seven-vitamin stock. All four linked MediaDive
    identifiers resolve to different formulations; names alone do not establish equivalence.
    No organism or strain growth claim is inferred.
  target_ids:
  - CultureMech:009276
  evidence_ids:
  - atccClostridium
  - togo2726
  - solution6108
  - solution6109
  - solution6187
  - solution6241
- assessment_id: classification
  area: representation
  topic: Complex liquid representation
  outcome: supported
  summary: Peptone supports complex/undefined classification. The primary contains
    no agar and the selected liquid state is consistent. Generic medium identity does
    not establish a pathogen-specific use or universal growth.
  target_ids:
  - CultureMech:009276
  evidence_ids:
  - atccClostridium
  - target
  - owner
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 74 current concentration fields are covered by 54 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009276
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b071-quantity-inventory-v1","target":"data/merge_yaml/merged/Clostridium_medium.yaml","quantity_field_count":74,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1077.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1077.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    stored 1077 G_PER_L adds the numerals 600 ml, 376 ml, 1 L and 100 ml from four
    different batches. Both units and solution-stage bases differ. Preserve the two
    receiving batches and two stock water inputs separately; no final volume follows
    from that sum.","source_stage":"four distinct water inputs","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 600,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 376,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 6-6","quote":"Distilled water............600.0 ml","quote_basis":"derivative
    text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 16-16","quote":"Distilled water........................376.0 ml","quote_basis":"derivative
    text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 31-31","quote":"Distilled water..............1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 41-41","quote":"Distilled water............100.0 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The
    stored 1077 G_PER_L adds the numerals 600 ml, 376 ml, 1 L and 100 ml from four
    different batches. Both units and solution-stage bases differ. Preserve the two
    receiving batches and two stock water inputs separately; no final volume follows
    from that sum."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[0].concentration","decision":"conflict","rationale":"The
    stored 1077 G_PER_L adds the numerals 600 ml, 376 ml, 1 L and 100 ml from four
    different batches. Both units and solution-stage bases differ. Preserve the two
    receiving batches and two stock water inputs separately; no final volume follows
    from that sum."}]},{"quantity_id":"q2","label":"Peptone","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium.","source_stage":"Solution 1","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"Peptone\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_000012\",\n          \"gmo_id\": \"GMO_000012\",\n          \"label\":
    \"Peptone\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 5-5","quote":"Peptone......................5.0 g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."}]},{"quantity_id":"q3","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 12-12","quote":"K2HPO4 ..................................10.0 g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."}]},{"quantity_id":"q4","label":"NaHCO3","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"NaHCO3\",\n          \"volume\": 20,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\":
    \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 13-13","quote":"NaHCO3 ..................................20.0 g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."}]},{"quantity_id":"q5","label":"Fructose","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"Fructose\",\n          \"volume\": 10,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001123\",\n          \"gmo_id\": \"GMO_001123\",\n          \"label\":
    \"D-Fructose\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 11-11","quote":"Fructose................................10.0 g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."}]},{"quantity_id":"q6","label":"Sodium thioglycollate","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.75","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium.","source_stage":"Solution 2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"Sodium thioglycollate\",\n          \"volume\": 0.75,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001132\",\n          \"gmo_id\": \"GMO_001132\",\n          \"label\":
    \"Sodium thioglycolate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 18-18","quote":"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust pH
    to 8.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    primary batch mass and TOGO amount agree, but the local G_PER_L has no explicit
    final-medium denominator. Preserve Solution 1 versus Solution 2 membership and
    the exact supplied material; the source does not instruct final make-up of the
    combined medium."}]},{"quantity_id":"q7","label":"CO2","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"VARIABLE
    truthfully retains unquantified CO2 gassing, not a dissolved concentration.","source_stage":"Solution
    2","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
    \"CO2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 18-18","quote":"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust pH
    to 8.0.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully retains unquantified CO2 gassing, not a dissolved concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"VARIABLE
    truthfully retains unquantified CO2 gassing, not a dissolved concentration."}]},{"quantity_id":"q8","label":"Na2MoO4
    . 2H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
    \"Na2MoO4 . 2H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 30-30","quote":"Na2MoO4 . 2H2O................3.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[7].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[7].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q9","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.03","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\":
    \"H3BO3\",\n          \"volume\": 0.03,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\":
    \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 26-26","quote":"H3BO3 ........................0.03 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[8].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[8].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q10","label":"FeSO4
    . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\":
    \"FeSO4 . 7H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\":
    \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 23-23","quote":"FeSO4 . 7H2O .................0.2 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[9].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[9].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q11","label":"MnCl2
    . 4H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[4]","quote":"{\n          \"component_name\":
    \"MnCl2 . 4H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\":
    \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 25-25","quote":"MnCl2 . 4H2O .................3.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[10].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[10].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q12","label":"CoCl2
    . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[5]","quote":"{\n          \"component_name\":
    \"CoCl2 . 6H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\":
    \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 27-27","quote":"CoCl2 . 6H2O .................0.02 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[11].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q13","label":"NiCl2
    . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[6]","quote":"{\n          \"component_name\":
    \"NiCl2 . 6H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\":
    \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 29-29","quote":"NiCl2 . 6H2O .................2.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[12].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q14","label":"ZnSO4
    . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[7]","quote":"{\n          \"component_name\":
    \"ZnSO4 . 7H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\":
    \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 24-24","quote":"ZnSO4 . 7H2O .................0.01 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[13].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q15","label":"CuCl2
    . 2H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[8]","quote":"{\n          \"component_name\":
    \"CuCl2 . 2H2O\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\":
    \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 28-28","quote":"CuCl2 . 2H2O ................ 1.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[14].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q16","label":"EDTA","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit.","source_stage":"ATCC 591 nine-component
    trace stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[9]","quote":"{\n          \"component_name\":
    \"EDTA\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001237\",\n          \"gmo_id\": \"GMO_001237\",\n          \"label\":
    \"EDTA\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 22-22","quote":"EDTA.........................0.5 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[15].concentration","decision":"conflict","rationale":"This
    is a trace-stock component, not a direct receiving-medium amount. Preserve its
    exact g or mg batch unit, the separate 1 L stock water input and the 10 ml addition
    to Solution 2. The unchanged root numeral G_PER_L both loses stock membership
    and, for milligram rows, changes the mass unit."}]},{"quantity_id":"q17","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 40-40","quote":"Biotin.......................1.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[16].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."}]},{"quantity_id":"q18","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 39-39","quote":"p-Aminobenzoic acid..........5.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[17].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."}]},{"quantity_id":"q19","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[3]","quote":"{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 38-38","quote":"Vitamin B12..................2.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[18].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."}]},{"quantity_id":"q20","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[4]","quote":"{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 35-35","quote":"Nicotinic acid...............0.05 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[19].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."}]},{"quantity_id":"q21","label":"Thiamine","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[5]","quote":"{\n          \"component_name\":
    \"Thiamine\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001230\",\n          \"gmo_id\": \"GMO_001230\",\n          \"label\":
    \"Thiamine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 34-34","quote":"Thiamine.....................0.1 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[20].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."}]},{"quantity_id":"q22","label":"Pantothenic acid","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[6]","quote":"{\n          \"component_name\":
    \"Pantothenic acid\",\n          \"volume\": 0.025,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001616\",\n          \"gmo_id\": \"GMO_001616\",\n          \"label\":
    \"Pantothenic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 36-36","quote":"Pantothenic acid.............0.025 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[21].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."}]},{"quantity_id":"q23","label":"Pyridoxine","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water.","source_stage":"ATCC 591 seven-vitamin stock","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[7]","quote":"{\n          \"component_name\":
    \"Pyridoxine\",\n          \"volume\": 0.05,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001632\",\n          \"gmo_id\": \"GMO_001632\",\n          \"label\":
    \"Pyridoxine\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 37-37","quote":"Pyridoxine...................0.05 g","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[4].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"ingredients[22].concentration","decision":"conflict","rationale":"This
    belongs to the seven-vitamin stock with a 100 ml water input and a separate 14
    ml addition to Solution 2. Preserve the printed g or mg batch unit; a flattened
    G_PER_L numeral is not a receiving-medium rate. No final stock volume is inferred
    from input water."}]},{"quantity_id":"q24","label":"Solution 1","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"600","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"600","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source describes Solution 1 with 600 ml input water; 600 G_PER_L is not that volume.
    Keep this local peptone batch, not the namesake FeNa-EDTA/Na2-EDTA stock 6108.","source_stage":"local
    batch or receiving-stock addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Solution 1\",\n          \"volume\": 600,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 6-6","quote":"Distilled water............600.0 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The
    source describes Solution 1 with 600 ml input water; 600 G_PER_L is not that volume.
    Keep this local peptone batch, not the namesake FeNa-EDTA/Na2-EDTA stock 6108."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[0].concentration","decision":"conflict","rationale":"The
    source describes Solution 1 with 600 ml input water; 600 G_PER_L is not that volume.
    Keep this local peptone batch, not the namesake FeNa-EDTA/Na2-EDTA stock 6108."}]},{"quantity_id":"q25","label":"Solution
    2","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"400","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"400","unit":"G_PER_L"}}],"decision":"conflict","rationale":"TOGO
    labels this batch 400 ml, equal to 376 ml water plus the 10 ml and 14 ml additions.
    That input-volume sum is not an explicit final-volume instruction and is not 400
    G_PER_L. Keep the source Solution 2 instead of unrelated stock 6109.","source_stage":"local
    batch or receiving-stock addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Solution 2\",\n          \"volume\": 400,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 16-16","quote":"Distilled water........................376.0 ml","quote_basis":"derivative
    text"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"TOGO
    labels this batch 400 ml, equal to 376 ml water plus the 10 ml and 14 ml additions.
    That input-volume sum is not an explicit final-volume instruction and is not 400
    G_PER_L. Keep the source Solution 2 instead of unrelated stock 6109."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[1].concentration","decision":"conflict","rationale":"TOGO
    labels this batch 400 ml, equal to 376 ml water plus the 10 ml and 14 ml additions.
    That input-volume sum is not an explicit final-volume instruction and is not 400
    G_PER_L. Keep the source Solution 2 instead of unrelated stock 6109."}]},{"quantity_id":"q26","label":"Trace
    Element Solution","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L.
    The exact local ATCC table differs from the linked standalone namesake; no stock
    composition transfer is justified.","source_stage":"local batch or receiving-stock
    addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"Trace Element Solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 14-14","quote":"Trace Element Solution (see below)......10.0 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[2].concentration","decision":"conflict","rationale":"The
    source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L.
    The exact local ATCC table differs from the linked standalone namesake; no stock
    composition transfer is justified."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[2].concentration","decision":"conflict","rationale":"The
    source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L.
    The exact local ATCC table differs from the linked standalone namesake; no stock
    composition transfer is justified."}]},{"quantity_id":"q27","label":"Vitamin Solution","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"14","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"14","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L.
    The exact local ATCC table differs from the linked standalone namesake; no stock
    composition transfer is justified.","source_stage":"local batch or receiving-stock
    addition","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 14,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2726\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 15-15","quote":"Vitamin Solution (see below)............14.0 ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/Clostridium_medium.yaml","field_path":"solutions[3].concentration","decision":"conflict","rationale":"The
    source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L.
    The exact local ATCC table differs from the linked standalone namesake; no stock
    composition transfer is justified."},{"path":"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml","field_path":"solutions[3].concentration","decision":"conflict","rationale":"The
    source gives a millilitre stock addition to Solution 2, not the same numeral G_PER_L.
    The exact local ATCC table differs from the linked standalone namesake; no stock
    composition transfer is justified."}]},{"quantity_id":"q28","label":"6108 FeNa-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[0].concentration","stored":{"value":"2.25","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6108","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"FeNa-EDTA\",\n                \"compound_id\":
    1230,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.45,\n                \"unit\":
    \"g\",\n                \"g_l\": 2.25,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q29","label":"6108 Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[1].concentration","stored":{"value":"2.25","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6108","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\":
    34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.45,\n                \"unit\":
    \"g\",\n                \"g_l\": 2.25,\n                \"mmol_l\": 6.69233,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q30","label":"6108 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact.","source_stage":"standalone structural
    placeholder","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"$.data.name","quote":"\"name\":
    \"Solution 1\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact."}]},{"quantity_id":"q31","label":"6108
    existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"preparation_notes","stored":"Original
    volume: 200 mL"}],"decision":"evidence_only","rationale":"The numeric note matches
    the declared provider volume or exact preparation. Preserve the distinction between
    original provider volume, input water and explicit make-up. It supplies no ATCC
    stock identity equivalence.","source_stage":"standalone preparation context","sources":[{"evidence_id":"solution6108","reference":"https://mediadive.dsmz.de/rest/solution/6108","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6108.bin","raw_sha256":"84b8d245a78f44d4212b9041f0b968ea575ae8fdb53c208942578c898d22dafd","text_sha256":"c75f63090c1176546119d2c754782be2595b439000328cfb6d652f6c6fe4df3c","accessed_at":"2026-10-28T15:22:22.755043Z","locator":"$.data.volume","quote":"\"volume\":
    200","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The
    numeric note matches the declared provider volume or exact preparation. Preserve
    the distinction between original provider volume, input water and explicit make-up.
    It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q32","label":"6109
    H3BO3","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[0].concentration","stored":{"value":"2.48","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6109","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.496,\n                \"unit\":
    \"g\",\n                \"g_l\": 2.48,\n                \"mmol_l\": 40.1035,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q33","label":"6109 MnCl2
    x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[1].concentration","stored":{"value":"1.39","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6109","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.278,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.39,\n                \"mmol_l\": 7.02357,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q34","label":"6109 (NH4)6Mo7O24
    x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6109","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"(NH4)6Mo7O24 x 4 H2O\",\n                \"compound_id\":
    120,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.2,\n                \"unit\":
    \"g\",\n                \"g_l\": 1,\n                \"mmol_l\": 0.809153,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q35","label":"6109 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact.","source_stage":"standalone structural
    placeholder","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"$.data.name","quote":"\"name\":
    \"Solution 2\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact."}]},{"quantity_id":"q36","label":"6109
    existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"preparation_notes","stored":"Original
    volume: 200 mL"}],"decision":"evidence_only","rationale":"The numeric note matches
    the declared provider volume or exact preparation. Preserve the distinction between
    original provider volume, input water and explicit make-up. It supplies no ATCC
    stock identity equivalence.","source_stage":"standalone preparation context","sources":[{"evidence_id":"solution6109","reference":"https://mediadive.dsmz.de/rest/solution/6109","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6109.bin","raw_sha256":"0237091763eabde9af4969bb91f2f115fa6bd5c7f6d81b30cdc54b7f12d78630","text_sha256":"aa6044b3294f4b159ead6031a01d70d042e9894b1822895def9096511db9cb65","accessed_at":"2026-10-28T15:22:23.083841Z","locator":"$.data.volume","quote":"\"volume\":
    200","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The
    numeric note matches the declared provider volume or exact preparation. Preserve
    the distinction between original provider volume, input water and explicit make-up.
    It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q37","label":"6187
    Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\":
    34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q38","label":"6187 Distilled
    water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1000","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The
    source specifies a 1000 ml water input, not 1000 percent. Preserve the input volume
    and stated ordered additions; no measured final-volume or water percentage is
    implied.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","decision":"conflict","rationale":"The
    source specifies a 1000 ml water input, not 1000 percent. Preserve the input volume
    and stated ordered additions; no measured final-volume or water percentage is
    implied."}]},{"quantity_id":"q39","label":"6187 FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.097","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\":
    82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q40","label":"6187 MnCl2
    x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"0.041","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q41","label":"6187 ZnCl2
    x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\":
    2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q42","label":"6187 CoCl2
    x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\":
    7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q43","label":"6187 Na2MoO4
    x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6187","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\":
    8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q44","label":"6187 placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact.","source_stage":"standalone structural
    placeholder","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"$.data.name","quote":"\"name\":
    \"Trace element solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact."}]},{"quantity_id":"q45","label":"6187
    existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","stored":"Add
    to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing
    sequence:"}],"decision":"evidence_only","rationale":"The numeric note matches
    the declared provider volume or exact preparation. Preserve the distinction between
    original provider volume, input water and explicit make-up. It supplies no ATCC
    stock identity equivalence.","source_stage":"standalone preparation context","sources":[{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"$.data.volume","quote":"\"volume\":
    1000","quote_basis":"raw UTF-8"},{"evidence_id":"solution6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6187.bin","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"29ab006e0ac5ff09ae1600726595d845c4974e377cef234694d16707c31c558b","accessed_at":"2026-10-28T15:22:23.161776Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The
    numeric note matches the declared provider volume or exact preparation. Preserve
    the distinction between original provider volume, input water and explicit make-up.
    It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q46","label":"6241
    Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\":
    847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q47","label":"6241 Thiamine
    HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed.","source_stage":"distinct standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","decision":"verified","rationale":"The
    current raw object, claimed digest, exact compound and provider-declared g_l authenticate
    the existing field claim. This support is confined to this standalone stock and
    does not establish equivalence to ATCC 591 or recover the original access event.
    Provider mmol_l is not endorsed."}]},{"quantity_id":"q48","label":"6241 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"conflict","rationale":"The
    source gives 200 micrograms biotin and explicitly says make up to 100 ml: 0.0002
    g / 0.1 L = 0.002 g/L in this stock, not 2000 G_PER_L. This corrected source-based
    rate is confined to distinct stock 6241, never substituted for the ATCC seven-vitamin
    stock.","source_stage":"distinct standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","decision":"conflict","rationale":"The
    source gives 200 micrograms biotin and explicitly says make up to 100 ml: 0.0002
    g / 0.1 L = 0.002 g/L in this stock, not 2000 G_PER_L. This corrected source-based
    rate is confined to distinct stock 6241, never substituted for the ATCC seven-vitamin
    stock."}]},{"quantity_id":"q49","label":"6241 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"conflict","rationale":"The
    source says make up to 100 ml with water, not 1000 percent. Preserve that final
    stock make-up instruction without inventing a water volume fraction.","source_stage":"distinct
    standalone stock 6241","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","decision":"conflict","rationale":"The
    source says make up to 100 ml with water, not 1000 percent. Preserve that final
    stock make-up instruction without inventing a water volume fraction."}]},{"quantity_id":"q50","label":"6241
    placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact.","source_stage":"standalone structural
    placeholder","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"$.data.name","quote":"\"name\":
    \"Vitamin solution\"","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"This
    is a schema placeholder, not a scientific ingredient or an amount. The real composition
    and supported claims must remain intact."}]},{"quantity_id":"q51","label":"6241
    existing preparation and original-volume note","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make
    up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The
    numeric note matches the declared provider volume or exact preparation. Preserve
    the distinction between original provider volume, input water and explicit make-up.
    It supplies no ATCC stock identity equivalence.","source_stage":"standalone preparation
    context","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"$.data.volume","quote":"\"volume\":
    100","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch071/source01-03-supplement/solution6241.bin","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"c5f502dbe70d9dd92187f9037fb9a22a4fa625c209cdd1704e77fc8e43866a01","accessed_at":"2026-10-28T15:22:23.264363Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","decision":"evidence_only","rationale":"The
    numeric note matches the declared provider volume or exact preparation. Preserve
    the distinction between original provider volume, input water and explicit make-up.
    It supplies no ATCC stock identity equivalence."}]},{"quantity_id":"q52","label":"Source-only
    staged preparation 0","local_fields":[],"decision":"evidence_only","rationale":"Retain
    Solution 1 autoclaving separately from Solution 2 gassing, thioglycollate addition,
    pH 8.0 and filtration before aseptic combination. ATCC 591 gives no autoclave
    temperature or duration; unrelated page defaults are not transferred.","source_stage":"ATCC
    591 source-only preparation","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Aseptically combine Solutions 1 and 2.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 19-19","quote":"Filter-sterilize. Aseptically combine Solutions 1 and 2.","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q53","label":"Source-only staged
    preparation 2","local_fields":[],"decision":"evidence_only","rationale":"Retain
    Solution 1 autoclaving separately from Solution 2 gassing, thioglycollate addition,
    pH 8.0 and filtration before aseptic combination. ATCC 591 gives no autoclave
    temperature or duration; unrelated page defaults are not transferred.","source_stage":"ATCC
    591 source-only preparation","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    5,\n      \"comment\": \"Autoclave.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 8-8","quote":"Autoclave.","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q54","label":"Source-only
    staged preparation 4","local_fields":[],"decision":"evidence_only","rationale":"Retain
    Solution 1 autoclaving separately from Solution 2 gassing, thioglycollate addition,
    pH 8.0 and filtration before aseptic combination. ATCC 591 gives no autoclave
    temperature or duration; unrelated page defaults are not transferred.","source_stage":"ATCC
    591 source-only preparation","sources":[{"evidence_id":"togo2726","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2726","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/togo2726.bin","raw_sha256":"2986e4c2fdbcf7b9caa563aa354407f895e6fcdab13afba1bbf43e882648a68b","text_sha256":"7e3be460f6e833e9678f29ea8a38a0b5ef6f630c783740cf62cf3174e11570b8","accessed_at":"2026-10-28T15:20:21.188559Z","locator":"comments[4]","quote":"{\n      \"paragraph_index\":
    8,\n      \"comment\": \"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust
    pH to 8.0. Filter-sterilize.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 18-18","quote":"Gas with CO2. Add 0.75 g Sodium thioglycollate. Adjust pH
    to 8.0.","quote_basis":"derivative text"},{"evidence_id":"atccClostridium","reference":"https://www.atcc.org/~/media/23CECE37C3794402A34CFDF21CA2DC37.ashx","raw_path":"REVIEW_WORK/batch071/source01-03-preflight/atccClostridium.bin","raw_sha256":"72fdcceacf2dfe2bf3c3f2f8b3c9582b588e418a6a5195901f9dec4e7b94c52f","text_sha256":"32b8eff5cf347abd76a5c6952fbfa6fd2946f6d23c513ad74233febb8c418d7b","accessed_at":"2026-10-28T15:20:22.109787Z","locator":"atccClostridium.txt
    lines 19-19","quote":"Filter-sterilize. Aseptically combine Solutions 1 and 2.","quote_basis":"derivative
    text"}],"layer_assessments":[]}],"document_scopes":{"data/merge_yaml/merged/Clostridium_medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml":null,"data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml":null,"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All current ontology slots and packaged MIM rows are checked. Sodium thioglycolate,
    sulfate hydrates, molybdate dihydrate and the generic vitamin B12 class are consistent.
    Cobalt/nickel/zinc hydrate mismatches are separated from the unverified fructose
    anomer assertion. CHEBI:91249 is ammonium orthomolybdate and does not represent
    stock 6109 ammonium heptamolybdate tetrahydrate; thiamine versus thiamine hydrochloride
    remains source-specific. Current absence of legacy 000898 does not establish historical
    invalidity.
  target_ids:
  - CultureMech:009276
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All ten complete reports and all four exact selected parent rows were read.
    Thirteen existing direct-stock solute claims match current literal raw objects
    and claimed digests; original retrieval events are not reconstructed. Earlier
    water/biotin exclusions remain explicit and are now resolved only where exact
    source text supports the decision. Current TOGO code separates stocks and current
    cleanup no longer sums duplicates; these observations are not proof of historical
    execution. Current singleton merge copies the existing owner, preserving rather
    than scientifically repairing its defects.
  target_ids:
  - CultureMech:009276
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009276-unit-and-solution-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate local batches, stocks and units
  description: Undo the incompatible water-numeral sum and preserve the exact source
    batch masses, milligram units and millilitre stock additions. Move trace and vitamin
    amounts back to their source stages rather than treating them as direct final-medium
    G_PER_L. Preserve CO2 VARIABLE as truthful unquantified gas context.
  target_ids:
  - CultureMech:009276
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - atccClostridium
  - togo2726
  - writer-togo
  - writer-cleanup
  rule_id: review-ingredient-concentrations/unit-and-solution-stage
  native_severity: P2
  normalization_reason: 'Custom unit/stage rule: mixed units and arithmetic across
    different solution bases materially misstate the recipe; native physical-state
    rules are not redefined.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-009276-stock-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve all four stocks to the actual local formulations
  description: Replace namesake links 6108/6109/6187/6241 only after representing
    the exact ATCC 591 local batches and stock tables. Existing standalone concentration
    claims remain valid in their own stock scope; none authenticates these selected-medium
    links.
  target_ids:
  - CultureMech:009276
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[2].term
  - solutions[3].term
  evidence_ids:
  - atccClostridium
  - togo2726
  - solution6108
  - solution6109
  - solution6187
  - solution6241
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
- finding_id: f3
  issue_key: culturemech-009276-preparation-and-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Retain the separate preparation stages and literal evidence
  description: 'Add the missing pH 8.0 and full scoped preparation: Solution 1 autoclaving
    versus Solution 2 gas, reductant and filtration before combination. Do not invent
    an autoclave temperature/duration or final volume. Attach ingredient evidence
    and root-level scoped solution/preparation evidence; replace Unknown solution
    names using the actual local identities.'
  target_ids:
  - CultureMech:009276
  field_paths:
  - ph_value
  - preparation_steps
  - evidence
  - solutions
  evidence_ids:
  - atccClostridium
  - togo2726
  - writer-togo
  rule_id: review-yaml-record/preparation-context
  native_severity: P3
  normalization_reason: Missing preparation is normalized to major because the entire
    distinct sterilization sequence and pH context are absent; placeholders alone
    would be minor.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-009276-comparison-stock-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Correct errors within the distinct standalone stocks
  description: For stock 6241, the source explicitly supports 200 micrograms biotin
    made up to 100 ml, or 0.002 g/L, not 2000 g/L. Its water is a final make-up instruction;
    stock 6187 water is an input. Neither is 1000 percent. Resolve the four placeholder
    ingredients while retaining all thirteen authenticated direct-solute claims and
    avoiding transfer into ATCC 591.
  target_ids:
  - CultureMech:009276
  field_paths:
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[2].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[3].concentration
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::composition[1].concentration
  - data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::ingredients[0]
  evidence_ids:
  - solution6241
  - solution6187
  - solution6108
  - solution6109
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
- finding_id: f5
  issue_key: culturemech-009276-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile hydrate and stereochemical assertions
  description: Selected cobalt and nickel hexahydrates carry anhydrous CHEBI:35696
    and CHEBI:34887. Distinct stock 6187 zinc hexahydrate carries anhydrous CHEBI:49976
    at composition[4].chebi_term; stock 6109 ammonium heptamolybdate tetrahydrate
    is incorrectly linked to CHEBI:91249 ammonium orthomolybdate (2:1 ammonium:molybdate).
    Verify and reconcile those supplied forms without changing supported mass claims.
    Generic fructose does not authenticate beta-D-fructofuranose in either selected
    primary or secondary slot; retain that specificity as unverified.
  target_ids:
  - CultureMech:009276
  field_paths:
  - ingredients[11].term
  - ingredients[12].term
  - ingredients[4].term
  - ingredients[4].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::composition[4].chebi_term
  - data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml::composition[2].chebi_term
  evidence_ids:
  - atccClostridium
  - togo2726
  - solution6187
  - chebi35696
  - chebi34887
  - chebi49976
  - chebi28645
  - chebi91249
  - solution6109
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    role: scoped dependency
- finding_id: f6
  issue_key: culturemech-009276-historical-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Retain exact historical context without rewriting original events
  description: The four standalone stocks retain naive timestamps in their earlier
    quality/category events. Preserve these original bytes; append verified time context
    only if original provenance is recovered. The current MIM snapshot does not contain
    legacy MediaIngredientMech:000898; that present-day lookup is not proof that the
    old link was historically invalid.
  target_ids:
  - CultureMech:009276
  field_paths:
  - ingredients[20].mediaingredientmech_term
  - data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml::curation_history[2].timestamp
  - data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml::curation_history[2].timestamp
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::curation_history[2].timestamp
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::curation_history[2].timestamp
  - data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml::curation_history[3].timestamp
  - data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml::curation_history[3].timestamp
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::curation_history[3].timestamp
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::curation_history[3].timestamp
  evidence_ids:
  - history
  - mim
  - mim-meta
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: Undo the incompatible water-numeral sum and preserve the exact source
    batch masses, milligram units and millilitre stock additions. Move trace and vitamin
    amounts back to their source stages rather than treating them as direct final-medium
    G_PER_L. Preserve CO2 VARIABLE as truthful unquantified gas context.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009276
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
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
  description: Replace namesake links 6108/6109/6187/6241 only after representing
    the exact ATCC 591 local batches and stock tables. Existing standalone concentration
    claims remain valid in their own stock scope; none authenticates these selected-medium
    links.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009276
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    role: scoped dependency
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
- action_id: a3
  description: 'Add the missing pH 8.0 and full scoped preparation: Solution 1 autoclaving
    versus Solution 2 gas, reductant and filtration before combination. Do not invent
    an autoclave temperature/duration or final volume. Attach ingredient evidence
    and root-level scoped solution/preparation evidence; replace Unknown solution
    names using the actual local identities.'
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009276
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
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
  description: For stock 6241, the source explicitly supports 200 micrograms biotin
    made up to 100 ml, or 0.002 g/L, not 2000 g/L. Its water is a final make-up instruction;
    stock 6187 water is an input. Neither is 1000 percent. Resolve the four placeholder
    ingredients while retaining all thirteen authenticated direct-solute claims and
    avoiding transfer into ATCC 591.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009276
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    role: scoped dependency
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
- action_id: a5
  description: Selected cobalt and nickel hexahydrates carry anhydrous CHEBI:35696
    and CHEBI:34887. Distinct stock 6187 zinc hexahydrate carries anhydrous CHEBI:49976
    at composition[4].chebi_term; stock 6109 ammonium heptamolybdate tetrahydrate
    is incorrectly linked to CHEBI:91249 ammonium orthomolybdate (2:1 ammonium:molybdate).
    Verify and reconcile those supplied forms without changing supported mass claims.
    Generic fructose does not authenticate beta-D-fructofuranose in either selected
    primary or secondary slot; retain that specificity as unverified.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009276
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
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
  description: The four standalone stocks retain naive timestamps in their earlier
    quality/category events. Preserve these original bytes; append verified time context
    only if original provenance is recovered. The current MIM snapshot does not contain
    legacy MediaIngredientMech:000898; that present-day lookup is not proof that the
    old link was historically invalid.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009276
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2726_Clostridium_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6108_Solution_1.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6109_Solution_2.yaml
    role: scoped dependency
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
limitations:
- ATCC 591 does not specify a measured final medium volume, final stock make-up for
  its own tables, or autoclave temperature/duration. No such values are borrowed from
  other sources.
- The four standalone stocks are reviewed independently because they are linked, but
  their valid source claims never establish equivalence to the ATCC local stocks.
- Provider mmol_l conversions are not certified; direct concentration credit uses
  exact declared g_l and explicit mass/final-make-up text only.
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
