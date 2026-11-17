# Scientific review: Clostridium R6 Medium

- Review: 20261028T151110Z-culturemech-010053-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T14:34:16.284026Z
- Finished UTC: 2026-10-28T15:11:10.216069Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Source-complete review identifies flattened A/B stages and wrong units, unrelated generic stock links, missing variant preparation and two scoped hydrate mappings. Existing repaired stock batch evidence is preserved; no final-volume or percentage-basis conversion is invented.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch070 index 10
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010053 | data/merge_yaml/merged/Clostridium_R6_Medium.yaml | generated | clostridium_r6_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:010053 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:010053 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:010053 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:010053 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact637 source identity and stock-link boundaries

identity: concern. Targets: CultureMech:010053.

TOGO M651 and current primary 637 identify the same R6 medium and exact 636 modification. The receiving A/B links are wrong generic-name cross-links; source identity is established without inventing strain taxonomy.

### Complex liquid formulation

consistency: supported. Targets: CultureMech:010053.

Yeast extract and tryptone support COMPLEX/UNDEFINED. No solidifying ingredient is asserted; LIQUID is consistent. No organism-growth claim is inferred.

### Original and additive inspection boundaries

schema: supported. Targets: CultureMech:010053.

The original four canonical diagnostics passed once; reference validation checked zero attached references. The additive inspection only adds current source-repair history/writer inputs and preserves all originals; no canonical rerun or formal save occurred.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:010053.

