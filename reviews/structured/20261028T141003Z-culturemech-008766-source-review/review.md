# Scientific review: Cedears Standard Medium 3

- Review: 20261028T141003Z-culturemech-008766-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:46:02.628531Z
- Finished UTC: 2026-10-28T14:10:03.772161Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Five major issues concern flattened source stages, wrong stock references, supplied forms, omitted preparation and separate linked-stock quantity defects; one minor classification/evidence issue remains. All target/owner and linked-stock quantities are inventoried, eight attached stock claims are credited, and no unspecified final-volume or hydrate assumption is made.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch069 index 07
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008766 | data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml | generated | cedears_standard_medium_3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:008766 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:008766 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:008766 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:008766 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and stock reference identity

identity: concern. Targets: CultureMech:008766.

CM008766 and TOGO2172/NBRC1562 identify the selected medium; the maintained owner is exact. The two generic provider stock links have demonstrably different formulations. No organism or strain is named in the inspected primary recipe, and no growth claim is inferred.

### Native diagnostics and representation

schema: supported. Targets: CultureMech:008766.

All four original native diagnostics passed once, strict reported zero errors and references checked zero entries. Shape validity does not validate stock equivalence, amounts or chemistry. Current conservative merger rejects incompatible formulations and singleton-copy behavior does not certify the owner.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:008766.

