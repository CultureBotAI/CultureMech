# Scientific review: Clostridium thermocellum medium

- Review: 20261028T104807Z-culturemech-009627-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:18:14.840118Z
- Finished UTC: 2026-10-28T10:48:07.916031Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The main explicit rates are supported, but historical flattening lost stock stages, corrupted units and linked an unrelated vitamin solution. Restore the exact ATCC variant and preparation, reconcile phosphate hydrate and linked-provider residual errors, and retain the remaining source-form uncertainties. No recipe files were changed.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch063 index 10
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009627 | data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml | generated | clostridium_thermocellum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:009627 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:009627 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:009627 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:009627 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### ATCC1191 variant and provider stock identity

identity: concern. Targets: CultureMech:009627.

The exact target/owner is TOGO M3174 citing ATCC1191. Full primary pages support its filter-paper variant of1190; provider6241 is a different vitamin formulation and provider3892 has an explicit hydrate version distinction. Stock labels alone do not establish identity.

### Diagnostics, classification and derived flag

schema: concern. Targets: CultureMech:009627.

Four original canonical checks pass with zero reference checks. Complex/undefined/liquid classification fits the source; high_metal is not authenticated by the primary and must be reevaluated after stock restoration rather than treated as a culture phenotype. Empty placeholder solution names are not source names.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:009627.

