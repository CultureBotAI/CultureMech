# Scientific review: CYC Agar

- Review: 20261028T124242Z-culturemech-008144-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:40:23.322377Z
- Finished UTC: 2026-10-28T12:42:42.350611Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

CYC Agar identity and the maintained water/pH repair are supported by exact NBRC402 and TOGO sources. The generated record is stale, while both layers overstate dry batch masses as final-medium concentrations. Two major and two minor findings cover representation, denominator, attached evidence and append-only writer provenance; no recipe was changed.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch067 index 08
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008144 | data/merge_yaml/merged/CYC_Agar.yaml | generated | cyc_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:008144 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:008144 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:008144 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:008144 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### TOGO M1593 and NBRC402 identity

identity: supported. Targets: CultureMech:008144.

The whole generated target and exact owner denote CYC Agar, and both current sources agree on NBRC402 identity and five components. This is distinct from NBRC1238 CYC Medium; no transfer from that sibling or organism-growth assertion is made.

### Complex solid medium and product scope

consistency: supported. Targets: CultureMech:008144.

The commercial Czapek-Dox mixture, vitamin-assay casamino acids and yeast extract remain opaque branded ingredients. Complex/undefined and SOLID_AGAR classifications are supported; no manufacturer formula, grade equivalence or premix expansion is inferred.

### Original native diagnostics

schema: supported. Targets: CultureMech:008144.

Schema, strict and terms passed; reference validation performed zero checks. These do not resolve amount basis, source truth or generated freshness.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:008144.

