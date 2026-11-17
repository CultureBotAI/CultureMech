# Scientific review of c41_medium

- Review: 20261028T052551Z-c41-medium-batch056
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T05:12:10.070189Z
- Finished UTC: 2026-10-28T05:25:51.202083Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

C41 retains the correct broad TOGO identity and mostly appropriate chemical forms, but several volume/milligram units and its SL-10 structure are wrong. Exact JCM 433 supports only the scoped SL-10 stock. The linked JCM 951 primary is unavailable, and listed water is not a verified final-volume denominator.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch056 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010426 | data/merge_yaml/merged/C41_MEDIUM.yaml | generated | c41_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010426 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:010426 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:010426 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:010426 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### TOGO M998 with unavailable linked JCM 951

identity: supported. Targets: CultureMech:010426.

The sole normalized contributor and target identify TOGO M998 over JCM 951. Current exact TOGO metadata agrees. JCM 951 HTTP 200 is an empty Nothing found response and cannot verify a primary recipe. C41 remains a partial scientific review for this primary-source gap.

### Organism and performance boundaries

scope: supported. Targets: CultureMech:010426.

The complete selected target and owner and the exact recipe sources name no strain or organism-specific growth experiment. Generic Microbial cultivation is a use category, not empirical growth support. No organism, incubation atmosphere, growth rate or performance claim is inferred from a medium name.

### Historical reports and current writers

provenance: concern. Targets: CultureMech:010426.

The September narrative is independently reassessed; the October target/owner concentration reports explicitly deferred source lookup rather than authenticating the quantities. Current TOGO code separates primary rows and stocks, maps mg/ml distinctly and retains comments. It still maps bare mass units to per-litre enums; _extract_ph reads a root ph key whereas these captured payloads put pH in meta. These inspected behaviors require explicit source-basis and pH review, but do not prove how the old imports ran. The current merger preserves scientific content and rejects incompatible formulations; stale generated data are not evidence that its present logic still discards these fields.

### Selected forms versus dependency forms

grounding: concern. Targets: CultureMech:010426.

All selected CHEBI labels match current canonical labels. Water, calcium chloride dihydrate, phosphate salts, magnesium chloride hexahydrate, iron sulfate heptahydrate, urea and L-cysteine hydrochloride monohydrate agree with TOGO supplied names. Resazurin is named without sodium, so its neutral CHEBI:8806 is not declared wrong. In the separate SL-10 dependency, CoCl2·6H2O and NiCl2·6H2O are instead linked to anhydrous CHEBI:35696/CHEBI:34887. The exact formulas confirm these scoped mismatches. Yeast extract/tryptone remain undefined products. Current MIM synonym rows are not historical-validity proof.

### Dependency boundary

scope: supported. Targets: CultureMech:010426.

The entire M433 YAML and JCM 433 page were read, but only SL-10 composition and dissolution instruction transfer. Its main Solution A/B amounts, main preparation, vitamins and receiving 1 ml SL-10 dose are context only, outside the C41 dependency. The empty local stock identity is partly named by preferred_term; its defect is unresolved composition and placeholder name, not absence of all source identity.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:010426.