91 current concentration fields are covered by 57 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b063-quantity-inventory-v1","target":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","quantity_field_count":91,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly prints g/L and water to 1.0 L; the existing number/unit has direct source support but no attached amount claim. Chemical supplied-form correspondence is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 11-11","quote":"KH2PO4 .........................................1.5 g/L","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 1.5,\n          \"unit\": \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly prints g/L and water to 1.0 L; the existing number/unit has direct source support but no attached amount claim. Chemical supplied-form correspondence is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 13-13","quote":"NH4Cl ..........................................0.5 g/L","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.5,\n          \"unit\": \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"MgCl2 . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly prints g/L and water to 1.0 L; the existing number/unit has direct source support but no attached amount claim. Chemical supplied-form correspondence is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 14-14","quote":"MgCl2 . 6H2O ...................................0.18 g/L","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"MgCl2 . 6H2O\",\n          \"volume\": 0.18,\n          \"unit\": \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Na2HPO4 . 12H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"4.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"4.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly prints g/L and water to 1.0 L; the existing number/unit has direct source support but no attached amount claim. Chemical supplied-form correspondence is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 12-12","quote":"Na2HPO4 . 12H2O.................................4.2 g/L","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\": \"Na2HPO4 . 12H2O\",\n          \"volume\": 4.2,\n          \"unit\": \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001115\",\n          \"gmo_id\": \"GMO_001115\",\n          \"label\": \"Disodium phosphate dodecahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"Yeast Extract (BD 212750)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The primary explicitly prints g/L and water to 1.0 L; the existing number/unit has direct source support but no attached amount claim. Chemical supplied-form correspondence is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 15-15","quote":"Yeast Extract (BD 212750)......................2.0 g/L","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\": \"Yeast Extract (BD 212750)\",\n          \"volume\": 2,\n          \"unit\": \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"Whatman #1 filter paper","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"18.75","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"18.75","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"TOGO explicitly represents the replacement as 18.75 g/L, consistent with 18.75 g replacing glucose in the ATCC one-litre recipe. Whatman grade and one 8 x 70 mm strip per tube are a conditional alternative, not an additional dose or an unconditional requirement for every batch.","source_stage":"ATCC1191 filter-paper variant","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 1-8","quote":"ATCC medium: 1191 Clostridium thermocellum medium (ATCC medium 1190)\nwith 18.75 g filter paper substituted for the glucose\n\n\nATCC Medium 1190 (see below) with 18.75 g filter paper substituted for\nthe glucose\nWhen preparing tubed medium, Whatman #1 filter paper may be used. In\nthis case, use one strip (8 X 70 mm) per tube of broth.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\": \"Whatman #1 filter paper\",\n          \"volume\": 18.75,\n          \"unit\": \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002360\",\n          \"gmo_id\": \"GMO_002360\",\n          \"label\": \"Whatman &amp;reg; qualitative filter paper, grade 1\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Resazurin (0.1%)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source is 1 ml/L of a 0.1% resazurin stock, not 1 g/L resazurin. Percentage basis is unspecified; preserve the stock label without conversion.","source_stage":"main stock transfer","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 19-19","quote":"Resazurin (0.1%)...............................1.0 ml/L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Resazurin (0.1%)\",\n          \"volume\": 1,\n          \"unit\": \"ml/l\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001403\",\n          \"gmo_id\": \"GMO_001403\",\n          \"label\": \"Resazurin solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Distilled deionized water","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Water is a makeup reagent to 1.0 L final main medium, not 1 G_PER_L or a separately measured fixed water addition.","source_stage":"main final-volume makeup","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Distilled deionized water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Wolfe's Modified Mineral Elixir","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source explicitly doses the separately defined mineral stock at 5 ml/L (also 0.5 ml/100 ml), not 5 g/L. Restore the receiving relationship without merging the stock internals into main ingredients.","source_stage":"mineral receiving dose","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 18-18","quote":"Wolfe's Modified Mineral Elixir (see below)....5.0 ml/L","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\": \"Wolfe's Modified Mineral Elixir\",\n          \"volume\": 5,\n          \"unit\": \"ml/l\",\n          \"reference_media_id\": \"M3174\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Nitrogen gas","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Gas amount is unspecified; preserve the printed 95% N2/5% H2 atmosphere separately. Repeated main/stock instructions do not create two dissolved-gas amounts.","source_stage":"gas context","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 27-34","quote":"Bring the medium to a boil while gassing with a mixture of 95% N2, 5%\nH2. Keep the solution boiling for several minutes until time the color\nturns from blue to reddish-pink. Add the reducing solution during\ncontinuous gassing and boiling. The pink color should disappear,\nindicating reduction. Boil briefly for reduction. Using anaerobic\n(Hungate) technique, dispense the medium in tubes flushed with N2/H2 gas\nmixture. Stopper the tubes with butyl rubber, secure and autoclave for\n15 minutes.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 41-44","quote":"Bring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"Hydrogen gas","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Gas amount is unspecified; preserve the printed 95% N2/5% H2 atmosphere separately. Repeated main/stock instructions do not create two dissolved-gas amounts.","source_stage":"gas context","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 27-34","quote":"Bring the medium to a boil while gassing with a mixture of 95% N2, 5%\nH2. Keep the solution boiling for several minutes until time the color\nturns from blue to reddish-pink. Add the reducing solution during\ncontinuous gassing and boiling. The pink color should disappear,\nindicating reduction. Boil briefly for reduction. Using anaerobic\n(Hungate) technique, dispense the medium in tubes flushed with N2/H2 gas\nmixture. Stopper the tubes with butyl rubber, secure and autoclave for\n15 minutes.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 41-44","quote":"Bring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"0.2 N NaOH","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"correct","rationale":"These are reducing-stock batch inputs, not direct main-medium g/L. Preserve 200 ml of 0.2 N NaOH and the two 2.5 g masses; no measured final stock volume or normality-to-molarity conversion is established. ATCC cysteine HCl does not explicitly specify the monohydrate in provider3892.","source_stage":"reducing-stock batch","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0 ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5 g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\": \"0.2 N NaOH\",\n          \"volume\": 200,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.2,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\": \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Na2S . 9H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"These are reducing-stock batch inputs, not direct main-medium g/L. Preserve 200 ml of 0.2 N NaOH and the two 2.5 g masses; no measured final stock volume or normality-to-molarity conversion is established. ATCC cysteine HCl does not explicitly specify the monohydrate in provider3892.","source_stage":"reducing-stock batch","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0 ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5 g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\": \"Na2S . 9H2O\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"L-Cysteine . HCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"These are reducing-stock batch inputs, not direct main-medium g/L. Preserve 200 ml of 0.2 N NaOH and the two 2.5 g masses; no measured final stock volume or normality-to-molarity conversion is established. ATCC cysteine HCl does not explicitly specify the monohydrate in provider3892.","source_stage":"reducing-stock batch","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0 ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5 g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\": \"L-Cysteine . HCl\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001828\",\n          \"gmo_id\": \"GMO_001828\",\n          \"label\": \"L-Cysteine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q15","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"501.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"501.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The 501 G_PER_L value combines 500 ml vitamin water with 1 L mineral water across different stages and units. Restore separate stock solvent/makeup fields: 500 ml is vitamin input, whereas mineral preparation explicitly makes up to 1.0 L. Do not sum them.","source_stage":"two separate stock water stages","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 81-87","quote":"Distilled water....................1.0 L\n\nSuspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 500,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 52-52","quote":"Biotin............................20.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q17","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 53-53","quote":"p-Aminobenzoic acid...............50.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q18","label":"Thiamine . HCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 58-58","quote":"Thiamine . HCl.....................5.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\": \"Thiamine . HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q19","label":"Pantothenic acid calcium salt","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 55-55","quote":"Pantothenic acid calcium salt.....50.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\": \"Pantothenic acid calcium salt\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q20","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 59-59","quote":"Pyridoxine hydrochloride.........100.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\": \"Pyridoxine hydrochloride\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 54-54","quote":"Folic acid........................20.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 20,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 57-57","quote":"Vitamin B12........................1.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 61-61","quote":"Riboflavin.........................5.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 56-56","quote":"Nicotinic acid....................50.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q25","label":"Thioctic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary prints an mg input in the ten-vitamin stock prepared in 500 ml water. The local G_PER_L value at main-medium level changes both unit and stage. Preserve the batch mass; water input alone is not final stock volume, and the stock dose remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 60-60","quote":"Thioctic acid.....................50.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\": \"Thioctic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"MgSO4 . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 69-69","quote":"MgSO4 . 7H2O .......................3.0 g","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\": \"MgSO4 . 7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 71-71","quote":"NaCl...............................1.0 g","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Na2MoO4 . 2H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 79-79","quote":"Na2MoO4 . 2H2O.....................10.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\": \"Na2MoO4 . 2H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Boric acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 78-78","quote":"Boric acid........................10.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[4]","quote":"{\n          \"component_name\": \"Boric acid\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"FeSO4 . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 72-72","quote":"FeSO4 . 7H2O .....................100.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[5]","quote":"{\n          \"component_name\": \"FeSO4 . 7H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\": \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"ZnSO4 . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 75-75","quote":"ZnSO4 . 7H2O .....................100.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[6]","quote":"{\n          \"component_name\": \"ZnSO4 . 7H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"CuSO4 . 5H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 76-76","quote":"CuSO4 . 5H2O ......................10.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[7]","quote":"{\n          \"component_name\": \"CuSO4 . 5H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\": \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Nitrilotriacetic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 68-68","quote":"Nitrilotriacetic acid..............1.5 g","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[8]","quote":"{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"CaCl2 (anhydrous)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 74-74","quote":"CaCl2 (anhydrous) ................100.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[9]","quote":"{\n          \"component_name\": \"CaCl2 (anhydrous)\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001061\",\n          \"gmo_id\": \"GMO_001061\",\n          \"label\": \"Calcium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"MnSO4 . H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"500","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"500","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 70-70","quote":"MnSO4 . H2O ......................500.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[10]","quote":"{\n          \"component_name\": \"MnSO4 . H2O\",\n          \"volume\": 500,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001081\",\n          \"gmo_id\": \"GMO_001081\",\n          \"label\": \"Manganese sulfate monohydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"AlK(SO4)2 (anhydrous)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[35].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[35].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 77-77","quote":"AlK(SO4)2 (anhydrous) .............10.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[11]","quote":"{\n          \"component_name\": \"AlK(SO4)2 (anhydrous)\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001088\",\n          \"gmo_id\": \"GMO_001088\",\n          \"label\": \"Aluminum potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Na2SeO3 (anhydrous)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[36].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[36].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 80-80","quote":"Na2SeO3 (anhydrous) ................1.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[12]","quote":"{\n          \"component_name\": \"Na2SeO3 (anhydrous)\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001093\",\n          \"gmo_id\": \"GMO_001093\",\n          \"label\": \"Sodium selenite\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Co(NO3)2 . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[37].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[37].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate conversion uses that explicit final volume only. The separate 5 ml/L dose must not be confused with stock concentration.","source_stage":"mineral stock with explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 73-73","quote":"Co(NO3)2 . 6H2O ..................100.0 mg","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[13]","quote":"{\n          \"component_name\": \"Co(NO3)2 . 6H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001110\",\n          \"gmo_id\": \"GMO_001110\",\n          \"label\": \"Cobalt(II) nitrate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"2-3 N KOH","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[38].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[38].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The variable titrant amount is appropriate: 2–3 N KOH is used to reach stock pH 6.5, not a fixed amount or main-medium pH. Retain normality without inventing molarity.","source_stage":"mineral-stock titration","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[14]","quote":"{\n          \"component_name\": \"2-3 N KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Vitamin Solution","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly prints an ml/L receiving dose, not G_PER_L. Preserve its own ATCC stock definition; generic names and current linked provider IDs do not authenticate equivalent formulations.","source_stage":"main stock receiving dose","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 17-17","quote":"Vitamin Solution (see below)...................0.5 ml/L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\": \"Vitamin Solution\",\n          \"volume\": 0.5,\n          \"unit\": \"ml/l\",\n          \"reference_media_id\": \"M3174\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q41","label":"Reducing Solution","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"40","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"40","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary explicitly prints an ml/L receiving dose, not G_PER_L. Preserve its own ATCC stock definition; generic names and current linked provider IDs do not authenticate equivalent formulations.","source_stage":"main stock receiving dose","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 20-20","quote":"Reducing Solution (see below).................40.0 ml/L","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\": \"Reducing Solution\",\n          \"volume\": 40,\n          \"unit\": \"ml/l\",\n          \"reference_media_id\": \"M3174\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q42","label":"Provider6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing provider-declared 0.1 g/L and attached exact raw evidence agree. The current source also explicitly makes up to 100 ml. This authenticates only solution6241, which differs from ATCC1191 vitamins.","source_stage":"provider6241 only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q43","label":"Provider6241 Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing provider-declared 0.1 g/L and attached exact raw evidence agree. The current source also explicitly makes up to 100 ml. This authenticates only solution6241, which differs from ATCC1191 vitamins.","source_stage":"provider6241 only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q44","label":"Provider6241 biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The source says 200 micrograms and explicitly makes up to 100 ml. Exact dimensional calculation: 200 micrograms = 0.0002 g; 0.0002 g / 0.1 L = 0.002 g/L, not 2000 g/L. This is that provider stock only and must not replace the ATCC ten-vitamin formula.","source_stage":"provider6241 explicit final stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q45","label":"Provider6241 water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"Preserve make-up water to 100 ml final stock. 1000 PERCENT_V_V is unsupported; a makeup instruction does not establish the actual volume of water added.","source_stage":"provider6241 makeup","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q46","label":"Provider3892 NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The provider gives 200 ml of 0.2 N NaOH, not 1000 PERCENT_V_V. Preserve volume and normality as distinct stock inputs; no arbitrary final-volume or molarity inference.","source_stage":"provider3892 reagent input","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"0.2 N\",\n                \"amount\": 200,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Provider3892 Na2S x 9 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"12.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing 12.5 g/L is explicitly provider-declared and already has an exact attached raw claim. This validates that provider stock normalization only; the ATCC recipe does not state measured final stock volume and its cysteine hydrate is not explicit.","source_stage":"provider3892 declared stock rate","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\": 54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\": \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": 52.0439,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Provider3892 L-Cysteine HCl x H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"12.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing 12.5 g/L is explicitly provider-declared and already has an exact attached raw claim. This validates that provider stock normalization only; the ATCC recipe does not state measured final stock volume and its cysteine hydrate is not explicit.","source_stage":"provider3892 declared stock rate","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\": 3,\n                \"compound\": \"L-Cysteine HCl x H2O\",\n                \"compound_id\": 770,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\": \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Obsolete provider placeholder solution6241","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The See source for composition placeholder is not a real ingredient; a complete provider composition is already present. Reconcile placeholder/incomplete-composition metadata without deleting supported components or their history.","source_stage":"provider metadata placeholder","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data","quote":"{\n        \"id\": 6241,\n        \"name\": \"Vitamin solution\",\n        \"volume\": 100,\n        \"recipe\": [\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }\n        ],\n        \"equipment\": []\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"Obsolete provider placeholder solution3892","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The See source for composition placeholder is not a real ingredient; a complete provider composition is already present. Reconcile placeholder/incomplete-composition metadata without deleting supported components or their history.","source_stage":"provider metadata placeholder","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data","quote":"{\n        \"id\": 3892,\n        \"name\": \"Reducing solution\",\n        \"volume\": 200,\n        \"recipe\": [\n            {\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"0.2 N\",\n                \"amount\": 200,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 2,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\": 54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\": \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": 52.0439,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\": \"L-Cysteine HCl x H2O\",\n                \"compound_id\": 770,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\": \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\": null,\n                \"step\": \"Boil NaOH solution and cool down under a N2-H2 (95:5) atmosphere, then add Na2S x 9H2O and L-cysteine x HCl x H2O to the solution. Autoclave it under a N2-H2 (95:5) atmosphere.\"\n            }\n        ],\n        \"equipment\": {\n            \"615\": \"Autoclave\"\n        }\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Provider3892 preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"preparation_notes","stored":"Boil NaOH solution and cool down under a N2-H2 (95:5) atmosphere, then add Na2S x 9H2O and L-cysteine x HCl x H2O to the solution. Autoclave it under a N2-H2 (95:5) atmosphere.\n\nOriginal volume: 200 mL"}],"decision":"evidence_only","rationale":"Retain its provider-specific stock preparation and 95:5 atmosphere; do not claim ATCC identity merely from a generic stock name. Its 0.2 N input and cysteine monohydrate must remain explicit.","source_stage":"provider stock preparation","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Boil NaOH solution and cool down under a N2-H2 (95:5) atmosphere, then add Na2S x 9H2O and L-cysteine x HCl x H2O to the solution. Autoclave it under a N2-H2 (95:5) atmosphere.\"\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q52","label":"ATCC main preparation and explicit hazard notice","local_fields":[],"decision":"evidence_only","rationale":"The primary has staged reduction, 95:5 gas, conditional color observations, sealed vessels and 15-minute autoclaving, plus an explicit hydrogen-sulfide hazard notice. Preserve the original notice and source stages during transcription; no autoclave temperature, pressure or organism growth claim is supplied.","source_stage":"source-only main preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 23-34","quote":"A note of caution: This medium contains sodium sulfide, and hydrogen\nsulfide production will occur, especially upon prolonged boiling.\nHydrogen sulfide is hazardous and preparation of this medium should be\ndone in a chemical fume hood.\nBring the medium to a boil while gassing with a mixture of 95% N2, 5%\nH2. Keep the solution boiling for several minutes until time the color\nturns from blue to reddish-pink. Add the reducing solution during\ncontinuous gassing and boiling. The pink color should disappear,\nindicating reduction. Boil briefly for reduction. Using anaerobic\n(Hungate) technique, dispense the medium in tubes flushed with N2/H2 gas\nmixture. Stopper the tubes with butyl rubber, secure and autoclave for\n15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q53","label":"ATCC reducing-stock preparation","local_fields":[],"decision":"evidence_only","rationale":"The stock has its own boil/cool/add/anaerobic-vessel sequence and 15-minute autoclaving. This sequence is distinct from main medium preparation; no final stock volume is asserted.","source_stage":"source-only reducing preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0 ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5 g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q54","label":"ATCC vitamins dose and storage","local_fields":[],"decision":"evidence_only","rationale":"The explicit 0.05 ml per 100 ml is 0.5 ml/L and agrees with the main table. Retain source freeze-or-refrigerate/dark storage without inventing a storage temperature or duration.","source_stage":"source-only vitamins preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 17-17","quote":"Vitamin Solution (see below)...................0.5 ml/L","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator in the absence of light.","quote_basis":"derivative text"}]},{"quantity_id":"q55","label":"ATCC mineral preparation","local_fields":[],"decision":"evidence_only","rationale":"Initial 500 ml water, 2–3 N titrant, pH 6.5, ordered dissolution and final makeup to 1.0 L are explicit. These controls belong only to this stock; 0.5 ml per 100 ml equals its 5 ml/L receiving dose.","source_stage":"source-only mineral preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"}]},{"quantity_id":"q56","label":"ATCC1190 versus1191 substrate","local_fields":[],"decision":"evidence_only","rationale":"ATCC1191 replaces the base1190 glucose with filter paper. Do not add the base glucose row to this variant. The alternative tube strip has an explicit size and no stated tube volume, so it is not converted into g/L.","source_stage":"variant-specific substrate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 1-8","quote":"ATCC medium: 1191 Clostridium thermocellum medium (ATCC medium 1190)\nwith 18.75 g filter paper substituted for the glucose\n\n\nATCC Medium 1190 (see below) with 18.75 g filter paper substituted for\nthe glucose\nWhen preparing tubed medium, Whatman #1 filter paper may be used. In\nthis case, use one strip (8 X 70 mm) per tube of broth.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt lines 16-16","quote":"Glucose........................................8.0 g/L","quote_basis":"derivative text"}]},{"quantity_id":"q57","label":"Provider6241 retained makeup instruction","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The existing preparation note accurately retains explicit makeup to 100 ml. Preserve it unchanged; the incorrect water concentration is assessed separately in q45.","source_stage":"provider6241 makeup","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\": null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:009627.