10 current concentration fields are covered by 8 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b067-quantity-inventory-v1","target":"data/merge_yaml/merged/CYC_Agar.yaml","quantity_field_count":10,"decisions":[{"quantity_id":"q1","label":"Generated water mass versus owner input volume","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary lists 1 L distilled water, not 1 g/L. Preserve the already repaired owner absolute solvent volume; no density or measured final-medium volume is supplied.","source_stage":"Input solvent","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"Owner retained water volume","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1.0","unit":"L"}}],"decision":"evidence_only","rationale":"The unchanged 1 L matches the primary and TOGO input volume. The owner has root references and source notes but lacks an attached literal claim for this amount.","source_stage":"Input solvent","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"16","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"16.0","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass is supported, but both local G_PER_L assertions and owner per-liter notes exceed the stated basis: the primary lists 1 L water without an explicit make-up-to-final-volume instruction. Preserve the literal batch mass and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\": \"Agar\",\n          \"volume\": 16,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\": \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\": \"Solidifying component\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 35-37","quote":"Agar\n16\ng","quote_basis":"derivative text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"Bacto Yeast Extract (Difco)","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass is supported, but both local G_PER_L assertions and owner per-liter notes exceed the stated basis: the primary lists 1 L water without an explicit make-up-to-final-volume instruction. Preserve the literal batch mass and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\": \"Bacto Yeast Extract (Difco)\",\n          \"volume\": 2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 29-31","quote":"Bacto Yeast Extract (Difco)\n2\ng","quote_basis":"derivative text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Bacto Vitamin Assay Casamino Acids (Difco)","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"6.0","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass is supported, but both local G_PER_L assertions and owner per-liter notes exceed the stated basis: the primary lists 1 L water without an explicit make-up-to-final-volume instruction. Preserve the literal batch mass and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\": \"Bacto Vitamin Assay Casamino Acids (Difco)\",\n          \"volume\": 6,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001169\",\n          \"gmo_id\": \"GMO_001169\",\n          \"label\": \"Difco &amp;trade; Casamino acids, vitamin assay\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 32-34","quote":"Bacto Vitamin Assay Casamino Acids (Difco)\n6\ng","quote_basis":"derivative text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Czapek-Dox Liquid Medium, Modified (OXOID)","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"33.4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"33.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The exact source batch mass is supported, but both local G_PER_L assertions and owner per-liter notes exceed the stated basis: the primary lists 1 L water without an explicit make-up-to-final-volume instruction. Preserve the literal batch mass and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\": \"Czapek-Dox Liquid Medium, Modified (OXOID)\",\n          \"volume\": 33.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001377\",\n          \"gmo_id\": \"GMO_001377\",\n          \"label\": \"Oxoid &amp;trade; Czapek-dox liquid medium, modified\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 26-28","quote":"Czapek-Dox Liquid Medium, Modified (OXOID)\n33.4\ng","quote_basis":"derivative text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Retained owner pH and adjustment description","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"preparation_steps[0].description","stored":"Adjust pH to 7.2."}],"decision":"evidence_only","rationale":"The owner pH 7.2 and adjustment instruction exactly match both current sources and should be retained. The generated target omits them. No acid/base identity or quantity is supplied.","source_stage":"Preparation target pH","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Adjust pH to 7.2\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 41-41","quote":"Adjust pH to 7.2","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"Unspecified final volume, sterilization and adjustment dose","local_fields":[],"decision":"not_quantified","rationale":"Neither exact source establishes measured final volume, sterilization conditions or a titrant dose. No typical values are substituted.","source_stage":"Unquantified source controls","sources":[{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt lines 25-42","quote":"Composition\nCzapek-Dox Liquid Medium, Modified (OXOID)\n33.4\ng\nBacto Yeast Extract (Difco)\n2\ng\nBacto Vitamin Assay Casamino Acids (Difco)\n6\ng\nAgar\n16\ng\nDistilled water\n1\nL\nAdjust pH to 7.2\nComment","quote_basis":"derivative text"},{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\": 2,\n      \"comment\": \"Adjust pH to 7.2\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CYC_Agar.yaml":null,"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: supported. Targets: CultureMech:008144.

All existing water/agar CHEBI and owner yeast-extract FOODON slots match current canonical identifiers and labels. Generic ontology identity does not certify commercial grade; no single chemical ID is imposed on Czapek-Dox premix or casamino acids. Exact current MIM and secondary-link populations are separately reported; no legacy numeric MIM assertion exists in these documents.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:008144.

Both complete October5 reports explicitly left source checks pending and contain no authenticated old external raw. The September11 owner repair is credited for water, pH, source identity and opaque products. Its current fixed-time replacement branch needs append-only follow-up; current code is not historical execution evidence. No new record event is authored.

## Findings

### f1: Generated record omits the maintained water and pH repair

major / open / confirmed; issue key: culturemech-008144-generated-repair-staleness.

The target retains water as 1 G_PER_L, omits the owner pH 7.2/ADJUST_PH step and yeast-extract grounding, and lacks the maintained source references. Credit those existing owner repairs and regenerate from the exact M1593 owner after resolving its remaining denominator and evidence issues. Current singleton merger copies the owner and conservative formulation matching does not license ingredient-only consolidation.

### f2: Mass concentrations overstate the source volume basis

major / open / confirmed; issue key: culturemech-008144-unestablished-final-volume.

Both layers encode the four dry components as G_PER_L; the owner repair explicitly calls their quantities g/L. NBRC402 and TOGO supply batch masses plus 1 L input water, without final-volume makeup. Retain exact supplied masses and product identities while withdrawing or clearly qualifying unsupported final-medium concentrations. The repair writer and current bare-g parsing must not manufacture a final-volume denominator.

### f3: Current source references lack narrow supporting excerpts

minor / open / confirmed; issue key: culturemech-008144-attached-claim-gap.

The owner contains exact references and source notes but no ingredient-level amount excerpts or pH evidence; the target omits the repaired provenance. Attach the inspected literal claims at their exact fields, distinguishing supported batch masses/input volume from unsupported final-medium rates. Root links alone are not full scientific evidence.

### f4: Current repair code replaces a prior curation event

minor / open / confirmed; issue key: culturemech-008144-repair-history-replacement.

The inspected _append_curation_event replaces history[index] for the same curator/action and uses a fixed 2026-09-11 timestamp. This is a current writer behavior, not proof of an unobserved replay. Preserve existing history and make any newly authorized repair append a new actual event instead of rewriting the old one.

## Recommended Actions And Acceptance Checks

### a1

The target retains water as 1 G_PER_L, omits the owner pH 7.2/ADJUST_PH step and yeast-extract grounding, and lacks the maintained source references. Credit those existing owner repairs and regenerate from the exact M1593 owner after resolving its remaining denominator and evidence issues. Current singleton merger copies the owner and conservative formulation matching does not license ingredient-only consolidation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Both layers encode the four dry components as G_PER_L; the owner repair explicitly calls their quantities g/L. NBRC402 and TOGO supply batch masses plus 1 L input water, without final-volume makeup. Retain exact supplied masses and product identities while withdrawing or clearly qualifying unsupported final-medium concentrations. The repair writer and current bare-g parsing must not manufacture a final-volume denominator.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

The owner contains exact references and source notes but no ingredient-level amount excerpts or pH evidence; the target omits the repaired provenance. Attach the inspected literal claims at their exact fields, distinguishing supported batch masses/input volume from unsupported final-medium rates. Root links alone are not full scientific evidence.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The inspected _append_curation_event replaces history[index] for the same curator/action and uses a fixed 2026-09-11 timestamp. This is a current writer behavior, not proof of an unobserved replay. Preserve existing history and make any newly authorized repair append a new actual event instead of rewriting the old one.

- Confirm a newly authorized repair preserves every existing event byte-equivalently and appends a new actual-time event; unchanged idempotent runs must not relabel history.
- Do not modify the current recipe history merely to demonstrate this review finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| togoM1593 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593; REVIEW_WORK/batch067/source07-08-10/togoM1593.json; exact original raw/text/hash/time metadata | context_only | Exact declared TOGO source; M1148 trace elements and M190 vitamin subsection only for07, parent receiving doses excluded. |
| nbrc402 | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402; REVIEW_WORK/batch067/source07-08-10/nbrc402.json; exact original raw/text/hash/time metadata | context_only | 08 exact recorded primary NBRC route. |
| target | data/merge_yaml/merged/CYC_Agar.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| report-17 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYC_Agar.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-18 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch067/record08/historical-reading.json; Complete lossless reader | context_only | Exact original documents and derivative historical report scopes; no historical execution inferred. |
| historical-selected-parent-rows | REVIEW_WORK/batch067/record08/historical-selected-parent-rows.json; Complete lossless reader | context_only | Exact original documents and derivative historical report scopes; no historical execution inferred. |
| complete-document-reader | REVIEW_WORK/batch067/record08/complete-document-reader.json; Complete lossless reader | context_only | Exact original documents and derivative historical report scopes; no historical execution inferred. |
| writer-repair | scripts/repair_togo_m1593_score15.py; _component, INGREDIENTS, _ensure_target, _append_curation_event, repair_record | context_only | Full source read: exact identity/signature gates, water L and pH repair, opaque commercial components, but unproven per-liter notes and replacement of matching curation event with a fixed historical timestamp. |
| writer-togo | src/culturemech/import/togo_importer.py; _ingredient_from_item, _extract_primary_components, _parse_unit, _extract_ph | context_only | Current parser separates primary sections from stocks and maps L to L; bare g still maps to G_PER_L without independent final-volume proof. Current source is not historical execution proof. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377; REVIEW_WORK/batch067/source07-08-10/chebi15377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509; REVIEW_WORK/batch067/source07-08-10/chebi2509.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| foodon03315426 | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315426; REVIEW_WORK/batch067/source07-08-10/foodon03315426.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology ID, canonical label, definition, formula and synonyms; source form assessed separately. |
| quantities | REVIEW_WORK/batch067/record08/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch067/record08/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch067/record08/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch067/record08/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch067/record08/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch067/record08/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch067/record08/existing-claim-authentication.json; Complete sidecar | supports | Existing literal and raw-digest matches; current content authentication is separate from original retrieval provenance. |
| check-schema | REVIEW_WORK/batch067/record08/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch067/record08/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch067/record08/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch067/record08/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Manufacturer composition of the named commercial premix is not established or expanded; this review assesses the exact source-listed product as an opaque component.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T124242Z-culturemech-008144-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: CYC Agar'
started_at: '2026-10-28T12:40:23.322377Z'
finished_at: '2026-10-28T12:42:42.350611Z'
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
summary: CYC Agar identity and the maintained water/pH repair are supported by exact
  NBRC402 and TOGO sources. The generated record is stale, while both layers overstate
  dry batch masses as final-medium concentrations. Two major and two minor findings
  cover representation, denominator, attached evidence and append-only writer provenance;
  no recipe was changed.
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
  - path: data/merge_yaml/merged/CYC_Agar.yaml
    sha256: 9cf61c40826db01e041c4ddb78ab1adb4a366f99a24d8572c8deceb9d09fa48c
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
    sha256: 910841e72207b5326593bd680ba9842c330ef36a2a16eaa34a48710f16cdebc7
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYC_Agar.md
    sha256: ddf3c8cb36c73fa49e61f4d8bffcb69a3159e75815b5b5fb7de23baf81181365
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.md
    sha256: ca3b10c63bc49af2a6df721864b9028efa5fb85188d314f8ec570c5aace7f816
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
  - path: scripts/repair_extraction_input_boundaries.py
    sha256: 6cf990762220c590e897731d91aafe229781c57fd707d4941ac1b37c20b125eb
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/repair_reviewed_medium_stock_boundaries.py
    sha256: fafff4038667c35c62bc6c146996d89f67c724fd3d40d3c9f4c0bc320bb599da
    role: context
  - path: scripts/repair_togo_m1593_score15.py
    sha256: 197f65676de5cfa61126805c57ac09fdb2c33c92e51ae354405323af3d844929
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
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
  selection: Authoritative batch067 index 08
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008144
targets:
- target_id: CultureMech:008144
  path: data/merge_yaml/merged/CYC_Agar.yaml
  label: cyc_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
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
  - CultureMech:008144
  command: just validate-schema data/merge_yaml/merged/CYC_Agar.yaml
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
  - CultureMech:008144
  command: just validate-strict data/merge_yaml/merged/CYC_Agar.yaml --out REVIEW_WORK/batch067/record08/strict.tsv
    --workers 1 --quiet
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
  - CultureMech:008144
  command: just validate-terms data/merge_yaml/merged/CYC_Agar.yaml
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
  - CultureMech:008144
  command: just validate-references data/merge_yaml/merged/CYC_Agar.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: togoM1593
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593
  accessed_at: '2026-10-28T12:40:20.267783Z'
  locator: REVIEW_WORK/batch067/source07-08-10/togoM1593.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact declared TOGO source; M1148 trace elements and M190 vitamin subsection
    only for07, parent receiving doses excluded.
  snapshot_sha256: 6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2
- evidence_id: nbrc402
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402
  accessed_at: '2026-10-28T12:40:21.543273Z'
  locator: REVIEW_WORK/batch067/source07-08-10/nbrc402.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: 08 exact recorded primary NBRC route.
  snapshot_sha256: 55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CYC_Agar.yaml
  locator: Complete file
  accessed_at: '2026-10-28T12:42:42.324582Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: 9cf61c40826db01e041c4ddb78ab1adb4a366f99a24d8572c8deceb9d09fa48c
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
  locator: Complete file
  accessed_at: '2026-10-28T12:42:42.324778Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 910841e72207b5326593bd680ba9842c330ef36a2a16eaa34a48710f16cdebc7
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T12:42:42.324810Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T12:42:42.325144Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T12:42:42.325171Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T12:42:42.325194Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: report-17
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CYC_Agar.md
  locator: Complete report
  accessed_at: '2026-10-28T12:42:42.325222Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ddf3c8cb36c73fa49e61f4d8bffcb69a3159e75815b5b5fb7de23baf81181365
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.md
  locator: Complete report
  accessed_at: '2026-10-28T12:42:42.325247Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: ca3b10c63bc49af2a6df721864b9028efa5fb85188d314f8ec570c5aace7f816
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/historical-reading.json
  locator: Complete lossless reader
  accessed_at: '2026-10-28T12:42:42.325618Z'
  support: context_only
  summary: Exact original documents and derivative historical report scopes; no historical
    execution inferred.
  snapshot_sha256: aff3ca08c6864d1222a468fce699f63f474a0b59a29c482496a0adab209e97fb
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/historical-selected-parent-rows.json
  locator: Complete lossless reader
  accessed_at: '2026-10-28T12:42:42.325657Z'
  support: context_only
  summary: Exact original documents and derivative historical report scopes; no historical
    execution inferred.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/complete-document-reader.json
  locator: Complete lossless reader
  accessed_at: '2026-10-28T12:42:42.325692Z'
  support: context_only
  summary: Exact original documents and derivative historical report scopes; no historical
    execution inferred.
  snapshot_sha256: 735753234f5f0e9ba07d12777afb751b2ccc227795a316eb90a63bba88474a90
- evidence_id: writer-repair
  kind: record_content
  reference: scripts/repair_togo_m1593_score15.py
  locator: _component, INGREDIENTS, _ensure_target, _append_curation_event, repair_record
  accessed_at: '2026-10-28T12:42:42.325717Z'
  support: context_only
  summary: 'Full source read: exact identity/signature gates, water L and pH repair,
    opaque commercial components, but unproven per-liter notes and replacement of
    matching curation event with a fixed historical timestamp.'
  snapshot_sha256: 197f65676de5cfa61126805c57ac09fdb2c33c92e51ae354405323af3d844929
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _ingredient_from_item, _extract_primary_components, _parse_unit, _extract_ph
  accessed_at: '2026-10-28T12:42:42.325743Z'
  support: context_only
  summary: Current parser separates primary sections from stocks and maps L to L;
    bare g still maps to G_PER_L without independent final-volume proof. Current source
    is not historical execution proof.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15377
  accessed_at: '2026-10-28T12:40:22.154049Z'
  locator: REVIEW_WORK/batch067/source07-08-10/chebi15377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: a5ab66402b598c137daa8e5c8ba95811f1619db3e0f8b4f9bd0214161bafa0fe
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:2509
  accessed_at: '2026-10-28T12:40:23.402907Z'
  locator: REVIEW_WORK/batch067/source07-08-10/chebi2509.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: e3f17ac3223021a957a5e3fffb5b118a0854f9ddbc537f51f70dd61ae23ff7a7
- evidence_id: foodon03315426
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?obo_id=FOODON:03315426
  accessed_at: '2026-10-28T12:40:27.217569Z'
  locator: REVIEW_WORK/batch067/source07-08-10/foodon03315426.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Exact current ontology ID, canonical label, definition, formula and synonyms;
    source form assessed separately.
  snapshot_sha256: 7812dff5a532367bf78b3a0fa93571cc657e52ec5f4b86f296a4e245aa75ba9b
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:42:42.350006Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: e1fc27676fde624d5394e1efc61be5d10b222c4b47ad2668352464aa41a33daf
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:42:42.350043Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: eb60cf21a0ef76226f6935c60b66e5fae2ed9d222b702d370ac53b54e0f7e445
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:42:42.350074Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 6ba3c6d3f84ba5aede13d4d131a91ba36e1e6e03fc13879bcaad76bb0371ee5b
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:42:42.350103Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 6058e01a9959afcb4e4147955b3633b93ff0aea254abf838027e7b3a635d9610
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:42:42.350130Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: cc2ead39c4f9cb834f94d0de97ec079a73c96615f7772d0864184bb62445e64f
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:42:42.350151Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 8acb88337bc1c87d00e7d3649ee54dd846283c1d0ece80d32ead196bd00ed5ce
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch067/record08/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T12:42:42.350170Z'
  support: supports
  summary: Existing literal and raw-digest matches; current content authentication
    is separate from original retrieval provenance.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch067/record08/schema-result.json
  accessed_at: '2026-10-28T12:40:24.332666Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 2feddbcdf6dd0073cc2f20bf5f252f6727362f99a620cf984ef6e7e94b6b8529
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch067/record08/strict-result.json
  accessed_at: '2026-10-28T12:40:25.260772Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 29c77e1847bd091f4263765f1e2755e79a3356af1ae15543132d85166fc5b908
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch067/record08/terms-result.json
  accessed_at: '2026-10-28T12:40:26.265773Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: c8a5622925ae964dc6a8eefcbe53ccef194db08790937db93b29bae41769cfc3
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch067/record08/references-result.json
  accessed_at: '2026-10-28T12:40:26.908527Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 96566f1fde1cdeec6928e96d0c8fe6ce24e7bd9ad0269c5d75aa2aa67cbb1b80
assessments:
- assessment_id: identity
  area: identity
  topic: TOGO M1593 and NBRC402 identity
  outcome: supported
  summary: The whole generated target and exact owner denote CYC Agar, and both current
    sources agree on NBRC402 identity and five components. This is distinct from NBRC1238
    CYC Medium; no transfer from that sibling or organism-growth assertion is made.
  target_ids:
  - CultureMech:008144
  evidence_ids:
  - target
  - owner
  - togoM1593
  - nbrc402
- assessment_id: classification
  area: consistency
  topic: Complex solid medium and product scope
  outcome: supported
  summary: The commercial Czapek-Dox mixture, vitamin-assay casamino acids and yeast
    extract remain opaque branded ingredients. Complex/undefined and SOLID_AGAR classifications
    are supported; no manufacturer formula, grade equivalence or premix expansion
    is inferred.
  target_ids:
  - CultureMech:008144
  evidence_ids:
  - target
  - owner
  - nbrc402
  - togoM1593
- assessment_id: native
  area: schema
  topic: Original native diagnostics
  outcome: supported
  summary: Schema, strict and terms passed; reference validation performed zero checks.
    These do not resolve amount basis, source truth or generated freshness.
  target_ids:
  - CultureMech:008144
  evidence_ids:
  - target
  - owner
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 10 current concentration fields are covered by 8 decisions, including unchanged
    support and explicit source-only conditions.
  target_ids:
  - CultureMech:008144
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b067-quantity-inventory-v1","target":"data/merge_yaml/merged/CYC_Agar.yaml","quantity_field_count":10,"decisions":[{"quantity_id":"q1","label":"Generated
    water mass versus owner input volume","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary lists 1 L distilled water, not 1 g/L. Preserve the already repaired owner
    absolute solvent volume; no density or measured final-medium volume is supplied.","source_stage":"Input
    solvent","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q2","label":"Owner
    retained water volume","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"1.0","unit":"L"}}],"decision":"evidence_only","rationale":"The
    unchanged 1 L matches the primary and TOGO input volume. The owner has root references
    and source notes but lacks an attached literal claim for this amount.","source_stage":"Input
    solvent","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[0]","quote":"{\n          \"component_name\":
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
    media\"\n            }\n          ]\n        }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q3","label":"Agar","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"16","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"16.0","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass is supported, but both local G_PER_L assertions and owner
    per-liter notes exceed the stated basis: the primary lists 1 L water without an
    explicit make-up-to-final-volume instruction. Preserve the literal batch mass
    and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass
    added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[1]","quote":"{\n          \"component_name\":
    \"Agar\",\n          \"volume\": 16,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001007\",\n          \"gmo_id\": \"GMO_001007\",\n          \"label\":
    \"Agar\",\n          \"properties\": [],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000048\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000048\",\n              \"label\":
    \"Solidifying component\"\n            }\n          ]\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 35-37","quote":"Agar\n16\ng","quote_basis":"derivative text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q4","label":"Bacto
    Yeast Extract (Difco)","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[1].concentration","stored":{"value":"2.0","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass is supported, but both local G_PER_L assertions and owner
    per-liter notes exceed the stated basis: the primary lists 1 L water without an
    explicit make-up-to-final-volume instruction. Preserve the literal batch mass
    and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass
    added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[2]","quote":"{\n          \"component_name\":
    \"Bacto Yeast Extract (Difco)\",\n          \"volume\": 2,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\":
    \"GMO_001018\",\n          \"label\": \"Bacto &trade; Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 29-31","quote":"Bacto Yeast Extract (Difco)\n2\ng","quote_basis":"derivative
    text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q5","label":"Bacto
    Vitamin Assay Casamino Acids (Difco)","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[3].concentration","stored":{"value":"6","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[2].concentration","stored":{"value":"6.0","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass is supported, but both local G_PER_L assertions and owner
    per-liter notes exceed the stated basis: the primary lists 1 L water without an
    explicit make-up-to-final-volume instruction. Preserve the literal batch mass
    and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass
    added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[3]","quote":"{\n          \"component_name\":
    \"Bacto Vitamin Assay Casamino Acids (Difco)\",\n          \"volume\": 6,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001169\",\n          \"gmo_id\":
    \"GMO_001169\",\n          \"label\": \"Difco &trade; Casamino acids, vitamin
    assay\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 32-34","quote":"Bacto Vitamin Assay Casamino Acids (Difco)\n6\ng","quote_basis":"derivative
    text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q6","label":"Czapek-Dox
    Liquid Medium, Modified (OXOID)","local_fields":[{"path":"data/merge_yaml/merged/CYC_Agar.yaml","field_path":"ingredients[4].concentration","stored":{"value":"33.4","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ingredients[0].concentration","stored":{"value":"33.4","unit":"G_PER_L"}}],"decision":"unsupported","rationale":"The
    exact source batch mass is supported, but both local G_PER_L assertions and owner
    per-liter notes exceed the stated basis: the primary lists 1 L water without an
    explicit make-up-to-final-volume instruction. Preserve the literal batch mass
    and commercial grade; do not invent final volume or decompose the premix.","source_stage":"Mass
    added to listed solvent input","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"components[0].items[4]","quote":"{\n          \"component_name\":
    \"Czapek-Dox Liquid Medium, Modified (OXOID)\",\n          \"volume\": 33.4,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001377\",\n          \"gmo_id\":
    \"GMO_001377\",\n          \"label\": \"Oxoid &trade; Czapek-dox liquid medium,
    modified\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }","quote_basis":"raw
    UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 26-28","quote":"Czapek-Dox Liquid Medium, Modified (OXOID)\n33.4\ng","quote_basis":"derivative
    text"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 38-40","quote":"Distilled water\n1\nL","quote_basis":"derivative text"}]},{"quantity_id":"q7","label":"Retained
    owner pH and adjustment description","local_fields":[{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml","field_path":"preparation_steps[0].description","stored":"Adjust
    pH to 7.2."}],"decision":"evidence_only","rationale":"The owner pH 7.2 and adjustment
    instruction exactly match both current sources and should be retained. The generated
    target omits them. No acid/base identity or quantity is supplied.","source_stage":"Preparation
    target pH","sources":[{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Adjust pH to 7.2\"\n    }","quote_basis":"raw UTF-8"},{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 41-41","quote":"Adjust pH to 7.2","quote_basis":"derivative text"}]},{"quantity_id":"q8","label":"Unspecified
    final volume, sterilization and adjustment dose","local_fields":[],"decision":"not_quantified","rationale":"Neither
    exact source establishes measured final volume, sterilization conditions or a
    titrant dose. No typical values are substituted.","source_stage":"Unquantified
    source controls","sources":[{"evidence_id":"nbrc402","reference":"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=402","raw_path":"REVIEW_WORK/batch067/source07-08-10/nbrc402.raw","raw_sha256":"55e50ee9a97b6f48d6c89b1032166ca8ff829fe35ae8f112886b21542a737f78","text_sha256":"64b9d2573eaac1f56ac5318ef2224b2546586c1ba2ba0c53a1c9537953cbefc8","accessed_at":"2026-10-28T12:40:21.543273Z","locator":"nbrc402.txt
    lines 25-42","quote":"Composition\nCzapek-Dox Liquid Medium, Modified (OXOID)\n33.4\ng\nBacto
    Yeast Extract (Difco)\n2\ng\nBacto Vitamin Assay Casamino Acids (Difco)\n6\ng\nAgar\n16\ng\nDistilled
    water\n1\nL\nAdjust pH to 7.2\nComment","quote_basis":"derivative text"},{"evidence_id":"togoM1593","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1593","raw_path":"REVIEW_WORK/batch067/source07-08-10/togoM1593.raw","raw_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","text_sha256":"6b1a2a7bffc2a15f64fb466fe791056140f2637da4158184c6aa11e770e62bd2","accessed_at":"2026-10-28T12:40:20.267783Z","locator":"comments[0]","quote":"{\n      \"paragraph_index\":
    2,\n      \"comment\": \"Adjust pH to 7.2\"\n    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/CYC_Agar.yaml":null,"data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: supported
  summary: All existing water/agar CHEBI and owner yeast-extract FOODON slots match
    current canonical identifiers and labels. Generic ontology identity does not certify
    commercial grade; no single chemical ID is imposed on Czapek-Dox premix or casamino
    acids. Exact current MIM and secondary-link populations are separately reported;
    no legacy numeric MIM assertion exists in these documents.
  target_ids:
  - CultureMech:008144
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: Both complete October5 reports explicitly left source checks pending and
    contain no authenticated old external raw. The September11 owner repair is credited
    for water, pH, source identity and opaque products. Its current fixed-time replacement
    branch needs append-only follow-up; current code is not historical execution evidence.
    No new record event is authored.
  target_ids:
  - CultureMech:008144
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
findings:
- finding_id: f1
  issue_key: culturemech-008144-generated-repair-staleness
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Generated record omits the maintained water and pH repair
  description: The target retains water as 1 G_PER_L, omits the owner pH 7.2/ADJUST_PH
    step and yeast-extract grounding, and lacks the maintained source references.
    Credit those existing owner repairs and regenerate from the exact M1593 owner
    after resolving its remaining denominator and evidence issues. Current singleton
    merger copies the owner and conservative formulation matching does not license
    ingredient-only consolidation.
  target_ids:
  - CultureMech:008144
  field_paths:
  - ingredients
  - ph_value
  - preparation_steps
  - references
  - curation_history
  evidence_ids:
  - target
  - owner
  - nbrc402
  - togoM1593
  - writer-repair
  - writer-merger
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-008144-unestablished-final-volume
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Mass concentrations overstate the source volume basis
  description: Both layers encode the four dry components as G_PER_L; the owner repair
    explicitly calls their quantities g/L. NBRC402 and TOGO supply batch masses plus
    1 L input water, without final-volume makeup. Retain exact supplied masses and
    product identities while withdrawing or clearly qualifying unsupported final-medium
    concentrations. The repair writer and current bare-g parsing must not manufacture
    a final-volume denominator.
  target_ids:
  - CultureMech:008144
  field_paths:
  - ingredients
  evidence_ids:
  - target
  - owner
  - nbrc402
  - togoM1593
  - writer-repair
  - writer-togo
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-008144-attached-claim-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Current source references lack narrow supporting excerpts
  description: The owner contains exact references and source notes but no ingredient-level
    amount excerpts or pH evidence; the target omits the repaired provenance. Attach
    the inspected literal claims at their exact fields, distinguishing supported batch
    masses/input volume from unsupported final-medium rates. Root links alone are
    not full scientific evidence.
  target_ids:
  - CultureMech:008144
  field_paths:
  - ingredients
  - ph_value
  - preparation_steps
  - evidence
  evidence_ids:
  - target
  - owner
  - nbrc402
  - togoM1593
  rule_id: review-yaml-record/evidence
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-008144-repair-history-replacement
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Current repair code replaces a prior curation event
  description: The inspected _append_curation_event replaces history[index] for the
    same curator/action and uses a fixed 2026-09-11 timestamp. This is a current writer
    behavior, not proof of an unobserved replay. Preserve existing history and make
    any newly authorized repair append a new actual event instead of rewriting the
    old one.
  target_ids:
  - CultureMech:008144
  field_paths:
  - scripts/repair_togo_m1593_score15.py::_append_curation_event
  evidence_ids:
  - writer-repair
  - owner
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_togo_m1593_score15.py
    role: maintained repair writer
actions:
- action_id: a1
  description: The target retains water as 1 G_PER_L, omits the owner pH 7.2/ADJUST_PH
    step and yeast-extract grounding, and lacks the maintained source references.
    Credit those existing owner repairs and regenerate from the exact M1593 owner
    after resolving its remaining denominator and evidence issues. Current singleton
    merger copies the owner and conservative formulation matching does not license
    ingredient-only consolidation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008144
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
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
  description: Both layers encode the four dry components as G_PER_L; the owner repair
    explicitly calls their quantities g/L. NBRC402 and TOGO supply batch masses plus
    1 L input water, without final-volume makeup. Retain exact supplied masses and
    product identities while withdrawing or clearly qualifying unsupported final-medium
    concentrations. The repair writer and current bare-g parsing must not manufacture
    a final-volume denominator.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008144
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
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
  description: The owner contains exact references and source notes but no ingredient-level
    amount excerpts or pH evidence; the target omits the repaired provenance. Attach
    the inspected literal claims at their exact fields, distinguishing supported batch
    masses/input volume from unsupported final-medium rates. Root links alone are
    not full scientific evidence.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008144
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1593_CYC_Agar.yaml
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
  description: The inspected _append_curation_event replaces history[index] for the
    same curator/action and uses a fixed 2026-09-11 timestamp. This is a current writer
    behavior, not proof of an unobserved replay. Preserve existing history and make
    any newly authorized repair append a new actual event instead of rewriting the
    old one.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:008144
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_togo_m1593_score15.py
    role: maintained repair writer
  acceptance_checks:
  - Confirm a newly authorized repair preserves every existing event byte-equivalently
    and appends a new actual-time event; unchanged idempotent runs must not relabel
    history.
  - Do not modify the current recipe history merely to demonstrate this review finding.
  generator: scripts/repair_togo_m1593_score15.py
limitations:
- Manufacturer composition of the named commercial premix is not established or expanded;
  this review assesses the exact source-listed product as an opaque component.
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