87 current concentration fields are covered by 56 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b069-quantity-inventory-v1","target":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","quantity_field_count":87,"decisions":[{"quantity_id":"q1","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source lists distinct 1 L water inputs for basal, vitamin and trace batches. The generated 3 G_PER_L aggregates those inputs; owner 1 G_PER_L credits duplicate repair but still has the wrong unit and loses source stage. Preserve the separate L inputs, not a mass concentration or assumed final volume.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 77-79","quote":"Distilled water\n1\nL","quote_basis":"derivative text"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"CaCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored 0.247 G_PER_L adds 0.147 g basal and 0.1 g trace-stock input across different solution bases. Those are distinct batch masses, not a final-medium total. Restore stage-specific assertions without calculating a receiving concentration from input water.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.147,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 50-56","quote":"CaCl\n2\n·2H\n2\nO\n0.147\ng","quote_basis":"derivative text"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"CaCl2·2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 150-156","quote":"CaCl\n2\n·2H\n2\nO\n0.1\ng","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numerical value matches the listed basal batch mass in grams, but the source specifies input water rather than measured final volume. Preserve the supported source mass separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 32-36","quote":"NH\n4\nCl\n0.02\ng","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numerical value matches the listed basal batch mass in grams, but the source specifies input water rather than measured final volume. Preserve the supported source mass separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"K2HPO4\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\": \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 44-49","quote":"K\n2\nHPO\n4\n0.02\ng","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"MgCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numerical value matches the listed basal batch mass in grams, but the source specifies input water rather than measured final volume. Preserve the supported source mass separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"MgCl2·6H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 37-43","quote":"MgCl\n2\n·6H\n2\nO\n0.01\ng","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Sodium acetate","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.164","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.164","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numerical value matches the listed basal batch mass in grams, but the source specifies input water rather than measured final volume. Preserve the supported source mass separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"Sodium acetate\",\n          \"volume\": 0.164,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\": \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 68-70","quote":"Sodium acetate\n0.164\ng","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0071","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0071","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numerical value matches the listed basal batch mass in grams, but the source specifies input water rather than measured final volume. Preserve the supported source mass separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"Na2SO4\",\n          \"volume\": 0.0071,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 26-31","quote":"Na\n2\nSO\n4\n0.0071\ng","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"CAPS","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3.32","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3.32","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numerical value matches the listed basal batch mass in grams, but the source specifies input water rather than measured final volume. Preserve the supported source mass separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"CAPS\",\n          \"volume\": 3.32,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002374\",\n          \"gmo_id\": \"GMO_002374\",\n          \"label\": \"CAPS\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 65-67","quote":"CAPS\n3.32\ng","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"Ca3(PO4)2","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.372","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.372","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The numerical value matches the listed basal batch mass in grams, but the source specifies input water rather than measured final volume. Preserve the supported source mass separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"Ca3(PO4)2\",\n          \"volume\": 0.372,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002207\",\n          \"gmo_id\": \"GMO_002207\",\n          \"label\": \"Tricalcium phosphate\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 57-64","quote":"Ca\n3\n(PO\n4\n)\n2\n0.372\ng","quote_basis":"derivative text"}]},{"quantity_id":"q10","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their context and the literal gas ratio without inventing ingredient concentrations or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\": \"NaOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6) in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their context and the literal gas ratio without inventing ingredient concentrations or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6) in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"Oxygen gas","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their context and the literal gas ratio without inventing ingredient concentrations or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\": \"Oxygen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002262\",\n          \"gmo_id\": \"GMO_002262\",\n          \"label\": \"Oxygen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6) in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"Hydrogen gas","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their context and the literal gas ratio without inventing ingredient concentrations or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[14]","quote":"{\n          \"component_name\": \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\": \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6) in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 93-95","quote":"Biotin\n2\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 114-117","quote":"p\n-Aminobenzoic acid\n1\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"Thiamine-HCl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[15].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[15].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\": \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 102-104","quote":"Thiamine-HCl\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"Ca-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[16].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[16].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\": \"Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 111-113","quote":"Ca-pantothenate\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"Pyridoxine-HCl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[17].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[17].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 99-101","quote":"Pyridoxine-HCl\n10\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 96-98","quote":"Folic acid\n2\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.01,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 118-121","quote":"Vitamin B\n12\n0.01\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[20].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[20].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 105-107","quote":"Riboflavin\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[21].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[21].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source value is a milligram input in the separately prepared NBRC vitamin batch. The existing number in G_PER_L is both the wrong unit and the wrong receiving stage. Preserve the literal mg amount and 1 L water input; no final stock volume or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 108-110","quote":"Nicotinic acid\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[22].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[22].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 183-185","quote":"NaCl\n1\ng","quote_basis":"derivative text"}]},{"quantity_id":"q24","label":"Na2MoO4·2H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"Na2MoO4·2H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 174-182","quote":"Na\n2\nMoO\n4\n·2H\n2\nO\n0.024\ng","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 168-173","quote":"H\n3\nBO\n3\n0.01\ng","quote_basis":"derivative text"}]},{"quantity_id":"q26","label":"MnCl2·4H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"MnCl2·4H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 136-142","quote":"MnCl\n2\n·4H\n2\nO\n0.1\ng","quote_basis":"derivative text"}]},{"quantity_id":"q27","label":"CoCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"CoCl2·6H2O\",\n          \"volume\": 0.024,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 143-149","quote":"CoCl\n2\n·6H\n2\nO\n0.024\ng","quote_basis":"derivative text"}]},{"quantity_id":"q28","label":"NiCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.12","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"NiCl2·6H2O\",\n          \"volume\": 0.12,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 186-192","quote":"NiCl\n2\n·6H\n2\nO\n0.12\ng","quote_basis":"derivative text"}]},{"quantity_id":"q29","label":"CuCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\": \"CuCl2·2H2O\",\n          \"volume\": 0.025,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 161-167","quote":"CuCl\n2\n·2H\n2\nO\n0.025\ng","quote_basis":"derivative text"}]},{"quantity_id":"q30","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 157-160","quote":"ZnCl\n2\n0.1\ng","quote_basis":"derivative text"}]},{"quantity_id":"q31","label":"FeCl3·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[30].concentration","stored":{"value":"1.35","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[30].concentration","stored":{"value":"1.35","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\": \"FeCl3·6H2O\",\n          \"volume\": 1.35,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001047\",\n          \"gmo_id\": \"GMO_001047\",\n          \"label\": \"Iron(III) chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 129-135","quote":"FeCl\n3\n·6H\n2\nO\n1.35\ng","quote_basis":"derivative text"}]},{"quantity_id":"q32","label":"KAl(SO4)2·12H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[11]","quote":"{\n          \"component_name\": \"KAl(SO4)2·12H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001051\",\n          \"gmo_id\": \"GMO_001051\",\n          \"label\": \"Aluminum potassium sulfate dodecahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 205-213","quote":"KAl(SO\n4\n)\n2\n·12H\n2\nO\n0.02\ng","quote_basis":"derivative text"}]},{"quantity_id":"q33","label":"Nitrilotriacetic acid (NTA)","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[32].concentration","stored":{"value":"12.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[32].concentration","stored":{"value":"12.8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[12]","quote":"{\n          \"component_name\": \"Nitrilotriacetic acid (NTA)\",\n          \"volume\": 12.8,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 126-128","quote":"Nitrilotriacetic acid (NTA)\n12.8\ng","quote_basis":"derivative text"}]},{"quantity_id":"q34","label":"Na2WO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[13]","quote":"{\n          \"component_name\": \"Na2WO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001086\",\n          \"gmo_id\": \"GMO_001086\",\n          \"label\": \"Sodium tungstate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 199-204","quote":"Na\n2\nWO\n4\n0.004\ng","quote_basis":"derivative text"}]},{"quantity_id":"q35","label":"Na2SeO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The value is a gram input in the separate NBRC trace batch, not a final-medium ingredient rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[14]","quote":"{\n          \"component_name\": \"Na2SeO4\",\n          \"volume\": 0.004,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001602\",\n          \"gmo_id\": \"GMO_001602\",\n          \"label\": \"Sodium selenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 193-198","quote":"Na\n2\nSeO\n4\n0.004\ng","quote_basis":"derivative text"}]},{"quantity_id":"q36","label":"Vitamin solution*","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a 10 ml addition of its own locally defined stock to this basal batch, not 10 g/L. The receiving final volume is not stated. The current mediadive solution reference resolves to a different composition and must not supply the receiving recipe.","source_stage":"Receiving stock addition","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Vitamin solution*\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2172\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 71-73","quote":"Vitamin solution*\n10\nml","quote_basis":"derivative text"}]},{"quantity_id":"q37","label":"Trace element solution**","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies a 10 ml addition of its own locally defined stock to this basal batch, not 10 g/L. The receiving final volume is not stated. The current mediadive solution reference resolves to a different composition and must not supply the receiving recipe.","source_stage":"Receiving stock addition","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Trace element solution**\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2172\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 74-76","quote":"Trace element solution**\n10\nml","quote_basis":"derivative text"}]},{"quantity_id":"q38","label":"stock6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"stock6241 Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"stock6241 Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source specifies 200 μg and explicitly makes up to 100 ml. 200 μg = 0.0002 g; divided by 0.1 L gives 0.002 g/L, not the retained 2000 G_PER_L. This calculation applies only to standalone6241, not the NBRC vitamin stock.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"stock6241 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The source is an input/makeup water quantity, not 1000 percent v/v. Preserve the original volume representation and preparation context; no water density conversion is used. The explicit final make-up is 100 ml, so a fixed water dose and a final stock volume must remain distinguished.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"stock6241 structural placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The VARIABLE See source for composition entry is a structural placeholder, not an extra reagent or quantified addition. The actual composition is present; do not count or transfer this placeholder as a recipe ingredient.","source_stage":"Standalone placeholder","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"stock6241 retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"Existing preparation wording and declared original provider volume are supported by the current source. This preparation field has no separate attached literal evidence claim; retain it separately from incorrect water concentration. For6187 water is an input; for6241 make-up explicitly fixes final100ml.","source_stage":"Standalone stock preparation","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"stock6187 Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\": 34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\": \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"stock6187 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1000","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The source is an input/makeup water quantity, not 1000 percent v/v. Preserve the original volume representation and preparation context; no water density conversion is used.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"stock6187 FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.097","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\": 82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\": \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"stock6187 MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"0.041","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\": \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"stock6187 ZnCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\": 6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\": 2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\": \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"stock6187 CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\": 7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"stock6187 Na2MoO4 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"verified","rationale":"The existing attached literal composition claim matches this exact current raw response and its recorded historical digest. Its stored value/unit equals explicit provider g_l on the standalone stock basis. This authenticates current content, not an independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\": 8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"stock6187 structural placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The VARIABLE See source for composition entry is a structural placeholder, not an extra reagent or quantified addition. The actual composition is present; do not count or transfer this placeholder as a recipe ingredient.","source_stage":"Standalone placeholder","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"stock6187 retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","stored":"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing sequence:"}],"decision":"evidence_only","rationale":"Existing preparation wording and declared original provider volume are supported by the current source. This preparation field has no separate attached literal evidence claim; retain it separately from incorrect water concentration. For6187 water is an input; for6241 make-up explicitly fixes final100ml.","source_stage":"Standalone stock preparation","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": 3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q53","label":"NBRC vitamin water","local_fields":[],"decision":"evidence_only","rationale":"Separate 1 L solvent input, not a stated final stock volume.","source_stage":"Source-only stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 122-124","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q54","label":"NBRC trace water","local_fields":[],"decision":"evidence_only","rationale":"Separate 1 L solvent input, not a stated final stock volume.","source_stage":"Source-only stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 214-216","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q55","label":"Basal pH, sterilization order and headspace","local_fields":[],"decision":"evidence_only","rationale":"Retain pH11, vitamin exclusion from autoclaving, filter-sterile addition and literal N2/H2/O2 59/35/6 headspace ratio. The ratio basis is not specified; do not manufacture gas concentrations, a temperature or an autoclave duration.","source_stage":"Source-only stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\": 4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6) in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q56","label":"Trace pH and dissolution order","local_fields":[],"decision":"evidence_only","rationale":"Retain NTA-first dissolution, initial pH6.5 and final pH7.0 in the trace-stock stage. The NaOH dose is unspecified.","source_stage":"Source-only stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[6]","quote":"{\n      \"paragraph_index\": 10,\n      \"comment\": \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt lines 217-217","quote":"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with NaOH, and then add minerals. Final pH 7.0.","quote_basis":"derivative text"}]}],"document_scopes":{"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml":null,"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:008766.

All current asserted ontology slots and exact MIM memberships are enumerated separately from scientific forms. Three selected supplied-form contradictions are confirmed (pantothenate anion, cobalt and nickel hydrate loss). Named other hydrates, NTA, CAPS, salts and vitamins were checked against exact current formula/charge/structure. B12 remains a generic vitamer class; generic calcium pantothenate does not establish D stereochemistry. The provider6187 zinc hydrate notation is unresolved against its anhydrous term. Missing primary/secondary links, rejected current preferred-name rows and current CHEBI29032 MIM absence are distinct from ontology validity; no all-labels-imply-form claim is made.

### Existing repair credit and writer limits

provenance: supported. Targets: CultureMech:008766.

Complete target, owner and both linked-stock histories plus six complete historical reports and two exact parent records were read. The owner duplicate-water correction is retained; generated water remains stale, and unequal-stage calcium was not repaired. Eight standalone composition claims match current literal raw content and exact October7 digests; eleven historical recipe objects join current sources. Those equal bytes do not recover original access timestamps. Current cleanup no longer sums duplicates, current TOGO preserves primary/stock layers, and current merge requires exact scientific assertions. Preserve all earlier events and append new curation metadata only.

## Findings

### f1: Basal and stock amounts are conflated

major / open / confirmed; issue key: culturemech-008766-flattened-stages.

Restore source stages before any normalization: the generated water sum and retained owner water unit are wrong; calcium sums basal and trace-batch inputs; nine vitamin mg inputs are stored as final G_PER_L; thirteen other trace components are flattened; both stock doses are 10 ml additions mislabeled G_PER_L. Basal mass values are supported as batch inputs, but their final-volume denominator is unresolved. Credit the owner duplicate-water repair without treating it as a scientific stage repair.

### f2: Generic stock names resolve to different formulations

major / open / confirmed; issue key: culturemech-008766-stock-link-identity.

The two declared provider references are not the NBRC1562 stocks: solution6241 has three vitamins and explicit 100 ml make-up, while NBRC1562 lists nine vitamins with 1 L input water; solution6187 uses EDTA and six mineral/chelator components, while NBRC1562 has NTA and fourteen components. Resolve the receiving links from exact source identity and preserve the NBRC local stocks. Do not rewrite the independent provider stocks to make them resemble NBRC or transfer their doses. Replace Unknown solution names with source-scoped names. Current name-to-single-ID migration lacks formulation verification, but its current body does not prove the exact historical execution.

### f3: Three supplied forms conflict with asserted ontology chemistry

major / open / confirmed; issue key: culturemech-008766-supplied-forms.

In both target and owner, calcium pantothenate is mapped to the pantothenate anion CHEBI29032; cobalt chloride hexahydrate and nickel chloride hexahydrate are mapped to anhydrous CHEBI35696 and CHEBI34887. Exact current formulas confirm these mismatches. CHEBI53503 and53542 represent the named hydrates. CHEBI31345 represents a calcium salt but its D stereochemistry cannot be inferred from the generic source name, so it is a bounded candidate rather than an automatic replacement. Keep masses unchanged while resolving exact supplied forms.

### f4: Stage-specific preparation and atmosphere are omitted

major / open / confirmed; issue key: culturemech-008766-preparation-loss.

The source pH and staged preparation are absent from both layers: basal pH11 and vitamin sterilization order, literal headspace ratio, and trace NTA-first/pH6.5→7.0 sequence. Preserve these as exact scoped preparation evidence, not VARIABLE liquid doses or universal organism growth conditions. No sterilization temperature/duration or gas percentage basis is supplied. Current TOGO comment preservation is credited; its root-ph reader does not itself read meta.ph in this captured payload.

### f5: The actually linked standalone records retain separate quantity defects

major / open / confirmed; issue key: culturemech-008766-linked-stock-defects.

Assess linked records on their own provider identity:6241 retains a biotin unit error and impossible water percent;6187 also retains impossible water percent. Preserve the eight already attached exact g_l claims and both supported preparation notes. The quantity inventory gives the bounded6241 calculation from explicit make-up and leaves6187 input-water basis separate. Provider6187 ZnCl2 x6H2O is not represented by anhydrous CHEBI49976; retain the unusual source hydrate as an unresolved exact-form issue without inventing a substitute. These are scoped linked-record issues, not a license to use either formulation for NBRC1562.

### f6: Default classification and structural placeholders need scoped review

minor / open / confirmed; issue key: culturemech-008766-classification-evidence.

COMPLEX/UNDEFINED was imported by default although the inspected NBRC formulation enumerates chemically named inputs without complex extracts. Reassess the medium classification after stock identities and unspecified vitamin form are resolved; do not infer exact B12 vitamer or calcium-pantothenate stereochemistry. Retain exact source citations and narrow concentration evidence. The linked standalone records have real compositions despite See source placeholders/incomplete flags; qualify those metadata separately.

## Recommended Actions And Acceptance Checks

### a1

Restore source stages before any normalization: the generated water sum and retained owner water unit are wrong; calcium sums basal and trace-batch inputs; nine vitamin mg inputs are stored as final G_PER_L; thirteen other trace components are flattened; both stock doses are 10 ml additions mislabeled G_PER_L. Basal mass values are supported as batch inputs, but their final-volume denominator is unresolved. Credit the owner duplicate-water repair without treating it as a scientific stage repair.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The two declared provider references are not the NBRC1562 stocks: solution6241 has three vitamins and explicit 100 ml make-up, while NBRC1562 lists nine vitamins with 1 L input water; solution6187 uses EDTA and six mineral/chelator components, while NBRC1562 has NTA and fourteen components. Resolve the receiving links from exact source identity and preserve the NBRC local stocks. Do not rewrite the independent provider stocks to make them resemble NBRC or transfer their doses. Replace Unknown solution names with source-scoped names. Current name-to-single-ID migration lacks formulation verification, but its current body does not prove the exact historical execution.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

In both target and owner, calcium pantothenate is mapped to the pantothenate anion CHEBI29032; cobalt chloride hexahydrate and nickel chloride hexahydrate are mapped to anhydrous CHEBI35696 and CHEBI34887. Exact current formulas confirm these mismatches. CHEBI53503 and53542 represent the named hydrates. CHEBI31345 represents a calcium salt but its D stereochemistry cannot be inferred from the generic source name, so it is a bounded candidate rather than an automatic replacement. Keep masses unchanged while resolving exact supplied forms.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The source pH and staged preparation are absent from both layers: basal pH11 and vitamin sterilization order, literal headspace ratio, and trace NTA-first/pH6.5→7.0 sequence. Preserve these as exact scoped preparation evidence, not VARIABLE liquid doses or universal organism growth conditions. No sterilization temperature/duration or gas percentage basis is supplied. Current TOGO comment preservation is credited; its root-ph reader does not itself read meta.ph in this captured payload.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Assess linked records on their own provider identity:6241 retains a biotin unit error and impossible water percent;6187 also retains impossible water percent. Preserve the eight already attached exact g_l claims and both supported preparation notes. The quantity inventory gives the bounded6241 calculation from explicit make-up and leaves6187 input-water basis separate. Provider6187 ZnCl2 x6H2O is not represented by anhydrous CHEBI49976; retain the unusual source hydrate as an unresolved exact-form issue without inventing a substitute. These are scoped linked-record issues, not a license to use either formulation for NBRC1562.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

COMPLEX/UNDEFINED was imported by default although the inspected NBRC formulation enumerates chemically named inputs without complex extracts. Reassess the medium classification after stock identities and unspecified vitamin form are resolved; do not infer exact B12 vitamer or calcium-pantothenate stereochemistry. Retain exact source citations and narrow concentration evidence. The linked standalone records have real compositions despite See source placeholders/incomplete flags; qualify those metadata separately.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| nbrc1562 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562; REVIEW_WORK/batch069/source07-08-10/nbrc1562.json; exact original raw/text/hash/time metadata | context_only | Exact official NBRC1562 primary for ordinary07, not a source for other media. |
| togo2172full | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172; REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.json; exact original raw/text/hash/time metadata | context_only | Exact TOGO2172 structured endpoint discovered in current repository source adapter. Earlier /rest/medium route was an uninformative app shell and is preserved. |
| togo2172 | https://togomedium.org/rest/medium/M2172; REVIEW_WORK/batch069/source07-08-10/togo2172.json; exact original raw/text/hash/time metadata | context_only | Exact ordinary07 TOGO source; source stages remain distinct. |
| stock6241 | https://mediadive.dsmz.de/rest/solution/6241; REVIEW_WORK/batch069/source07-08-10/stock6241.json; exact original raw/text/hash/time metadata | context_only | Exact linked standalone solution identity/claims only. Do not assume synonymy with the source07 embedded stocks. |
| stock6187 | https://mediadive.dsmz.de/rest/solution/6187; REVIEW_WORK/batch069/source07-08-10/stock6187.json; exact original raw/text/hash/time metadata | context_only | Exact linked standalone solution identity/claims only. Do not assume synonymy with the source07 embedded stocks. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch069/source07-08-10/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch069/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| target | data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cedears_Standard_Medium_3.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cedears_standard_medium_3.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| dep-vitamin | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Full composition, placeholder, preparation, evidence and history | context_only | Complete actually linked standalone stock, assessed against its own source; it is not equivalent to the NBRC1562 local stock. |
| dep-trace | data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml; Full composition, placeholder, preparation, evidence and history | context_only | Complete actually linked standalone stock, assessed against its own source; it is not equivalent to the NBRC1562 local stock. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _extract_primary_components, _solution_from_item, _local_batch_volume_ml, _parse_unit, _extract_ph, _extract_preparation_steps | context_only | Current code preserves primary/stock sections and local references, maps l to L and mg to MG_PER_L, and retains comments. _local_batch_volume_ml requires corroborating volumes before inline normalization. Current _extract_ph reads root ph while the captured payload stores meta.ph, so that direct parser path does not extract this metadata field. This is present-code behavior, not historical execution proof. |
| writer-migrate | scripts/migrate_solutions_from_ingredients.py; __init__, _resolve_solution, _migrate_media_file | context_only | Current migration resolves a cleaned generic stock name through a single-ID dictionary and copies its quantity without verifying formulation equivalence. This explains a current risk, not proof of the old executed dictionary or state. |
| writer-cleanup | scripts/cleanup_media_quality.py; _merge_ingredient_group | context_only | Current _merge_ingredient_group no longer sums agreeing duplicates and flags disagreements. Neither numeric agreement nor generic name equality establishes solution-stage equivalence. |
| writer-repair | scripts/repair_merged_duplicates.py; repair_ingredient, repair_record, main | context_only | Current repair_ingredient repairs eligible identical-part notes and preserves the existing unit; repair_record visits ingredients and nested solution compositions. Owner water duplicate repair is credited but did not restore three source stages or water units. |
| writer-default | src/culturemech/validation/schema_defaulter.py; apply_defaults, _fix_ingredient, _fix_solution | context_only | Current _fix_ingredient inserts VARIABLE placeholders and _fix_solution inserts Unknown solution. These are structural defaults, not source quantities or resolved identities. |
| historical-reading | REVIEW_WORK/batch069/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch069/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch069/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch069/record07/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch069/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch069/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch069/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527; REVIEW_WORK/batch069/source07-08-10/chebi131527.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch069/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954; REVIEW_WORK/batch069/source07-08-10/chebi32954.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch069/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi191088 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:191088; REVIEW_WORK/batch069/source07-08-10/chebi191088.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; REVIEW_WORK/batch069/source07-08-10/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997; REVIEW_WORK/batch069/source07-08-10/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276; REVIEW_WORK/batch069/source07-08-10/chebi18276.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch069/source07-08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch069/source07-08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch069/source07-08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi29032 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29032; REVIEW_WORK/batch069/source07-08-10/chebi29032.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch069/source07-08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch069/source07-08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch069/source07-08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch069/source07-08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch069/source07-08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch069/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch069/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch069/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch069/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696; REVIEW_WORK/batch069/source07-08-10/chebi35696.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch069/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch069/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch069/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254; REVIEW_WORK/batch069/source07-08-10/chebi86254.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465; REVIEW_WORK/batch069/source07-08-10/chebi86465.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557; REVIEW_WORK/batch069/source07-08-10/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi63940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63940; REVIEW_WORK/batch069/source07-08-10/chebi63940.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi77775 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:77775; REVIEW_WORK/batch069/source07-08-10/chebi77775.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439; REVIEW_WORK/batch069/source07-08-10/chebi17439.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi64734 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734; REVIEW_WORK/batch069/source07-08-10/chebi64734.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch069/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Ordinary07/08 exact current ontology object; formula/form and source match assessed separately. No restricted10 operational chemistry. |
| quantities | REVIEW_WORK/batch069/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch069/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch069/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch069/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch069/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch069/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch069/record07/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch069/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch069/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch069/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch069/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- NBRC1562 is the primary recipe; TOGO2172 is a corresponding structured transcription. The earlier guessed /rest/medium route returned an application shell and is not recipe evidence.
- No final-medium volume is asserted from input water. Only standalone6241 has explicit final make-up supporting its scoped microgram conversion. All stock transfers require exact identity and receiving-volume evidence.
- Current MIM preferred rows marked REJECTED are retained as catalogue facts, not approval to change source chemistry. Generic B12 and calcium-pantothenate stereochemistry remain unresolved.
- The source contains no named organism; no strain-growth relationship is assigned. Standalone6241/6187 are examined as actual current links, not replacement recipes.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T141003Z-culturemech-008766-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Cedears Standard Medium 3'
started_at: '2026-10-28T13:46:02.628531Z'
finished_at: '2026-10-28T14:10:03.772161Z'
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
summary: Five major issues concern flattened source stages, wrong stock references,
  supplied forms, omitted preparation and separate linked-stock quantity defects;
  one minor classification/evidence issue remains. All target/owner and linked-stock
  quantities are inventoried, eight attached stock claims are credited, and no unspecified
  final-volume or hydrate assumption is made.
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
  - path: data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml
    sha256: 2644b5bbd5e27fad86cdedb3976fefcf0d49168bcffb5732d20271128a27928c
    role: target
  - path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    sha256: 9a218d72425183c0c8f01c396577e0da2b871aa5e714ec0fae8e0e84026a2e25
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cedears_Standard_Medium_3.md
    sha256: 69269265f79e7aec7d58121b17ceaa796fb715bc94889004f7ad364a31f981ee
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cedears_standard_medium_3.md
    sha256: 76e715be8bfcca4239737abb2c5bc41e089048efce1ab8794cadde9c03fc2687
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
  selection: Authoritative batch069 index 07
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008766
targets:
- target_id: CultureMech:008766
  path: data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml
  label: cedears_standard_medium_3
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
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
  - CultureMech:008766
  command: just validate-schema data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml
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
  - CultureMech:008766
  command: just validate-strict data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml
    --out REVIEW_WORK/batch069/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:008766
  command: just validate-terms data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml
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
  - CultureMech:008766
  command: just validate-references data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: nbrc1562
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562
  accessed_at: '2026-10-28T13:46:49.564551Z'
  locator: REVIEW_WORK/batch069/source07-08-10/nbrc1562.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact official NBRC1562 primary for ordinary07, not a source for other
    media.
  snapshot_sha256: fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac
- evidence_id: togo2172full
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172
  accessed_at: '2026-10-28T13:47:34.982199Z'
  locator: REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Exact TOGO2172 structured endpoint discovered in current repository source
    adapter. Earlier /rest/medium route was an uninformative app shell and is preserved.
  snapshot_sha256: c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793
- evidence_id: togo2172
  kind: database
  reference: https://togomedium.org/rest/medium/M2172
  accessed_at: '2026-10-28T13:46:49.537838Z'
  locator: REVIEW_WORK/batch069/source07-08-10/togo2172.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact ordinary07 TOGO source; source stages remain distinct.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: stock6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  accessed_at: '2026-10-28T13:46:49.381061Z'
  locator: REVIEW_WORK/batch069/source07-08-10/stock6241.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact linked standalone solution identity/claims only. Do not assume synonymy
    with the source07 embedded stocks.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: stock6187
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6187
  accessed_at: '2026-10-28T13:46:49.377334Z'
  locator: REVIEW_WORK/batch069/source07-08-10/stock6187.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact linked standalone solution identity/claims only. Do not assume synonymy
    with the source07 embedded stocks.
  snapshot_sha256: d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T13:47:13.554079Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi31345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T13:47:16.033648Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:58:28.825768Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 2644b5bbd5e27fad86cdedb3976fefcf0d49168bcffb5732d20271128a27928c
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
  locator: Complete file
  accessed_at: '2026-10-28T13:58:28.825926Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 9a218d72425183c0c8f01c396577e0da2b871aa5e714ec0fae8e0e84026a2e25
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T13:58:28.825953Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T13:58:28.826246Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T13:58:28.826268Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T13:58:28.826288Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:58:28.826315Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6187_Trace_element_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:58:28.827020Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 51447d8fea765972d4344a448ea87c9dd84eb196a0e80dbacc00290a627b10cc
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T13:58:28.827046Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Cedears_Standard_Medium_3.md
  locator: Complete report
  accessed_at: '2026-10-28T13:58:28.827067Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 69269265f79e7aec7d58121b17ceaa796fb715bc94889004f7ad364a31f981ee
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/cedears_standard_medium_3.md
  locator: Complete report
  accessed_at: '2026-10-28T13:58:28.827095Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 76e715be8bfcca4239737abb2c5bc41e089048efce1ab8794cadde9c03fc2687
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T13:58:28.827121Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 2ec3be557e14096c1fdf3abb674976cd044d552f48bafa76fc3e52d15dddbd6c
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T13:58:28.827140Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
- evidence_id: dep-vitamin
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Full composition, placeholder, preparation, evidence and history
  accessed_at: '2026-10-28T13:58:28.829577Z'
  support: context_only
  summary: Complete actually linked standalone stock, assessed against its own source;
    it is not equivalent to the NBRC1562 local stock.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: dep-trace
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
  locator: Full composition, placeholder, preparation, evidence and history
  accessed_at: '2026-10-28T13:58:28.833991Z'
  support: context_only
  summary: Complete actually linked standalone stock, assessed against its own source;
    it is not equivalent to the NBRC1562 local stock.
  snapshot_sha256: 955006bc9e48d5032fd4cd252d70fb954591eb54cd393da5bb89b3b763702987
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _extract_primary_components, _solution_from_item,
    _local_batch_volume_ml, _parse_unit, _extract_ph, _extract_preparation_steps
  accessed_at: '2026-10-28T13:58:28.834020Z'
  support: context_only
  summary: Current code preserves primary/stock sections and local references, maps
    l to L and mg to MG_PER_L, and retains comments. _local_batch_volume_ml requires
    corroborating volumes before inline normalization. Current _extract_ph reads root
    ph while the captured payload stores meta.ph, so that direct parser path does
    not extract this metadata field. This is present-code behavior, not historical
    execution proof.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-migrate
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: __init__, _resolve_solution, _migrate_media_file
  accessed_at: '2026-10-28T13:58:28.834052Z'
  support: context_only
  summary: Current migration resolves a cleaned generic stock name through a single-ID
    dictionary and copies its quantity without verifying formulation equivalence.
    This explains a current risk, not proof of the old executed dictionary or state.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: _merge_ingredient_group
  accessed_at: '2026-10-28T13:58:28.834074Z'
  support: context_only
  summary: Current _merge_ingredient_group no longer sums agreeing duplicates and
    flags disagreements. Neither numeric agreement nor generic name equality establishes
    solution-stage equivalence.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_merged_duplicates.py
  locator: repair_ingredient, repair_record, main
  accessed_at: '2026-10-28T13:58:28.834095Z'
  support: context_only
  summary: Current repair_ingredient repairs eligible identical-part notes and preserves
    the existing unit; repair_record visits ingredients and nested solution compositions.
    Owner water duplicate repair is credited but did not restore three source stages
    or water units.
  snapshot_sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
- evidence_id: writer-default
  kind: record_content
  reference: src/culturemech/validation/schema_defaulter.py
  locator: apply_defaults, _fix_ingredient, _fix_solution
  accessed_at: '2026-10-28T13:58:28.834113Z'
  support: context_only
  summary: Current _fix_ingredient inserts VARIABLE placeholders and _fix_solution
    inserts Unknown solution. These are structural defaults, not source quantities
    or resolved identities.
  snapshot_sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/historical-reading.json
  accessed_at: '2026-10-28T13:58:28.836363Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 5ff5d10418796ba619a3ba4156549e6a0a13280f8a7b62e2d00a62e63200476d
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T13:58:28.836402Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 8120cbb5f46771483dbc9312f324d7e130422c2ef3def5295d5332d4c663f893
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/complete-document-reader.json
  accessed_at: '2026-10-28T13:58:28.836548Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 53e8d195e2fce6d3bf635221d539f4c4319e2bcc086a3c85f7b78a08d3a38c76
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T13:58:28.836593Z'
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
  accessed_at: '2026-10-28T13:58:28.836624Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch069/record07/historical-current-object-joins.json
  accessed_at: '2026-10-28T13:58:28.836646Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: c2c77c81e2fd9a2c035f1073475195195b3993070ebd78eb79476fbfec91501b
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T13:46:59.030541Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T13:47:16.931907Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T13:47:13.487973Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131527
  accessed_at: '2026-10-28T13:46:54.218512Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi131527.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 0a5297c84ea9dd82508960482211f6b3c993fd8e2b83fe755dd2b23316cc4068
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T13:47:17.543043Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32954
  accessed_at: '2026-10-28T13:47:14.161322Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi32954.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 6718762e0aceec57316f70ff5a6264c973f1f2b235e6d5bbe077a9c349394fb8
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T13:47:14.086258Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi191088
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:191088
  accessed_at: '2026-10-28T13:47:26.716881Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi191088.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: e68705e573070d9a40240cd7822d9b40c6d525eb11f73eb9069db0996b1da3e8
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  accessed_at: '2026-10-28T13:47:13.887499Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi32145.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997
  accessed_at: '2026-10-28T13:47:12.058088Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: c4f240d59927c0f5c6c8d29c14830d0f278cfeabc4ed924be5c2b6bbe1039c05
- evidence_id: chebi18276
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276
  accessed_at: '2026-10-28T13:47:20.763023Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi18276.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: e9495ec2aad65253b7f792e780c1610f9f12f2c0bb20e06c2526156d37b09ed7
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T13:46:52.522310Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T13:47:12.876896Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T13:47:15.369580Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi29032
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29032
  accessed_at: '2026-10-28T13:47:12.657537Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi29032.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: a402e7df7ea27e470b448a3c8c72e60f8deb5000961702e91e8a1f87211861c4
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T13:47:13.301243Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T13:47:12.944254Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T13:47:04.357267Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T13:47:02.181654Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T13:47:02.583235Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T13:47:12.250439Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T13:47:16.607305Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T13:47:14.499495Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T13:47:17.927212Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:35696
  accessed_at: '2026-10-28T13:47:14.796845Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi35696.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 22f49067d1405baa8e2bbd7c4405035d8663c69aa045b7bbacf363bb30729244
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T13:47:14.718043Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T13:47:17.288332Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T13:47:15.401600Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254
  accessed_at: '2026-10-28T13:47:17.204671Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi86254.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: b3a79ee6d9359b7b827f6f87134bc166d84d3948ec20c54965c6e706aecde3a4
- evidence_id: chebi86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465
  accessed_at: '2026-10-28T13:47:18.012978Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi86465.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 76cce7fa8230c57138e3569858ecf6a79119be85281bd5d2864ada3223785dc1
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557
  accessed_at: '2026-10-28T13:47:15.104234Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi44557.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 25e8fb689e4dfc294e2823ca36290cdce6d21ad174238e0e958ebe09d4c1262b
- evidence_id: chebi63940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63940
  accessed_at: '2026-10-28T13:47:16.002964Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi63940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: cd639452d53fc8afcbd2da590ff0f93a573b2abfb4f486020f4e10030b42cf7a
- evidence_id: chebi77775
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:77775
  accessed_at: '2026-10-28T13:47:16.653638Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi77775.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 5e587ae9b9bdc01f8f5c6399f6e0050bf609d8c2b29a844aa28b26d07e6e42ae
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439
  accessed_at: '2026-10-28T13:47:03.147159Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi17439.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 71dca75ee64801424c519bde7667291decd3b97f0c4e46c3d9b9405fa04a71d4
- evidence_id: chebi64734
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:64734
  accessed_at: '2026-10-28T13:47:16.335443Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi64734.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: 4afcce140f81023fe7e21d1081a51e76eb83b0d89e158079ef5be695df2388ec
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T13:47:15.729311Z'
  locator: REVIEW_WORK/batch069/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Ordinary07/08 exact current ontology object; formula/form and source match
    assessed separately. No restricted10 operational chemistry.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:58:28.995447Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 5e717af6d030f3faf4f2f864558417c2b448f6fde4f0144064c4c720166375e2
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:58:28.995531Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 448480ccf3bee3eca59a4e867b25f702c9d74f2ac0ca86e131fcd300d339e520
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:58:28.995668Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: d2eaec1df64cfb6db5e5be3af1289f97848b0f0579c00ee7f2a03a43d7bd609a
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:58:28.995747Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 2db4ac8dc5f0f54eb973c20d47e240bb0d782a125d8dcc6d4df437a9ea9855b1
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:58:28.995816Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 78b94568ae99f5139fd74d4a06867785aa13dd14d1efaccc7d95ecadb2129f1e
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:58:28.995841Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: c16c9ab878c0c829875f950b1ef6f0809013265919b2141b8109fe624e2b1225
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch069/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T13:58:28.995860Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: fb353dcb0c765ea8d3e971e53e63e2bf6ffcf9d30e0319893db5c256f15329aa
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch069/record07/schema-result.json
  accessed_at: '2026-10-28T13:46:03.941354Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 24c3eb6e71af9e185597206f141e658fc27b4de0638b51bdd1142330a18b63a8
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch069/record07/strict-result.json
  accessed_at: '2026-10-28T13:46:04.933828Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 92321f649cd6457b3c0ba77c9adefc54f50005e33c0dc54145ed9793e0464110
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch069/record07/terms-result.json
  accessed_at: '2026-10-28T13:46:06.465371Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 13f80c6deb5042eb53e4e169564a83ff461ed804c1b2084795b2fa4f003e872c
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch069/record07/references-result.json
  accessed_at: '2026-10-28T13:46:07.419839Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 3551569da3fd3a27c32e03377f231b0931a6f511417f1dcac8fde3beafd5ed86
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and stock reference identity
  outcome: concern
  summary: CM008766 and TOGO2172/NBRC1562 identify the selected medium; the maintained
    owner is exact. The two generic provider stock links have demonstrably different
    formulations. No organism or strain is named in the inspected primary recipe,
    and no growth claim is inferred.
  target_ids:
  - CultureMech:008766
  evidence_ids:
  - target
  - owner
  - togo2172full
  - nbrc1562
  - stock6241
  - stock6187
- assessment_id: schema
  area: schema
  topic: Native diagnostics and representation
  outcome: supported
  summary: All four original native diagnostics passed once, strict reported zero
    errors and references checked zero entries. Shape validity does not validate stock
    equivalence, amounts or chemistry. Current conservative merger rejects incompatible
    formulations and singleton-copy behavior does not certify the owner.
  target_ids:
  - CultureMech:008766
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
  - writer-merger
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 87 current concentration fields are covered by 56 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:008766
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b069-quantity-inventory-v1","target":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","quantity_field_count":87,"decisions":[{"quantity_id":"q1","label":"Distilled
    water","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[0].concentration","stored":{"value":"3.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source lists distinct 1 L water inputs for basal, vitamin and trace batches. The
    generated 3 G_PER_L aggregates those inputs; owner 1 G_PER_L credits duplicate
    repair but still has the wrong unit and loses source stage. Preserve the separate
    L inputs, not a mass concentration or assumed final volume.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 77-79","quote":"Distilled water\n1\nL","quote_basis":"derivative text"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"CaCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.247","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored 0.247 G_PER_L adds 0.147 g basal and 0.1 g trace-stock input across different
    solution bases. Those are distinct batch masses, not a final-medium total. Restore
    stage-specific assertions without calculating a receiving concentration from input
    water.","source_stage":"NBRC1562 basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 50-56","quote":"CaCl\n2\n·2H\n2\nO\n0.147\ng","quote_basis":"derivative
    text"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 150-156","quote":"CaCl\n2\n·2H\n2\nO\n0.1\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numerical value matches the listed basal batch mass in grams, but the source specifies
    input water rather than measured final volume. Preserve the supported source mass
    separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 32-36","quote":"NH\n4\nCl\n0.02\ng","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"K2HPO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numerical value matches the listed basal batch mass in grams, but the source specifies
    input water rather than measured final volume. Preserve the supported source mass
    separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"K2HPO4\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001009\",\n          \"gmo_id\": \"GMO_001009\",\n          \"label\":
    \"Potassium phosphate dibasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 44-49","quote":"K\n2\nHPO\n4\n0.02\ng","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"MgCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numerical value matches the listed basal batch mass in grams, but the source specifies
    input water rather than measured final volume. Preserve the supported source mass
    separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"MgCl2·6H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 37-43","quote":"MgCl\n2\n·6H\n2\nO\n0.01\ng","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Sodium
    acetate","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.164","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[5].concentration","stored":{"value":"0.164","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numerical value matches the listed basal batch mass in grams, but the source specifies
    input water rather than measured final volume. Preserve the supported source mass
    separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"Sodium acetate\",\n          \"volume\": 0.164,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\":
    \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 68-70","quote":"Sodium acetate\n0.164\ng","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0071","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.0071","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numerical value matches the listed basal batch mass in grams, but the source specifies
    input water rather than measured final volume. Preserve the supported source mass
    separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"Na2SO4\",\n          \"volume\": 0.0071,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\":
    \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 26-31","quote":"Na\n2\nSO\n4\n0.0071\ng","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"CAPS","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3.32","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[7].concentration","stored":{"value":"3.32","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numerical value matches the listed basal batch mass in grams, but the source specifies
    input water rather than measured final volume. Preserve the supported source mass
    separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"CAPS\",\n          \"volume\": 3.32,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002374\",\n          \"gmo_id\": \"GMO_002374\",\n          \"label\":
    \"CAPS\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 65-67","quote":"CAPS\n3.32\ng","quote_basis":"derivative text"}]},{"quantity_id":"q9","label":"Ca3(PO4)2","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.372","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[8].concentration","stored":{"value":"0.372","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    numerical value matches the listed basal batch mass in grams, but the source specifies
    input water rather than measured final volume. Preserve the supported source mass
    separately; the existing final-medium G_PER_L denominator is not established.","source_stage":"NBRC1562
    basal batch","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"Ca3(PO4)2\",\n          \"volume\": 0.372,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002207\",\n          \"gmo_id\": \"GMO_002207\",\n          \"label\":
    \"Tricalcium phosphate\",\n          \"properties\": [],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 57-64","quote":"Ca\n3\n(PO\n4\n)\n2\n0.372\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q10","label":"NaOH","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE
    is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH
    adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their
    context and the literal gas ratio without inventing ingredient concentrations
    or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final
    ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[11]","quote":"{\n          \"component_name\":
    \"NaOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\":
    \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH
    to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin
    solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust
    pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile
    vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6)
    in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"N2","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE
    is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH
    adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their
    context and the literal gas ratio without inventing ingredient concentrations
    or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final
    ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[12]","quote":"{\n          \"component_name\":
    \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH
    to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin
    solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust
    pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile
    vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6)
    in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"Oxygen
    gas","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[11].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE
    is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH
    adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their
    context and the literal gas ratio without inventing ingredient concentrations
    or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final
    ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[13]","quote":"{\n          \"component_name\":
    \"Oxygen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002262\",\n          \"gmo_id\":
    \"GMO_002262\",\n          \"label\": \"Oxygen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH
    to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin
    solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust
    pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile
    vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6)
    in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"Hydrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[12].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"VARIABLE
    is an unquantified placeholder, not a liquid or mass dose. Source NaOH is a pH
    adjustment reagent, while N2/O2/H2 describe atmosphere/headspace. Retain their
    context and the literal gas ratio without inventing ingredient concentrations
    or a percent basis.","source_stage":"Adjustment reagent or atmosphere, not final
    ingredient dose","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[14]","quote":"{\n          \"component_name\":
    \"Hydrogen gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002263\",\n          \"gmo_id\":
    \"GMO_002263\",\n          \"label\": \"Hydrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"ガス\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH
    to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin
    solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust
    pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile
    vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6)
    in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 93-95","quote":"Biotin\n2\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[14].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 114-117","quote":"p\n-Aminobenzoic acid\n1\nmg","quote_basis":"derivative
    text"}]},{"quantity_id":"q16","label":"Thiamine-HCl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[15].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[15].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[3]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 102-104","quote":"Thiamine-HCl\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"Ca-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[16].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[16].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[4]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 111-113","quote":"Ca-pantothenate\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"Pyridoxine-HCl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[17].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[17].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 99-101","quote":"Pyridoxine-HCl\n10\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"Folic
    acid","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[18].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 96-98","quote":"Folic acid\n2\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 118-121","quote":"Vitamin B\n12\n0.01\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q21","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[20].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[20].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 105-107","quote":"Riboflavin\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q22","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[21].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[21].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source value is a milligram input in the separately prepared NBRC vitamin batch.
    The existing number in G_PER_L is both the wrong unit and the wrong receiving
    stage. Preserve the literal mg amount and 1 L water input; no final stock volume
    or diluted final-medium rate is inferred.","source_stage":"NBRC local vitamin
    stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 108-110","quote":"Nicotinic acid\n5\nmg","quote_basis":"derivative text"}]},{"quantity_id":"q23","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[22].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[22].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 183-185","quote":"NaCl\n1\ng","quote_basis":"derivative text"}]},{"quantity_id":"q24","label":"Na2MoO4·2H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 174-182","quote":"Na\n2\nMoO\n4\n·2H\n2\nO\n0.024\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q25","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.01","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.01","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 168-173","quote":"H\n3\nBO\n3\n0.01\ng","quote_basis":"derivative text"}]},{"quantity_id":"q26","label":"MnCl2·4H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 136-142","quote":"MnCl\n2\n·4H\n2\nO\n0.1\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q27","label":"CoCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 143-149","quote":"CoCl\n2\n·6H\n2\nO\n0.024\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q28","label":"NiCl2·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.12","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.12","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 186-192","quote":"NiCl\n2\n·6H\n2\nO\n0.12\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q29","label":"CuCl2·2H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.025","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.025","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 161-167","quote":"CuCl\n2\n·2H\n2\nO\n0.025\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q30","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 157-160","quote":"ZnCl\n2\n0.1\ng","quote_basis":"derivative text"}]},{"quantity_id":"q31","label":"FeCl3·6H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[30].concentration","stored":{"value":"1.35","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[30].concentration","stored":{"value":"1.35","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 129-135","quote":"FeCl\n3\n·6H\n2\nO\n1.35\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q32","label":"KAl(SO4)2·12H2O","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[31].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[11]","quote":"{\n          \"component_name\":
    \"KAl(SO4)2·12H2O\",\n          \"volume\": 0.02,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001051\",\n          \"gmo_id\": \"GMO_001051\",\n          \"label\":
    \"Aluminum potassium sulfate dodecahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 205-213","quote":"KAl(SO\n4\n)\n2\n·12H\n2\nO\n0.02\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q33","label":"Nitrilotriacetic acid (NTA)","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[32].concentration","stored":{"value":"12.8","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[32].concentration","stored":{"value":"12.8","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[12]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 126-128","quote":"Nitrilotriacetic acid (NTA)\n12.8\ng","quote_basis":"derivative
    text"}]},{"quantity_id":"q34","label":"Na2WO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[33].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[13]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 199-204","quote":"Na\n2\nWO\n4\n0.004\ng","quote_basis":"derivative text"}]},{"quantity_id":"q35","label":"Na2SeO4","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"ingredients[34].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    value is a gram input in the separate NBRC trace batch, not a final-medium ingredient
    rate. Preserve the exact hydrate and stock stage; do not transfer the unrelated
    EDTA-based provider6187 formulation or infer dilution from water alone.","source_stage":"NBRC
    local trace stock","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[14]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 193-198","quote":"Na\n2\nSeO\n4\n0.004\ng","quote_basis":"derivative text"}]},{"quantity_id":"q36","label":"Vitamin
    solution*","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"solutions[0].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a 10 ml addition of its own locally defined stock to this basal
    batch, not 10 g/L. The receiving final volume is not stated. The current mediadive
    solution reference resolves to a different composition and must not supply the
    receiving recipe.","source_stage":"Receiving stock addition","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Vitamin solution*\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2172\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 71-73","quote":"Vitamin solution*\n10\nml","quote_basis":"derivative text"}]},{"quantity_id":"q37","label":"Trace
    element solution**","local_fields":[{"path":"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml","field_path":"solutions[1].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies a 10 ml addition of its own locally defined stock to this basal
    batch, not 10 g/L. The receiving final volume is not stated. The current mediadive
    solution reference resolves to a different composition and must not supply the
    receiving recipe.","source_stage":"Receiving stock addition","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Trace element solution**\",\n          \"volume\": 10,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M2172\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 74-76","quote":"Trace element solution**\n10\nml","quote_basis":"derivative
    text"}]},{"quantity_id":"q38","label":"stock6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\":
    847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"stock6241
    Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"stock6241
    Biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source specifies 200 μg and explicitly makes up to 100 ml. 200 μg = 0.0002 g;
    divided by 0.1 L gives 0.002 g/L, not the retained 2000 G_PER_L. This calculation
    applies only to standalone6241, not the NBRC vitamin stock.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q41","label":"stock6241 Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The
    source is an input/makeup water quantity, not 1000 percent v/v. Preserve the original
    volume representation and preparation context; no water density conversion is
    used. The explicit final make-up is 100 ml, so a fixed water dose and a final
    stock volume must remain distinguished.","source_stage":"Standalone provider stock,
    identity comparison only","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q42","label":"stock6241 structural placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    VARIABLE See source for composition entry is a structural placeholder, not an
    extra reagent or quantified addition. The actual composition is present; do not
    count or transfer this placeholder as a recipe ingredient.","source_stage":"Standalone
    placeholder","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q43","label":"stock6241 retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make
    up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"Existing
    preparation wording and declared original provider volume are supported by the
    current source. This preparation field has no separate attached literal evidence
    claim; retain it separately from incorrect water concentration. For6187 water
    is an input; for6241 make-up explicitly fixes final100ml.","source_stage":"Standalone
    stock preparation","sources":[{"evidence_id":"stock6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T13:46:49.381061Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q44","label":"stock6187 Na2-EDTA","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.75","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"Na2-EDTA\",\n                \"compound_id\":
    34,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.75,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.75,\n                \"mmol_l\": 2.23078,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"stock6187
    Distilled water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"1000","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The
    source is an input/makeup water quantity, not 1000 percent v/v. Preserve the original
    volume representation and preparation context; no water density conversion is
    used.","source_stage":"Standalone provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q46","label":"stock6187 FeCl3 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"0.097","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"FeCl3 x 6 H2O\",\n                \"compound_id\":
    82,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 97,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.097,\n                \"mmol_l\": 0.358866,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"stock6187
    MnCl2 x 4 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"0.041","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 41,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.041,\n                \"mmol_l\": 0.20717,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"stock6187
    ZnCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[4].concentration","stored":{"value":"0.005","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[4]","quote":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"ZnCl2 x 6 H2O\",\n                \"compound_id\":
    2351,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 5,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.005,\n                \"mmol_l\": 0.0204583,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"stock6187
    CoCl2 x 6 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[5].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[5]","quote":"{\n                \"recipe_order\":
    7,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0154037,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"stock6187
    Na2MoO4 x 2 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"composition[6].concentration","stored":{"value":"0.004","unit":"G_PER_L"}}],"decision":"verified","rationale":"The
    existing attached literal composition claim matches this exact current raw response
    and its recorded historical digest. Its stored value/unit equals explicit provider
    g_l on the standalone stock basis. This authenticates current content, not an
    independently recovered original access event or receiving-medium equivalence.","source_stage":"Standalone
    provider stock, identity comparison only","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.recipe[6]","quote":"{\n                \"recipe_order\":
    8,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0165323,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"stock6187
    structural placeholder","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    VARIABLE See source for composition entry is a structural placeholder, not an
    extra reagent or quantified addition. The actual composition is present; do not
    count or transfer this placeholder as a recipe ingredient.","source_stage":"Standalone
    placeholder","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q52","label":"stock6187 retained preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml","field_path":"preparation_notes","stored":"Add
    to 1000 ml of distilled water 0.75 g Na2EDTA and the minerals in exactly the \r\nfollowing
    sequence:"}],"decision":"evidence_only","rationale":"Existing preparation wording
    and declared original provider volume are supported by the current source. This
    preparation field has no separate attached literal evidence claim; retain it separately
    from incorrect water concentration. For6187 water is an input; for6241 make-up
    explicitly fixes final100ml.","source_stage":"Standalone stock preparation","sources":[{"evidence_id":"stock6187","reference":"https://mediadive.dsmz.de/rest/solution/6187","raw_path":"REVIEW_WORK/batch069/source07-08-10/stock6187.raw","raw_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","text_sha256":"d31ecb8b693ab4516fccb451babae9631a8a073b47acec0285b57f55ba309916","accessed_at":"2026-10-28T13:46:49.377334Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    3,\n                \"step\": \"Add to 1000 ml of distilled water 0.75 g Na2EDTA
    and the minerals in exactly the \\r\\nfollowing sequence:\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q53","label":"NBRC vitamin water","local_fields":[],"decision":"evidence_only","rationale":"Separate
    1 L solvent input, not a stated final stock volume.","source_stage":"Source-only
    stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 122-124","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q54","label":"NBRC
    trace water","local_fields":[],"decision":"evidence_only","rationale":"Separate
    1 L solvent input, not a stated final stock volume.","source_stage":"Source-only
    stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 214-216","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q55","label":"Basal
    pH, sterilization order and headspace","local_fields":[],"decision":"evidence_only","rationale":"Retain
    pH11, vitamin exclusion from autoclaving, filter-sterile addition and literal
    N2/H2/O2 59/35/6 headspace ratio. The ratio basis is not specified; do not manufacture
    gas concentrations, a temperature or an autoclave duration.","source_stage":"Source-only
    stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[2]","quote":"{\n      \"paragraph_index\":
    4,\n      \"comment\": \"Mix ingredients except for vitamin solution, adjust pH
    to 11 with NaOH, and autoclave under a N2 atmosphere. Add the filter-sterile vitamin
    solution, and exchange N2 to a gas mixture of N2/H2/O2 (59/35/6) in the headspace.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 80-91","quote":"pH 11\nMix ingredients except for vitamin solution, adjust
    pH to 11 with NaOH, and autoclave under a N\n2\natmosphere. Add the filter-sterile
    vitamin solution, and exchange N\n2\nto a gas mixture of N\n2\n/H\n2\n/O\n2\n(59/35/6)
    in the headspace.","quote_basis":"derivative text"}]},{"quantity_id":"q56","label":"Trace
    pH and dissolution order","local_fields":[],"decision":"evidence_only","rationale":"Retain
    NTA-first dissolution, initial pH6.5 and final pH7.0 in the trace-stock stage.
    The NaOH dose is unspecified.","source_stage":"Source-only stage control","sources":[{"evidence_id":"togo2172full","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2172","raw_path":"REVIEW_WORK/batch069/source07-08-10-supplement/togo2172full.raw","raw_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","text_sha256":"c546754afc277253f715916997c5d5853611464f0bebb97ad04a9c6a975ca793","accessed_at":"2026-10-28T13:47:34.982199Z","locator":"comments[6]","quote":"{\n      \"paragraph_index\":
    10,\n      \"comment\": \"First dissolve nitrilotriacetic acid and adjust pH to
    6.5 with NaOH, and then add minerals. Final pH 7.0.\"\n    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc1562","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1562","raw_path":"REVIEW_WORK/batch069/source07-08-10/nbrc1562.raw","raw_sha256":"fe98117c8c8bcb32336eefcfc3b08494123d11ca56d45d3370bf388bc3b387ac","text_sha256":"c10c81c9f9ac9172a983a73879520a4d6eb9f9b7b1cde801bb8233c23f0f5240","accessed_at":"2026-10-28T13:46:49.564551Z","locator":"nbrc1562.txt
    lines 217-217","quote":"First dissolve nitrilotriacetic acid and adjust pH to
    6.5 with NaOH, and then add minerals. Final pH 7.0.","quote_basis":"derivative
    text"}]}],"document_scopes":{"data/merge_yaml/merged/Cedears_Standard_Medium_3.yaml":null,"data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All current asserted ontology slots and exact MIM memberships are enumerated
    separately from scientific forms. Three selected supplied-form contradictions
    are confirmed (pantothenate anion, cobalt and nickel hydrate loss). Named other
    hydrates, NTA, CAPS, salts and vitamins were checked against exact current formula/charge/structure.
    B12 remains a generic vitamer class; generic calcium pantothenate does not establish
    D stereochemistry. The provider6187 zinc hydrate notation is unresolved against
    its anhydrous term. Missing primary/secondary links, rejected current preferred-name
    rows and current CHEBI29032 MIM absence are distinct from ontology validity; no
    all-labels-imply-form claim is made.
  target_ids:
  - CultureMech:008766
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: supported
  summary: Complete target, owner and both linked-stock histories plus six complete
    historical reports and two exact parent records were read. The owner duplicate-water
    correction is retained; generated water remains stale, and unequal-stage calcium
    was not repaired. Eight standalone composition claims match current literal raw
    content and exact October7 digests; eleven historical recipe objects join current
    sources. Those equal bytes do not recover original access timestamps. Current
    cleanup no longer sums duplicates, current TOGO preserves primary/stock layers,
    and current merge requires exact scientific assertions. Preserve all earlier events
    and append new curation metadata only.
  target_ids:
  - CultureMech:008766
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-008766-flattened-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Basal and stock amounts are conflated
  description: 'Restore source stages before any normalization: the generated water
    sum and retained owner water unit are wrong; calcium sums basal and trace-batch
    inputs; nine vitamin mg inputs are stored as final G_PER_L; thirteen other trace
    components are flattened; both stock doses are 10 ml additions mislabeled G_PER_L.
    Basal mass values are supported as batch inputs, but their final-volume denominator
    is unresolved. Credit the owner duplicate-water repair without treating it as
    a scientific stage repair.'
  target_ids:
  - CultureMech:008766
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - target
  - owner
  - togo2172full
  - nbrc1562
  - quantities
  - writer-togo
  - writer-cleanup
  - writer-repair
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-008766-stock-link-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Generic stock names resolve to different formulations
  description: 'The two declared provider references are not the NBRC1562 stocks:
    solution6241 has three vitamins and explicit 100 ml make-up, while NBRC1562 lists
    nine vitamins with 1 L input water; solution6187 uses EDTA and six mineral/chelator
    components, while NBRC1562 has NTA and fourteen components. Resolve the receiving
    links from exact source identity and preserve the NBRC local stocks. Do not rewrite
    the independent provider stocks to make them resemble NBRC or transfer their doses.
    Replace Unknown solution names with source-scoped names. Current name-to-single-ID
    migration lacks formulation verification, but its current body does not prove
    the exact historical execution.'
  target_ids:
  - CultureMech:008766
  field_paths:
  - solutions[0]
  - solutions[1]
  evidence_ids:
  - target
  - owner
  - togo2172full
  - nbrc1562
  - stock6241
  - stock6187
  - dep-vitamin
  - dep-trace
  - writer-migrate
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-008766-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Three supplied forms conflict with asserted ontology chemistry
  description: In both target and owner, calcium pantothenate is mapped to the pantothenate
    anion CHEBI29032; cobalt chloride hexahydrate and nickel chloride hexahydrate
    are mapped to anhydrous CHEBI35696 and CHEBI34887. Exact current formulas confirm
    these mismatches. CHEBI53503 and53542 represent the named hydrates. CHEBI31345
    represents a calcium salt but its D stereochemistry cannot be inferred from the
    generic source name, so it is a bounded candidate rather than an automatic replacement.
    Keep masses unchanged while resolving exact supplied forms.
  target_ids:
  - CultureMech:008766
  field_paths:
  - ingredients[16].term
  - ingredients[16].mediaingredientmech_chebi_term
  - ingredients[26].term
  - ingredients[27].term
  - ingredients[27].mediaingredientmech_chebi_term
  evidence_ids:
  - target
  - owner
  - togo2172full
  - nbrc1562
  - chebi29032
  - chebi35696
  - chebi34887
  - chebi53503
  - chebi53542
  - chebi31345
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-008766-preparation-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Stage-specific preparation and atmosphere are omitted
  description: 'The source pH and staged preparation are absent from both layers:
    basal pH11 and vitamin sterilization order, literal headspace ratio, and trace
    NTA-first/pH6.5→7.0 sequence. Preserve these as exact scoped preparation evidence,
    not VARIABLE liquid doses or universal organism growth conditions. No sterilization
    temperature/duration or gas percentage basis is supplied. Current TOGO comment
    preservation is credited; its root-ph reader does not itself read meta.ph in this
    captured payload.'
  target_ids:
  - CultureMech:008766
  field_paths:
  - ph_value
  - preparation_steps
  - ingredients[9]
  - ingredients[10]
  - ingredients[11]
  - ingredients[12]
  evidence_ids:
  - target
  - owner
  - togo2172full
  - nbrc1562
  - writer-togo
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-008766-linked-stock-defects
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: The actually linked standalone records retain separate quantity defects
  description: Assess linked records on their own provider identity:6241 retains a
    biotin unit error and impossible water percent;6187 also retains impossible water
    percent. Preserve the eight already attached exact g_l claims and both supported
    preparation notes. The quantity inventory gives the bounded6241 calculation from
    explicit make-up and leaves6187 input-water basis separate. Provider6187 ZnCl2
    x6H2O is not represented by anhydrous CHEBI49976; retain the unusual source hydrate
    as an unresolved exact-form issue without inventing a substitute. These are scoped
    linked-record issues, not a license to use either formulation for NBRC1562.
  target_ids:
  - CultureMech:008766
  field_paths:
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[2].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[3].concentration
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::composition[1].concentration
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::composition[4].chebi_term
  evidence_ids:
  - dep-vitamin
  - dep-trace
  - stock6241
  - stock6187
  - chebi49976
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
- finding_id: f6
  issue_key: culturemech-008766-classification-evidence
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Default classification and structural placeholders need scoped review
  description: COMPLEX/UNDEFINED was imported by default although the inspected NBRC
    formulation enumerates chemically named inputs without complex extracts. Reassess
    the medium classification after stock identities and unspecified vitamin form
    are resolved; do not infer exact B12 vitamer or calcium-pantothenate stereochemistry.
    Retain exact source citations and narrow concentration evidence. The linked standalone
    records have real compositions despite See source placeholders/incomplete flags;
    qualify those metadata separately.
  target_ids:
  - CultureMech:008766
  field_paths:
  - medium_type
  - composition_type
  - evidence
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::data_quality_flags
  - data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml::data_quality_flags
  evidence_ids:
  - target
  - owner
  - togo2172full
  - nbrc1562
  - writer-togo
  - writer-default
  - dep-vitamin
  - dep-trace
  rule_id: review-yaml-record/consistency
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml
    role: scoped dependency
actions:
- action_id: a1
  description: 'Restore source stages before any normalization: the generated water
    sum and retained owner water unit are wrong; calcium sums basal and trace-batch
    inputs; nine vitamin mg inputs are stored as final G_PER_L; thirteen other trace
    components are flattened; both stock doses are 10 ml additions mislabeled G_PER_L.
    Basal mass values are supported as batch inputs, but their final-volume denominator
    is unresolved. Credit the owner duplicate-water repair without treating it as
    a scientific stage repair.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008766
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
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
  description: 'The two declared provider references are not the NBRC1562 stocks:
    solution6241 has three vitamins and explicit 100 ml make-up, while NBRC1562 lists
    nine vitamins with 1 L input water; solution6187 uses EDTA and six mineral/chelator
    components, while NBRC1562 has NTA and fourteen components. Resolve the receiving
    links from exact source identity and preserve the NBRC local stocks. Do not rewrite
    the independent provider stocks to make them resemble NBRC or transfer their doses.
    Replace Unknown solution names with source-scoped names. Current name-to-single-ID
    migration lacks formulation verification, but its current body does not prove
    the exact historical execution.'
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008766
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
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
  description: In both target and owner, calcium pantothenate is mapped to the pantothenate
    anion CHEBI29032; cobalt chloride hexahydrate and nickel chloride hexahydrate
    are mapped to anhydrous CHEBI35696 and CHEBI34887. Exact current formulas confirm
    these mismatches. CHEBI53503 and53542 represent the named hydrates. CHEBI31345
    represents a calcium salt but its D stereochemistry cannot be inferred from the
    generic source name, so it is a bounded candidate rather than an automatic replacement.
    Keep masses unchanged while resolving exact supplied forms.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008766
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
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
  description: 'The source pH and staged preparation are absent from both layers:
    basal pH11 and vitamin sterilization order, literal headspace ratio, and trace
    NTA-first/pH6.5→7.0 sequence. Preserve these as exact scoped preparation evidence,
    not VARIABLE liquid doses or universal organism growth conditions. No sterilization
    temperature/duration or gas percentage basis is supplied. Current TOGO comment
    preservation is credited; its root-ph reader does not itself read meta.ph in this
    captured payload.'
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008766
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
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
  description: Assess linked records on their own provider identity:6241 retains a
    biotin unit error and impossible water percent;6187 also retains impossible water
    percent. Preserve the eight already attached exact g_l claims and both supported
    preparation notes. The quantity inventory gives the bounded6241 calculation from
    explicit make-up and leaves6187 input-water basis separate. Provider6187 ZnCl2
    x6H2O is not represented by anhydrous CHEBI49976; retain the unusual source hydrate
    as an unresolved exact-form issue without inventing a substitute. These are scoped
    linked-record issues, not a license to use either formulation for NBRC1562.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:008766
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
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
- action_id: a6
  description: COMPLEX/UNDEFINED was imported by default although the inspected NBRC
    formulation enumerates chemically named inputs without complex extracts. Reassess
    the medium classification after stock identities and unspecified vitamin form
    are resolved; do not infer exact B12 vitamer or calcium-pantothenate stereochemistry.
    Retain exact source citations and narrow concentration evidence. The linked standalone
    records have real compositions despite See source placeholders/incomplete flags;
    qualify those metadata separately.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:008766
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/cedears_standard_medium_3.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
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
limitations:
- NBRC1562 is the primary recipe; TOGO2172 is a corresponding structured transcription.
  The earlier guessed /rest/medium route returned an application shell and is not
  recipe evidence.
- No final-medium volume is asserted from input water. Only standalone6241 has explicit
  final make-up supporting its scoped microgram conversion. All stock transfers require
  exact identity and receiving-volume evidence.
- Current MIM preferred rows marked REJECTED are retained as catalogue facts, not
  approval to change source chemistry. Generic B12 and calcium-pantothenate stereochemistry
  remain unresolved.
- The source contains no named organism; no strain-growth relationship is assigned.
  Standalone6241/6187 are examined as actual current links, not replacement recipes.
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