All asserted CHEBI and provider slots are inventoried with exact current raw OLS objects and packaged MIM membership; provider compound IDs are separately checked against their exact solution responses. Na2HPO4 dodecahydrate versus anhydrous34683 is a confirmed mismatch. Thioctic acid versus R-specific30314 remains unresolved specificity, not proof of an opposite enantiomer. Other explicit magnesium/cobalt/manganese/copper/zinc/iron/sulfide hydrates agree. Generic vitaminB12 correctly remains a class rather than being replaced by the provider6241 cyanocobalamin. Missing annotations and no-current-row results do not authorize guessed IDs.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:009627.

All six exact historical reports and both selected historical parent objects were fully read. Four October5 ledgers were zero-checked. The two October7 provider reports preserve seven exact recipe objects and four attached provider-rate claims; fresh raw digests and quoted content are joined independently, without recreating old retrieval timestamps. Those reports intentionally left preparation-dependent inputs open. Current cleanup avoids summing unequal duplicates, exact-name migration can resolve only a generic name, and current merge compares scientific formulation. Append actual evidence-backed curation events; do not overwrite earlier history.

## Findings

### f1: Stock recipes and mixed-unit water were flattened into the main formulation

major / open / confirmed; issue key: culturemech-009627-stage-units.

Restore ATCC main, reducing, vitamin and mineral stages in the maintained owner. Source liquid doses/water are not G_PER_L, vitamin and mineral mg rows are not grams per litre of medium, and 501 G_PER_L water adds 500 ml to 1 L from different stocks. Keep correctly printed main g/L values unchanged. Mineral final makeup is explicit; vitamin/reducing final volumes are not. Current cleanup no longer sums unequal duplicates, and current singleton merge preserves its input; this is retained historical corruption.

### f2: The linked vitamin provider is not the ATCC ten-vitamin stock

major / open / confirmed; issue key: culturemech-009627-provider-identity.

The current link to mediadive.solution:6241 resolves to three vitamins made up to 100 ml, while ATCC1191 defines ten vitamins in 500 ml water. Replace the unsupported identity link with the exact ATCC stock representation. Reducing3892 separately declares cysteine monohydrate whereas ATCC prints cysteine HCl without that hydrate; retain this version/form limit rather than asserting equivalence from its name. No provider record is rewritten to match an unrelated stock.

### f3: Dodecahydrate phosphate is grounded to anhydrous disodium phosphate

major / open / confirmed; issue key: culturemech-009627-phosphate-hydrate.

The selected target and owner name Na2HPO4·12H2O, corroborated by ATCC and TOGO. CHEBI34683 has anhydrous HO4P.2Na formula and no twelve waters. Reconcile the supplied-form mapping using verified exact hydrate evidence; a valid canonical label does not make this chemical form correct. Preserve other correctly specific hydrates.

### f4: Exact ATCC preparation and variant controls are absent

major / open / confirmed; issue key: culturemech-009627-preparation.

Preserve separate main and stock preparation, source hazard notice, 15-minute sterilization durations, gas composition, vitamin storage and mineral pH/makeup. Retain the filter-paper replacement and conditional strip alternative; no glucose reintroduction, unstated temperature, final-stock volume or growth assertion. Current TOGO stage-aware paths and exact-name migration require source-specific reconciliation, not blind rerunning.

### f5: Linked provider records retain unresolved concentration and placeholder errors

major / open / confirmed; issue key: culturemech-009627-dependency-units.

Within solution6241 only, biotin 200 micrograms made up to 100 ml supports 0.002 g/L instead of 2000 g/L; water is makeup, not 1000 PERCENT_V_V. In3892, 200 ml 0.2 N NaOH is not 1000 PERCENT_V_V. Reconcile both placeholder ingredients/incomplete-composition flags while retaining four already-supported provider concentration claims. These repairs do not authenticate either stock as the ATCC formulation.

### f6: Generic thioctic-acid source does not establish the asserted R form

minor / open / confirmed; issue key: culturemech-009627-stereochemical-scope.

The source prints Thioctic acid without stereochemistry, while primary and secondary CHEBI30314 slots encode (R)-lipoic acid. Preserve this as an unresolved specificity claim; do not label it the opposite enantiomer or silently choose a replacement. Resolve exact supplied form if a narrower mapping is retained.

## Recommended Actions And Acceptance Checks

### a1

Restore ATCC main, reducing, vitamin and mineral stages in the maintained owner. Source liquid doses/water are not G_PER_L, vitamin and mineral mg rows are not grams per litre of medium, and 501 G_PER_L water adds 500 ml to 1 L from different stocks. Keep correctly printed main g/L values unchanged. Mineral final makeup is explicit; vitamin/reducing final volumes are not. Current cleanup no longer sums unequal duplicates, and current singleton merge preserves its input; this is retained historical corruption.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The current link to mediadive.solution:6241 resolves to three vitamins made up to 100 ml, while ATCC1191 defines ten vitamins in 500 ml water. Replace the unsupported identity link with the exact ATCC stock representation. Reducing3892 separately declares cysteine monohydrate whereas ATCC prints cysteine HCl without that hydrate; retain this version/form limit rather than asserting equivalence from its name. No provider record is rewritten to match an unrelated stock.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The selected target and owner name Na2HPO4·12H2O, corroborated by ATCC and TOGO. CHEBI34683 has anhydrous HO4P.2Na formula and no twelve waters. Reconcile the supplied-form mapping using verified exact hydrate evidence; a valid canonical label does not make this chemical form correct. Preserve other correctly specific hydrates.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

Preserve separate main and stock preparation, source hazard notice, 15-minute sterilization durations, gas composition, vitamin storage and mineral pH/makeup. Retain the filter-paper replacement and conditional strip alternative; no glucose reintroduction, unstated temperature, final-stock volume or growth assertion. Current TOGO stage-aware paths and exact-name migration require source-specific reconciliation, not blind rerunning.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Within solution6241 only, biotin 200 micrograms made up to 100 ml supports 0.002 g/L instead of 2000 g/L; water is makeup, not 1000 PERCENT_V_V. In3892, 200 ml 0.2 N NaOH is not 1000 PERCENT_V_V. Reconcile both placeholder ingredients/incomplete-composition flags while retaining four already-supported provider concentration claims. These repairs do not authenticate either stock as the ATCC formulation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

The source prints Thioctic acid without stereochemistry, while primary and secondary CHEBI30314 slots encode (R)-lipoic acid. Preserve this as an unresolved specificity claim; do not label it the opposite enantiomer or silently choose a replacement. Resolve exact supplied form if a narrower mapping is retained.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| atcc1191 | https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331; REVIEW_WORK/batch063/source08-10/atcc1191.json; exact original raw/text/hash/time metadata | context_only | Exact source identity; dependency only named stock subsection, no parent basal transfer. Source-specific biological identity screened before assessment. |
| togoM3174 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174; REVIEW_WORK/batch063/source08-10/togoM3174.json; exact original raw/text/hash/time metadata | context_only | Exact source identity; dependency only named stock subsection, no parent basal transfer. Source-specific biological identity screened before assessment. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; REVIEW_WORK/batch063/source08-10/solution6241.json; exact original raw/text/hash/time metadata | context_only | Exact source identity; dependency only named stock subsection, no parent basal transfer. Source-specific biological identity screened before assessment. |
| solution3892 | https://mediadive.dsmz.de/rest/solution/3892; REVIEW_WORK/batch063/source08-10/solution3892.json; exact original raw/text/hash/time metadata | context_only | Exact source identity; dependency only named stock subsection, no parent basal transfer. Source-specific biological identity screened before assessment. |
| target | data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-19 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-2500-3000/records/bacterial/mediadive_3892_Reducing_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch063/record10/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch063/record10/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch063/record10/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _assembled_solution_sections, _extract_primary_components, _parse_unit, _convert_to_culturemech | context_only | Current primary-component and assembled-section paths preserve stages when their predicates hold. Unit parsing still maps g to G_PER_L, ml to ML_PER_L and bare percent to PERCENT_W_V; L maps to L. Current code is not historical execution proof. |
| writer-migration | scripts/migrate_solutions_from_ingredients.py; __init__, _resolve_solution, _migrate_media_file | context_only | Current exact-name solution migration preserves the original concentration and can resolve a name to one provider ID; this does not establish source-specific formulation equivalence. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-cleanup | scripts/cleanup_media_quality.py; merge_duplicate_ingredients, _merge_ingredient_group | context_only | Current merge_duplicate_ingredients/_merge_ingredient_group no longer sums unequal duplicate amounts; differing values are flagged and first retained. The old 501-water sum is a historical artifact, not current execution evidence. |
| visual-1 | REVIEW_WORK/batch063/record10/atcc1191-page1.png; ATCC1191 PDF page 1 | context_only | Original captured PDF rendered and completely visually read; text table order and numeric typography agree. |
| visual-2 | REVIEW_WORK/batch063/record10/atcc1191-page2.png; ATCC1191 PDF page 2 | context_only | Original captured PDF rendered and completely visually read; text table order and numeric typography agree. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch063/source08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch063/source08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch063/source08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34683; REVIEW_WORK/batch063/source08-10/chebi34683.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997; REVIEW_WORK/batch063/source08-10/chebi17997.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276; REVIEW_WORK/batch063/source08-10/chebi18276.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch063/source08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch063/source08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch063/source08-10/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch063/source08-10/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch063/source08-10/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch063/source08-10/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch063/source08-10/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch063/source08-10/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch063/source08-10/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi30314 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30314; REVIEW_WORK/batch063/source08-10/chebi30314.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; REVIEW_WORK/batch063/source08-10/chebi31795.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch063/source08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch063/source08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch063/source08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; REVIEW_WORK/batch063/source08-10/chebi75836.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; REVIEW_WORK/batch063/source08-10/chebi32312.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31440; REVIEW_WORK/batch063/source08-10/chebi31440.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557; REVIEW_WORK/batch063/source08-10/chebi44557.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364; REVIEW_WORK/batch063/source08-10/chebi86364.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi86214 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86214; REVIEW_WORK/batch063/source08-10/chebi86214.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439; REVIEW_WORK/batch063/source08-10/chebi17439.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch063/source08-10/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145; REVIEW_WORK/batch063/source08-10/chebi32145.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248; REVIEW_WORK/batch063/source08-10/chebi91248.json; exact original raw/text/hash/time metadata | context_only | Exact current returned ontology ID/label/formula/definitions; label correspondence alone does not verify supplied form. |
| quantities | REVIEW_WORK/batch063/record10/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch063/record10/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch063/record10/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch063/record10/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch063/record10/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch063/record10/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch063/record10/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch063/record10/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch063/record10/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch063/record10/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch063/record10/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- ATCC1191 two-page primary was completely read as text and visually. No organism strain, culture performance or optimization is inferred from its title.
- ATCC vitamin stock uses water input without explicit final makeup; reducing stock uses a reagent volume without explicit measured final stock volume. Mineral stock and main medium have explicit final makeup and must not inherit that uncertainty.
- The 0.1% resazurin basis and generic thioctic-acid stereochemistry remain unresolved; normality is retained as printed, not converted.
- Provider6241 and3892 are reviewed under their own source identities. Their data are not automatically transferred into the ATCC recipe.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T104807Z-culturemech-009627-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: Clostridium thermocellum medium'
started_at: '2026-10-28T10:18:14.840118Z'
finished_at: '2026-10-28T10:48:07.916031Z'
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
summary: The main explicit rates are supported, but historical flattening lost stock
  stages, corrupted units and linked an unrelated vitamin solution. Restore the exact
  ATCC variant and preparation, reconcile phosphate hydrate and linked-provider residual
  errors, and retain the remaining source-form uncertainties. No recipe files were
  changed.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml
    sha256: dbef0d8f659ab36ea2484ec3322f11c54cf96fe0ace7ffab48c7cda3efac61a3
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    sha256: 693548ba2284b84076bf31ee2410a08af8932b95492e572302dc13403a67adca
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml
    sha256: 355e9c0ee3390afcc50447b73431fea46dbd376284db63aef73f85b1225e1afd
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-2500-3000/plan.json
    sha256: 672b4be1b9c19f8e8c0a1b7dcd2c8a0ac8c8d7150aef74aadc05dd1cd41cf9c4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-2500-3000/records/bacterial/mediadive_3892_Reducing_solution.yaml.md
    sha256: d8d18f04d861d159d50c3df4a8cb2f1eb5aa027791b01de82c8df90a7024d409
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
    sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
    sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.md
    sha256: 8d4fcdd2cabbd9106712a68ddbb4c0e822c0944acee0dabddeb931ba557a8bd1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.md
    sha256: 39f07ec4c1851f05422dfc41927309915f67759c78924242c09c2bb8d04958e0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.md
    sha256: 94c172d49b1aaf17cc515935005c6a81bdab4b2db9ab164a1942b7edec4d3c4c
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
    sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
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
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_m142_nested_traces.py
    sha256: d015c2df13aadb722e2ada9cd45fbd0e86e4cd48390edae78dab78d5df5ce80f
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/repair_togo_m1066_score15.py
    sha256: 0c827219e43de0ada0eb19514f9f243b0695ef15bfc54d6a5dd89d303aa65784
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
  selection: Authoritative batch063 index 10
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009627
targets:
- target_id: CultureMech:009627
  path: data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml
  label: clostridium_thermocellum_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
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
  - CultureMech:009627
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml
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
  - CultureMech:009627
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml
    --out REVIEW_WORK/batch063/record10/strict.tsv --workers 1 --quiet
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
  - CultureMech:009627
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml
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
  - CultureMech:009627
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: atcc1191
  kind: primary_source
  reference: https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331
  accessed_at: '2026-10-28T10:18:43.798179Z'
  locator: REVIEW_WORK/batch063/source08-10/atcc1191.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity; dependency only named stock subsection, no parent
    basal transfer. Source-specific biological identity screened before assessment.
  snapshot_sha256: 3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3