47 current concentration fields are covered by 49 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b070-quantity-inventory-v1","target":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","quantity_field_count":47,"decisions":[{"quantity_id":"q1","label":"Na2S・9H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"VARIABLE does not retain the explicitly stated 0.025% receiving-medium declaration and separately prepared 5% stock. Keep both exact source stages and unspecified percentage bases; do not infer mass, volume, density or stock dose.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"Na2S・9H2O\",\n          \"conc_value\": 0.025,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\": \"GMO_001494\",\n          \"label\": \"Sodium sulfide nonahydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 6,\n      \"comment\": \"Distribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers. Prior to inoculation, reduce the medium with 0.025% L--cysteine・HCl・H2O and 0.025% Na2S・9H2O (autoclaved as 5% solutions under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt lines 88-96","quote":"Distribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers.  Prior to inoculation, reduce the medium with 0.025% L-cysteine·HCl·H\n2\nO and 0.025% Na\n2\nS·9H\n2\nO (autoclaved as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"L--cysteine・HCl・H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"VARIABLE does not retain the explicitly stated 0.025% receiving-medium declaration and separately prepared 5% stock. Keep both exact source stages and unspecified percentage bases; do not infer mass, volume, density or stock dose.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"L--cysteine・HCl・H2O\",\n          \"conc_value\": 0.025,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001496\",\n          \"gmo_id\": \"GMO_001496\",\n          \"label\": \"L-Cysteine hydrochloride monohydrate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 6,\n      \"comment\": \"Distribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers. Prior to inoculation, reduce the medium with 0.025% L--cysteine・HCl・H2O and 0.025% Na2S・9H2O (autoclaved as 5% solutions under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt lines 88-96","quote":"Distribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers.  Prior to inoculation, reduce the medium with 0.025% L-cysteine·HCl·H\n2\nO and 0.025% Na\n2\nS·9H\n2\nO (autoclaved as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"Carbon dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"Retain the VARIABLE entry as a truthful unquantified gas placeholder. The exact637 override and its gas-phase mixture belong to the separately assessed preparation; they do not establish a dissolved concentration or liquid dose. Base nitrogen handling remains separate preparation context.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\": 8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"Retain the VARIABLE entry as a truthful unquantified gas placeholder. The exact637 override and its gas-phase mixture belong to the separately assessed preparation; they do not establish a dissolved concentration or liquid dose. Base nitrogen handling remains separate preparation context.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\": 8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Hydrogen gas","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"Retain the VARIABLE entry as a truthful unquantified gas placeholder. The exact637 override and its gas-phase mixture belong to the separately assessed preparation; they do not establish a dissolved concentration or liquid dose. Base nitrogen handling remains separate preparation context.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\": \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\": 8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"960.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"960.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The two water inputs belong to different stock batches. Their historical sum960 G_PER_L is neither a water amount in an allowed volume unit nor a final-medium concentration. Restore separate input volumes without asserting final mixed volume.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 860,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;860.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.54","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.54","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution A, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.54,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 0 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; KH&lt;sub&gt;2&lt;/sub&gt;PO&lt;sub&gt;4&lt;/sub&gt;                                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.54&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.54,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.627907,\n                        \"mmol_l\": 4.61405,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution A, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator. The source unit is mg, not g; local 1 G_PER_L additionally loses that unit.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 4 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Resazurin                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00116279,\n                        \"mmol_l\": 0.00507348,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Na2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.34","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.34","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution A, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Na2HPO4\",\n          \"volume\": 1.34,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001069\",\n          \"gmo_id\": \"GMO_001069\",\n          \"label\": \"Disodium phosphate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 1 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;HPO&lt;sub&gt;4&lt;/sub&gt;                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.34&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 1.34,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.55814,\n                        \"mmol_l\": 10.976,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Yeast extract (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution A, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 2 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Yeast extract (BD-Difco)                                           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;3.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.48837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"Tryptone (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution A, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Tryptone (BD-Difco)\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001043\",\n          \"gmo_id\": \"GMO_001043\",\n          \"label\": \"Bacto &amp;trade; Tryptone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 3 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Tryptone (BD-Difco)                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.581395,\n                        \"mmol_l\": 8.17945,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution B, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 0.19,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 7 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NaCl                                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.19&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 0.19,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.86275,\n                        \"mmol_l\": 31.8745,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution B, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"CaCl2・2H2O\",\n          \"volume\": 0.006,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 8 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CaCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.006&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0588235,\n                        \"mmol_l\": 0.400119,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution B, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.19,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 6 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NH&lt;sub&gt;4&lt;/sub&gt;Cl                                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.19&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.19,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.86275,\n                        \"mmol_l\": 34.8242,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.063","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.063","unit":"G_PER_L"}}],"decision":"correct","rationale":"The exact source places this amount in local solution B, not as a direct final-medium G_PER_L rate. Preserve the literal batch amount/form and source stage; provider g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"MgCl2・6H2O\",\n          \"volume\": 0.063,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 9 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MgCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.063&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.063,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.617647,\n                        \"mmol_l\": 3.03806,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Solution A","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"860","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"860","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock stage; do not substitute ML_PER_L without a final-medium denominator. Resolve the wrong generic-name provider link against exact local A/B, not against a similarly named stock.","source_stage":"Selected receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Solution A\",\n          \"volume\": 860,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M651\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 5 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;860.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"Solution B","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"102","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"102","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock stage; do not substitute ML_PER_L without a final-medium denominator. Resolve the wrong generic-name provider link against exact local A/B, not against a similarly named stock.","source_stage":"Selected receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Solution B\",\n          \"volume\": 102,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M651\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 12 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"FeCl2 solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock stage; do not substitute ML_PER_L without a final-medium denominator. Use only the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 10 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt; solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"Trace element solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock stage; do not substitute ML_PER_L without a final-medium denominator. Use only the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 11 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace element solution (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\"&gt;187&lt;/a&gt;)           &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"8% NaHCO3 solution","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock stage; do not substitute ML_PER_L without a final-medium denominator. Use only the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Trace vitamins (see Medium [M190])","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock stage; do not substitute ML_PER_L without a final-medium denominator. Use only the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 14 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Trace vitamins (see Medium No. &lt;a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\"&gt;197&lt;/a&gt;)                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Iron stock water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;990.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Iron stock FeCl2 tetrahydrate batch input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 1.5 g. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"FeCl2・4H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; FeCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.5&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; g  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Nested HCl reagent addition","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"Existing 0.01 L is the exact 10 ml addition within the iron stock. M180 root evidence[0] contains the additional literal HCl excerpt and exact nested concentration locator, with a digest matching the current source. This authenticates the retained dose at that stock stage only; the unspecified 25% basis and parent receiving-medium doses are not inferred or transferred.","source_stage":"HCl dose within iron stock","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Nested HCl explicit reagent strength","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Existing 7.7 M is explicit reagent strength with a matching attached TOGO literal/digest. The 25% basis remains unspecified and is not used for a conversion. The older JCM plain-text snippet is corroborated by the current table but not asserted to match current raw HTML bytes.","source_stage":"HCl reagent, not final medium","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"25% HCl (7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"conc_value\": 25,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 25% HCl (7.7 M)                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Trace stock Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 26 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L        &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Trace stock Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 36 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Na&lt;sub&gt;2&lt;/sub&gt;MoO&lt;sub&gt;4&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                            &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;36.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Trace stock H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 6 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; H&lt;sub&gt;3&lt;/sub&gt;BO&lt;sub&gt;3&lt;/sub&gt;                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;6.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Trace stock MnCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 100 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"MnCl2・4H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; MnCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;4H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;100.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Trace stock CoCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 190 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"CoCl2・6H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CoCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;190.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Trace stock NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 24 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; NiCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;6H&lt;sub&gt;2&lt;/sub&gt;O                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;24.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Trace stock CuCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"CuCl2・2H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; CuCl&lt;sub&gt;2&lt;/sub&gt;&amp;#183;2H&lt;sub&gt;2&lt;/sub&gt;O                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Trace stock ZnCl2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource batch input: 70 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; ZnCl&lt;sub&gt;2&lt;/sub&gt;                                               &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;70.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Vitamin stock Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 25 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Distilled water                                         &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;1.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; L  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Vitamin stock Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Biotin                                                  &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Vitamin stock p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 23 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; &lt;I&gt;p&lt;/I&gt;-Aminobenzoic acid                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Vitamin stock Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 18 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Thiamine&amp;#183;HCl                                      &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Vitamin stock Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 21 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Calcium pantothenate                                    &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Vitamin stock Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 17 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Pyridoxine&amp;#183;HCl                                   &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;10.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Vitamin stock Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 16 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Folic acid                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;2.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Vitamin stock Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 22 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Vitamin B&lt;sub&gt;1&lt;/sub&gt;&lt;sub&gt;2&lt;/sub&gt;                                       &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;0.1&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Vitamin stock Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 19 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Riboflavin                                              &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Vitamin stock Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 20 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Nicotinic acid                                          &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Vitamin stock Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration."}],"decision":"verified","rationale":"Retain the existing exact batch-input claim and attached literal source evidence; its cited raw SHA matches the current capture. This authenticates content, not a newly recovered original access event or an absent final-volume concentration.","source_stage":"Scoped stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML table row 24 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; Lipoic acid                                             &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;5.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; mg  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Exact637 override","local_fields":[],"decision":"evidence_only","rationale":"Omit base636 methanol and apply the explicitly replaced gas-phase identity/ratio. No taxonomic identity or strain growth is inferred from R6.","source_stage":"Source-only preparation or variant control","sources":[{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"},{"evidence_id":"apiJ637","reference":"https://mediadive.dsmz.de/rest/medium/J637","raw_path":"REVIEW_WORK/batch070/source07-08-10/apiJ637.raw","raw_sha256":"e765ff2d61eed716a560057abdc1fd1f4dbb2ae1afac17248deae3516537d453","text_sha256":"e765ff2d61eed716a560057abdc1fd1f4dbb2ae1afac17248deae3516537d453","accessed_at":"2026-10-28T14:34:10.810177Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Use Medium No. 636 without methanol. Replace the gas phase with a H2-CO2 (80:20, v/v) gas mixture.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\": 8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Separate sterilization and order","local_fields":[],"decision":"evidence_only","rationale":"Retain primary A/B preparation, cooling and subsequent filter-sterilized additions, scoped by the637 no-methanol override. Do not carry over the excluded methanol/C recipe as an R6 ingredient.","source_stage":"Source-only preparation or variant control","sources":[{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt lines 73-96","quote":"Autoclave Solutions A and B separately and autoclave Solution C in a closed tube or vial.  After cooling, combine the three solutions under a stream of N\n2\n-CO\n2\n(80:20, v/v), then add the following solutions (filter-sterilized):\nTrace vitamins (see Medium No.\n197\n)\n10.0\nml\n8% NaHCO\n3\nsolution\n30.0\nml\nDistribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers.  Prior to inoculation, reduce the medium with 0.025% L-cysteine·HCl·H\n2\nO and 0.025% Na\n2\nS·9H\n2\nO (autoclaved as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative text"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 4,\n      \"comment\": \"Autoclave Solutions A and B separately and autoclave Solution C in a closed tube or vial. After cooling, combine the three solutions under a stream of N2--CO2 (80:20, v/v), then add the following solutions (filter--sterilized):\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Reducing-agent stock stage","local_fields":[],"decision":"evidence_only","rationale":"The source states separate 5% stocks and 0.025% receiving declarations. Their percentage bases and amount of stock added are not independently specified; no calculation or operational optimization is performed.","source_stage":"Source-only preparation or variant control","sources":[{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt lines 88-96","quote":"Distribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers.  Prior to inoculation, reduce the medium with 0.025% L-cysteine·HCl·H\n2\nO and 0.025% Na\n2\nS·9H\n2\nO (autoclaved as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative text"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\": 6,\n      \"comment\": \"Distribute the medium into culture vessels under the same gas mixture and seal with butyl rubber stoppers. Prior to inoculation, reduce the medium with 0.025% L--cysteine・HCl・H2O and 0.025% Na2S・9H2O (autoclaved as 5% solutions under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Bicarbonate stock label","local_fields":[],"decision":"evidence_only","rationale":"Retain 8% as the source label attached to the 30 ml addition, without assuming w/v or density. No unsupported concentration object is added.","source_stage":"Source-only preparation or variant control","sources":[{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML table row 15 (zero-based)","quote":"&lt;TR&gt;&lt;TD WIDTH=75%&gt; 8% NaHCO&lt;sub&gt;3&lt;/sub&gt; solution                                 &lt;/TD&gt;&lt;TD WIDTH=15% ALIGN=RIGHT&gt;&lt;font size=+1&gt;&lt;tt&gt;&amp;nbsp;30.0&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;&lt;/tt&gt;&lt;/font&gt;&lt;/TD&gt;&lt;TD WIDTH=10% ALIGN=RIGHT&gt; ml  &lt;/TD&gt;&lt;/TR&gt;","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"8% NaHCO3 solution\",\n          \"volume\": 30,\n          \"unit\": \"ml\",\n          \"conc_value\": 8,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001119\",\n          \"gmo_id\": \"GMO_001119\",\n          \"label\": \"Sodium bicarbonate solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Primary catalogue default","local_fields":[],"decision":"evidence_only","rationale":"The catalogue prints a default sterilization statement, not an incubation temperature/time. Specific filtration and variant exclusions take precedence within their source scope.","source_stage":"Source-only preparation or variant control","sources":[{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/Clostridium_R6_Medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].preferred_term","solutions[0].name","solutions[0].composition","solutions[0].solutions","solutions[1].preferred_term","solutions[1].name","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].preferred_term","solutions[1].composition"],"data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml":["preferred_term","name","term","composition[0].preferred_term","composition[0].term","composition[0].chebi_term","composition[1].preferred_term","composition[1].term","composition[1].chebi_term","composition[2].preferred_term","composition[2].term","composition[2].chebi_term","composition[3].preferred_term","composition[3].term","composition[3].chebi_term","composition[4].preferred_term","composition[4].term","composition[4].chebi_term","composition[5].preferred_term","composition[5].term","composition[5].chebi_term","composition[6].preferred_term","composition[6].term","composition[6].chebi_term","composition[7].preferred_term","composition[7].term","composition[7].chebi_term"],"data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml":["preferred_term","name","term","composition[0].preferred_term","composition[0].term","composition[0].chebi_term","composition[1].preferred_term","composition[1].term","composition[1].chebi_term"]},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:010053.

Exact current ontology objects and MIM rows are inspected for every in-scope slot. Selected salts/gases/hydrates are credited. In the explicitly referenced trace stock, cobalt and nickel hexahydrates map to anhydrous chemical entities. The source leaves calcium-pantothenate stereochemistry unspecified while CHEBI31345 has stereochemical structure; preserve this uncertainty rather than claiming a confirmed wrong ID or converting mass. Wrong-linked5342/5343 chemistry is comparison context only; its citrate label/form issue is not promoted as a finding affecting the selected medium. Current label agreement and secondary-link presence are reported separately from chemical-form support.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:010053.

All 12 complete historical reports and exact selected parent objects are retained with scoped current-object joins. Historical per-liter interpretations are not silently inherited. Existing M180/M190 water, reagent and batch-note repairs are credited against attached literal snippets and equal current raw SHA values; this does not recover their original access events. Current staged importer, conservative merger and non-summing cleanup behavior differ from old flattened records. The Oct8 repair wrapper was inspected through additive native inputs; only its scoped stock effects are assessed.

## Findings

### f1: Local A/B batches and additions are flattened into final-medium concentrations

major / open / confirmed; issue key: culturemech-010053-stock-stages-and-units.

The target and maintained owner flatten local A/B ingredients, sum distinct water inputs into 960 G_PER_L, label source 1 mg resazurin as 1 G_PER_L, and encode all six source ml additions as G_PER_L. Restore the exact stock/addition hierarchy and source units. Retained gram numbers are source batch inputs, not established final-medium rates; do not calculate a final volume from the listed input volumes.

### f2: Generic Solution A/B links identify unrelated stocks

major / open / confirmed; issue key: culturemech-010053-wrong-generic-stock-links.

The two maintained links point to provider 5342/5343, whose current compositions are salt-rich stocks unrelated to the source 636 local A/B recipes. Generic-name equality is insufficient. Resolve receiving links to exact source-specific A/B compositions and retain separate provenance. The standalone comparison stocks are not requested to be reformulated.

### f3: Exact source variant and preparation stages are absent

major / open / confirmed; issue key: culturemech-010053-missing-variant-preparation.

The current owner/target lack preparation prose and encode gases as generic VARIABLE ingredients. Preserve exact 637 methanol exclusion and gas-phase replacement, separate A/B preparation, subsequent additions, and the distinction between declared reducing-stock and receiving percentages. Percent basis and unspecified doses remain unresolved; do not import parent M180/M190 procedures.

### f4: Two scoped trace-stock IDs omit the source hexahydrate form

major / open / confirmed; issue key: culturemech-010053-referenced-trace-hydrates.

The explicitly referenced M180 trace stock retains correct source batch amounts and names, but its cobalt and nickel hexahydrate rows use anhydrous CHEBI:35696 and CHEBI:34887. Exact current ontology formulas confirm the form mismatch; correct those scoped IDs or retain the form explicitly unresolved without mass conversion. Other current mappings and source-supported batch notes are credited.

### f5: Stock placeholders and missing receiving-claim evidence remain

minor / open / confirmed; issue key: culturemech-010053-stock-placeholders-and-evidence.

All six selected descriptors have name Unknown solution despite source-specific preferred terms. Correct those placeholders and attach exact claim-level receiving evidence while preserving existing repaired dependency evidence. M180 iron/trace Unknown solution names should be replaced only within their explicit scoped stock descriptors. Do not invent a species or strain from R6.

## Recommended Actions And Acceptance Checks

### a1

The target and maintained owner flatten local A/B ingredients, sum distinct water inputs into 960 G_PER_L, label source 1 mg resazurin as 1 G_PER_L, and encode all six source ml additions as G_PER_L. Restore the exact stock/addition hierarchy and source units. Retained gram numbers are source batch inputs, not established final-medium rates; do not calculate a final volume from the listed input volumes.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The two maintained links point to provider 5342/5343, whose current compositions are salt-rich stocks unrelated to the source 636 local A/B recipes. Generic-name equality is insufficient. Resolve receiving links to exact source-specific A/B compositions and retain separate provenance. The standalone comparison stocks are not requested to be reformulated.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The current owner/target lack preparation prose and encode gases as generic VARIABLE ingredients. Preserve exact 637 methanol exclusion and gas-phase replacement, separate A/B preparation, subsequent additions, and the distinction between declared reducing-stock and receiving percentages. Percent basis and unspecified doses remain unresolved; do not import parent M180/M190 procedures.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The explicitly referenced M180 trace stock retains correct source batch amounts and names, but its cobalt and nickel hexahydrate rows use anhydrous CHEBI:35696 and CHEBI:34887. Exact current ontology formulas confirm the form mismatch; correct those scoped IDs or retain the form explicitly unresolved without mass conversion. Other current mappings and source-supported batch notes are credited.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

All six selected descriptors have name Unknown solution despite source-specific preferred terms. Correct those placeholders and attach exact claim-level receiving evidence while preserving existing repaired dependency evidence. M180 iron/trace Unknown solution names should be replaced only within their explicit scoped stock descriptors. Do not invent a species or strain from R6.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| currentTogo651 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651; REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.json; exact original raw/text/hash/time metadata | context_only | Official structured TOGO route observed in prior reviewed application; exact source object and original timestamp retained. M180 iron/trace and M190 vitamin sections only are potential dependencies. |
| togo651 | https://togomedium.org/rest/medium/M651; REVIEW_WORK/batch070/source07-08-10/togo651.json; exact original raw/text/hash/time metadata | context_only | Exact source identity first; generic medium names alone do not establish strain growth or hazardous organism association. No scientific assessment before native inspection. |
| jcm637 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637; REVIEW_WORK/batch070/source07-08-10/jcm637.json; exact original raw/text/hash/time metadata | context_only | Exact source identity first; generic medium names alone do not establish strain growth or hazardous organism association. No scientific assessment before native inspection. |
| jcm636 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636; REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.json; exact original raw/text/hash/time metadata | context_only | Exact public source discovery or scoped dependency; parent basal formulations and receiving doses are not automatically transferred. |
| apiJ637 | https://mediadive.dsmz.de/rest/medium/J637; REVIEW_WORK/batch070/source07-08-10/apiJ637.json; exact original raw/text/hash/time metadata | context_only | Exact source identity first; generic medium names alone do not establish strain growth or hazardous organism association. No scientific assessment before native inspection. |
| apiJ636 | https://mediadive.dsmz.de/rest/medium/J636; REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.json; exact original raw/text/hash/time metadata | context_only | Exact public source discovery or scoped dependency; parent basal formulations and receiving doses are not automatically transferred. |
| currentTogo180 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180; REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.json; exact original raw/text/hash/time metadata | context_only | Official structured TOGO route observed in prior reviewed application; exact source object and original timestamp retained. M180 iron/trace and M190 vitamin sections only are potential dependencies. |
| currentTogo190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.json; exact original raw/text/hash/time metadata | context_only | Official structured TOGO route observed in prior reviewed application; exact source object and original timestamp retained. M180 iron/trace and M190 vitamin sections only are potential dependencies. |
| jcm187 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187; REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.json; exact original raw/text/hash/time metadata | context_only | Exact public source discovery or scoped dependency; parent basal formulations and receiving doses are not automatically transferred. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.json; exact original raw/text/hash/time metadata | context_only | Exact public source discovery or scoped dependency; parent basal formulations and receiving doses are not automatically transferred. |
| stock5342 | https://mediadive.dsmz.de/rest/solution/5342; REVIEW_WORK/batch070/source07-08-10-supplement/stock5342.json; exact original raw/text/hash/time metadata | context_only | Exact public source discovery or scoped dependency; parent basal formulations and receiving doses are not automatically transferred. |
| stock5343 | https://mediadive.dsmz.de/rest/solution/5343; REVIEW_WORK/batch070/source07-08-10-supplement/stock5343.json; exact original raw/text/hash/time metadata | context_only | Exact public source discovery or scoped dependency; parent basal formulations and receiving doses are not automatically transferred. |
| target | data/merge_yaml/merged/Clostridium_R6_Medium.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5342_Solution_A.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5343_Solution_B.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_R6_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5342_Solution_A.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5343_Solution_B.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-32 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-33 | reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| dep180 | data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml; Exact document_scopes in quantity inventory | context_only | Only iron/trace compositions and acid within the iron stock; parent receiving doses, other stocks and basal conditions excluded. |
| dep190 | data/normalized_yaml/bacterial/togo_medium_m190.yaml; Exact document_scopes in quantity inventory | context_only | Only vitamin composition. Parent receiving dose, mineral stock, basal ingredients and parent preparation excluded. |
| compare5342 | data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml; Exact document_scopes in quantity inventory | context_only | Comparison-only wrong linked stock identity; full bytes retained, concentrations/preparation excluded from receiving-medium assessment. |
| compare5343 | data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml; Exact document_scopes in quantity inventory | context_only | Comparison-only wrong linked stock identity; full bytes retained, concentrations/preparation excluded from receiving-medium assessment. |
| writer-togo | src/culturemech/import/togo_importer.py; _assembled_solution_sections, _extract_assembled_solutions, _local_batch_volume_ml, _local_solution_composition, _solution_from_item, _parse_unit | context_only | Current importer preserves local solution stages and nested references; _local_batch_volume_ml uses a source-volume corroboration heuristic. Its declared inference is not independent measured final-volume evidence. _parse_unit now maps L correctly, but bare g/ml mappings and bare-percent basis still need source-specific assessment. Current code is not historical execution proof. |
| writer-migration | scripts/migrate_solutions_from_ingredients.py; _resolve_solution and _migrate_media_file | context_only | Current name-to-single-ID lookup can resolve generic Solution A/B to unrelated provider records and preserves original quantities when moving them. Present links are checked directly; current code alone does not establish the exact old execution. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group collapses identical concentrations and flags unequal values rather than adding them. Existing historical 960 water sum is not attributed to unchanged current behavior. |
| writer-stock-repair | scripts/repair_jcm_stock_preparations.py; frozen, sources, Review.leaf, Review.stock, build, process | context_only | Current source-specific repair wrapper checks frozen raw pins and separates water volume, explicit reagent strength, receiving dose and batch-input notes. Credit the existing M180/M190 repairs within the selected subsections; their parent doses and procedures are not transferred. |
| historical-reading | REVIEW_WORK/batch070/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch070/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch070/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch070/record10/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch070/source07-08-10-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248; REVIEW_WORK/batch070/source07-08-10-supplement/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526; REVIEW_WORK/batch070/source07-08-10-supplement/chebi16526.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997; REVIEW_WORK/batch070/source07-08-10-supplement/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276; REVIEW_WORK/batch070/source07-08-10-supplement/chebi18276.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch070/source07-08-10-supplement/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch070/source07-08-10-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch070/source07-08-10-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34683; REVIEW_WORK/batch070/source07-08-10-supplement/chebi34683.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch070/source07-08-10-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch070/source07-08-10-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch070/source07-08-10-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch070/source07-08-10-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch070/source07-08-10-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch070/source07-08-10-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch070/source07-08-10-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch070/source07-08-10-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696; REVIEW_WORK/batch070/source07-08-10-supplement/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch070/source07-08-10-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch070/source07-08-10-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch070/source07-08-10-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch070/source07-08-10-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch070/source07-08-10-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch070/source07-08-10-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch070/source07-08-10-supplement/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch070/source07-08-10-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch070/source07-08-10-supplement/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch070/source07-08-10-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch070/source07-08-10-supplement/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch070/source07-08-10-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch070/source07-08-10-supplement/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi64220 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64220; REVIEW_WORK/batch070/source07-08-10-supplement/chebi64220.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi53258 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53258; REVIEW_WORK/batch070/source07-08-10-supplement/chebi53258.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; REVIEW_WORK/batch070/source07-08-10-supplement/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi32583 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32583; REVIEW_WORK/batch070/source07-08-10-supplement/chebi32583.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch070/source07-08-10-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch070/source07-08-10-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Current exact ontology object for existing scoped local slots; source chemical form assessed separately. |
| quantities | REVIEW_WORK/batch070/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch070/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch070/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch070/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch070/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch070/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch070/record10/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch070/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch070/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch070/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch070/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Only M180 iron/trace subfields and M190 vitamin composition are scientifically assessed. Their parent basal ingredients, receiving doses, parent pH/gas and unrelated stock recipes are excluded. Full bytes/history remain provenance context.
- Provider5342/5343 are compared only to establish the incorrect receiving link; their concentrations and preparation are not assessed as R6 ingredients.
- APIJ636 provider g_l and volume fields are not independent measured final-volume evidence. Base methanol and its C-stock volume are explicitly excluded by637.
- The initial TOGO /rest/medium/M651 response is an application shell; the successful official JSON capture is separate. No source absence is inferred from that initial route.
- No taxon is inferred from R6; iModulonDB is not applicable because this record asserts no gene/transcriptomic claim.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T151110Z-culturemech-010053-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Clostridium R6 Medium'
started_at: '2026-10-28T14:34:16.284026Z'
finished_at: '2026-10-28T15:11:10.216069Z'
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
summary: Source-complete review identifies flattened A/B stages and wrong units, unrelated
  generic stock links, missing variant preparation and two scoped hydrate mappings.
  Existing repaired stock batch evidence is preserved; no final-volume or percentage-basis
  conversion is invented.
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
  - path: data/merge_yaml/merged/Clostridium_R6_Medium.yaml
    sha256: fdeb9b4add2a1c44178419e9ffc47c54bafe7769a02736ff3b0f7996bd8ed76a
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
    sha256: 0eba8f76d332af192a941860f0d7a9247b42b5abb1097c0127db91df8b94fb6b
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
    sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
    sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/plan.json
    sha256: 458245c753b023bf5e9b57d7ac836f18fda493553786e735de56d9fdc026c46d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5342_Solution_A.yaml.md
    sha256: f68b7d85766061aa31ffef0f0172844d47d0aae036221dc66d608c86e8dce7a6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5343_Solution_B.yaml.md
    sha256: aca054ad3ae72ab8aee9908cb67ceac62a96adf84ff60a5141dda9b4f13ff6d8
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
    sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
    role: context
  - path: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
    sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_R6_Medium.md
    sha256: b78399c4fa3ffe2b333026e5e083fbf225b4f4299242a2c503f4e12573c5597f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
    sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
    sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.md
    sha256: d3e08dab853358cc229c72adda689e35048eee9a5544b36bac85a8c5649a85c7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5342_Solution_A.md
    sha256: 31d821180b177a4395ac64cfe2eb443091729cb74309085beeb1b765ed2dd2f2
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5343_Solution_B.md
    sha256: a1f8fb64c671e4aae298c328e3a93b1ad420e2d60c7400dbae6775f8081a0e33
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
    sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
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
  selection: Authoritative batch070 index 10
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010053
targets:
- target_id: CultureMech:010053
  path: data/merge_yaml/merged/Clostridium_R6_Medium.yaml
  label: clostridium_r6_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
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
  - CultureMech:010053
  command: just validate-schema data/merge_yaml/merged/Clostridium_R6_Medium.yaml
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
  - CultureMech:010053
  command: just validate-strict data/merge_yaml/merged/Clostridium_R6_Medium.yaml
    --out REVIEW_WORK/batch070/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:010053
  command: just validate-terms data/merge_yaml/merged/Clostridium_R6_Medium.yaml
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
  - CultureMech:010053
  command: just validate-references data/merge_yaml/merged/Clostridium_R6_Medium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: currentTogo651
  kind: primary_source
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651
  accessed_at: '2026-10-28T14:35:16.265977Z'
  locator: REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Official structured TOGO route observed in prior reviewed application;
    exact source object and original timestamp retained. M180 iron/trace and M190
    vitamin sections only are potential dependencies.
  snapshot_sha256: 5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e
- evidence_id: togo651
  kind: database
  reference: https://togomedium.org/rest/medium/M651
  accessed_at: '2026-10-28T14:34:10.267040Z'
  locator: REVIEW_WORK/batch070/source07-08-10/togo651.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity first; generic medium names alone do not establish
    strain growth or hazardous organism association. No scientific assessment before
    native inspection.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: jcm637
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637
  accessed_at: '2026-10-28T14:34:10.653890Z'
  locator: REVIEW_WORK/batch070/source07-08-10/jcm637.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity first; generic medium names alone do not establish
    strain growth or hazardous organism association. No scientific assessment before
    native inspection.
  snapshot_sha256: 62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea
- evidence_id: jcm636
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636
  accessed_at: '2026-10-28T14:35:00.347725Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact public source discovery or scoped dependency; parent basal formulations
    and receiving doses are not automatically transferred.
  snapshot_sha256: dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b
- evidence_id: apiJ637
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J637
  accessed_at: '2026-10-28T14:34:10.810177Z'
  locator: REVIEW_WORK/batch070/source07-08-10/apiJ637.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity first; generic medium names alone do not establish
    strain growth or hazardous organism association. No scientific assessment before
    native inspection.
  snapshot_sha256: e765ff2d61eed716a560057abdc1fd1f4dbb2ae1afac17248deae3516537d453
- evidence_id: apiJ636
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J636
  accessed_at: '2026-10-28T14:35:00.431313Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact public source discovery or scoped dependency; parent basal formulations
    and receiving doses are not automatically transferred.
  snapshot_sha256: db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16
- evidence_id: currentTogo180
  kind: primary_source
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180
  accessed_at: '2026-10-28T14:35:16.260746Z'
  locator: REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Official structured TOGO route observed in prior reviewed application;
    exact source object and original timestamp retained. M180 iron/trace and M190
    vitamin sections only are potential dependencies.
  snapshot_sha256: a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba
- evidence_id: currentTogo190
  kind: primary_source
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  accessed_at: '2026-10-28T14:35:16.184204Z'
  locator: REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Official structured TOGO route observed in prior reviewed application;
    exact source object and original timestamp retained. M180 iron/trace and M190
    vitamin sections only are potential dependencies.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: jcm187
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187
  accessed_at: '2026-10-28T14:35:00.347668Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact public source discovery or scoped dependency; parent basal formulations
    and receiving doses are not automatically transferred.
  snapshot_sha256: e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  accessed_at: '2026-10-28T14:35:00.337347Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact public source discovery or scoped dependency; parent basal formulations
    and receiving doses are not automatically transferred.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: stock5342
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5342
  accessed_at: '2026-10-28T14:35:00.861543Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/stock5342.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact public source discovery or scoped dependency; parent basal formulations
    and receiving doses are not automatically transferred.
  snapshot_sha256: 4bf262e02d0a83f9d1a24a52d2a14383aa8c6f27384e446d7da6274a05319240
- evidence_id: stock5343
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5343
  accessed_at: '2026-10-28T14:35:00.863751Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/stock5343.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact public source discovery or scoped dependency; parent basal formulations
    and receiving doses are not automatically transferred.
  snapshot_sha256: 28c315b1d9cf9a5c19f4d79c639298f5818c06ea87462c84336f66297d20f4c0
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Clostridium_R6_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:51:42.323144Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: fdeb9b4add2a1c44178419e9ffc47c54bafe7769a02736ff3b0f7996bd8ed76a
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T14:51:42.323290Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 0eba8f76d332af192a941860f0d7a9247b42b5abb1097c0127db91df8b94fb6b
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T14:51:42.323318Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T14:51:42.323625Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T14:51:42.323652Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T14:51:42.323675Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T14:51:42.323701Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 458245c753b023bf5e9b57d7ac836f18fda493553786e735de56d9fdc026c46d
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5342_Solution_A.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325689Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f68b7d85766061aa31ffef0f0172844d47d0aae036221dc66d608c86e8dce7a6
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5343_Solution_B.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325730Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: aca054ad3ae72ab8aee9908cb67ceac62a96adf84ff60a5141dda9b4f13ff6d8
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M180.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325753Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 92add964ce82b4d35cd58f93897f8bea6420fd3ce37ce77049e8449173263c30
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261008-jcm-stock-preparations/records/M190.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325791Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 89725cdcefc5da88b06931c4db253e065a5f48c2d2b9c8c0a9bc07f6fdc157e8
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Clostridium_R6_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325828Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: b78399c4fa3ffe2b333026e5e083fbf225b4f4299242a2c503f4e12573c5597f
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325858Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 4ee172b59b8f9a19921c300ecf394dc632e301c0f375a6e86adfade6ec86a619
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325881Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: f7fa9416148a602515b571aedb11d7794ccdd4b2cce57bed8b84b78fc355a46e
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325904Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d3e08dab853358cc229c72adda689e35048eee9a5544b36bac85a8c5649a85c7
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5342_Solution_A.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325926Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 31d821180b177a4395ac64cfe2eb443091729cb74309085beeb1b765ed2dd2f2
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5343_Solution_B.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325946Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: a1f8fb64c671e4aae298c328e3a93b1ad420e2d60c7400dbae6775f8081a0e33
- evidence_id: report-32
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/togo_medium_m190.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325966Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: d29c2d8798f20259a253d2b17745d675b4a789de94bdcef5279332d086383022
- evidence_id: report-33
  kind: prior_review
  reference: reports/yaml_record_review/20260923T163955Z-jcm_medium_no_197.md
  locator: Complete report
  accessed_at: '2026-10-28T14:51:42.325988Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 6497a50f712e4169a8f7a7cf4ae62d97e909b6695d86b7c522679b8f08909d7f
- evidence_id: dep180
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
  locator: Exact document_scopes in quantity inventory
  accessed_at: '2026-10-28T14:51:42.370152Z'
  support: context_only
  summary: Only iron/trace compositions and acid within the iron stock; parent receiving
    doses, other stocks and basal conditions excluded.
  snapshot_sha256: 5d4cf1d8c967ba57f9ecc15143ebbe65a2d8d6f7b0944cf21e59388d04285331
- evidence_id: dep190
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: Exact document_scopes in quantity inventory
  accessed_at: '2026-10-28T14:51:42.370211Z'
  support: context_only
  summary: Only vitamin composition. Parent receiving dose, mineral stock, basal ingredients
    and parent preparation excluded.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: compare5342
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml
  locator: Exact document_scopes in quantity inventory
  accessed_at: '2026-10-28T14:51:42.370257Z'
  support: context_only
  summary: Comparison-only wrong linked stock identity; full bytes retained, concentrations/preparation
    excluded from receiving-medium assessment.
  snapshot_sha256: fbc65564968b86b312f7795ff5c4527f199c51d04dc2764452d46bb5ba339566
- evidence_id: compare5343
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml
  locator: Exact document_scopes in quantity inventory
  accessed_at: '2026-10-28T14:51:42.370277Z'
  support: context_only
  summary: Comparison-only wrong linked stock identity; full bytes retained, concentrations/preparation
    excluded from receiving-medium assessment.
  snapshot_sha256: 84a4c07adfb1f11f32159a52f5e575738eb641428074b0958a68b8d5ba265ba5
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _assembled_solution_sections, _extract_assembled_solutions, _local_batch_volume_ml,
    _local_solution_composition, _solution_from_item, _parse_unit
  accessed_at: '2026-10-28T14:51:42.384588Z'
  support: context_only
  summary: Current importer preserves local solution stages and nested references;
    _local_batch_volume_ml uses a source-volume corroboration heuristic. Its declared
    inference is not independent measured final-volume evidence. _parse_unit now maps
    L correctly, but bare g/ml mappings and bare-percent basis still need source-specific
    assessment. Current code is not historical execution proof.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-migration
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _resolve_solution and _migrate_media_file
  accessed_at: '2026-10-28T14:51:42.384651Z'
  support: context_only
  summary: Current name-to-single-ID lookup can resolve generic Solution A/B to unrelated
    provider records and preserves original quantities when moving them. Present links
    are checked directly; current code alone does not establish the exact old execution.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T14:51:42.384678Z'
  support: context_only
  summary: Current _merge_ingredient_group collapses identical concentrations and
    flags unequal values rather than adding them. Existing historical 960 water sum
    is not attributed to unchanged current behavior.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-stock-repair
  kind: record_content
  reference: scripts/repair_jcm_stock_preparations.py
  locator: frozen, sources, Review.leaf, Review.stock, build, process
  accessed_at: '2026-10-28T14:51:42.384701Z'
  support: context_only
  summary: Current source-specific repair wrapper checks frozen raw pins and separates
    water volume, explicit reagent strength, receiving dose and batch-input notes.
    Credit the existing M180/M190 repairs within the selected subsections; their parent
    doses and procedures are not transferred.
  snapshot_sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/historical-reading.json
  accessed_at: '2026-10-28T14:51:42.389553Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: f75b83cfa4a84db7a1c7b79a637b22b65c2454e640ec5087749f8e79399aeaf0
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T14:51:42.389630Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 12207e0c12810a34321eda9116c168fc85a6e572ac80d24fcda2601244b7fb28
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/complete-document-reader.json
  accessed_at: '2026-10-28T14:51:42.389661Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 7530e5397963af34f4cfeab8faf56e3f473712ac4fef2652a6ef2ddaa0f3c6ac
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T14:51:42.389751Z'
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
  accessed_at: '2026-10-28T14:51:42.389783Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch070/record10/historical-current-object-joins.json
  accessed_at: '2026-10-28T14:51:42.389806Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: 1c68abb71b75aefd3711b5914fb4743f450da8c587fb93dbc05fd4d0c639429a
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T14:35:06.728776Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248
  accessed_at: '2026-10-28T14:35:07.525342Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi91248.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: d0959ac455ece32a6e94c13fd8e592403109201b6c61144dccfe0d58f1916380
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16526
  accessed_at: '2026-10-28T14:35:01.936923Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi16526.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 1fc9ed85cc20ea796dc5884bab2961c0cb13288fec88089767d5ca0349e6ab66
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997
  accessed_at: '2026-10-28T14:35:02.382360Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi17997.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: c4f240d59927c0f5c6c8d29c14830d0f278cfeabc4ed924be5c2b6bbe1039c05
- evidence_id: chebi18276
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276
  accessed_at: '2026-10-28T14:35:02.688312Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi18276.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: e9495ec2aad65253b7f792e780c1610f9f12f2c0bb20e06c2526156d37b09ed7
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T14:35:01.173152Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi15377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T14:35:06.253293Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T14:35:07.435195Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34683
  accessed_at: '2026-10-28T14:35:05.186042Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi34683.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 77f17276e9ef67f5b284232543dcfb3c01546658eb9e93fad4cbd1a5374bfb56
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T14:35:02.822174Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T14:35:06.792236Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T14:35:03.855941Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T14:35:07.256538Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T14:35:06.849931Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T14:35:06.661699Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T14:35:04.988953Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T14:35:07.378592Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696
  accessed_at: '2026-10-28T14:35:05.487011Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi35696.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 22f49067d1405baa8e2bbd7c4405035d8663c69aa045b7bbacf363bb30729244
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T14:35:05.375503Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T14:35:07.069916Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T14:35:05.804165Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T14:35:01.618721Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T14:35:03.585856Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T14:35:05.860963Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi49105.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T14:35:03.969274Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi31345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T14:35:03.675361Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi30961.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T14:35:03.186082Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi27470.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T14:35:02.184841Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi176843.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T14:35:02.068406Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi17015.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T14:35:01.589989Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T14:35:01.559653Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi16494.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: chebi64220
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64220
  accessed_at: '2026-10-28T14:35:06.424484Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi64220.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 7b853c2e1de3c4e8d3fc3e2a0fd323e1255065dd90557ad3b76d2b9d2955906d
- evidence_id: chebi53258
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53258
  accessed_at: '2026-10-28T14:35:06.015891Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi53258.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 2548ceaeb44e95b27d651544eb77e4500566e542c4837e5d7f2725e4f0ac55ad
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795
  accessed_at: '2026-10-28T14:35:04.075672Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi31795.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: ceb0c93d1964844e99454d74730971855710441d92eec74aff5c873c833e324a
- evidence_id: chebi32583
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32583
  accessed_at: '2026-10-28T14:35:04.582091Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi32583.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: f396bbf9a431ab7d3eed7ea3b8305dfddaf26ec3a9b88b3f507b1427c8723826
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T14:35:04.576516Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  accessed_at: '2026-10-28T14:35:03.339895Z'
  locator: REVIEW_WORK/batch070/source07-08-10-supplement/chebi29377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Current exact ontology object for existing scoped local slots; source chemical
    form assessed separately.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:11:10.216016Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 452bf5fbc8f56db96834698849e154b76e43f6861936f22548791167f5fae0fb
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:51:42.499279Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 70fc29bdd340a2b54a838c3fb54b9c8264c32177008f1a51de9d3e33e2338424
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:51:42.499421Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 44c0b0584c39f5413dbd9aeecf683afc5838b502cd5bdd7387136e3ee18b5d57
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:51:42.499565Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 4135d2403fe18bd161710c501ed232d875608f1e54c55768895eefd2550421fb
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:51:42.499697Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 9a7754a9b8262328f35dbb33454a4abc404eec58257a21686004f29796e29529
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T14:51:42.499733Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 6c787b23b10228a2aeceb98d1012b557c632f4b9f625b3e992fe60d07617f8c3
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch070/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T15:11:10.216067Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 98c4e963e1d8c672c17dc13d727b09d649c64b731e3b7dfb7d4d7672274fb6c5
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch070/record10/schema-result.json
  accessed_at: '2026-10-28T14:34:17.296349Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 62f0ab82711aa0a1d9e4fc836da9ea259825b5a6fcc9dcf5d45e419abc8b19aa
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch070/record10/strict-result.json
  accessed_at: '2026-10-28T14:34:18.208275Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 7f1412e9ae422a9e17c03a3fcd535b2c5915e80365d1f87db544475e8982f6fa
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch070/record10/terms-result.json
  accessed_at: '2026-10-28T14:34:19.214472Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 0043a91ae9a37c20c23e212aa07be4dc24c25622849124c5f1efc595289df852
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch070/record10/references-result.json
  accessed_at: '2026-10-28T14:34:19.897782Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 56eec737c7159c76640d70636cfbca1de4454bef5ce8552d0c3eaea4485fc1e2
assessments:
- assessment_id: identity
  area: identity
  topic: Exact637 source identity and stock-link boundaries
  outcome: concern
  summary: TOGO M651 and current primary 637 identify the same R6 medium and exact
    636 modification. The receiving A/B links are wrong generic-name cross-links;
    source identity is established without inventing strain taxonomy.
  target_ids:
  - CultureMech:010053
  evidence_ids:
  - target
  - owner
  - jcm637
  - currentTogo651
  - stock5342
  - stock5343
- assessment_id: classification
  area: consistency
  topic: Complex liquid formulation
  outcome: supported
  summary: Yeast extract and tryptone support COMPLEX/UNDEFINED. No solidifying ingredient
    is asserted; LIQUID is consistent. No organism-growth claim is inferred.
  target_ids:
  - CultureMech:010053
  evidence_ids:
  - target
  - owner
  - jcm636
- assessment_id: structure
  area: schema
  topic: Original and additive inspection boundaries
  outcome: supported
  summary: The original four canonical diagnostics passed once; reference validation
    checked zero attached references. The additive inspection only adds current source-repair
    history/writer inputs and preserves all originals; no canonical rerun or formal
    save occurred.
  target_ids:
  - CultureMech:010053
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 47 current concentration fields are covered by 49 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:010053
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b070-quantity-inventory-v1","target":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","quantity_field_count":47,"decisions":[{"quantity_id":"q1","label":"Na2S・9H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"VARIABLE
    does not retain the explicitly stated 0.025% receiving-medium declaration and
    separately prepared 5% stock. Keep both exact source stages and unspecified percentage
    bases; do not infer mass, volume, density or stock dose.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"Na2S・9H2O\",\n          \"conc_value\": 0.025,\n          \"conc_unit\": \"%\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001494\",\n          \"gmo_id\": \"GMO_001494\",\n          \"label\":
    \"Sodium sulfide nonahydrate solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    6,\n      \"comment\": \"Distribute the medium into culture vessels under the
    same gas mixture and seal with butyl rubber stoppers. Prior to inoculation, reduce
    the medium with 0.025% L--cysteine・HCl・H2O and 0.025% Na2S・9H2O (autoclaved as
    5% solutions under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt
    lines 88-96","quote":"Distribute the medium into culture vessels under the same
    gas mixture and seal with butyl rubber stoppers.  Prior to inoculation, reduce
    the medium with 0.025% L-cysteine·HCl·H\n2\nO and 0.025% Na\n2\nS·9H\n2\nO (autoclaved
    as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"L--cysteine・HCl・H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"VARIABLE
    does not retain the explicitly stated 0.025% receiving-medium declaration and
    separately prepared 5% stock. Keep both exact source stages and unspecified percentage
    bases; do not infer mass, volume, density or stock dose.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"L--cysteine・HCl・H2O\",\n          \"conc_value\": 0.025,\n          \"conc_unit\":
    \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001496\",\n          \"gmo_id\":
    \"GMO_001496\",\n          \"label\": \"L-Cysteine hydrochloride monohydrate solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    6,\n      \"comment\": \"Distribute the medium into culture vessels under the
    same gas mixture and seal with butyl rubber stoppers. Prior to inoculation, reduce
    the medium with 0.025% L--cysteine・HCl・H2O and 0.025% Na2S・9H2O (autoclaved as
    5% solutions under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt
    lines 88-96","quote":"Distribute the medium into culture vessels under the same
    gas mixture and seal with butyl rubber stoppers.  Prior to inoculation, reduce
    the medium with 0.025% L-cysteine·HCl·H\n2\nO and 0.025% Na\n2\nS·9H\n2\nO (autoclaved
    as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"Carbon
    dioxide gas","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"Retain
    the VARIABLE entry as a truthful unquantified gas placeholder. The exact637 override
    and its gas-phase mixture belong to the separately assessed preparation; they
    do not establish a dissolved concentration or liquid dose. Base nitrogen handling
    remains separate preparation context.","source_stage":"Selected R6: local A/B
    and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\":
    8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas
    phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt
    lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase
    with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"Retain
    the VARIABLE entry as a truthful unquantified gas placeholder. The exact637 override
    and its gas-phase mixture belong to the separately assessed preparation; they
    do not establish a dissolved concentration or liquid dose. Base nitrogen handling
    remains separate preparation context.","source_stage":"Selected R6: local A/B
    and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\":
    8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas
    phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt
    lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase
    with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Hydrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"evidence_only","rationale":"Retain
    the VARIABLE entry as a truthful unquantified gas placeholder. The exact637 override
    and its gas-phase mixture belong to the separately assessed preparation; they
    do not establish a dissolved concentration or liquid dose. Base nitrogen handling
    remains separate preparation context.","source_stage":"Selected R6: local A/B
    and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\":
    \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\":
    8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas
    phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt
    lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase
    with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"960.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"960.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    two water inputs belong to different stock batches. Their historical sum960 G_PER_L
    is neither a water amount in an allowed volume unit nor a final-medium concentration.
    Restore separate input volumes without asserting final mixed volume.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 860,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 100,\n          \"unit\": \"ml\",\n          \"gmo\":
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
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;860.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.54","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.54","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution A, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.54,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\":
    \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 0 (zero-based)","quote":"<TR><TD WIDTH=75%> KH<sub>2</sub>PO<sub>4</sub>                                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.54&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.54,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.627907,\n                        \"mmol_l\":
    4.61405,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q8","label":"Resazurin","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution A, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.
    The source unit is mg, not g; local 1 G_PER_L additionally loses that unit.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\":
    \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\":
    \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 4 (zero-based)","quote":"<TR><TD WIDTH=75%> Resazurin                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\":
    25,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.00116279,\n                        \"mmol_l\":
    0.00507348,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Na2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.34","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"1.34","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution A, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
    \"Na2HPO4\",\n          \"volume\": 1.34,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001069\",\n          \"gmo_id\": \"GMO_001069\",\n          \"label\":
    \"Disodium phosphate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 1 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>HPO<sub>4</sub>                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.34&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\":
    233,\n                        \"amount\": 1.34,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.55814,\n                        \"mmol_l\":
    10.976,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Yeast extract (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution A, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
    \"Yeast extract (BD-Difco)\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\":
    \"Bacto &trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 2 (zero-based)","quote":"<TR><TD WIDTH=75%> Yeast extract (BD-Difco)                                           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;3.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3.48837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"Tryptone (BD-Difco)","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution A, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
    \"Tryptone (BD-Difco)\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001043\",\n          \"gmo_id\": \"GMO_001043\",\n          \"label\":
    \"Bacto &trade; Tryptone\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 3 (zero-based)","quote":"<TR><TD WIDTH=75%> Tryptone (BD-Difco)                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\":
    71,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.581395,\n                        \"mmol_l\": 8.17945,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q12","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution B, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
    \"NaCl\",\n          \"volume\": 0.19,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\":
    \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 7 (zero-based)","quote":"<TR><TD WIDTH=75%> NaCl                                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.19&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 0.19,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.86275,\n                        \"mmol_l\":
    31.8745,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q13","label":"CaCl2・2H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution B, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
    \"CaCl2・2H2O\",\n          \"volume\": 0.006,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\":
    \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 8 (zero-based)","quote":"<TR><TD WIDTH=75%> CaCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.006&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0588235,\n                        \"mmol_l\":
    0.400119,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q14","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution B, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.19,\n          \"unit\": \"g\",\n          \"gmo\":
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
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 6 (zero-based)","quote":"<TR><TD WIDTH=75%> NH<sub>4</sub>Cl                                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.19&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.19,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.86275,\n                        \"mmol_l\":
    34.8242,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"MgCl2・6H2O","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.063","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.063","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    exact source places this amount in local solution B, not as a direct final-medium
    G_PER_L rate. Preserve the literal batch amount/form and source stage; provider
    g_l is a separately declared stock rate, not proof of the final R6 denominator.","source_stage":"Selected
    R6: local A/B and exact 637 override","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"MgCl2・6H2O\",\n          \"volume\": 0.063,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 9 (zero-based)","quote":"<TR><TD WIDTH=75%> MgCl<sub>2</sub>&#183;6H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.063&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"apiJ636","reference":"https://mediadive.dsmz.de/rest/medium/J636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/apiJ636.raw","raw_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","text_sha256":"db99fe99d41f212feb1333f90a13d879d0b19ac06eeb01a8c886fab246c29c16","accessed_at":"2026-10-28T14:35:00.431313Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.063,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.617647,\n                        \"mmol_l\":
    3.03806,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q16","label":"Solution A","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"860","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"860","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock
    stage; do not substitute ML_PER_L without a final-medium denominator. Resolve
    the wrong generic-name provider link against exact local A/B, not against a similarly
    named stock.","source_stage":"Selected receiving addition; A/B local, iron/trace
    withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Solution A\",\n          \"volume\": 860,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M651\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 5 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;860.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"Solution
    B","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"102","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"102","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock
    stage; do not substitute ML_PER_L without a final-medium denominator. Resolve
    the wrong generic-name provider link against exact local A/B, not against a similarly
    named stock.","source_stage":"Selected receiving addition; A/B local, iron/trace
    withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Solution B\",\n          \"volume\": 102,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M651\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 12 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"FeCl2
    solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[2].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock
    stage; do not substitute ML_PER_L without a final-medium denominator. Use only
    the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected
    receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
    \"FeCl2 solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 10 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub> solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"Trace
    element solution (see Medium [M180])","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[3].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock
    stage; do not substitute ML_PER_L without a final-medium denominator. Use only
    the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected
    receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
    \"Trace element solution (see Medium [M180])\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M180\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 11 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace element solution
    (see Medium No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=187\">187</a>)           </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"8%
    NaHCO3 solution","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"30","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[4].concentration","stored":{"value":"30","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock
    stage; do not substitute ML_PER_L without a final-medium denominator. Use only
    the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected
    receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Trace
    vitamins (see Medium [M190])","local_fields":[{"path":"data/merge_yaml/merged/Clostridium_R6_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml","field_path":"solutions[5].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"Source
    ml additions have been mislabeled G_PER_L. Retain batch volumes and nested stock
    stage; do not substitute ML_PER_L without a final-medium denominator. Use only
    the explicitly referenced stock subsection; no parent-medium dose transfer.","source_stage":"Selected
    receiving addition; A/B local, iron/trace withinB, vitamins/bicarbonate separate","sources":[{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
    \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 14 (zero-based)","quote":"<TR><TD WIDTH=75%> Trace vitamins (see Medium
    No. <a href=\"/cgi-bin/jcm/jcm_grmd?GRMD=197\">197</a>)                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Iron
    stock water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[0].concentration","stored":{"value":"0.99","unit":"L"}}],"decision":"verified","rationale":"Retain
    the existing exact batch-input claim and attached literal source evidence; its
    cited raw SHA matches the current capture. This authenticates content, not a newly
    recovered original access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;990.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Iron
    stock FeCl2 tetrahydrate batch input","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 1.5 g. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> FeCl<sub>2</sub>&#183;4H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.5&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> g  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Nested
    HCl reagent addition","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].concentration","stored":{"value":"0.01","unit":"L"}}],"decision":"verified","rationale":"Existing
    0.01 L is the exact 10 ml addition within the iron stock. M180 root evidence[0]
    contains the additional literal HCl excerpt and exact nested concentration locator,
    with a digest matching the current source. This authenticates the retained dose
    at that stock stage only; the unspecified 25% basis and parent receiving-medium
    doses are not inferred or transferred.","source_stage":"HCl dose within iron stock","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% HCl (7.7 M)                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Nested
    HCl explicit reagent strength","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[0].solutions[0].composition[0].concentration","stored":{"value":"7.7","unit":"MOLAR"}}],"decision":"verified","rationale":"Existing
    7.7 M is explicit reagent strength with a matching attached TOGO literal/digest.
    The 25% basis remains unspecified and is not used for a conversion. The older
    JCM plain-text snippet is corroborated by the current table but not asserted to
    match current raw HTML bytes.","source_stage":"HCl reagent, not final medium","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> 25% HCl (7.7 M)                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Trace
    stock Distilled water","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Retain
    the existing exact batch-input claim and attached literal source evidence; its
    cited raw SHA matches the current capture. This authenticates content, not a newly
    recovered original access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 26 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L        </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Trace
    stock Na2MoO4・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 36 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Na<sub>2</sub>MoO<sub>4</sub>&#183;2H<sub>2</sub>O                            </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;36.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Trace
    stock H3BO3","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 6 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> H<sub>3</sub>BO<sub>3</sub>                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;6.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Trace
    stock MnCl2・4H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 100 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> MnCl<sub>2</sub>&#183;4H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;100.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"Trace
    stock CoCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 190 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> CoCl<sub>2</sub>&#183;6H<sub>2</sub>O                                </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;190.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Trace
    stock NiCl2・6H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 24 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> NiCl<sub>2</sub>&#183;6H<sub>2</sub>O                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;24.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"Trace
    stock CuCl2・2H2O","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> CuCl<sub>2</sub>&#183;2H<sub>2</sub>O                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Trace
    stock ZnCl2","local_fields":[{"path":"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Mineral source; Properties: Inorganic compound, Defined component, Simple component\n\nSource
    batch input: 70 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo180","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M180","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo180.raw","raw_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","text_sha256":"a2ba84bc75a35379b464d5ac8a7ce0f787642b69838cdc2b4763a5657555edba","accessed_at":"2026-10-28T14:35:16.260746Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm187","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm187.raw","raw_sha256":"e01f3a9740644bb7c30a64c901083747c0a05ff1c6bc123f63de8632ecfce804","text_sha256":"9770fd9e001c3a8aab8415d94c72cca1fadec4928f262f480c37c99279a0aa7b","accessed_at":"2026-10-28T14:35:00.347668Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> ZnCl<sub>2</sub>                                               </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;70.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"Vitamin
    stock Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[0].concentration","stored":{"value":"1","unit":"L"}}],"decision":"verified","rationale":"Retain
    the existing exact batch-input claim and attached literal source evidence; its
    cited raw SHA matches the current capture. This authenticates content, not a newly
    recovered original access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 25 (zero-based)","quote":"<TR><TD WIDTH=75%> Distilled water                                         </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;1.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> L  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"Vitamin
    stock Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[1].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> Biotin                                                  </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"Vitamin
    stock p--Aminobenzoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[2].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 23 (zero-based)","quote":"<TR><TD WIDTH=75%> <I>p</I>-Aminobenzoic acid                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Vitamin
    stock Thiamine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[3].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 18 (zero-based)","quote":"<TR><TD WIDTH=75%> Thiamine&#183;HCl                                      </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Vitamin
    stock Calcium pantothenate","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[4].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 21 (zero-based)","quote":"<TR><TD WIDTH=75%> Calcium pantothenate                                    </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"Vitamin
    stock Pyridoxine・HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[5].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 10 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 17 (zero-based)","quote":"<TR><TD WIDTH=75%> Pyridoxine&#183;HCl                                   </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;10.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Vitamin
    stock Folic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[6].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 2 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 16 (zero-based)","quote":"<TR><TD WIDTH=75%> Folic acid                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;2.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Vitamin
    stock Vitamin B12","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[7].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 0.1 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 22 (zero-based)","quote":"<TR><TD WIDTH=75%> Vitamin B<sub>1</sub><sub>2</sub>                                       </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;0.1&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Vitamin
    stock Riboflavin","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[8].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 19 (zero-based)","quote":"<TR><TD WIDTH=75%> Riboflavin                                              </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Vitamin
    stock Nicotinic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[9].notes","stored":"Role:
    Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 20 (zero-based)","quote":"<TR><TD WIDTH=75%> Nicotinic acid                                          </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Vitamin
    stock Lipoic acid","local_fields":[{"path":"data/normalized_yaml/bacterial/togo_medium_m190.yaml","field_path":"solutions[1].composition[10].notes","stored":"Role:
    Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource
    batch input: 5 mg. Final preparation volume is not independently established;
    the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter
    concentration."}],"decision":"verified","rationale":"Retain the existing exact
    batch-input claim and attached literal source evidence; its cited raw SHA matches
    the current capture. This authenticates content, not a newly recovered original
    access event or an absent final-volume concentration.","source_stage":"Scoped
    stock recipe only","sources":[{"evidence_id":"currentTogo190","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo190.raw","raw_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","text_sha256":"61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528","accessed_at":"2026-10-28T14:35:16.184204Z","locator":"components[1].items[10]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"jcm197","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm197.raw","raw_sha256":"39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532","text_sha256":"4238f8aa85abfecffbc78f341694b20dc48537d7742cec72962105e3ea3cb450","accessed_at":"2026-10-28T14:35:00.337347Z","locator":"HTML
    table row 24 (zero-based)","quote":"<TR><TD WIDTH=75%> Lipoic acid                                             </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;5.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> mg  </TD></TR>","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Exact637
    override","local_fields":[],"decision":"evidence_only","rationale":"Omit base636
    methanol and apply the explicitly replaced gas-phase identity/ratio. No taxonomic
    identity or strain growth is inferred from R6.","source_stage":"Source-only preparation
    or variant control","sources":[{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt
    lines 6-12","quote":"Use Medium No.\n636\nwithout methanol.  Replace the gas phase
    with a H\n2\n-CO\n2\n(80:20, v/v) gas mixture.","quote_basis":"derivative text"},{"evidence_id":"apiJ637","reference":"https://mediadive.dsmz.de/rest/medium/J637","raw_path":"REVIEW_WORK/batch070/source07-08-10/apiJ637.raw","raw_sha256":"e765ff2d61eed716a560057abdc1fd1f4dbb2ae1afac17248deae3516537d453","text_sha256":"e765ff2d61eed716a560057abdc1fd1f4dbb2ae1afac17248deae3516537d453","accessed_at":"2026-10-28T14:34:10.810177Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Use Medium No. 636 without methanol. Replace the gas phase with a H2-CO2 (80:20,
    v/v) gas mixture.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[3]","quote":"{\n      \"paragraph_index\":
    8,\n      \"comment\": \"Use Medium No. [636] without methanol. Replace the gas
    phase with a H2--CO2 (80:20, v/v) gas mixture.\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Separate
    sterilization and order","local_fields":[],"decision":"evidence_only","rationale":"Retain
    primary A/B preparation, cooling and subsequent filter-sterilized additions, scoped
    by the637 no-methanol override. Do not carry over the excluded methanol/C recipe
    as an R6 ingredient.","source_stage":"Source-only preparation or variant control","sources":[{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt
    lines 73-96","quote":"Autoclave Solutions A and B separately and autoclave Solution
    C in a closed tube or vial.  After cooling, combine the three solutions under
    a stream of N\n2\n-CO\n2\n(80:20, v/v), then add the following solutions (filter-sterilized):\nTrace
    vitamins (see Medium No.\n197\n)\n10.0\nml\n8% NaHCO\n3\nsolution\n30.0\nml\nDistribute
    the medium into culture vessels under the same gas mixture and seal with butyl
    rubber stoppers.  Prior to inoculation, reduce the medium with 0.025% L-cysteine·HCl·H\n2\nO
    and 0.025% Na\n2\nS·9H\n2\nO (autoclaved as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative
    text"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Autoclave Solutions A and B separately and autoclave
    Solution C in a closed tube or vial. After cooling, combine the three solutions
    under a stream of N2--CO2 (80:20, v/v), then add the following solutions (filter--sterilized):\"\n    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q47","label":"Reducing-agent stock stage","local_fields":[],"decision":"evidence_only","rationale":"The
    source states separate 5% stocks and 0.025% receiving declarations. Their percentage
    bases and amount of stock added are not independently specified; no calculation
    or operational optimization is performed.","source_stage":"Source-only preparation
    or variant control","sources":[{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt
    lines 88-96","quote":"Distribute the medium into culture vessels under the same
    gas mixture and seal with butyl rubber stoppers.  Prior to inoculation, reduce
    the medium with 0.025% L-cysteine·HCl·H\n2\nO and 0.025% Na\n2\nS·9H\n2\nO (autoclaved
    as 5% solutions under a N\n2\natmosphere).","quote_basis":"derivative text"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"comments[1]","quote":"{\n      \"paragraph_index\":
    6,\n      \"comment\": \"Distribute the medium into culture vessels under the
    same gas mixture and seal with butyl rubber stoppers. Prior to inoculation, reduce
    the medium with 0.025% L--cysteine・HCl・H2O and 0.025% Na2S・9H2O (autoclaved as
    5% solutions under a N2 atmosphere).\"\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Bicarbonate
    stock label","local_fields":[],"decision":"evidence_only","rationale":"Retain
    8% as the source label attached to the 30 ml addition, without assuming w/v or
    density. No unsupported concentration object is added.","source_stage":"Source-only
    preparation or variant control","sources":[{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"HTML
    table row 15 (zero-based)","quote":"<TR><TD WIDTH=75%> 8% NaHCO<sub>3</sub> solution                                 </TD><TD
    WIDTH=15% ALIGN=RIGHT><font size=+1><tt>&nbsp;30.0&nbsp;&nbsp;&nbsp;&nbsp;</tt></font></TD><TD
    WIDTH=10% ALIGN=RIGHT> ml  </TD></TR>","quote_basis":"raw UTF-8"},{"evidence_id":"currentTogo651","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M651","raw_path":"REVIEW_WORK/batch070/source07-08-10-current-json/currentTogo651.raw","raw_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","text_sha256":"5c6a18cd2f41e1e9ae6acf011622d53df8489cd3880a12f72c6a884088e8945e","accessed_at":"2026-10-28T14:35:16.265977Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q49","label":"Primary catalogue default","local_fields":[],"decision":"evidence_only","rationale":"The
    catalogue prints a default sterilization statement, not an incubation temperature/time.
    Specific filtration and variant exclusions take precedence within their source
    scope.","source_stage":"Source-only preparation or variant control","sources":[{"evidence_id":"jcm637","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=637","raw_path":"REVIEW_WORK/batch070/source07-08-10/jcm637.raw","raw_sha256":"62e1697caf29d8b2b166acb55f313b6cb6ffa4aec22a3356823d6596574643ea","text_sha256":"619cb046803c7179aa856c2db88713ee3ca5642b53a793da52a820807f660898","accessed_at":"2026-10-28T14:34:10.653890Z","locator":"jcm637.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"},{"evidence_id":"jcm636","reference":"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=636","raw_path":"REVIEW_WORK/batch070/source07-08-10-supplement/jcm636.raw","raw_sha256":"dafcc2ffbee3d30fae13d4ba208df2e1d54636063c4e61a6c7096081d4edd27b","text_sha256":"0fc6855a49f712e8ec392406cc0b1f3d7062b93c2616679a40d44de25977b38a","accessed_at":"2026-10-28T14:35:00.347725Z","locator":"jcm636.txt
    lines 4-4","quote":"Unless otherwise stated, sterilize media by autoclaving at
    121°C for 15 min.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/Clostridium_R6_Medium.yaml":null,"data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml":null,"data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml":["solutions[0].preferred_term","solutions[0].name","solutions[0].composition","solutions[0].solutions","solutions[1].preferred_term","solutions[1].name","solutions[1].composition"],"data/normalized_yaml/bacterial/togo_medium_m190.yaml":["solutions[1].preferred_term","solutions[1].composition"],"data/normalized_yaml/bacterial/mediadive_5342_Solution_A.yaml":["preferred_term","name","term","composition[0].preferred_term","composition[0].term","composition[0].chebi_term","composition[1].preferred_term","composition[1].term","composition[1].chebi_term","composition[2].preferred_term","composition[2].term","composition[2].chebi_term","composition[3].preferred_term","composition[3].term","composition[3].chebi_term","composition[4].preferred_term","composition[4].term","composition[4].chebi_term","composition[5].preferred_term","composition[5].term","composition[5].chebi_term","composition[6].preferred_term","composition[6].term","composition[6].chebi_term","composition[7].preferred_term","composition[7].term","composition[7].chebi_term"],"data/normalized_yaml/bacterial/mediadive_5343_Solution_B.yaml":["preferred_term","name","term","composition[0].preferred_term","composition[0].term","composition[0].chebi_term","composition[1].preferred_term","composition[1].term","composition[1].chebi_term"]},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: Exact current ontology objects and MIM rows are inspected for every in-scope
    slot. Selected salts/gases/hydrates are credited. In the explicitly referenced
    trace stock, cobalt and nickel hexahydrates map to anhydrous chemical entities.
    The source leaves calcium-pantothenate stereochemistry unspecified while CHEBI31345
    has stereochemical structure; preserve this uncertainty rather than claiming a
    confirmed wrong ID or converting mass. Wrong-linked5342/5343 chemistry is comparison
    context only; its citrate label/form issue is not promoted as a finding affecting
    the selected medium. Current label agreement and secondary-link presence are reported
    separately from chemical-form support.
  target_ids:
  - CultureMech:010053
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: All 12 complete historical reports and exact selected parent objects are
    retained with scoped current-object joins. Historical per-liter interpretations
    are not silently inherited. Existing M180/M190 water, reagent and batch-note repairs
    are credited against attached literal snippets and equal current raw SHA values;
    this does not recover their original access events. Current staged importer, conservative
    merger and non-summing cleanup behavior differ from old flattened records. The
    Oct8 repair wrapper was inspected through additive native inputs; only its scoped
    stock effects are assessed.
  target_ids:
  - CultureMech:010053
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-010053-stock-stages-and-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Local A/B batches and additions are flattened into final-medium concentrations
  description: The target and maintained owner flatten local A/B ingredients, sum
    distinct water inputs into 960 G_PER_L, label source 1 mg resazurin as 1 G_PER_L,
    and encode all six source ml additions as G_PER_L. Restore the exact stock/addition
    hierarchy and source units. Retained gram numbers are source batch inputs, not
    established final-medium rates; do not calculate a final volume from the listed
    input volumes.
  target_ids:
  - CultureMech:010053
  field_paths:
  - ingredients
  - solutions
  - ingredients[5].concentration
  - ingredients[7].concentration
  evidence_ids:
  - jcm636
  - jcm637
  - currentTogo651
  - apiJ636
  - quantities
  - writer-togo
  - writer-cleanup
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-010053-wrong-generic-stock-links
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Generic Solution A/B links identify unrelated stocks
  description: The two maintained links point to provider 5342/5343, whose current
    compositions are salt-rich stocks unrelated to the source 636 local A/B recipes.
    Generic-name equality is insufficient. Resolve receiving links to exact source-specific
    A/B compositions and retain separate provenance. The standalone comparison stocks
    are not requested to be reformulated.
  target_ids:
  - CultureMech:010053
  field_paths:
  - solutions[0].term
  - solutions[1].term
  - solutions[0].composition
  - solutions[1].composition
  evidence_ids:
  - jcm636
  - currentTogo651
  - stock5342
  - stock5343
  - compare5342
  - compare5343
  - writer-migration
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-010053-missing-variant-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Exact source variant and preparation stages are absent
  description: The current owner/target lack preparation prose and encode gases as
    generic VARIABLE ingredients. Preserve exact 637 methanol exclusion and gas-phase
    replacement, separate A/B preparation, subsequent additions, and the distinction
    between declared reducing-stock and receiving percentages. Percent basis and unspecified
    doses remain unresolved; do not import parent M180/M190 procedures.
  target_ids:
  - CultureMech:010053
  field_paths:
  - preparation_steps
  - sterilization
  - ingredients[0]
  - ingredients[1]
  - ingredients[2]
  - ingredients[3]
  - ingredients[4]
  evidence_ids:
  - jcm637
  - jcm636
  - currentTogo651
  - quantities
  - writer-togo
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: 'Major preparation-completeness issue: source variant exclusions
    and ordered atmosphere/stock handling are absent. Unquantified gas placeholders
    are not themselves erroneous concentration values.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-010053-referenced-trace-hydrates
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Two scoped trace-stock IDs omit the source hexahydrate form
  description: The explicitly referenced M180 trace stock retains correct source batch
    amounts and names, but its cobalt and nickel hexahydrate rows use anhydrous CHEBI:35696
    and CHEBI:34887. Exact current ontology formulas confirm the form mismatch; correct
    those scoped IDs or retain the form explicitly unresolved without mass conversion.
    Other current mappings and source-supported batch notes are credited.
  target_ids:
  - CultureMech:010053
  field_paths:
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[4].term
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].composition[5].term
  evidence_ids:
  - dep180
  - jcm187
  - currentTogo180
  - groundings
  - old-claims
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
- finding_id: f5
  issue_key: culturemech-010053-stock-placeholders-and-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Stock placeholders and missing receiving-claim evidence remain
  description: All six selected descriptors have name Unknown solution despite source-specific
    preferred terms. Correct those placeholders and attach exact claim-level receiving
    evidence while preserving existing repaired dependency evidence. M180 iron/trace
    Unknown solution names should be replaced only within their explicit scoped stock
    descriptors. Do not invent a species or strain from R6.
  target_ids:
  - CultureMech:010053
  field_paths:
  - solutions
  - references
  - evidence
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[0].name
  - data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml::solutions[1].name
  evidence_ids:
  - currentTogo651
  - jcm637
  - dep180
  - dep190
  - old-claims
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: The target and maintained owner flatten local A/B ingredients, sum
    distinct water inputs into 960 G_PER_L, label source 1 mg resazurin as 1 G_PER_L,
    and encode all six source ml additions as G_PER_L. Restore the exact stock/addition
    hierarchy and source units. Retained gram numbers are source batch inputs, not
    established final-medium rates; do not calculate a final volume from the listed
    input volumes.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
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
  description: The two maintained links point to provider 5342/5343, whose current
    compositions are salt-rich stocks unrelated to the source 636 local A/B recipes.
    Generic-name equality is insufficient. Resolve receiving links to exact source-specific
    A/B compositions and retain separate provenance. The standalone comparison stocks
    are not requested to be reformulated.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
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
  description: The current owner/target lack preparation prose and encode gases as
    generic VARIABLE ingredients. Preserve exact 637 methanol exclusion and gas-phase
    replacement, separate A/B preparation, subsequent additions, and the distinction
    between declared reducing-stock and receiving percentages. Percent basis and unspecified
    doses remain unresolved; do not import parent M180/M190 procedures.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
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
  description: The explicitly referenced M180 trace stock retains correct source batch
    amounts and names, but its cobalt and nickel hexahydrate rows use anhydrous CHEBI:35696
    and CHEBI:34887. Exact current ontology formulas confirm the form mismatch; correct
    those scoped IDs or retain the form explicitly unresolved without mass conversion.
    Other current mappings and source-supported batch notes are credited.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:010053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
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
  description: All six selected descriptors have name Unknown solution despite source-specific
    preferred terms. Correct those placeholders and attach exact claim-level receiving
    evidence while preserving existing repaired dependency evidence. M180 iron/trace
    Unknown solution names should be replaced only within their explicit scoped stock
    descriptors. Do not invent a species or strain from R6.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:010053
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M651_Clostridium_R6_Medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M180_Desulfurococcus_Amylolyticus_Medium.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/togo_medium_m190.yaml
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
- Only M180 iron/trace subfields and M190 vitamin composition are scientifically assessed.
  Their parent basal ingredients, receiving doses, parent pH/gas and unrelated stock
  recipes are excluded. Full bytes/history remain provenance context.
- Provider5342/5343 are compared only to establish the incorrect receiving link; their
  concentrations and preparation are not assessed as R6 ingredients.
- APIJ636 provider g_l and volume fields are not independent measured final-volume
  evidence. Base methanol and its C-stock volume are explicitly excluded by637.
- The initial TOGO /rest/medium/M651 response is an application shell; the successful
  official JSON capture is separate. No source absence is inferred from that initial
  route.
- No taxon is inferred from R6; iModulonDB is not applicable because this record asserts
  no gene/transcriptomic claim.
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