All 24 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema":"private explicit quantity decisions v1","target_id":"CultureMech:010426","selected_concentration_field_count":24,"selected_concentration_fields_covered":24,"decisions":[{"decision_id":"q1","subject":"Distilled water","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[0].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO explicitly lists 1 L water, not 1 G_PER_L. Restore the volume, without a density conversion or inference that listed water is measured final medium volume.","sources":[{"locator":"$.components[0].items[0]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q2","subject":"CaCl2・2H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[1].concentration","original":{"value":"5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO lists 5 mg of the named supplied substance, whereas local G_PER_L retains the mg number as grams. Preserve the milligram batch amount and correct the unit scale; a measured final-litre denominator remains unverified. No physiological plausibility guess is needed.","sources":[{"locator":"$.components[0].items[1]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q3","subject":"KH2PO4","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[2].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO supports the same supplied substance and gram batch amount. Retain that amount and form. The local per-litre denominator is not explicit in a source that only lists 1 L water plus a stock addition, so qualify its basis rather than claiming exact final concentration.","sources":[{"locator":"$.components[0].items[2]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q4","subject":"K2HPO4","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO supports the same supplied substance and gram batch amount. Retain that amount and form. The local per-litre denominator is not explicit in a source that only lists 1 L water plus a stock addition, so qualify its basis rather than claiming exact final concentration.","sources":[{"locator":"$.components[0].items[3]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q5","subject":"Resazurin","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[4].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO lists 1 mg of the named supplied substance, whereas local G_PER_L retains the mg number as grams. Preserve the milligram batch amount and correct the unit scale; a measured final-litre denominator remains unverified. No physiological plausibility guess is needed.","sources":[{"locator":"$.components[0].items[4]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q6","subject":"MgCl2・6H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[5].concentration","original":{"value":"0.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO supports the same supplied substance and gram batch amount. Retain that amount and form. The local per-litre denominator is not explicit in a source that only lists 1 L water plus a stock addition, so qualify its basis rather than claiming exact final concentration.","sources":[{"locator":"$.components[0].items[5]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q7","subject":"FeSO4・7H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.25","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.25","unit":"G_PER_L"}}],"decision":"correct","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO lists 1.25 mg of the named supplied substance, whereas local G_PER_L retains the mg number as grams. Preserve the milligram batch amount and correct the unit scale; a measured final-litre denominator remains unverified. No physiological plausibility guess is needed.","sources":[{"locator":"$.components[0].items[6]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"FeSO4・7H2O\",\n          \"volume\": 1.25,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q8","subject":"Yeast extract (BD-Difco)","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[7].concentration","original":{"value":"2","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"2","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO supports the same supplied substance and gram batch amount. Retain that amount and form. The local per-litre denominator is not explicit in a source that only lists 1 L water plus a stock addition, so qualify its basis rather than claiming exact final concentration.","sources":[{"locator":"$.components[0].items[7]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q9","subject":"Tryptone (BD-Difco)","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[8].concentration","original":{"value":"2","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"2","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO supports the same supplied substance and gram batch amount. Retain that amount and form. The local per-litre denominator is not explicit in a source that only lists 1 L water plus a stock addition, so qualify its basis rather than claiming exact final concentration.","sources":[{"locator":"$.components[0].items[8]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"Tryptone (BD-Difco)\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001043\",\n          \"gmo_id\": \"GMO_001043\",\n          \"label\": \"Bacto &amp;trade; Tryptone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q10","subject":"Urea","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[9].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO supports the same supplied substance and gram batch amount. Retain that amount and form. The local per-litre denominator is not explicit in a source that only lists 1 L water plus a stock addition, so qualify its basis rather than claiming exact final concentration.","sources":[{"locator":"$.components[0].items[9]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"Urea\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001133\",\n          \"gmo_id\": \"GMO_001133\",\n          \"label\": \"Urea\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q11","subject":"L-Cysteine・HCl・H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[10].concentration","original":{"value":"0.6","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"0.6","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41 main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO supports the same supplied substance and gram batch amount. Retain that amount and form. The local per-litre denominator is not explicit in a source that only lists 1 L water plus a stock addition, so qualify its basis rather than claiming exact final concentration.","sources":[{"locator":"$.components[0].items[10]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"L-Cysteine・HCl・H2O\",\n          \"volume\": 0.6,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001205\",\n          \"gmo_id\": \"GMO_001205\",\n          \"label\": \"L-Cysteine hydrochloride monohydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q12","subject":"SL-10 working addition","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"solutions[0].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"solutions[0].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","stage":"C41 receiving stock dose","interpretation":"TOGO specifies 1 ml of SL-10 from M433, not 1 g/L. Preserve the absolute stock dose separately from stock composition. Neither 1 L nor 1.001 L is asserted as measured final medium volume.","sources":[{"locator":"$.components[0].items[11]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\": \"Trace element solution SL--10 (see Medium [M433])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M433\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q13","subject":"C41 pH adjustment","local_fields":[],"decision":"evidence_only","stage":"C41 main-medium condition","interpretation":"TOGO explicitly specifies pH 7.0 and adjustment. Retain this provider-supported condition; the unavailable JCM 951 page does not independently authenticate preparation or supply a sterilization default.","sources":[{"locator":"$.meta","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n    \"gm\": \"http://togomedium.org/medium/M998\",\n    \"name\": \"C41 Medium\",\n    \"original_media_id\": \"JCM_M951\",\n    \"src_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=951\",\n    \"ph\": \"7.0\"\n  }","quote_representation":"raw JSON object"},{"locator":"$.comments[0]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Adjust pH to 7.0.\"\n    }","quote_representation":"raw JSON object"}]},{"decision_id":"q14","subject":"Scoped SL-10: Distilled water","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"1981.0","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The SL-10 stock uses 990 ml water. The local 1981 G_PER_L aggregates multiple parent sections; it is not transferable stock water. Preserve 990 ml within SL-10 only, without treating 990 ml + 10 ml acid as measured final stock volume.","sources":[{"locator":"$.components[3].items[0]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[18]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"Distilled water\n990.0\nml","quote_representation":"HTML tr[18] DOM text"}]},{"decision_id":"q15","subject":"Scoped SL-10: Na2MoO4・2H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"36","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 36 mg of this salt. The parent record holds the same number under G_PER_L outside a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium final rate is derived.","sources":[{"locator":"$.components[3].items[1]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[17]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"Na\n2\nMoO\n4\n·2H\n2\nO\n36.0\nmg","quote_representation":"HTML tr[17] DOM text"}]},{"decision_id":"q16","subject":"Scoped SL-10: H3BO3","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 6 mg of this compound. The parent record holds the same number under G_PER_L outside a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium final rate is derived.","sources":[{"locator":"$.components[3].items[2]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[13]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"H\n3\nBO\n3\n6.0\nmg","quote_representation":"HTML tr[13] DOM text"}]},{"decision_id":"q17","subject":"Scoped SL-10: MnCl2・4H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 100 mg of this salt. The parent record holds the same number under G_PER_L outside a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium final rate is derived.","sources":[{"locator":"$.components[3].items[3]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[12]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"MnCl\n2\n·4H\n2\nO\n100.0\nmg","quote_representation":"HTML tr[12] DOM text"}]},{"decision_id":"q18","subject":"Scoped SL-10: CoCl2・6H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 190 mg of this salt. The parent record holds the same number under G_PER_L outside a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium final rate is derived.","sources":[{"locator":"$.components[3].items[4]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[14]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"CoCl\n2\n·6H\n2\nO\n190.0\nmg","quote_representation":"HTML tr[14] DOM text"}]},{"decision_id":"q19","subject":"Scoped SL-10: NiCl2・6H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 24 mg of this salt. The parent record holds the same number under G_PER_L outside a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium final rate is derived.","sources":[{"locator":"$.components[3].items[5]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[16]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"NiCl\n2\n·6H\n2\nO\n24.0\nmg","quote_representation":"HTML tr[16] DOM text"}]},{"decision_id":"q20","subject":"Scoped SL-10: CuCl2・2H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 2 mg of this salt. The parent record holds the same number under G_PER_L outside a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium final rate is derived.","sources":[{"locator":"$.components[3].items[6]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[15]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"CuCl\n2\n·2H\n2\nO\n2.0\nmg","quote_representation":"HTML tr[15] DOM text"}]},{"decision_id":"q21","subject":"Scoped SL-10: ZnCl2","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"70","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 70 mg of this salt. The parent record holds the same number under G_PER_L outside a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium final rate is derived.","sources":[{"locator":"$.components[3].items[7]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[11]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"ZnCl\n2\n70.0\nmg","quote_representation":"HTML tr[11] DOM text"}]},{"decision_id":"q22","subject":"Scoped SL-10: HCl (25%, 7.7 M)","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","stage":"separate SL-10 stock formulation","interpretation":"This is 10 ml of HCl solution labelled 25%, 7.7 M, not 10 g/L HCl. Preserve both source strength descriptions and stock-stage dose; no unprinted percentage basis or density conversion is supplied.","sources":[{"locator":"$.components[3].items[8]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"HCl (25%, 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[9]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"HCl (25%, 7.7 M)\n10.0\nml","quote_representation":"HTML tr[9] DOM text"}]},{"decision_id":"q23","subject":"Scoped SL-10: FeCl2・4H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"1.5","unit":"G_PER_L"}}],"decision":"unsupported","stage":"separate SL-10 stock formulation","interpretation":"The source specifies 1.5 g iron dichloride tetrahydrate for the SL-10 stock batch. Keep that salt form and quantity, but not as a direct C41 ingredient or a verified final-medium G/L value.","sources":[{"locator":"$.components[3].items[9]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw JSON object"},{"locator":"HTML tr[10]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"FeCl\n2\n·4H\n2\nO\n1.5\ng","quote_representation":"HTML tr[10] DOM text"}]},{"decision_id":"q24","subject":"SL-10 dissolution order","local_fields":[],"decision":"evidence_only","stage":"stock preparation only","interpretation":"Dissolve iron chloride first in the acid, then dilute and add the other salts as the primary says. JCM 433 main-medium autoclaving, vitamin filtration and pH are outside this stock dependency and do not transfer to C41.","sources":[{"locator":"extracted-text lines 105-109","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"Dissolve FeCl\n2\n·4H\n2\nO first in HCl. Then dilute in distilled water and add the remaining salts.","quote_representation":"captured extracted text"}]},{"decision_id":"q25","subject":"Unresolved C41 preparation controls","local_fields":[],"decision":"not_quantified","stage":"unavailable primary preparation","interpretation":"TOGO has only the pH-adjustment comment and JCM 951 says Nothing found. No autoclave cycle, urea sterilization, gas, incubation or stock-addition order beyond the explicit dose is imported from another medium.","sources":[{"locator":"$.comments[0]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Adjust pH to 7.0.\"\n    }","quote_representation":"raw JSON object"},{"locator":"extracted-text lines 4-4","source_key":"jcm951","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=951","source_raw_sha256":"9444154f4322dcdd0d815d926c10d3e6f1da364be2278122ae0ace8fd866f080","source_text_sha256":"97559e145c2d45b5262bd1068383785f04c81089c08844af582276f2da801767","accessed_at":"2026-10-28T05:12:25.749928Z","exact_source_quote":"Nothing found.","quote_representation":"captured extracted text"}]}],"local_field_census_reference":"REVIEW_WORK/batch056/record06/grounding-inventory.json","source_only_gaps_are_explicit":true,"note":"Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:010426.

data/merge_yaml/merged/C41_MEDIUM.yaml: primary 9/11, secondary 5/11; data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml: primary 9/11, secondary 5/11. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI/UBERON term is joined to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Native structural checks

schema: supported. Targets: CultureMech:010426.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: C41 water and three milligram rows have incorrect local units

major / open / confirmed; issue key: culturemech-010426-main-source-unit-slips.

Water 1 L became 1 G_PER_L; calcium chloride dihydrate 5 mg, resazurin 1 mg and iron sulfate heptahydrate 1.25 mg retain their numbers under G_PER_L. TOGO provides direct unit evidence, although the linked primary is currently unavailable.

### f2: SL-10 dose and stock composition are unresolved

major / open / confirmed; issue key: culturemech-010426-stock-unresolved.

The source 1 ml addition is stored as 1 G_PER_L with empty composition and Unknown solution name. The named M433 relationship is meaningful but its current YAML has flattened stock amounts and cannot be reused wholesale.

### f3: The candidate dependency contains stock-unit and hydrate mismatches

major / open / confirmed; issue key: culturemech-010426-sl10-dependency.

M433 stores SL-10 milligram salts as G_PER_L and acid volume as mass, aggregates water across sections, and assigns Co/Ni hexahydrate names anhydrous primary identifiers. Correct only these explicitly scoped stock claims before linking; the parent medium remains separate.

### f4: Unchanged gram amounts have an unverified final-volume basis

minor / open / confirmed; issue key: culturemech-010426-main-denominator.

The remaining main amounts match TOGO grams, but local G_PER_L assumes a final litre that is not explicitly established by 1 L water plus 1 ml stock. The older narrative also used per-litre wording without resolving this distinction.

### f5: Provider-supported pH and claim evidence are missing

minor / open / confirmed; issue key: culturemech-010426-missing-ph-evidence.

TOGO states pH 7.0 and an adjustment instruction. Neither selected layer contains that condition, structured source references or attached formulation evidence. The missing primary and zero native reference checks must remain explicit.

## Recommended Actions And Acceptance Checks

### action1

Repair the source unit scale and preserve batch water separately; qualify provider-only authentication and avoid a guessed final denominator.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Resolve only the exact SL-10 stock and preserve its C41 volume dose; exclude parent main medium and vitamins.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Repair the exact SL-10 subgraph and source forms with claim-scoped evidence before reuse; do not transfer the parent receiving dose, main salts or vitamins.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Keep the matched gram amounts and supplied forms, explicitly annotate the batch basis, and defer any final concentration calculation.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Preserve exact TOGO pH and source claims with current capture metadata, and retain the unresolved primary/preparation boundary rather than borrowing a general JCM cycle.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/C41_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch056/record06/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch056/record06/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch056/record06/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch056/record06/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| togoM998 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| jcm951 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=951; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Current JCM 951 HTTP 200 body says Nothing found; no recipe or sterilization default transferred from this unavailable primary. |
| jcm433 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full current JCM 433 read; ONLY Trace element solution SL-10 table and its dissolution instruction are dependencies of C41. Main medium, vitamins and main preparation excluded. |
| togoM433 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current source read, including exact identity, all formulation rows, units and preparation. It establishes a formulation, not strain-specific growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16199 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16199 = urea; definition ['A carbonyl group with two C-bound amine groups. The commercially available fertilizer has an analysis of 46-0-0 (N-P2O5-K2O).']; formula ['CH4N2O']; mass ['60.056']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17754 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17754 = glycerol; definition ['A triol with a structure of propane substituted at positions 1, 2 and 3 by hydroxy groups.']; formula ['C3H8O3']; mass ['92.094']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt salt in which the cobalt metal is in the +2 oxidation state and the counter-anion is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co']; mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage treatments; for solid-dosage treatments, the monohydrate is normally used).']; formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:91248 = L-cysteine hydrochloride hydrate; definition ['A hydrate that is the monohydrate form of &lt;small&gt;L&lt;/small&gt;-cysteine hydrochloride.']; formula ['C3H7NO2S.H2O.HCl']; mass ['175.637']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch056/record06/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T012902Z-C41_MEDIUM.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M998_C41_Medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/C41_MEDIUM.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.md; entire report | supports | Entire historical report read, including unresolved and unchanged rows. October reports are derivative assertions with original cited hash/time; their raw payload is not authenticated by the report alone. September narratives are historical leads reassessed against current captures, not fresh review proof. |
| writer45 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer46 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer47 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer48 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch056/record06/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Current JCM 951 HTTP 200 body says Nothing found. TOGO supports the documented comparisons, but no primary C41 preparation or strain-growth evidence is recovered. A bounded ignored-inclusive search of the old batch048-tail cache path and durable preserved task evidence found no jcm951/M998/C41 capture filename; this is not a universal absence claim.
- Only JCM 433 SL-10 transfers. Main parent medium, vitamins, its receiving stock dose and generic sterilization header are excluded from C41.
- The stock lists 990 ml water plus 10 ml acid; C41 lists 1 L water plus 1 ml stock. Neither sum is promoted to a measured final volume. Current ontology/MIM labels do not establish historical mapping validity.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T052551Z-c41-medium-batch056
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of c41_medium
started_at: '2026-10-28T05:12:10.070189Z'
finished_at: '2026-10-28T05:25:51.202083Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: C41 retains the correct broad TOGO identity and mostly appropriate chemical
  forms, but several volume/milligram units and its SL-10 structure are wrong. Exact
  JCM 433 supports only the scoped SL-10 stock. The linked JCM 951 primary is unavailable,
  and listed water is not a verified final-volume denominator.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
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
  - path: data/merge_yaml/merged/C41_MEDIUM.yaml
    sha256: 33bab0dad8f7e1aedaf97c91f56375a4253e74b5aed74fd9d8f60401981cf3c7
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml
    sha256: 33a016afbc69069242603dff0c39d8ac64e71684294d8279416564e597648f8c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    sha256: 84df0c00112e77dd961d5cb7aa78a718c1166de387bf62d1515cb9d291fa42e6
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/C41_MEDIUM.md
    sha256: 278b36c5961334b0628b9fb299863e27419874aa0765b70ed95e80584f7ad8e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.md
    sha256: b8dc545f539ed8a12e5cff552763630f422cf22e800196a900387707bb3b1994
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M998_C41_Medium.md
    sha256: f1a4a898ef5eaa6adaa84d863b092c6fff8b18b8ea72f9089d3225b08e85cbb1
    role: context
  - path: reports/yaml_record_review/20260922T012902Z-C41_MEDIUM.md
    sha256: 1620764b8f1d89c12f02ac2688efd50f4c70131b2f9b37f5d04a074c1a260249
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
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
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch056 selection index 6 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010426
targets:
- target_id: CultureMech:010426
  path: data/merge_yaml/merged/C41_MEDIUM.yaml
  label: c41_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:010426
  command: just validate-schema data/merge_yaml/merged/C41_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:010426
  command: just validate-strict data/merge_yaml/merged/C41_MEDIUM.yaml --workers 1
    --out REVIEW_WORK/batch056/record06/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:010426
  command: just validate-terms data/merge_yaml/merged/C41_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:010426
  command: just validate-references data/merge_yaml/merged/C41_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/C41_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T05:18:11.058433Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 33bab0dad8f7e1aedaf97c91f56375a4253e74b5aed74fd9d8f60401981cf3c7
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T05:18:11.058597Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 84df0c00112e77dd961d5cb7aa78a718c1166de387bf62d1515cb9d291fa42e6
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch056/record06/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:11.220547Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 40ff371cefe9b1984707a707c1fcbf45c7bfdf2b615f047c234c25df8d482bdc
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch056/record06/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:12.280023Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 40a22c011c730bd23a463897e10f20985d6ca2c1fb8d9256c057de10e9ba224f
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch056/record06/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:13.461836Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 9cf68d197567f12596ec93b9ece8c163abd72fe5f14fd3528a24cc44aeac36d4
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch056/record06/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T05:12:14.208036Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 6345ab803cfeffe55b43a7c4a328d910ae032cf1b7681769fa5a381c11f73f16
- evidence_id: togoM998
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:25.740041Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: 41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7
- evidence_id: jcm951
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=951
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:25.749928Z'
  support: unknown
  summary: Current JCM 951 HTTP 200 body says Nothing found; no recipe or sterilization
    default transferred from this unavailable primary.
  snapshot_sha256: 9444154f4322dcdd0d815d926c10d3e6f1da364be2278122ae0ace8fd866f080
- evidence_id: jcm433
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:25.760817Z'
  support: supports
  summary: Full current JCM 433 read; ONLY Trace element solution SL-10 table and
    its dissolution instruction are dependencies of C41. Main medium, vitamins and
    main preparation excluded.
  snapshot_sha256: bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b
- evidence_id: togoM433
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T05:12:25.936433Z'
  support: supports
  summary: Complete current source read, including exact identity, all formulation
    rows, units and preparation. It establishes a formulation, not strain-specific
    growth.
  snapshot_sha256: b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131527
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:25.953160Z'
  support: supports
  summary: OLS current exact CHEBI:131527 = dipotassium hydrogen phosphate; definition
    ['A potassium salt that is the dipotassium salt of phosphoric acid.']; formula
    ['HO4P.2K']; mass ['174.174']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 349a12965f35042f5768040a63856b162c81bac3541674d571ac980605f846b3
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.313769Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.330974Z'
  support: supports
  summary: OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic
    acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy
    group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.341030Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16199
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16199
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.359404Z'
  support: supports
  summary: OLS current exact CHEBI:16199 = urea; definition ['A carbonyl group with
    two C-bound amine groups. The commercially available fertilizer has an analysis
    of 46-0-0 (N-P2O5-K2O).']; formula ['CH4N2O']; mass ['60.056']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5298ca6b7d402b8a6e2091f03adf139a2d777c9614d760976b3953bc88bd862e
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.578976Z'
  support: supports
  summary: OLS current exact CHEBI:17015 = riboflavin; definition ['<small>D</small>-Ribitol
    in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[<em>g</em>]pteridin-10(2<em>H</em>)-yl
    moiety. It is a nutritional factor found in milk, eggs, malted barley, liver,
    kidney, heart, and leafy vegetables, but the richest natural source is yeast.
    The free form occurs only in the retina of the eye, in whey, and in urine; its
    principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine
    dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.617689Z'
  support: supports
  summary: OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of
    a group of cobalamin vitamers that exhibit biological activity against vitamin
    B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
    deficiency is associated with low red blood cell count and anemia. The vitamers
    are found in foods such as cereals, meat, fish, and poultry. The vitamers include
    adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin
    and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi17754
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17754
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.933632Z'
  support: supports
  summary: OLS current exact CHEBI:17754 = glycerol; definition ['A triol with a structure
    of propane substituted at positions 1, 2 and 3 by hydroxy groups.']; formula ['C3H8O3'];
    mass ['92.094']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 0231975176416cbaad3ad04c9efeedbe9bef0b826645e592a4a2f511e8d1db95
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.967763Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:26.990395Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.067569Z'
  support: supports
  summary: OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic
    acid in which the amino group is <em>para</em> to the carboxy group.']; formula
    ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.208333Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.324125Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.567178Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.585957Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.627128Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.704724Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.851465Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_35696
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:27.916339Z'
  support: supports
  summary: OLS current exact CHEBI:35696 = cobalt dichloride; definition ['A cobalt
    salt in which the cobalt metal is in the +2 oxidation state and the counter-anion
    is chloride. It is used as an indicator for water in desiccants.']; formula ['2Cl.Co'];
    mass ['129.839']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: d9d394d79450b1671c699eaa08d3ef5d66d1f14909f1bd9c464b3d457e37a7ca
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.192976Z'
  support: supports
  summary: OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound
    of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms,
    in each of which the Zn<small><sup>2+</small></sup> ions are trigonal planar coordinated
    to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.198828Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.261488Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.320280Z'
  support: supports
  summary: OLS current exact CHEBI:75836 = iron(2+) sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of iron(2+) sulfate. It is used as a
    source of iron in the treatment of iron-deficiency anaemia (generally in liquid-dosage
    treatments; for solid-dosage treatments, the monohydrate is normally used).'];
    formula ['Fe.7H2O.O4S']; mass ['278.013']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.453873Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.525768Z'
  support: supports
  summary: OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O'];
    mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.788223Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.812132Z'
  support: supports
  summary: OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition
    ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg'];
    mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.872038Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:28.934500Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91248
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T05:12:29.042837Z'
  support: supports
  summary: OLS current exact CHEBI:91248 = L-cysteine hydrochloride hydrate; definition
    ['A hydrate that is the monohydrate form of <small>L</small>-cysteine hydrochloride.'];
    formula ['C3H7NO2S.H2O.HCl']; mass ['175.637']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 7ef9e26cec1a5833d216a01df066c0b6a0bfba77bad16db354c690a7a814a683
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch056/record06/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T05:18:11.069306Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: d9a9677b1dc0fdbdb41a8b2465d731f0279389db2803ee6b9d6505d77c90c8ba
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T012902Z-C41_MEDIUM.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:11.069340Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: 1620764b8f1d89c12f02ac2688efd50f4c70131b2f9b37f5d04a074c1a260249
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M998_C41_Medium.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:11.069368Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: f1a4a898ef5eaa6adaa84d863b092c6fff8b18b8ea72f9089d3225b08e85cbb1
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/C41_MEDIUM.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:11.069393Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: 278b36c5961334b0628b9fb299863e27419874aa0765b70ed95e80584f7ad8e1
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.md
  locator: entire report
  accessed_at: '2026-10-28T05:18:11.069415Z'
  support: supports
  summary: Entire historical report read, including unresolved and unchanged rows.
    October reports are derivative assertions with original cited hash/time; their
    raw payload is not authenticated by the report alone. September narratives are
    historical leads reassessed against current captures, not fresh review proof.
  snapshot_sha256: b8dc545f539ed8a12e5cff552763630f422cf22e800196a900387707bb3b1994
- evidence_id: writer45
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:11.069450Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer46
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:11.069470Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer47
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:11.069490Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer48
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T05:18:11.069511Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch056/record06/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T05:18:11.137540Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 07f21f30bcfb6b4943d1ae3218ea65aef7fd67e9b4bdd1ea59ce84ce19ffcd79
assessments:
- assessment_id: a1
  area: identity
  topic: TOGO M998 with unavailable linked JCM 951
  outcome: supported
  summary: The sole normalized contributor and target identify TOGO M998 over JCM
    951. Current exact TOGO metadata agrees. JCM 951 HTTP 200 is an empty Nothing
    found response and cannot verify a primary recipe. C41 remains a partial scientific
    review for this primary-source gap.
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - local0
  - local1
  - togoM998
  - jcm951
- assessment_id: a2
  area: scope
  topic: Organism and performance boundaries
  outcome: supported
  summary: The complete selected target and owner and the exact recipe sources name
    no strain or organism-specific growth experiment. Generic Microbial cultivation
    is a use category, not empirical growth support. No organism, incubation atmosphere,
    growth rate or performance claim is inferred from a medium name.
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - togoM998
  - jcm951
  - jcm433
  - local0
  - local1
- assessment_id: a3
  area: provenance
  topic: Historical reports and current writers
  outcome: concern
  summary: The September narrative is independently reassessed; the October target/owner
    concentration reports explicitly deferred source lookup rather than authenticating
    the quantities. Current TOGO code separates primary rows and stocks, maps mg/ml
    distinctly and retains comments. It still maps bare mass units to per-litre enums;
    _extract_ph reads a root ph key whereas these captured payloads put pH in meta.
    These inspected behaviors require explicit source-basis and pH review, but do
    not prove how the old imports ran. The current merger preserves scientific content
    and rejects incompatible formulations; stale generated data are not evidence that
    its present logic still discards these fields.
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - local0
  - local1
  - history0
  - history1
  - history2
  - history3
  - writer45
  - writer46
  - writer47
  - writer48
- assessment_id: a4
  area: grounding
  topic: Selected forms versus dependency forms
  outcome: concern
  summary: All selected CHEBI labels match current canonical labels. Water, calcium
    chloride dihydrate, phosphate salts, magnesium chloride hexahydrate, iron sulfate
    heptahydrate, urea and L-cysteine hydrochloride monohydrate agree with TOGO supplied
    names. Resazurin is named without sodium, so its neutral CHEBI:8806 is not declared
    wrong. In the separate SL-10 dependency, CoCl2·6H2O and NiCl2·6H2O are instead
    linked to anhydrous CHEBI:35696/CHEBI:34887. The exact formulas confirm these
    scoped mismatches. Yeast extract/tryptone remain undefined products. Current MIM
    synonym rows are not historical-validity proof.
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - grounding
  - togoM998
  - jcm433
  - chebi35696
  - chebi34887
  - chebi8806
  - chebi91248
- assessment_id: a5
  area: scope
  topic: Dependency boundary
  outcome: supported
  summary: The entire M433 YAML and JCM 433 page were read, but only SL-10 composition
    and dissolution instruction transfer. Its main Solution A/B amounts, main preparation,
    vitamins and receiving 1 ml SL-10 dose are context only, outside the C41 dependency.
    The empty local stock identity is partly named by preferred_term; its defect is
    unresolved composition and placeholder name, not absence of all source identity.
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - jcm433
  - togoM433
  - grounding
- assessment_id: a6
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 24 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - quantity-inventory
  details: '{"schema":"private explicit quantity decisions v1","target_id":"CultureMech:010426","selected_concentration_field_count":24,"selected_concentration_fields_covered":24,"decisions":[{"decision_id":"q1","subject":"Distilled
    water","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[0].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    explicitly lists 1 L water, not 1 G_PER_L. Restore the volume, without a density
    conversion or inference that listed water is measured final medium volume.","sources":[{"locator":"$.components[0].items[0]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"}]},{"decision_id":"q2","subject":"CaCl2・2H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[1].concentration","original":{"value":"5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[1].concentration","original":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    lists 5 mg of the named supplied substance, whereas local G_PER_L retains the
    mg number as grams. Preserve the milligram batch amount and correct the unit scale;
    a measured final-litre denominator remains unverified. No physiological plausibility
    guess is needed.","sources":[{"locator":"$.components[0].items[1]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"}]},{"decision_id":"q3","subject":"KH2PO4","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[2].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[2].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    supports the same supplied substance and gram batch amount. Retain that amount
    and form. The local per-litre denominator is not explicit in a source that only
    lists 1 L water plus a stock addition, so qualify its basis rather than claiming
    exact final concentration.","sources":[{"locator":"$.components[0].items[2]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q4","subject":"K2HPO4","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[3].concentration","original":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    supports the same supplied substance and gram batch amount. Retain that amount
    and form. The local per-litre denominator is not explicit in a source that only
    lists 1 L water plus a stock addition, so qualify its basis rather than claiming
    exact final concentration.","sources":[{"locator":"$.components[0].items[3]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q5","subject":"Resazurin","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[4].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[4].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    lists 1 mg of the named supplied substance, whereas local G_PER_L retains the
    mg number as grams. Preserve the milligram batch amount and correct the unit scale;
    a measured final-litre denominator remains unverified. No physiological plausibility
    guess is needed.","sources":[{"locator":"$.components[0].items[4]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\":
    \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q6","subject":"MgCl2・6H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[5].concentration","original":{"value":"0.5","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[5].concentration","original":{"value":"0.5","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    supports the same supplied substance and gram batch amount. Retain that amount
    and form. The local per-litre denominator is not explicit in a source that only
    lists 1 L water plus a stock addition, so qualify its basis rather than claiming
    exact final concentration.","sources":[{"locator":"$.components[0].items[5]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q7","subject":"FeSO4・7H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.25","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"1.25","unit":"G_PER_L"}}],"decision":"correct","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    lists 1.25 mg of the named supplied substance, whereas local G_PER_L retains the
    mg number as grams. Preserve the milligram batch amount and correct the unit scale;
    a measured final-litre denominator remains unverified. No physiological plausibility
    guess is needed.","sources":[{"locator":"$.components[0].items[6]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"FeSO4・7H2O\",\n          \"volume\": 1.25,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\":
    \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q8","subject":"Yeast extract (BD-Difco)","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[7].concentration","original":{"value":"2","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"2","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    supports the same supplied substance and gram batch amount. Retain that amount
    and form. The local per-litre denominator is not explicit in a source that only
    lists 1 L water plus a stock addition, so qualify its basis rather than claiming
    exact final concentration.","sources":[{"locator":"$.components[0].items[7]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"Yeast extract (BD-Difco)\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\":
    \"Bacto &trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q9","subject":"Tryptone (BD-Difco)","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[8].concentration","original":{"value":"2","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"2","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    supports the same supplied substance and gram batch amount. Retain that amount
    and form. The local per-litre denominator is not explicit in a source that only
    lists 1 L water plus a stock addition, so qualify its basis rather than claiming
    exact final concentration.","sources":[{"locator":"$.components[0].items[8]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"Tryptone (BD-Difco)\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001043\",\n          \"gmo_id\": \"GMO_001043\",\n          \"label\":
    \"Bacto &trade; Tryptone\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q10","subject":"Urea","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[9].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    supports the same supplied substance and gram batch amount. Retain that amount
    and form. The local per-litre denominator is not explicit in a source that only
    lists 1 L water plus a stock addition, so qualify its basis rather than claiming
    exact final concentration.","sources":[{"locator":"$.components[0].items[9]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"Urea\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001133\",\n          \"gmo_id\": \"GMO_001133\",\n          \"label\":
    \"Urea\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q11","subject":"L-Cysteine・HCl・H2O","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"ingredients[10].concentration","original":{"value":"0.6","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"0.6","unit":"G_PER_L"}}],"decision":"unsupported","stage":"C41
    main batch; TOGO evidence, primary JCM 951 unavailable","interpretation":"TOGO
    supports the same supplied substance and gram batch amount. Retain that amount
    and form. The local per-litre denominator is not explicit in a source that only
    lists 1 L water plus a stock addition, so qualify its basis rather than claiming
    exact final concentration.","sources":[{"locator":"$.components[0].items[10]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"L-Cysteine・HCl・H2O\",\n          \"volume\": 0.6,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001205\",\n          \"gmo_id\": \"GMO_001205\",\n          \"label\":
    \"L-Cysteine hydrochloride monohydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q12","subject":"SL-10
    working addition","local_fields":[{"record_path":"data/merge_yaml/merged/C41_MEDIUM.yaml","field_path":"solutions[0].concentration","original":{"value":"1","unit":"G_PER_L"}},{"record_path":"data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml","field_path":"solutions[0].concentration","original":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","stage":"C41
    receiving stock dose","interpretation":"TOGO specifies 1 ml of SL-10 from M433,
    not 1 g/L. Preserve the absolute stock dose separately from stock composition.
    Neither 1 L nor 1.001 L is asserted as measured final medium volume.","sources":[{"locator":"$.components[0].items[11]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n          \"component_name\":
    \"Trace element solution SL--10 (see Medium [M433])\",\n          \"volume\":
    1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M433\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_representation":"raw JSON object"}]},{"decision_id":"q13","subject":"C41
    pH adjustment","local_fields":[],"decision":"evidence_only","stage":"C41 main-medium
    condition","interpretation":"TOGO explicitly specifies pH 7.0 and adjustment.
    Retain this provider-supported condition; the unavailable JCM 951 page does not
    independently authenticate preparation or supply a sterilization default.","sources":[{"locator":"$.meta","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n    \"gm\":
    \"http://togomedium.org/medium/M998\",\n    \"name\": \"C41 Medium\",\n    \"original_media_id\":
    \"JCM_M951\",\n    \"src_url\": \"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=951\",\n    \"ph\":
    \"7.0\"\n  }","quote_representation":"raw JSON object"},{"locator":"$.comments[0]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Adjust pH to 7.0.\"\n    }","quote_representation":"raw
    JSON object"}]},{"decision_id":"q14","subject":"Scoped SL-10: Distilled water","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[0].concentration","original":{"value":"1981.0","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The SL-10 stock uses 990 ml water.
    The local 1981 G_PER_L aggregates multiple parent sections; it is not transferable
    stock water. Preserve 990 ml within SL-10 only, without treating 990 ml + 10 ml
    acid as measured final stock volume.","sources":[{"locator":"$.components[3].items[0]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[18]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"Distilled
    water\n990.0\nml","quote_representation":"HTML tr[18] DOM text"}]},{"decision_id":"q15","subject":"Scoped
    SL-10: Na2MoO4・2H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[6].concentration","original":{"value":"36","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 36
    mg of this salt. The parent record holds the same number under G_PER_L outside
    a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium
    final rate is derived.","sources":[{"locator":"$.components[3].items[1]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[17]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"Na\n2\nMoO\n4\n·2H\n2\nO\n36.0\nmg","quote_representation":"HTML
    tr[17] DOM text"}]},{"decision_id":"q16","subject":"Scoped SL-10: H3BO3","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[7].concentration","original":{"value":"6","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 6 mg
    of this compound. The parent record holds the same number under G_PER_L outside
    a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium
    final rate is derived.","sources":[{"locator":"$.components[3].items[2]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[13]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"H\n3\nBO\n3\n6.0\nmg","quote_representation":"HTML
    tr[13] DOM text"}]},{"decision_id":"q17","subject":"Scoped SL-10: MnCl2・4H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[8].concentration","original":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 100
    mg of this salt. The parent record holds the same number under G_PER_L outside
    a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium
    final rate is derived.","sources":[{"locator":"$.components[3].items[3]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[12]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"MnCl\n2\n·4H\n2\nO\n100.0\nmg","quote_representation":"HTML
    tr[12] DOM text"}]},{"decision_id":"q18","subject":"Scoped SL-10: CoCl2・6H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[9].concentration","original":{"value":"190","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 190
    mg of this salt. The parent record holds the same number under G_PER_L outside
    a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium
    final rate is derived.","sources":[{"locator":"$.components[3].items[4]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[14]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"CoCl\n2\n·6H\n2\nO\n190.0\nmg","quote_representation":"HTML
    tr[14] DOM text"}]},{"decision_id":"q19","subject":"Scoped SL-10: NiCl2・6H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[10].concentration","original":{"value":"24","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 24
    mg of this salt. The parent record holds the same number under G_PER_L outside
    a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium
    final rate is derived.","sources":[{"locator":"$.components[3].items[5]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[16]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"NiCl\n2\n·6H\n2\nO\n24.0\nmg","quote_representation":"HTML
    tr[16] DOM text"}]},{"decision_id":"q20","subject":"Scoped SL-10: CuCl2・2H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[11].concentration","original":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 2 mg
    of this salt. The parent record holds the same number under G_PER_L outside a
    resolved stock; restore the milligram stock amount before any reuse. No receiving-medium
    final rate is derived.","sources":[{"locator":"$.components[3].items[6]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[15]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"CuCl\n2\n·2H\n2\nO\n2.0\nmg","quote_representation":"HTML
    tr[15] DOM text"}]},{"decision_id":"q21","subject":"Scoped SL-10: ZnCl2","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[12].concentration","original":{"value":"70","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"The exact SL-10 table specifies 70
    mg of this salt. The parent record holds the same number under G_PER_L outside
    a resolved stock; restore the milligram stock amount before any reuse. No receiving-medium
    final rate is derived.","sources":[{"locator":"$.components[3].items[7]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[11]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"ZnCl\n2\n70.0\nmg","quote_representation":"HTML
    tr[11] DOM text"}]},{"decision_id":"q22","subject":"Scoped SL-10: HCl (25%, 7.7
    M)","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[13].concentration","original":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","stage":"separate
    SL-10 stock formulation","interpretation":"This is 10 ml of HCl solution labelled
    25%, 7.7 M, not 10 g/L HCl. Preserve both source strength descriptions and stock-stage
    dose; no unprinted percentage basis or density conversion is supplied.","sources":[{"locator":"$.components[3].items[8]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
    \"HCl (25%, 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\":
    \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[9]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"HCl
    (25%, 7.7 M)\n10.0\nml","quote_representation":"HTML tr[9] DOM text"}]},{"decision_id":"q23","subject":"Scoped
    SL-10: FeCl2・4H2O","local_fields":[{"record_path":"data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml","field_path":"ingredients[14].concentration","original":{"value":"1.5","unit":"G_PER_L"}}],"decision":"unsupported","stage":"separate
    SL-10 stock formulation","interpretation":"The source specifies 1.5 g iron dichloride
    tetrahydrate for the SL-10 stock batch. Keep that salt form and quantity, but
    not as a direct C41 ingredient or a verified final-medium G/L value.","sources":[{"locator":"$.components[3].items[9]","source_key":"togoM433","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M433","source_raw_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","source_text_sha256":"b0e92380fc64ea5b9bd975a00f6cd6318452dea5623139816a6458e27fe3f922","accessed_at":"2026-10-28T05:12:25.936433Z","exact_source_quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_representation":"raw JSON
    object"},{"locator":"HTML tr[10]","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"FeCl\n2\n·4H\n2\nO\n1.5\ng","quote_representation":"HTML
    tr[10] DOM text"}]},{"decision_id":"q24","subject":"SL-10 dissolution order","local_fields":[],"decision":"evidence_only","stage":"stock
    preparation only","interpretation":"Dissolve iron chloride first in the acid,
    then dilute and add the other salts as the primary says. JCM 433 main-medium autoclaving,
    vitamin filtration and pH are outside this stock dependency and do not transfer
    to C41.","sources":[{"locator":"extracted-text lines 105-109","source_key":"jcm433","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=433","source_raw_sha256":"bd2a35c651cd8b8db154b7025c37fd0bdbcdfc4e7b6e578128ee4500a611333b","source_text_sha256":"2dfc29781ee3a6fcb12c6eadc7fc74bc3dc3c36ca41a7accb8c75d07aacd3d33","accessed_at":"2026-10-28T05:12:25.760817Z","exact_source_quote":"Dissolve
    FeCl\n2\n·4H\n2\nO first in HCl. Then dilute in distilled water and add the remaining
    salts.","quote_representation":"captured extracted text"}]},{"decision_id":"q25","subject":"Unresolved
    C41 preparation controls","local_fields":[],"decision":"not_quantified","stage":"unavailable
    primary preparation","interpretation":"TOGO has only the pH-adjustment comment
    and JCM 951 says Nothing found. No autoclave cycle, urea sterilization, gas, incubation
    or stock-addition order beyond the explicit dose is imported from another medium.","sources":[{"locator":"$.comments[0]","source_key":"togoM998","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M998","source_raw_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","source_text_sha256":"41e301ca825fef196fb6f925cb20f2391a8210ee6ee340fe03ae1ca1e30e2cc7","accessed_at":"2026-10-28T05:12:25.740041Z","exact_source_quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Adjust pH to 7.0.\"\n    }","quote_representation":"raw
    JSON object"},{"locator":"extracted-text lines 4-4","source_key":"jcm951","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=951","source_raw_sha256":"9444154f4322dcdd0d815d926c10d3e6f1da364be2278122ae0ace8fd866f080","source_text_sha256":"97559e145c2d45b5262bd1068383785f04c81089c08844af582276f2da801767","accessed_at":"2026-10-28T05:12:25.749928Z","exact_source_quote":"Nothing
    found.","quote_representation":"captured extracted text"}]}],"local_field_census_reference":"REVIEW_WORK/batch056/record06/grounding-inventory.json","source_only_gaps_are_explicit":true,"note":"Batch
    amounts, provider normalization, stock composition, working dose and preparation
    controls are separate. No source edits or automatic curation performed."}'
- assessment_id: a7
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/C41_MEDIUM.yaml: primary 9/11, secondary 5/11;
    data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml: primary 9/11, secondary
    5/11. These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI/UBERON term is joined
    to its exact current OLS object and packaged MIM CSV rows. Zero numeric legacy
    MediaIngredientMech identifiers occur in the full selected documents; NNNNNN is
    a historical placeholder, not an ID. Complex commercial/product components are
    not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - grounding
- assessment_id: a8
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:010426
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-010426-main-source-unit-slips
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: C41 water and three milligram rows have incorrect local units
  description: Water 1 L became 1 G_PER_L; calcium chloride dihydrate 5 mg, resazurin
    1 mg and iron sulfate heptahydrate 1.25 mg retain their numbers under G_PER_L.
    TOGO provides direct unit evidence, although the linked primary is currently unavailable.
  target_ids:
  - CultureMech:010426
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[4].concentration
  - ingredients[6].concentration
  evidence_ids:
  - togoM998
  - jcm951
  rule_id: source-quantity-unit-stage
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-010426-stock-unresolved
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: SL-10 dose and stock composition are unresolved
  description: The source 1 ml addition is stored as 1 G_PER_L with empty composition
    and Unknown solution name. The named M433 relationship is meaningful but its current
    YAML has flattened stock amounts and cannot be reused wholesale.
  target_ids:
  - CultureMech:010426
  field_paths:
  - solutions[0].concentration
  - solutions[0].composition
  - solutions[0].name
  evidence_ids:
  - togoM998
  - jcm433
  - togoM433
  rule_id: source-stock-preparation-completeness
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-010426-sl10-dependency
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The candidate dependency contains stock-unit and hydrate mismatches
  description: M433 stores SL-10 milligram salts as G_PER_L and acid volume as mass,
    aggregates water across sections, and assigns Co/Ni hexahydrate names anhydrous
    primary identifiers. Correct only these explicitly scoped stock claims before
    linking; the parent medium remains separate.
  target_ids:
  - CultureMech:010426
  field_paths:
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[0].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[6].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[7].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[8].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[9].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[10].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[11].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[12].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[13].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[14].concentration
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[9].term
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::ingredients[10].term
  - data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml::solutions[2].composition
  evidence_ids:
  - grounding
  - jcm433
  - togoM433
  - chebi35696
  - chebi34887
  rule_id: scoped-stock-quantity-form-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml
    role: scoped SL10 dependency, not a selected merge contributor
- finding_id: f4
  issue_key: culturemech-010426-main-denominator
  category: quantity
  severity: minor
  status: open
  certainty: confirmed
  title: Unchanged gram amounts have an unverified final-volume basis
  description: The remaining main amounts match TOGO grams, but local G_PER_L assumes
    a final litre that is not explicitly established by 1 L water plus 1 ml stock.
    The older narrative also used per-litre wording without resolving this distinction.
  target_ids:
  - CultureMech:010426
  field_paths:
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[5].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  evidence_ids:
  - togoM998
  - history0
  rule_id: source-quantity-basis
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-010426-missing-ph-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Provider-supported pH and claim evidence are missing
  description: TOGO states pH 7.0 and an adjustment instruction. Neither selected
    layer contains that condition, structured source references or attached formulation
    evidence. The missing primary and zero native reference checks must remain explicit.
  target_ids:
  - CultureMech:010426
  field_paths:
  - ph_value
  - preparation_steps
  - references
  - ingredients[*].evidence
  evidence_ids:
  - togoM998
  - jcm951
  - grounding
  rule_id: source-preparation-evidence-completeness
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Repair the source unit scale and preserve batch water separately; qualify
    provider-only authentication and avoid a guessed final denominator.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010426
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action2
  description: Resolve only the exact SL-10 stock and preserve its C41 volume dose;
    exclude parent main medium and vitamins.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010426
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Repair the exact SL-10 subgraph and source forms with claim-scoped
    evidence before reuse; do not transfer the parent receiving dose, main salts or
    vitamins.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010426
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M433_Pseudomonas_Halophila_Medium.yaml
    role: scoped SL10 dependency, not a selected merge contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action4
  description: Keep the matched gram amounts and supplied forms, explicitly annotate
    the batch basis, and defer any final concentration calculation.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010426
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Preserve exact TOGO pH and source claims with current capture metadata,
    and retain the unresolved primary/preparation boundary rather than borrowing a
    general JCM cycle.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010426
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M998_C41_Medium.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- Current JCM 951 HTTP 200 body says Nothing found. TOGO supports the documented comparisons,
  but no primary C41 preparation or strain-growth evidence is recovered. A bounded
  ignored-inclusive search of the old batch048-tail cache path and durable preserved
  task evidence found no jcm951/M998/C41 capture filename; this is not a universal
  absence claim.
- Only JCM 433 SL-10 transfers. Main parent medium, vitamins, its receiving stock
  dose and generic sterilization header are excluded from C41.
- The stock lists 990 ml water plus 10 ml acid; C41 lists 1 L water plus 1 ml stock.
  Neither sum is promoted to a measured final volume. Current ontology/MIM labels
  do not establish historical mapping validity.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