- evidence_id: togoM3174
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174
  accessed_at: '2026-10-28T10:18:42.276479Z'
  locator: REVIEW_WORK/batch063/source08-10/togoM3174.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity; dependency only named stock subsection, no parent
    basal transfer. Source-specific biological identity screened before assessment.
  snapshot_sha256: 7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  accessed_at: '2026-10-28T10:18:43.274206Z'
  locator: REVIEW_WORK/batch063/source08-10/solution6241.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity; dependency only named stock subsection, no parent
    basal transfer. Source-specific biological identity screened before assessment.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: solution3892
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/3892
  accessed_at: '2026-10-28T10:18:43.286264Z'
  locator: REVIEW_WORK/batch063/source08-10/solution3892.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact source identity; dependency only named stock subsection, no parent
    basal transfer. Source-specific biological identity screened before assessment.
  snapshot_sha256: d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T10:43:09.977796Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: dbef0d8f659ab36ea2484ec3322f11c54cf96fe0ace7ffab48c7cda3efac61a3
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T10:43:09.977948Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 693548ba2284b84076bf31ee2410a08af8932b95492e572302dc13403a67adca
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T10:43:09.977974Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T10:43:09.978286Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T10:43:09.978308Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T10:43:09.978328Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T10:43:09.978351Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 672b4be1b9c19f8e8c0a1b7dcd2c8a0ac8c8d7150aef74aadc05dd1cd41cf9c4
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-2500-3000/records/bacterial/mediadive_3892_Reducing_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T10:43:09.980283Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: d8d18f04d861d159d50c3df4a8cb2f1eb5aa027791b01de82c8df90a7024d409
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T10:43:09.980310Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T10:43:09.981071Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T10:43:09.981096Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8d4fcdd2cabbd9106712a68ddbb4c0e822c0944acee0dabddeb931ba557a8bd1
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T10:43:09.981121Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 39f07ec4c1851f05422dfc41927309915f67759c78924242c09c2bb8d04958e0
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T10:43:09.981143Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 94c172d49b1aaf17cc515935005c6a81bdab4b2db9ab164a1942b7edec4d3c4c
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
  locator: Complete report
  accessed_at: '2026-10-28T10:43:09.981163Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/historical-reading.json
  accessed_at: '2026-10-28T10:43:09.986477Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 75631b26d91d714fa58ff33231aa047972aba6ab61b3e657958915bdd9808007
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T10:43:09.986668Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: 04465527dfcdb32360a99a8781c709d565327408c7645d81da4b3a735f4af28b
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/complete-document-reader.json
  accessed_at: '2026-10-28T10:43:09.986818Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 2dae5af338d65f4d1aec89ff3365fff541500e9a084ce54e9edf6eee5e638955
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _assembled_solution_sections, _extract_primary_components,
    _parse_unit, _convert_to_culturemech
  accessed_at: '2026-10-28T10:43:09.986860Z'
  support: context_only
  summary: Current primary-component and assembled-section paths preserve stages when
    their predicates hold. Unit parsing still maps g to G_PER_L, ml to ML_PER_L and
    bare percent to PERCENT_W_V; L maps to L. Current code is not historical execution
    proof.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-migration
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: __init__, _resolve_solution, _migrate_media_file
  accessed_at: '2026-10-28T10:43:09.986892Z'
  support: context_only
  summary: Current exact-name solution migration preserves the original concentration
    and can resolve a name to one provider ID; this does not establish source-specific
    formulation equivalence.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T10:43:09.986914Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: merge_duplicate_ingredients, _merge_ingredient_group
  accessed_at: '2026-10-28T10:43:09.986935Z'
  support: context_only
  summary: Current merge_duplicate_ingredients/_merge_ingredient_group no longer sums
    unequal duplicate amounts; differing values are flagged and first retained. The
    old 501-water sum is a historical artifact, not current execution evidence.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: visual-1
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/atcc1191-page1.png
  accessed_at: '2026-10-28T10:43:09.987377Z'
  locator: ATCC1191 PDF page 1
  support: context_only
  summary: Original captured PDF rendered and completely visually read; text table
    order and numeric typography agree.
  snapshot_sha256: 74f470b996c382ab140124a53251758d1f606798c9ad4ff363579a44e0ea94ad
- evidence_id: visual-2
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/atcc1191-page2.png
  accessed_at: '2026-10-28T10:43:09.987760Z'
  locator: ATCC1191 PDF page 2
  support: context_only
  summary: Original captured PDF rendered and completely visually read; text table
    order and numeric typography agree.
  snapshot_sha256: 111c909db6b47fa0f1726f1f353c8e534061599dac0619096a554b157c518aaf
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T10:18:49.616797Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T10:18:46.674421Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T10:18:50.828691Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34683
  accessed_at: '2026-10-28T10:18:48.371779Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi34683.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 77f17276e9ef67f5b284232543dcfb3c01546658eb9e93fad4cbd1a5374bfb56
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17997
  accessed_at: '2026-10-28T10:18:45.472164Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi17997.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: c4f240d59927c0f5c6c8d29c14830d0f278cfeabc4ed924be5c2b6bbe1039c05
- evidence_id: chebi18276
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:18276
  accessed_at: '2026-10-28T10:18:45.774303Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi18276.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: e9495ec2aad65253b7f792e780c1610f9f12f2c0bb20e06c2526156d37b09ed7
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T10:18:50.062783Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T10:18:43.885271Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T10:18:44.174948Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi15956.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T10:18:46.402616Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi30753.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T10:18:46.573939Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi30961.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T10:18:46.023352Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi27470.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T10:18:45.164181Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi176843.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T10:18:44.751874Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi17015.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T10:18:44.024087Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi15940.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi30314
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30314
  accessed_at: '2026-10-28T10:18:46.080367Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi30314.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: c65311307ace44e29b902c93926f9a84f7fd601f7666e192d2af3dd18d4727e4
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795
  accessed_at: '2026-10-28T10:18:47.098567Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi31795.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: ceb0c93d1964844e99454d74730971855710441d92eec74aff5c873c833e324a
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T10:18:45.871475Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T10:18:49.846722Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T10:18:47.908112Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  accessed_at: '2026-10-28T10:18:49.747926Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi75836.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  accessed_at: '2026-10-28T10:18:47.697130Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi32312.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31440
  accessed_at: '2026-10-28T10:18:47.087853Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi31440.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: a0af950191bab322f858a701486e40e51a4780a18d9d03913d351b383f05cb7d
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:44557
  accessed_at: '2026-10-28T10:18:48.906099Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi44557.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 25e8fb689e4dfc294e2823ca36290cdce6d21ad174238e0e958ebe09d4c1262b
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364
  accessed_at: '2026-10-28T10:18:51.025728Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi86364.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 6e685ea7654bc1f4e16b3e3a05d73d8541e84cddcc28de59c4ae57ac288a1505
- evidence_id: chebi86214
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86214
  accessed_at: '2026-10-28T10:18:50.438890Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi86214.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 9523f9163575dfb800448b401eb6eb5e75e892c56ff33c1134894e2b5d58779c
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439
  accessed_at: '2026-10-28T10:18:45.161448Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi17439.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 71dca75ee64801424c519bde7667291decd3b97f0c4e46c3d9b9405fa04a71d4
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T10:18:49.001303Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi49105.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32145
  accessed_at: '2026-10-28T10:18:47.313539Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi32145.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: 089212e8c86e2d4a4b145366c8bc67e0056565ef6970dcdc3df63ad20dac234d
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:91248
  accessed_at: '2026-10-28T10:18:51.624061Z'
  locator: REVIEW_WORK/batch063/source08-10/chebi91248.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current returned ontology ID/label/formula/definitions; label correspondence
    alone does not verify supplied form.
  snapshot_sha256: d0959ac455ece32a6e94c13fd8e592403109201b6c61144dccfe0d58f1916380
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T10:48:07.916031Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: e16570d32ea61940883d29f561dfa11c868ddf26f8b5a92eabdbfb1cc2f9d910
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T10:43:10.124701Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 07084e807891ef288a548b5b963c27fd935260e665016923cb08065ff13662b1
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T10:43:10.124826Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: a45a6143235152ab434b66a158f00ccf032ef2b4e39986429b4e20779b2484a7
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T10:43:10.124898Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: e851ba9eb39400ae0fd34569cc5516b0c231867cd276e7c51d32cf3375b7720e
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T10:43:10.124958Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: a14893157cd471627914f697ad8b24b551ec4b0534402283a7f015eb69880d06
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T10:43:10.124982Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 757ffb20f023a137f58580934166b0e48fee34a071d0a060996ffb00360b2ec0
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch063/record10/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T10:43:10.125001Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: c1f3365ab7f2b7a16020ded3fc35d30fb601f471d4b7dc1acea328632935774b
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch063/record10/schema-result.json
  accessed_at: '2026-10-28T10:18:15.935502Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: f357b49181bb43b88ec8e3a6d28a0d122259e4d020dca6ec246b98db9c220460
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch063/record10/strict-result.json
  accessed_at: '2026-10-28T10:18:16.924047Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: ea5583241596114490707450b57316e80345d3da0177b44b7ddfdad92446cace
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch063/record10/terms-result.json
  accessed_at: '2026-10-28T10:18:18.017903Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 1430d251ce1d9b8af9f18bddb0d27b84cf45d07b64e399a778d8cd4222165c53
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch063/record10/references-result.json
  accessed_at: '2026-10-28T10:18:18.808976Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 6e8778656d9384c47018eea16be0d2c0c5b85e09528e53e50515c4a506d794f6
assessments:
- assessment_id: identity
  area: identity
  topic: ATCC1191 variant and provider stock identity
  outcome: concern
  summary: The exact target/owner is TOGO M3174 citing ATCC1191. Full primary pages
    support its filter-paper variant of1190; provider6241 is a different vitamin formulation
    and provider3892 has an explicit hydrate version distinction. Stock labels alone
    do not establish identity.
  target_ids:
  - CultureMech:009627
  evidence_ids:
  - atcc1191
  - togoM3174
  - solution6241
  - solution3892
- assessment_id: structure
  area: schema
  topic: Diagnostics, classification and derived flag
  outcome: concern
  summary: Four original canonical checks pass with zero reference checks. Complex/undefined/liquid
    classification fits the source; high_metal is not authenticated by the primary
    and must be reevaluated after stock restoration rather than treated as a culture
    phenotype. Empty placeholder solution names are not source names.
  target_ids:
  - CultureMech:009627
  evidence_ids:
  - check-schema
  - check-strict
  - target
  - owner
  - atcc1191
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 91 current concentration fields are covered by 57 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:009627
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b063-quantity-inventory-v1","target":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","quantity_field_count":91,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly prints g/L and water to 1.0 L; the existing number/unit has
    direct source support but no attached amount claim. Chemical supplied-form correspondence
    is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit
    main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 11-11","quote":"KH2PO4 .........................................1.5 g/L","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 1.5,\n          \"unit\": \"g/L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly prints g/L and water to 1.0 L; the existing number/unit has
    direct source support but no attached amount claim. Chemical supplied-form correspondence
    is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit
    main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 13-13","quote":"NH4Cl ..........................................0.5 g/L","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"NH4Cl\",\n          \"volume\": 0.5,\n          \"unit\": \"g/L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\":
    \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"MgCl2
    . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.18","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.18","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly prints g/L and water to 1.0 L; the existing number/unit has
    direct source support but no attached amount claim. Chemical supplied-form correspondence
    is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit
    main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 14-14","quote":"MgCl2 . 6H2O ...................................0.18 g/L","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"MgCl2 . 6H2O\",\n          \"volume\": 0.18,\n          \"unit\": \"g/L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\":
    \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"Na2HPO4
    . 12H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"4.2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"4.2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly prints g/L and water to 1.0 L; the existing number/unit has
    direct source support but no attached amount claim. Chemical supplied-form correspondence
    is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit
    main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 12-12","quote":"Na2HPO4 . 12H2O.................................4.2 g/L","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[5]","quote":"{\n          \"component_name\":
    \"Na2HPO4 . 12H2O\",\n          \"volume\": 4.2,\n          \"unit\": \"g/L\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001115\",\n          \"gmo_id\": \"GMO_001115\",\n          \"label\":
    \"Disodium phosphate dodecahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"Yeast Extract (BD 212750)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"2","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"The
    primary explicitly prints g/L and water to 1.0 L; the existing number/unit has
    direct source support but no attached amount claim. Chemical supplied-form correspondence
    is separately assessed, including phosphate dodecahydrate.","source_stage":"explicit
    main-medium rate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 15-15","quote":"Yeast Extract (BD 212750)......................2.0 g/L","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[6]","quote":"{\n          \"component_name\":
    \"Yeast Extract (BD 212750)\",\n          \"volume\": 2,\n          \"unit\":
    \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\":
    \"GMO_001018\",\n          \"label\": \"Bacto &trade; Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"Whatman #1 filter paper","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"18.75","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"18.75","unit":"G_PER_L"}}],"decision":"evidence_only","rationale":"TOGO
    explicitly represents the replacement as 18.75 g/L, consistent with 18.75 g replacing
    glucose in the ATCC one-litre recipe. Whatman grade and one 8 x 70 mm strip per
    tube are a conditional alternative, not an additional dose or an unconditional
    requirement for every batch.","source_stage":"ATCC1191 filter-paper variant","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 1-8","quote":"ATCC medium: 1191 Clostridium thermocellum medium (ATCC medium
    1190)\nwith 18.75 g filter paper substituted for the glucose\n\n\nATCC Medium
    1190 (see below) with 18.75 g filter paper substituted for\nthe glucose\nWhen
    preparing tubed medium, Whatman #1 filter paper may be used. In\nthis case, use
    one strip (8 X 70 mm) per tube of broth.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[7]","quote":"{\n          \"component_name\":
    \"Whatman #1 filter paper\",\n          \"volume\": 18.75,\n          \"unit\":
    \"g/L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002360\",\n          \"gmo_id\":
    \"GMO_002360\",\n          \"label\": \"Whatman &reg; qualitative filter paper,
    grade 1\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"Resazurin (0.1%)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source is 1 ml/L of a 0.1% resazurin stock, not 1 g/L resazurin. Percentage basis
    is unspecified; preserve the stock label without conversion.","source_stage":"main
    stock transfer","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 19-19","quote":"Resazurin (0.1%)...............................1.0 ml/L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
    \"Resazurin (0.1%)\",\n          \"volume\": 1,\n          \"unit\": \"ml/l\",\n          \"conc_value\":
    0.1,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001403\",\n          \"gmo_id\":
    \"GMO_001403\",\n          \"label\": \"Resazurin solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent
    redox indicator\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Distilled
    deionized water","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"Water
    is a makeup reagent to 1.0 L final main medium, not 1 G_PER_L or a separately
    measured fixed water addition.","source_stage":"main final-volume makeup","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 21-21","quote":"Distilled deionized water to...................1.0 L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Distilled deionized water\",\n          \"volume\": 1,\n          \"unit\":
    \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Wolfe''s
    Modified Mineral Elixir","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source explicitly doses the separately defined mineral stock at 5 ml/L (also 0.5
    ml/100 ml), not 5 g/L. Restore the receiving relationship without merging the
    stock internals into main ingredients.","source_stage":"mineral receiving dose","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 18-18","quote":"Wolfe''s Modified Mineral Elixir (see below)....5.0 ml/L","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[9]","quote":"{\n          \"component_name\":
    \"Wolfe''s Modified Mineral Elixir\",\n          \"volume\": 5,\n          \"unit\":
    \"ml/l\",\n          \"reference_media_id\": \"M3174\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Nitrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Gas
    amount is unspecified; preserve the printed 95% N2/5% H2 atmosphere separately.
    Repeated main/stock instructions do not create two dissolved-gas amounts.","source_stage":"gas
    context","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 27-34","quote":"Bring the medium to a boil while gassing with a mixture
    of 95% N2, 5%\nH2. Keep the solution boiling for several minutes until time the
    color\nturns from blue to reddish-pink. Add the reducing solution during\ncontinuous
    gassing and boiling. The pink color should disappear,\nindicating reduction. Boil
    briefly for reduction. Using anaerobic\n(Hungate) technique, dispense the medium
    in tubes flushed with N2/H2 gas\nmixture. Stopper the tubes with butyl rubber,
    secure and autoclave for\n15 minutes.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 41-44","quote":"Bring the sodium hydroxide solution to a boil and bubble
    with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium
    sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith
    butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q11","label":"Hydrogen
    gas","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"Gas
    amount is unspecified; preserve the printed 95% N2/5% H2 atmosphere separately.
    Repeated main/stock instructions do not create two dissolved-gas amounts.","source_stage":"gas
    context","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 27-34","quote":"Bring the medium to a boil while gassing with a mixture
    of 95% N2, 5%\nH2. Keep the solution boiling for several minutes until time the
    color\nturns from blue to reddish-pink. Add the reducing solution during\ncontinuous
    gassing and boiling. The pink color should disappear,\nindicating reduction. Boil
    briefly for reduction. Using anaerobic\n(Hungate) technique, dispense the medium
    in tubes flushed with N2/H2 gas\nmixture. Stopper the tubes with butyl rubber,
    secure and autoclave for\n15 minutes.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 41-44","quote":"Bring the sodium hydroxide solution to a boil and bubble
    with 95% N2, 5%\nH2 gas mixture. Allow the solution to cool and add the sodium
    sulfide\nand cysteine. Under anaerobic conditions, tube the solution, stopper\nwith
    butyl rubber, and autoclave for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"0.2
    N NaOH","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"200","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"200","unit":"G_PER_L"}}],"decision":"correct","rationale":"These
    are reducing-stock batch inputs, not direct main-medium g/L. Preserve 200 ml of
    0.2 N NaOH and the two 2.5 g masses; no measured final stock volume or normality-to-molarity
    conversion is established. ATCC cysteine HCl does not explicitly specify the monohydrate
    in provider3892.","source_stage":"reducing-stock batch","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0
    ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5
    g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2
    gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine.
    Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and
    autoclave for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[1].items[0]","quote":"{\n          \"component_name\":
    \"0.2 N NaOH\",\n          \"volume\": 200,\n          \"unit\": \"ml\",\n          \"conc_value\":
    0.2,\n          \"conc_unit\": \"N\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001300\",\n          \"gmo_id\":
    \"GMO_001300\",\n          \"label\": \"Sodium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    []\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q13","label":"Na2S
    . 9H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"These
    are reducing-stock batch inputs, not direct main-medium g/L. Preserve 200 ml of
    0.2 N NaOH and the two 2.5 g masses; no measured final stock volume or normality-to-molarity
    conversion is established. ATCC cysteine HCl does not explicitly specify the monohydrate
    in provider3892.","source_stage":"reducing-stock batch","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0
    ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5
    g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2
    gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine.
    Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and
    autoclave for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[1].items[1]","quote":"{\n          \"component_name\":
    \"Na2S . 9H2O\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\":
    \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q14","label":"L-Cysteine
    . HCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"These
    are reducing-stock batch inputs, not direct main-medium g/L. Preserve 200 ml of
    0.2 N NaOH and the two 2.5 g masses; no measured final stock volume or normality-to-molarity
    conversion is established. ATCC cysteine HCl does not explicitly specify the monohydrate
    in provider3892.","source_stage":"reducing-stock batch","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0
    ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5
    g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2
    gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine.
    Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and
    autoclave for 15 minutes.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[1].items[2]","quote":"{\n          \"component_name\":
    \"L-Cysteine . HCl\",\n          \"volume\": 2.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001828\",\n          \"gmo_id\": \"GMO_001828\",\n          \"label\":
    \"L-Cysteine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q15","label":"Distilled water","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"501.0","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"501.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    501 G_PER_L value combines 500 ml vitamin water with 1 L mineral water across
    different stages and units. Restore separate stock solvent/makeup fields: 500
    ml is vitamin input, whereas mineral preparation explicitly makes up to 1.0 L.
    Do not sum them.","source_stage":"two separate stock water stages","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 81-87","quote":"Distilled water....................1.0 L\n\nSuspend the
    nitrilotriacetic acid in 500 ml water. Dissolve it by\ntitrating with 2-3 N KOH
    until the pH is stabilized at 6.5. Add the rest\nof the ingredients and dissolve
    in the order they are listed. Finally,\nadjust the volume to 1.0 L For 100 ml
    of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[0]","quote":"{\n          \"component_name\":
    \"Distilled water\",\n          \"volume\": 500,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\":
    \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q16","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 52-52","quote":"Biotin............................20.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[1]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q17","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 53-53","quote":"p-Aminobenzoic acid...............50.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[2]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q18","label":"Thiamine . HCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 58-58","quote":"Thiamine . HCl.....................5.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[3]","quote":"{\n          \"component_name\":
    \"Thiamine . HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q19","label":"Pantothenic acid calcium salt","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 55-55","quote":"Pantothenic acid calcium salt.....50.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[4]","quote":"{\n          \"component_name\":
    \"Pantothenic acid calcium salt\",\n          \"volume\": 50,\n          \"unit\":
    \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\":
    \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q20","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 59-59","quote":"Pyridoxine hydrochloride.........100.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[5]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q21","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"20","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"20","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 54-54","quote":"Folic acid........................20.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[6]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q22","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 57-57","quote":"Vitamin B12........................1.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[7]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q23","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 61-61","quote":"Riboflavin.........................5.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[8]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q24","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 56-56","quote":"Nicotinic acid....................50.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[9]","quote":"{\n          \"component_name\":
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
    UTF-8"}]},{"quantity_id":"q25","label":"Thioctic acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary prints an mg input in the ten-vitamin stock prepared in 500 ml water.
    The local G_PER_L value at main-medium level changes both unit and stage. Preserve
    the batch mass; water input alone is not final stock volume, and the stock dose
    remains a separate field.","source_stage":"ATCC ten-vitamin stock","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 60-60","quote":"Thioctic acid.....................50.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[2].items[10]","quote":"{\n          \"component_name\":
    \"Thioctic acid\",\n          \"volume\": 50,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\":
    \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"MgSO4 . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"3","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"3","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 69-69","quote":"MgSO4 . 7H2O .......................3.0 g","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[1]","quote":"{\n          \"component_name\":
    \"MgSO4 . 7H2O\",\n          \"volume\": 3,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\":
    \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 71-71","quote":"NaCl...............................1.0 g","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[2]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Na2MoO4
    . 2H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 79-79","quote":"Na2MoO4 . 2H2O.....................10.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[3]","quote":"{\n          \"component_name\":
    \"Na2MoO4 . 2H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\":
    \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Boric
    acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 78-78","quote":"Boric acid........................10.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[4]","quote":"{\n          \"component_name\":
    \"Boric acid\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\":
    \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q30","label":"FeSO4
    . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 72-72","quote":"FeSO4 . 7H2O .....................100.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[5]","quote":"{\n          \"component_name\":
    \"FeSO4 . 7H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001016\",\n          \"gmo_id\": \"GMO_001016\",\n          \"label\":
    \"Iron(II) sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"ZnSO4
    . 7H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[30].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 75-75","quote":"ZnSO4 . 7H2O .....................100.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[6]","quote":"{\n          \"component_name\":
    \"ZnSO4 . 7H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\":
    \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"CuSO4
    . 5H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[31].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 76-76","quote":"CuSO4 . 5H2O ......................10.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[7]","quote":"{\n          \"component_name\":
    \"CuSO4 . 5H2O\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\":
    \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q33","label":"Nitrilotriacetic
    acid","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[32].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 68-68","quote":"Nitrilotriacetic acid..............1.5 g","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[8]","quote":"{\n          \"component_name\":
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
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q34","label":"CaCl2
    (anhydrous)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[33].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 74-74","quote":"CaCl2 (anhydrous) ................100.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[9]","quote":"{\n          \"component_name\":
    \"CaCl2 (anhydrous)\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001061\",\n          \"gmo_id\": \"GMO_001061\",\n          \"label\":
    \"Calcium chloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q35","label":"MnSO4
    . H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored":{"value":"500","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[34].concentration","stored":{"value":"500","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 70-70","quote":"MnSO4 . H2O ......................500.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[10]","quote":"{\n          \"component_name\":
    \"MnSO4 . H2O\",\n          \"volume\": 500,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001081\",\n          \"gmo_id\": \"GMO_001081\",\n          \"label\":
    \"Manganese sulfate monohydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q36","label":"AlK(SO4)2
    (anhydrous)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[35].concentration","stored":{"value":"10","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[35].concentration","stored":{"value":"10","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 77-77","quote":"AlK(SO4)2 (anhydrous) .............10.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[11]","quote":"{\n          \"component_name\":
    \"AlK(SO4)2 (anhydrous)\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001088\",\n          \"gmo_id\": \"GMO_001088\",\n          \"label\":
    \"Aluminum potassium sulfate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q37","label":"Na2SeO3
    (anhydrous)","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[36].concentration","stored":{"value":"1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[36].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 80-80","quote":"Na2SeO3 (anhydrous) ................1.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[12]","quote":"{\n          \"component_name\":
    \"Na2SeO3 (anhydrous)\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001093\",\n          \"gmo_id\": \"GMO_001093\",\n          \"label\":
    \"Sodium selenite\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q38","label":"Co(NO3)2
    . 6H2O","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[37].concentration","stored":{"value":"100","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[37].concentration","stored":{"value":"100","unit":"G_PER_L"}}],"decision":"correct","rationale":"This
    amount belongs to the mineral stock with explicit final makeup to 1.0 L, not to
    the receiving medium. Preserve source mg/g units and supplied hydrates; any stock-rate
    conversion uses that explicit final volume only. The separate 5 ml/L dose must
    not be confused with stock concentration.","source_stage":"mineral stock with
    explicit final volume","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 73-73","quote":"Co(NO3)2 . 6H2O ..................100.0 mg","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[13]","quote":"{\n          \"component_name\":
    \"Co(NO3)2 . 6H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001110\",\n          \"gmo_id\": \"GMO_001110\",\n          \"label\":
    \"Cobalt(II) nitrate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q39","label":"2-3
    N KOH","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"ingredients[38].concentration","stored":{"value":"variable","unit":"VARIABLE"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"ingredients[38].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"not_quantified","rationale":"The
    variable titrant amount is appropriate: 2–3 N KOH is used to reach stock pH 6.5,
    not a fixed amount or main-medium pH. Retain normality without inventing molarity.","source_stage":"mineral-stock
    titration","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[3].items[14]","quote":"{\n          \"component_name\":
    \"2-3 N KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\":
    \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q40","label":"Vitamin
    Solution","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"solutions[0].concentration","stored":{"value":"0.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly prints an ml/L receiving dose, not G_PER_L. Preserve its own
    ATCC stock definition; generic names and current linked provider IDs do not authenticate
    equivalent formulations.","source_stage":"main stock receiving dose","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 17-17","quote":"Vitamin Solution (see below)...................0.5 ml/L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[8]","quote":"{\n          \"component_name\":
    \"Vitamin Solution\",\n          \"volume\": 0.5,\n          \"unit\": \"ml/l\",\n          \"reference_media_id\":
    \"M3174\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q41","label":"Reducing Solution","local_fields":[{"path":"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml","field_path":"solutions[1].concentration","stored":{"value":"40","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml","field_path":"solutions[1].concentration","stored":{"value":"40","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary explicitly prints an ml/L receiving dose, not G_PER_L. Preserve its own
    ATCC stock definition; generic names and current linked provider IDs do not authenticate
    equivalent formulations.","source_stage":"main stock receiving dose","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 20-20","quote":"Reducing Solution (see below).................40.0 ml/L","quote_basis":"derivative
    text"},{"evidence_id":"togoM3174","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3174","raw_path":"REVIEW_WORK/batch063/source08-10/togoM3174.raw","raw_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","text_sha256":"7c61d46843f5475ecd61249de912494e47f5cecb86071366c38d44dbc5bcd3a5","accessed_at":"2026-10-28T10:18:42.276479Z","locator":"components[0].items[10]","quote":"{\n          \"component_name\":
    \"Reducing Solution\",\n          \"volume\": 40,\n          \"unit\": \"ml/l\",\n          \"reference_media_id\":
    \"M3174\",\n          \"properties\": [],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q42","label":"Provider6241 Cyanocobalamine","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing
    provider-declared 0.1 g/L and attached exact raw evidence agree. The current source
    also explicitly makes up to 100 ml. This authenticates only solution6241, which
    differs from ATCC1191 vitamins.","source_stage":"provider6241 only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\":
    847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q43","label":"Provider6241 Thiamine HCl","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing
    provider-declared 0.1 g/L and attached exact raw evidence agree. The current source
    also explicitly makes up to 100 ml. This authenticates only solution6241, which
    differs from ATCC1191 vitamins.","source_stage":"provider6241 only","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q44","label":"Provider6241 biotin","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"2000.0","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    source says 200 micrograms and explicitly makes up to 100 ml. Exact dimensional
    calculation: 200 micrograms = 0.0002 g; 0.0002 g / 0.1 L = 0.002 g/L, not 2000
    g/L. This is that provider stock only and must not replace the ATCC ten-vitamin
    formula.","source_stage":"provider6241 explicit final stock","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q45","label":"Provider6241 water","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"Preserve
    make-up water to 100 ml final stock. 1000 PERCENT_V_V is unsupported; a makeup
    instruction does not establish the actual volume of water added.","source_stage":"provider6241
    makeup","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q46","label":"Provider3892 NaOH","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"composition[0].concentration","stored":{"value":"1000.0","unit":"PERCENT_V_V"}}],"decision":"correct","rationale":"The
    provider gives 200 ml of 0.2 N NaOH, not 1000 PERCENT_V_V. Preserve volume and
    normality as distinct stock inputs; no arbitrary final-volume or molarity inference.","source_stage":"provider3892
    reagent input","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.recipe[0]","quote":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"NaOH\",\n                \"compound_id\":
    256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": \"0.2 N\",\n                \"amount\":
    200,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\":
    null,\n                \"optional\": 0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q47","label":"Provider3892
    Na2S x 9 H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"composition[1].concentration","stored":{"value":"12.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing
    12.5 g/L is explicitly provider-declared and already has an exact attached raw
    claim. This validates that provider stock normalization only; the ATCC recipe
    does not state measured final stock volume and its cysteine hydrate is not explicit.","source_stage":"provider3892
    declared stock rate","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.recipe[1]","quote":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\":
    54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": 52.0439,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q48","label":"Provider3892
    L-Cysteine HCl x H2O","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"composition[2].concentration","stored":{"value":"12.5","unit":"G_PER_L"}}],"decision":"verified","rationale":"Existing
    12.5 g/L is explicitly provider-declared and already has an exact attached raw
    claim. This validates that provider stock normalization only; the ATCC recipe
    does not state measured final stock volume and its cysteine hydrate is not explicit.","source_stage":"provider3892
    declared stock rate","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.recipe[2]","quote":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"L-Cysteine HCl x H2O\",\n                \"compound_id\":
    770,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q49","label":"Obsolete
    provider placeholder solution6241","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The
    See source for composition placeholder is not a real ingredient; a complete provider
    composition is already present. Reconcile placeholder/incomplete-composition metadata
    without deleting supported components or their history.","source_stage":"provider
    metadata placeholder","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data","quote":"{\n        \"id\":
    6241,\n        \"name\": \"Vitamin solution\",\n        \"volume\": 100,\n        \"recipe\":
    [\n            {\n                \"recipe_order\": 2,\n                \"compound\":
    \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 4,\n                \"compound\":
    \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 5,\n                \"compound\":
    \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }\n        ],\n        \"equipment\":
    []\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q50","label":"Obsolete
    provider placeholder solution3892","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"ingredients[0].concentration","stored":{"value":"variable","unit":"VARIABLE"}}],"decision":"correct","rationale":"The
    See source for composition placeholder is not a real ingredient; a complete provider
    composition is already present. Reconcile placeholder/incomplete-composition metadata
    without deleting supported components or their history.","source_stage":"provider
    metadata placeholder","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data","quote":"{\n        \"id\":
    3892,\n        \"name\": \"Reducing solution\",\n        \"volume\": 200,\n        \"recipe\":
    [\n            {\n                \"recipe_order\": 1,\n                \"compound\":
    \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": \"0.2 N\",\n                \"amount\":
    200,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\":
    null,\n                \"optional\": 0\n            },\n            {\n                \"recipe_order\":
    2,\n                \"compound\": \"Na2S x 9 H2O\",\n                \"compound_id\":
    54,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": 52.0439,\n                \"optional\":
    0\n            },\n            {\n                \"recipe_order\": 3,\n                \"compound\":
    \"L-Cysteine HCl x H2O\",\n                \"compound_id\": 770,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 12.5,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }\n        ],\n        \"steps\": [\n            {\n                \"recipe_order\":
    null,\n                \"step\": \"Boil NaOH solution and cool down under a N2-H2
    (95:5) atmosphere, then add Na2S x 9H2O and L-cysteine x HCl x H2O to the solution.
    Autoclave it under a N2-H2 (95:5) atmosphere.\"\n            }\n        ],\n        \"equipment\":
    {\n            \"615\": \"Autoclave\"\n        }\n    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q51","label":"Provider3892
    preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml","field_path":"preparation_notes","stored":"Boil
    NaOH solution and cool down under a N2-H2 (95:5) atmosphere, then add Na2S x 9H2O
    and L-cysteine x HCl x H2O to the solution. Autoclave it under a N2-H2 (95:5)
    atmosphere.\n\nOriginal volume: 200 mL"}],"decision":"evidence_only","rationale":"Retain
    its provider-specific stock preparation and 95:5 atmosphere; do not claim ATCC
    identity merely from a generic stock name. Its 0.2 N input and cysteine monohydrate
    must remain explicit.","source_stage":"provider stock preparation","sources":[{"evidence_id":"solution3892","reference":"https://mediadive.dsmz.de/rest/solution/3892","raw_path":"REVIEW_WORK/batch063/source08-10/solution3892.raw","raw_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","text_sha256":"d70a91ddc61360f40b5faf2f88484cfbf2a25def39cf62e332ec3eacb4aaf268","accessed_at":"2026-10-28T10:18:43.286264Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Boil NaOH solution and cool down under a N2-H2
    (95:5) atmosphere, then add Na2S x 9H2O and L-cysteine x HCl x H2O to the solution.
    Autoclave it under a N2-H2 (95:5) atmosphere.\"\n            }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q52","label":"ATCC main preparation and explicit hazard
    notice","local_fields":[],"decision":"evidence_only","rationale":"The primary
    has staged reduction, 95:5 gas, conditional color observations, sealed vessels
    and 15-minute autoclaving, plus an explicit hydrogen-sulfide hazard notice. Preserve
    the original notice and source stages during transcription; no autoclave temperature,
    pressure or organism growth claim is supplied.","source_stage":"source-only main
    preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 23-34","quote":"A note of caution: This medium contains sodium sulfide,
    and hydrogen\nsulfide production will occur, especially upon prolonged boiling.\nHydrogen
    sulfide is hazardous and preparation of this medium should be\ndone in a chemical
    fume hood.\nBring the medium to a boil while gassing with a mixture of 95% N2,
    5%\nH2. Keep the solution boiling for several minutes until time the color\nturns
    from blue to reddish-pink. Add the reducing solution during\ncontinuous gassing
    and boiling. The pink color should disappear,\nindicating reduction. Boil briefly
    for reduction. Using anaerobic\n(Hungate) technique, dispense the medium in tubes
    flushed with N2/H2 gas\nmixture. Stopper the tubes with butyl rubber, secure and
    autoclave for\n15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q53","label":"ATCC
    reducing-stock preparation","local_fields":[],"decision":"evidence_only","rationale":"The
    stock has its own boil/cool/add/anaerobic-vessel sequence and 15-minute autoclaving.
    This sequence is distinct from main medium preparation; no final stock volume
    is asserted.","source_stage":"source-only reducing preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 36-44","quote":"Reducing Solution:\n0.2 N NaOH.......................200.0
    ml\nNa2S . 9H2O ........................2.5 g\nL-Cysteine . HCl...................2.5
    g\n\nBring the sodium hydroxide solution to a boil and bubble with 95% N2, 5%\nH2
    gas mixture. Allow the solution to cool and add the sodium sulfide\nand cysteine.
    Under anaerobic conditions, tube the solution, stopper\nwith butyl rubber, and
    autoclave for 15 minutes.","quote_basis":"derivative text"}]},{"quantity_id":"q54","label":"ATCC
    vitamins dose and storage","local_fields":[],"decision":"evidence_only","rationale":"The
    explicit 0.05 ml per 100 ml is 0.5 ml/L and agrees with the main table. Retain
    source freeze-or-refrigerate/dark storage without inventing a storage temperature
    or duration.","source_stage":"source-only vitamins preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 17-17","quote":"Vitamin Solution (see below)...................0.5 ml/L","quote_basis":"derivative
    text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 63-65","quote":"Dissolve the vitamins in 500 ml of water. Add 0.05 ml of
    this solution\nper 100 ml of medium. Freeze the vitamin solution or store in a\nrefrigerator
    in the absence of light.","quote_basis":"derivative text"}]},{"quantity_id":"q55","label":"ATCC
    mineral preparation","local_fields":[],"decision":"evidence_only","rationale":"Initial
    500 ml water, 2–3 N titrant, pH 6.5, ordered dissolution and final makeup to 1.0
    L are explicit. These controls belong only to this stock; 0.5 ml per 100 ml equals
    its 5 ml/L receiving dose.","source_stage":"source-only mineral preparation","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 83-87","quote":"Suspend the nitrilotriacetic acid in 500 ml water. Dissolve
    it by\ntitrating with 2-3 N KOH until the pH is stabilized at 6.5. Add the rest\nof
    the ingredients and dissolve in the order they are listed. Finally,\nadjust the
    volume to 1.0 L For 100 ml of medium, use 0.5 ml of the\nmineral elixir.","quote_basis":"derivative
    text"}]},{"quantity_id":"q56","label":"ATCC1190 versus1191 substrate","local_fields":[],"decision":"evidence_only","rationale":"ATCC1191
    replaces the base1190 glucose with filter paper. Do not add the base glucose row
    to this variant. The alternative tube strip has an explicit size and no stated
    tube volume, so it is not converted into g/L.","source_stage":"variant-specific
    substrate","sources":[{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 1-8","quote":"ATCC medium: 1191 Clostridium thermocellum medium (ATCC medium
    1190)\nwith 18.75 g filter paper substituted for the glucose\n\n\nATCC Medium
    1190 (see below) with 18.75 g filter paper substituted for\nthe glucose\nWhen
    preparing tubed medium, Whatman #1 filter paper may be used. In\nthis case, use
    one strip (8 X 70 mm) per tube of broth.","quote_basis":"derivative text"},{"evidence_id":"atcc1191","reference":"https://www.atcc.org/-/media/product-assets/documents/microbial-media-formulations/1/1/9/1/atcc-medium-1191.pdf?rev=ee45c41e11f14bdcb44ffc84735f6331","raw_path":"REVIEW_WORK/batch063/source08-10/atcc1191.raw","raw_sha256":"3226509b558f3fa90e1466ed5a9be5d0fc05db2156dcdec37301890246ef00f3","text_sha256":"6941a1a0c7e58ccbdd232d4d56ee18874b92a3fbda68d7fd56832ed2694463e2","accessed_at":"2026-10-28T10:18:43.798179Z","locator":"atcc1191.txt
    lines 16-16","quote":"Glucose........................................8.0 g/L","quote_basis":"derivative
    text"}]},{"quantity_id":"q57","label":"Provider6241 retained makeup instruction","local_fields":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"preparation_notes","stored":"Make
    up to 100 ml with distilled water.\n\nOriginal volume: 100 mL"}],"decision":"evidence_only","rationale":"The
    existing preparation note accurately retains explicit makeup to 100 ml. Preserve
    it unchanged; the incorrect water concentration is assessed separately in q45.","source_stage":"provider6241
    makeup","sources":[{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.recipe[3]","quote":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","quote_basis":"raw UTF-8"},{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch063/source08-10/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","text_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","accessed_at":"2026-10-28T10:18:43.274206Z","locator":"data.steps[0]","quote":"{\n                \"recipe_order\":
    null,\n                \"step\": \"Make up to 100 ml with distilled water.\"\n            }","quote_basis":"raw
    UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CLOSTRIDIUM_THERMOCELLUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml":null,"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml":null,"data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted CHEBI and provider slots are inventoried with exact current
    raw OLS objects and packaged MIM membership; provider compound IDs are separately
    checked against their exact solution responses. Na2HPO4 dodecahydrate versus anhydrous34683
    is a confirmed mismatch. Thioctic acid versus R-specific30314 remains unresolved
    specificity, not proof of an opposite enantiomer. Other explicit magnesium/cobalt/manganese/copper/zinc/iron/sulfide
    hydrates agree. Generic vitaminB12 correctly remains a class rather than being
    replaced by the provider6241 cyanocobalamin. Missing annotations and no-current-row
    results do not authorize guessed IDs.
  target_ids:
  - CultureMech:009627
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All six exact historical reports and both selected historical parent objects
    were fully read. Four October5 ledgers were zero-checked. The two October7 provider
    reports preserve seven exact recipe objects and four attached provider-rate claims;
    fresh raw digests and quoted content are joined independently, without recreating
    old retrieval timestamps. Those reports intentionally left preparation-dependent
    inputs open. Current cleanup avoids summing unequal duplicates, exact-name migration
    can resolve only a generic name, and current merge compares scientific formulation.
    Append actual evidence-backed curation events; do not overwrite earlier history.
  target_ids:
  - CultureMech:009627
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-009627-stage-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock recipes and mixed-unit water were flattened into the main formulation
  description: Restore ATCC main, reducing, vitamin and mineral stages in the maintained
    owner. Source liquid doses/water are not G_PER_L, vitamin and mineral mg rows
    are not grams per litre of medium, and 501 G_PER_L water adds 500 ml to 1 L from
    different stocks. Keep correctly printed main g/L values unchanged. Mineral final
    makeup is explicit; vitamin/reducing final volumes are not. Current cleanup no
    longer sums unequal duplicates, and current singleton merge preserves its input;
    this is retained historical corruption.
  target_ids:
  - CultureMech:009627
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - atcc1191
  - togoM3174
  - target
  - owner
  - writer-cleanup
  - writer-formulation
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-009627-provider-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The linked vitamin provider is not the ATCC ten-vitamin stock
  description: The current link to mediadive.solution:6241 resolves to three vitamins
    made up to 100 ml, while ATCC1191 defines ten vitamins in 500 ml water. Replace
    the unsupported identity link with the exact ATCC stock representation. Reducing3892
    separately declares cysteine monohydrate whereas ATCC prints cysteine HCl without
    that hydrate; retain this version/form limit rather than asserting equivalence
    from its name. No provider record is rewritten to match an unrelated stock.
  target_ids:
  - CultureMech:009627
  field_paths:
  - solutions[0].term
  - solutions[1].term
  evidence_ids:
  - atcc1191
  - togoM3174
  - solution6241
  - solution3892
  - writer-migration
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-009627-phosphate-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Dodecahydrate phosphate is grounded to anhydrous disodium phosphate
  description: The selected target and owner name Na2HPO4·12H2O, corroborated by ATCC
    and TOGO. CHEBI34683 has anhydrous HO4P.2Na formula and no twelve waters. Reconcile
    the supplied-form mapping using verified exact hydrate evidence; a valid canonical
    label does not make this chemical form correct. Preserve other correctly specific
    hydrates.
  target_ids:
  - CultureMech:009627
  field_paths:
  - ingredients[5].term
  evidence_ids:
  - atcc1191
  - togoM3174
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-009627-preparation
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Exact ATCC preparation and variant controls are absent
  description: Preserve separate main and stock preparation, source hazard notice,
    15-minute sterilization durations, gas composition, vitamin storage and mineral
    pH/makeup. Retain the filter-paper replacement and conditional strip alternative;
    no glucose reintroduction, unstated temperature, final-stock volume or growth
    assertion. Current TOGO stage-aware paths and exact-name migration require source-specific
    reconciliation, not blind rerunning.
  target_ids:
  - CultureMech:009627
  field_paths:
  - preparation_steps
  - sterilization
  - notes
  - solutions
  evidence_ids:
  - atcc1191
  - togoM3174
  - writer-togo
  - writer-migration
  rule_id: review-yaml-record/completeness
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-009627-dependency-units
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Linked provider records retain unresolved concentration and placeholder errors
  description: Within solution6241 only, biotin 200 micrograms made up to 100 ml supports
    0.002 g/L instead of 2000 g/L; water is makeup, not 1000 PERCENT_V_V. In3892,
    200 ml 0.2 N NaOH is not 1000 PERCENT_V_V. Reconcile both placeholder ingredients/incomplete-composition
    flags while retaining four already-supported provider concentration claims. These
    repairs do not authenticate either stock as the ATCC formulation.
  target_ids:
  - CultureMech:009627
  field_paths:
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[2].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::composition[3].concentration
  - data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml::composition[0].concentration
  - data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml::ingredients[0]
  - data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml::ingredients[0]
  evidence_ids:
  - solution6241
  - solution3892
  - old-claims
  - quantities
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml
    role: scoped dependency
- finding_id: f6
  issue_key: culturemech-009627-stereochemical-scope
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Generic thioctic-acid source does not establish the asserted R form
  description: The source prints Thioctic acid without stereochemistry, while primary
    and secondary CHEBI30314 slots encode (R)-lipoic acid. Preserve this as an unresolved
    specificity claim; do not label it the opposite enantiomer or silently choose
    a replacement. Resolve exact supplied form if a narrower mapping is retained.
  target_ids:
  - CultureMech:009627
  field_paths:
  - ingredients[24].term
  - ingredients[24].mediaingredientmech_chebi_term
  evidence_ids:
  - atcc1191
  - togoM3174
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    role: maintained source
actions:
- action_id: a1
  description: Restore ATCC main, reducing, vitamin and mineral stages in the maintained
    owner. Source liquid doses/water are not G_PER_L, vitamin and mineral mg rows
    are not grams per litre of medium, and 501 G_PER_L water adds 500 ml to 1 L from
    different stocks. Keep correctly printed main g/L values unchanged. Mineral final
    makeup is explicit; vitamin/reducing final volumes are not. Current cleanup no
    longer sums unequal duplicates, and current singleton merge preserves its input;
    this is retained historical corruption.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009627
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
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
  description: The current link to mediadive.solution:6241 resolves to three vitamins
    made up to 100 ml, while ATCC1191 defines ten vitamins in 500 ml water. Replace
    the unsupported identity link with the exact ATCC stock representation. Reducing3892
    separately declares cysteine monohydrate whereas ATCC prints cysteine HCl without
    that hydrate; retain this version/form limit rather than asserting equivalence
    from its name. No provider record is rewritten to match an unrelated stock.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009627
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
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
  description: The selected target and owner name Na2HPO4·12H2O, corroborated by ATCC
    and TOGO. CHEBI34683 has anhydrous HO4P.2Na formula and no twelve waters. Reconcile
    the supplied-form mapping using verified exact hydrate evidence; a valid canonical
    label does not make this chemical form correct. Preserve other correctly specific
    hydrates.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009627
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
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
  description: Preserve separate main and stock preparation, source hazard notice,
    15-minute sterilization durations, gas composition, vitamin storage and mineral
    pH/makeup. Retain the filter-paper replacement and conditional strip alternative;
    no glucose reintroduction, unstated temperature, final-stock volume or growth
    assertion. Current TOGO stage-aware paths and exact-name migration require source-specific
    reconciliation, not blind rerunning.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009627
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
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
  description: Within solution6241 only, biotin 200 micrograms made up to 100 ml supports
    0.002 g/L instead of 2000 g/L; water is makeup, not 1000 PERCENT_V_V. In3892,
    200 ml 0.2 N NaOH is not 1000 PERCENT_V_V. Reconcile both placeholder ingredients/incomplete-composition
    flags while retaining four already-supported provider concentration claims. These
    repairs do not authenticate either stock as the ATCC formulation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009627
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
    role: scoped dependency
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_3892_Reducing_solution.yaml
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
  description: The source prints Thioctic acid without stereochemistry, while primary
    and secondary CHEBI30314 slots encode (R)-lipoic acid. Preserve this as an unresolved
    specificity claim; do not label it the opposite enantiomer or silently choose
    a replacement. Resolve exact supplied form if a narrower mapping is retained.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009627
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M3174_Clostridium_thermocellum_medium.yaml
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
- ATCC1191 two-page primary was completely read as text and visually. No organism
  strain, culture performance or optimization is inferred from its title.
- ATCC vitamin stock uses water input without explicit final makeup; reducing stock
  uses a reagent volume without explicit measured final stock volume. Mineral stock
  and main medium have explicit final makeup and must not inherit that uncertainty.
- The 0.1% resazurin basis and generic thioctic-acid stereochemistry remain unresolved;
  normality is retained as printed, not converted.
- Provider6241 and3892 are reviewed under their own source identities. Their data
  are not automatically transferred into the ATCC recipe.
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
