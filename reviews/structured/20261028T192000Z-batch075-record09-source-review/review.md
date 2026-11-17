# Review Desulfofarcimen medium and its TOGO contributor

- Review: 20261028T192000Z-batch075-record09-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:55:58.742538Z
- Finished UTC: 2026-10-28T19:20:00.387353Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM124 and TOGO M2526 establish identity. Stock constituents and solvents were flattened into the main recipe, quantities have wrong units or unsupported bases, and the vitamin link denotes a different stock. Missing preparation, nickel hydrate grounding and provenance require curation. Existing source-backed stock repairs and current writer improvements are credited. No recipe was changed.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch075 native selection index 09.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009096 | data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml | generated | desulfofarcimen_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009096 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:009096 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:009096 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:009096 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact record and source identity

identity: supported. Targets: CultureMech:009096.

The selected generated record and soleTOGO M2526 maintained contributor shareCultureMech009096 and all scientific fields. Current TOGO points exactly toDSM124. Historical alias000709 names three different contributors and is not the selected target. Standalone4178 and5543 match the relevant stock identities;6241 is a three-vitamin stock and is not the source ten-vitamin formulation.

### Classification and claim boundaries

scope: supported. Targets: CultureMech:009096.

Yeast extract and current DSM/API complex_medium=yes support complex/undefined medium; no gelling agent is specified, consistent with liquid form. Genus classification supports bacterial filing. Cultivation application is generic, without strain-grounded growth claims. Source DSM2925/7213/100382 replacement variants remain separate and do not become base recipe ingredients or growth assertions.

### Retain current source-backed stock repairs

provenance: supported. Targets: CultureMech:009096.

Fresh standalone payloads exactly match all three historical source digests. All21 plan claims and14 current attached evidence entries reconcile to current after hashes. Retain eight SL10 compound rates, three selenium/tungsten rates and its1 L water repair, plus two0.1 g/L rates in the separate6241 stock. HCl, SL10 water,6241 biotin/water and placeholders were explicitly unresolved. Source bytes and plan linkage are authenticated; historical capture times/execution are not.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:009096.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id":"q1","topic":"Main recipe \u2014 Na-resazurin solution (0.1% w/v)","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na-resazurin solution (0.1% w/v)","volume":0.5,"unit":"ml","conc_value":0.1,"conc_unit":"(w/v)","gmo":"http://purl.jp/bio/10/gmo/GMO_001453","gmo_id":"GMO_001453","label":"Sodium resazurin solution","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000051","uri":"http://purl.jp/bio/10/gmo/GMO_000051","label":"Solution"}],"roles":[{"id":"GMO_000055","uri":"http://purl.jp/bio/10/gmo/GMO_000055","label":"pH dependent redox indicator"}]},"literal_excerpt":"{\n          \"component_name\": \"Na-resazurin solution (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\": \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001453\",\n          \"gmo_id\": \"GMO_001453\",\n          \"label\": \"Sodium resazurin solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The source specifies0.5 ml of this stock per listed batch, not0.5 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit. Explicit0.1% w/v means1 g/L stock;0.5 ml supplies0.5 mg sodium resazurin per batch. This arithmetic is not a final medium rate.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[0].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies0.5 ml of this stock per listed batch, not0.5 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit. Explicit0.1% w/v means1 g/L stock;0.5 ml supplies0.5 mg sodium resazurin per batch. This arithmetic is not a final medium rate."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[0].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies0.5 ml of this stock per listed batch, not0.5 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit. Explicit0.1% w/v means1 g/L stock;0.5 ml supplies0.5 mg sodium resazurin per batch. This arithmetic is not a final medium rate."}]},{"quantity_id":"q2","topic":"Main recipe \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled water","volume":1000,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The main source water input is1000 ml (1 L). Current3990 G_PER_L sums this with990/1000/1000 ml from three separate stock recipes. Separate all four solvent amounts; neither this sum nor1 L water is a measured final medium volume.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"3990.0","unit":"G_PER_L"},"decision":"correct","rationale":"The main source water input is1000 ml (1 L). Current3990 G_PER_L sums this with990/1000/1000 ml from three separate stock recipes. Separate all four solvent amounts; neither this sum nor1 L water is a measured final medium volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"3990.0","unit":"G_PER_L"},"decision":"correct","rationale":"The main source water input is1000 ml (1 L). Current3990 G_PER_L sums this with990/1000/1000 ml from three separate stock recipes. Separate all four solvent amounts; neither this sum nor1 L water is a measured final medium volume."}]},{"quantity_id":"q3","topic":"Main recipe \u2014 Yeast extract","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Yeast extract","volume":1,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001003","gmo_id":"GMO_001003","label":"Yeast extract","properties":[{"id":"GMO_000047","uri":"http://purl.jp/bio/10/gmo/GMO_000047","label":"Undefined component"}],"roles":[{"id":"GMO_000042","uri":"http://purl.jp/bio/10/gmo/GMO_000042","label":"Nutrient source"}]},"literal_excerpt":"{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":10,"compound":"Yeast extract","compound_id":16,"amount":1,"unit":"g","g_l":0.997009,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical1 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q4","topic":"Main recipe \u2014 NaCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NaCl","volume":1.17,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001004","gmo_id":"GMO_001004","label":"Sodium chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"NaCl\",\n          \"volume\": 1.17,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":1,"compound":"NaCl","compound_id":43,"amount":1.17,"unit":"g","g_l":1.1665,"mmol_l":19.9607,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1.17,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.1665,\n                        \"mmol_l\": 19.9607,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical1.17 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored_value":{"value":"1.17","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1.17 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[2].concentration","stored_value":{"value":"1.17","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1.17 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q5","topic":"Main recipe \u2014 CaCl2 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[4]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"CaCl2 x 2 H2O","volume":0.15,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001005","gmo_id":"GMO_001005","label":"Calcium chloride dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"CaCl2 x 2 H2O\",\n          \"volume\": 0.15,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\": \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":4,"compound":"CaCl2 x 2 H2O","compound_id":7,"amount":0.15,"unit":"g","g_l":0.149551,"mmol_l":1.01725,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\": 1.01725,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical0.15 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored_value":{"value":"0.15","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.15 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[3].concentration","stored_value":{"value":"0.15","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.15 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q6","topic":"Main recipe \u2014 KH2PO4","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[5]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"KH2PO4","volume":0.2,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001006","gmo_id":"GMO_001006","label":"Potassium phosphate monobasic","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000038","uri":"http://purl.jp/bio/10/gmo/GMO_000038","label":"Buffer"}]},"literal_excerpt":"{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":6,"compound":"KH2PO4","compound_id":11,"amount":0.2,"unit":"g","g_l":0.199402,"mmol_l":1.46527,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\": 1.46527,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical0.2 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored_value":{"value":"0.2","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.2 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[4].concentration","stored_value":{"value":"0.2","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.2 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q7","topic":"Main recipe \u2014 NH4Cl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[6]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NH4Cl","volume":0.27,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001008","gmo_id":"GMO_001008","label":"Ammonium chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000062","uri":"http://purl.jp/bio/10/gmo/GMO_000062","label":"Nitrogen source"}]},"literal_excerpt":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 0.27,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":5,"compound":"NH4Cl","compound_id":42,"amount":0.27,"unit":"g","g_l":0.269192,"mmol_l":5.03257,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.27,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.269192,\n                        \"mmol_l\": 5.03257,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical0.27 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored_value":{"value":"0.27","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.27 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[5].concentration","stored_value":{"value":"0.27","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.27 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q8","topic":"Main recipe \u2014 MgCl2x 6 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[7]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"MgCl2x 6 H2O","volume":0.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001013","gmo_id":"GMO_001013","label":"Magnesium chloride hexahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"MgCl2x 6 H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\": \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":2,"compound":"MgCl2 x 6 H2O","compound_id":79,"amount":0.4,"unit":"g","g_l":0.398804,"mmol_l":1.96162,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 1.96162,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical0.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[6].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q9","topic":"Main recipe \u2014 Na2S x 9 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[8]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2S x 9 H2O","volume":0.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001014","gmo_id":"GMO_001014","label":"Sodium sulfide nonahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000064","uri":"http://purl.jp/bio/10/gmo/GMO_000064","label":"Reducing agent"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2S x 9 H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":16,"compound":"Na2S x 9 H2O","compound_id":54,"amount":0.4,"unit":"g","g_l":0.398804,"mmol_l":1.66042,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 1.66042,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical0.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[7].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q10","topic":"Main recipe \u2014 KCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[9]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"KCl","volume":0.3,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001017","gmo_id":"GMO_001017","label":"Potassium chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":3,"compound":"KCl","compound_id":61,"amount":0.3,"unit":"g","g_l":0.299103,"mmol_l":4.01211,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 4.01211,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical0.3 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored_value":{"value":"0.3","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.3 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[8].concentration","stored_value":{"value":"0.3","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical0.3 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q11","topic":"Main recipe \u2014 NaHCO3","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[10]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NaHCO3","volume":4.5,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001019","gmo_id":"GMO_001019","label":"Sodium bicarbonate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000038","uri":"http://purl.jp/bio/10/gmo/GMO_000038","label":"Buffer"}]},"literal_excerpt":"{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 4.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":12,"compound":"NaHCO3","compound_id":55,"amount":4.5,"unit":"g","g_l":4.48654,"mmol_l":53.4067,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 4.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.48654,\n                        \"mmol_l\": 53.4067,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical4.5 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored_value":{"value":"4.5","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical4.5 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[9].concentration","stored_value":{"value":"4.5","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical4.5 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q12","topic":"Main recipe \u2014 Na-acetate","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[11]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na-acetate","volume":1.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001031","gmo_id":"GMO_001031","label":"Sodium acetate","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000038","uri":"http://purl.jp/bio/10/gmo/GMO_000038","label":"Buffer"}]},"literal_excerpt":"{\n          \"component_name\": \"Na-acetate\",\n          \"volume\": 1.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\": \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":13,"compound":"Na-acetate","compound_id":23,"amount":1.4,"unit":"g","g_l":1.39581,"mmol_l":17.0151,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 1.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.39581,\n                        \"mmol_l\": 17.0151,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical1.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[10].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q13","topic":"Main recipe \u2014 Na2SO4","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[12]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2SO4","volume":2.84,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001052","gmo_id":"GMO_001052","label":"Sodium sulfate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2SO4\",\n          \"volume\": 2.84,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\": \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":7,"compound":"Na2SO4","compound_id":110,"amount":2.84,"unit":"g","g_l":2.83151,"mmol_l":19.9346,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 2.84,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.83151,\n                        \"mmol_l\": 19.9346,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical2.84 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored_value":{"value":"2.84","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical2.84 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[11].concentration","stored_value":{"value":"2.84","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical2.84 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q14","topic":"Main recipe \u2014 Na-butyrate","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[13]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na-butyrate","volume":1.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001648","gmo_id":"GMO_001648","label":"Sodium butyrate","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"},{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"Na-butyrate\",\n          \"volume\": 1.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001648\",\n          \"gmo_id\": \"GMO_001648\",\n          \"label\": \"Sodium butyrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":14,"compound":"Na-butyrate","compound_id":232,"amount":1.4,"unit":"g","g_l":1.39581,"mmol_l":12.6792,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na-butyrate\",\n                        \"compound_id\": 232,\n                        \"amount\": 1.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.39581,\n                        \"mmol_l\": 12.6792,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The numerical1.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[12].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The numerical1.4 matches the statedg batch input. TOGO does not declare final makeup, so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and a revised vitamin/preparation version; use that denominator only after an explicit source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q15","topic":"Main recipe \u2014 Trace element solution SL-10","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[14]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Trace element solution SL-10","volume":1,"unit":"ml","reference_media_id":"M2526","properties":[],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"Trace element solution SL-10\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2526\",\n          \"properties\": [],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit."}]},{"quantity_id":"q16","topic":"Main recipe \u2014 Selenite-tungstate solution","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[15]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Selenite-tungstate solution","volume":1,"unit":"ml","reference_media_id":"M2526","properties":[],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"Selenite-tungstate solution\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2526\",\n          \"properties\": [],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[2].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[2].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit."}]},{"quantity_id":"q17","topic":"Main recipe \u2014 Vitamin solution","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[16]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Vitamin solution","volume":10,"unit":"ml","reference_media_id":"M2526","properties":[],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"Vitamin solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M2526\",\n          \"properties\": [],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The source specifies10 ml of this stock per listed batch, not10 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit. TOGO uses10 ml of a ten-vitamin1x stock; current DSM uses1 ml of the corresponding10x stock. On their nominal1 L stock basis these supply equal vitamin masses, so this is not a tenfold dose error. Different liquid additions/preparation versions remain distinct. Linked6241 is a different three-vitamin stock and cannot supply either formulation.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[3].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies10 ml of this stock per listed batch, not10 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit. TOGO uses10 ml of a ten-vitamin1x stock; current DSM uses1 ml of the corresponding10x stock. On their nominal1 L stock basis these supply equal vitamin masses, so this is not a tenfold dose error. Different liquid additions/preparation versions remain distinct. Linked6241 is a different three-vitamin stock and cannot supply either formulation."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[3].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The source specifies10 ml of this stock per listed batch, not10 G_PER_L. Preserve the addition volume, separate stock strength and composition, and keep source version/stage explicit. TOGO uses10 ml of a ten-vitamin1x stock; current DSM uses1 ml of the corresponding10x stock. On their nominal1 L stock basis these supply equal vitamin masses, so this is not a tenfold dose error. Different liquid additions/preparation versions remain distinct. Linked6241 is a different three-vitamin stock and cannot supply either formulation."}]},{"quantity_id":"q18","topic":"Main recipe \u2014 N2","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[17]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"N2","conc_value":100,"conc_unit":"%","gmo":"http://purl.jp/bio/10/gmo/GMO_002261","gmo_id":"GMO_002261","label":"Nitrogen gas","properties":[{"id":"GMO_000077","uri":"http://purl.jp/bio/10/gmo/GMO_000077","label":"Gas"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"N2\",\n          \"conc_value\": 100,\n          \"conc_unit\": \"%\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"evidence_only","rationale":"Gas is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100% N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into a main-medium nutrient concentration.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100% N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into a main-medium nutrient concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[13].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100% N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into a main-medium nutrient concentration."}]},{"quantity_id":"q19","topic":"Main recipe \u2014 Carbon dioxide gas","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[18]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Carbon dioxide gas","gmo":"http://purl.jp/bio/10/gmo/GMO_002260","gmo_id":"GMO_002260","label":"Carbon dioxide gas","properties":[{"id":"GMO_000077","uri":"http://purl.jp/bio/10/gmo/GMO_000077","label":"\u30ac\u30b9"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\": \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"\u30ac\u30b9\"\n            }\n          ],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"evidence_only","rationale":"Gas is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100% N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into a main-medium nutrient concentration.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100% N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into a main-medium nutrient concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[14].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100% N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into a main-medium nutrient concentration."}]},{"quantity_id":"q20","topic":"Trace element solution SL-10 \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled water","volume":990,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"add","rationale":"This990 ml is solvent for the separate Trace element solution SL-10 stock. Represent it within that stock, never in the main3990 G_PER_L sum. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[]},{"quantity_id":"q21","topic":"Trace element solution SL-10 \u2014 Na2MoO4 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2MoO4 x 2 H2O","volume":36,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001011","gmo_id":"GMO_001011","label":"Sodium molybdate dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2MoO4 x 2 H2O\",\n          \"volume\": 36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source36 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored_value":{"value":"36","unit":"G_PER_L"},"decision":"correct","rationale":"The source36 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[15].concentration","stored_value":{"value":"36","unit":"G_PER_L"},"decision":"correct","rationale":"The source36 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q22","topic":"Trace element solution SL-10 \u2014 H3BO3","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"H3BO3","volume":6,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001015","gmo_id":"GMO_001015","label":"Boric acid","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\": 6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\": \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source6 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored_value":{"value":"6","unit":"G_PER_L"},"decision":"correct","rationale":"The source6 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[16].concentration","stored_value":{"value":"6","unit":"G_PER_L"},"decision":"correct","rationale":"The source6 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q23","topic":"Trace element solution SL-10 \u2014 MnCl2 x 4 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"MnCl2 x 4 H2O","volume":100,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001020","gmo_id":"GMO_001020","label":"Manganese chloride tetrahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"MnCl2 x 4 H2O\",\n          \"volume\": 100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\": \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source100 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored_value":{"value":"100","unit":"G_PER_L"},"decision":"correct","rationale":"The source100 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[17].concentration","stored_value":{"value":"100","unit":"G_PER_L"},"decision":"correct","rationale":"The source100 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q24","topic":"Trace element solution SL-10 \u2014 CoCl2 x 6 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[4]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"CoCl2 x 6 H2O","volume":190,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001021","gmo_id":"GMO_001021","label":"Cobalt dichloride hexahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"CoCl2 x 6 H2O\",\n          \"volume\": 190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\": \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source190 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored_value":{"value":"190","unit":"G_PER_L"},"decision":"correct","rationale":"The source190 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[18].concentration","stored_value":{"value":"190","unit":"G_PER_L"},"decision":"correct","rationale":"The source190 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q25","topic":"Trace element solution SL-10 \u2014 NiCl2 x 6 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[5]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NiCl2 x 6 H2O","volume":24,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001022","gmo_id":"GMO_001022","label":"Nickel chloride hexahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"NiCl2 x 6 H2O\",\n          \"volume\": 24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source24 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. Preserve nickel chloride hexahydrate; the current anhydrous CHEBI mapping is a separate identity defect. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored_value":{"value":"24","unit":"G_PER_L"},"decision":"correct","rationale":"The source24 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. Preserve nickel chloride hexahydrate; the current anhydrous CHEBI mapping is a separate identity defect."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[19].concentration","stored_value":{"value":"24","unit":"G_PER_L"},"decision":"correct","rationale":"The source24 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. Preserve nickel chloride hexahydrate; the current anhydrous CHEBI mapping is a separate identity defect."}]},{"quantity_id":"q26","topic":"Trace element solution SL-10 \u2014 CuCl2 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[6]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"CuCl2 x 2 H2O","volume":2,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001024","gmo_id":"GMO_001024","label":"Copper(II) chloride dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"CuCl2 x 2 H2O\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\": \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source2 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The source2 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[20].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The source2 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q27","topic":"Trace element solution SL-10 \u2014 ZnCl2","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[7]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"ZnCl2","volume":70,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001035","gmo_id":"GMO_001035","label":"Zinc chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\": 70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\": \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source70 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored_value":{"value":"70","unit":"G_PER_L"},"decision":"correct","rationale":"The source70 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[21].concentration","stored_value":{"value":"70","unit":"G_PER_L"},"decision":"correct","rationale":"The source70 mg belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q28","topic":"Trace element solution SL-10 \u2014 HCl (25%; 7.7 M)","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[8]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"HCl (25%; 7.7 M)","volume":10,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001499","gmo_id":"GMO_001499","label":"Hydrochloric acid solution","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000051","uri":"http://purl.jp/bio/10/gmo/GMO_000051","label":"Solution"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating media"}]},"literal_excerpt":"{\n          \"component_name\": \"HCl (25%; 7.7 M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\": \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source10 ml belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. Preserve the10 ml HCl reagent labeled25%;7.7 M. Percentage basis/density is unstated; do not accept the provider2.5 g/L blindly. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The source10 ml belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. Preserve the10 ml HCl reagent labeled25%;7.7 M. Percentage basis/density is unstated; do not accept the provider2.5 g/L blindly."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[22].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The source10 ml belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. Preserve the10 ml HCl reagent labeled25%;7.7 M. Percentage basis/density is unstated; do not accept the provider2.5 g/L blindly."}]},{"quantity_id":"q29","topic":"Trace element solution SL-10 \u2014 FeCl2 x 4 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[9]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"FeCl2 x 4 H2O","volume":1.5,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001548","gmo_id":"GMO_001548","label":"Iron(II) chloride tetrahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"FeCl2 x 4 H2O\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\": \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace element solution SL-10"}},"decision":"correct","rationale":"The source1.5 g belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The explicit source instruction makes SL10 up to1000 ml; this supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored_value":{"value":"1.5","unit":"G_PER_L"},"decision":"correct","rationale":"The source1.5 g belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[23].concentration","stored_value":{"value":"1.5","unit":"G_PER_L"},"decision":"correct","rationale":"The source1.5 g belongs to the Trace element solution SL-10 stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose."}]},{"quantity_id":"q30","topic":"Selenite-tungstate solution \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled water","volume":1000,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate solution"}},"decision":"add","rationale":"This1000 ml is solvent for the separate Selenite-tungstate solution stock. Represent it within that stock, never in the main3990 G_PER_L sum. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[]},{"quantity_id":"q31","topic":"Selenite-tungstate solution \u2014 Na2SeO3 x 5 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2SeO3 x 5 H2O","volume":3,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001046","gmo_id":"GMO_001046","label":"Sodium selenite pentahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2SeO3 x 5 H2O\",\n          \"volume\": 3,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\": \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate solution"}},"decision":"correct","rationale":"The source3 mg belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored_value":{"value":"3","unit":"G_PER_L"},"decision":"correct","rationale":"The source3 mg belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[24].concentration","stored_value":{"value":"3","unit":"G_PER_L"},"decision":"correct","rationale":"The source3 mg belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q32","topic":"Selenite-tungstate solution \u2014 Na2WO4 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2WO4 x 2 H2O","volume":4,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001057","gmo_id":"GMO_001057","label":"Sodium tungstate dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2WO4 x 2 H2O\",\n          \"volume\": 4,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate solution"}},"decision":"correct","rationale":"The source4 mg belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored_value":{"value":"4","unit":"G_PER_L"},"decision":"correct","rationale":"The source4 mg belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[25].concentration","stored_value":{"value":"4","unit":"G_PER_L"},"decision":"correct","rationale":"The source4 mg belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q33","topic":"Selenite-tungstate solution \u2014 NaOH","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NaOH","volume":0.5,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001078","gmo_id":"GMO_001078","label":"Sodium hydroxide","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"NaOH\",\n          \"volume\": 0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\": \"GMO_001078\",\n          \"label\": \"Sodium hydroxide\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": []\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate solution"}},"decision":"correct","rationale":"The source0.5 g belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The source0.5 g belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[26].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The source0.5 g belongs to the Selenite-tungstate solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose."}]},{"quantity_id":"q34","topic":"Vitamin solution \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled water","volume":1000,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"add","rationale":"This1000 ml is solvent for the separate Vitamin solution stock. Represent it within that stock, never in the main3990 G_PER_L sum. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[]},{"quantity_id":"q35","topic":"Vitamin solution \u2014 Biotin","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Biotin","volume":2,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001025","gmo_id":"GMO_001025","label":"Biotin","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[27].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q36","topic":"Vitamin solution \u2014 p-Aminobenzoic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"p-Aminobenzoic acid","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001026","gmo_id":"GMO_001026","label":"4-Aminobenzoic acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[28].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q37","topic":"Vitamin solution \u2014 Thiamine-HCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Thiamine-HCl","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001027","gmo_id":"GMO_001027","label":"Thiamine hydrochloride","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[29].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q38","topic":"Vitamin solution \u2014 Pyridoxine-HCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[4]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Pyridoxine-HCl","volume":10,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001029","gmo_id":"GMO_001029","label":"Pyridoxine hydrochloride","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source10 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The source10 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[30].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The source10 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q39","topic":"Vitamin solution \u2014 Folic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[5]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Folic acid","volume":2,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001033","gmo_id":"GMO_001033","label":"Folic acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[31].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q40","topic":"Vitamin solution \u2014 Vitamin B12","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[6]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Vitamin B12","volume":0.1,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001034","gmo_id":"GMO_001034","label":"Cobalamin","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source0.1 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"correct","rationale":"The source0.1 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[32].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"correct","rationale":"The source0.1 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q41","topic":"Vitamin solution \u2014 Riboflavin","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[7]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Riboflavin","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001037","gmo_id":"GMO_001037","label":"Riboflavin","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[33].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q42","topic":"Vitamin solution \u2014 Nicotinic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[8]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Nicotinic acid","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001038","gmo_id":"GMO_001038","label":"Nicotinic acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[34].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q43","topic":"Vitamin solution \u2014 Lipoic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[9]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Lipoic acid","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001699","gmo_id":"GMO_001699","label":"Lipoic acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple component"}],"roles":[{"id":"GMO_000067","uri":"http://purl.jp/bio/10/gmo/GMO_000067","label":"Growth factor"}]},"literal_excerpt":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[35].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[35].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q44","topic":"Vitamin solution \u2014 D-Ca-pantothenate","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[10]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"D-Ca-pantothenate","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001940","gmo_id":"GMO_001940","label":"D-Calcium pantothenate","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\": \"D-Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001940\",\n          \"gmo_id\": \"GMO_001940\",\n          \"label\": \"D-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[36].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[36].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin solution stock batch, not a root ingredient concentration. Restore stock placement and source units before applying its separately stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale error, independently of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock has tenfold component masses and a tenfold smaller receiving volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q45","topic":"Current DSM Wolin10x comparison \u2014 Biotin","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[0]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":1,"compound":"Biotin","compound_id":46,"amount":20,"unit":"mg","g_l":0.02,"mmol_l":0.0818632,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 20 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q46","topic":"Current DSM Wolin10x comparison \u2014 Folic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[1]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":2,"compound":"Folic acid","compound_id":138,"amount":20,"unit":"mg","g_l":0.02,"mmol_l":0.0453104,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 20 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q47","topic":"Current DSM Wolin10x comparison \u2014 Pyridoxine hydrochloride","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[2]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":3,"compound":"Pyridoxine hydrochloride","compound_id":519,"amount":100,"unit":"mg","g_l":0.1,"mmol_l":0.486287,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 100 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q48","topic":"Current DSM Wolin10x comparison \u2014 Thiamine HCl","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[3]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":4,"compound":"Thiamine HCl","compound_id":1207,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.148236,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q49","topic":"Current DSM Wolin10x comparison \u2014 Riboflavin","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[4]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":5,"compound":"Riboflavin","compound_id":136,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.132837,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q50","topic":"Current DSM Wolin10x comparison \u2014 Nicotinic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[5]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":6,"compound":"Nicotinic acid","compound_id":139,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.406141,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q51","topic":"Current DSM Wolin10x comparison \u2014 Calcium D-(+)-pantothenate","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[6]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":7,"compound":"Calcium D-(+)-pantothenate","compound_id":1512,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.209846,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q52","topic":"Current DSM Wolin10x comparison \u2014 Vitamin B12","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[7]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":8,"compound":"Vitamin B12","compound_id":18,"amount":1,"unit":"mg","g_l":0.001,"mmol_l":0.00073779,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 1 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q53","topic":"Current DSM Wolin10x comparison \u2014 p-Aminobenzoic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[8]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":9,"compound":"p-Aminobenzoic acid","compound_id":47,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.364591,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q54","topic":"Current DSM Wolin10x comparison \u2014 (DL)-alpha-Lipoic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[9]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":10,"compound":"(DL)-alpha-Lipoic acid","compound_id":252,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.24233,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together.","layer_assessments":[]},{"quantity_id":"q55","topic":"Current DSM Wolin10x comparison \u2014 Distilled water","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[10]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":11,"compound":"Distilled water","compound_id":4,"amount":1000,"unit":"ml","optional":0},"literal_excerpt":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current DSM/API Wolin10x stock: 1000 ml in provider1000 ml stock, added at1 ml in current main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration and dose together. This is stock water input, not a main ingredient or measured final-volume evidence by itself.","layer_assessments":[]},{"quantity_id":"q56","topic":"Linked solution4178 \u2014 HCl","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[0]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":1,"compound":"HCl","compound_id":68,"solution":null,"solution_id":null,"condition":null,"attribute":"25%, 7.7 M","amount":10,"unit":"ml","g_l":2.5,"mmol_l":68.5683,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\": 10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\": 68.5683,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"conflict","rationale":"The source gives10 ml HCl25%,7.7 M into a1000 ml stock. The provider2.5 g/L cannot be accepted without reconciling reagent strength:7.7 mol/L \u00d70.010 L gives0.077 mol HCl per stock, about2.8075 g using OLS36.461 g/mol, versus provider2.5 g. Preserve the explicit reagent volume/strength; percentage basis/density is not invented.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[0].concentration","stored_value":{"value":"2.5","unit":"G_PER_L"},"decision":"conflict","rationale":"The source gives10 ml HCl25%,7.7 M into a1000 ml stock. The provider2.5 g/L cannot be accepted without reconciling reagent strength:7.7 mol/L \u00d70.010 L gives0.077 mol HCl per stock, about2.8075 g using OLS36.461 g/mol, versus provider2.5 g. Preserve the explicit reagent volume/strength; percentage basis/density is not invented."}]},{"quantity_id":"q57","topic":"Linked solution4178 \u2014 FeCl2 x 4 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[1]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":2,"compound":"FeCl2 x 4 H2O","compound_id":260,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":1.5,"unit":"g","g_l":1.5,"mmol_l":7.54482,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\": 260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\": \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[1].concentration","stored_value":{"value":"1.5","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q58","topic":"Linked solution4178 \u2014 ZnCl2","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[2]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":3,"compound":"ZnCl2","compound_id":64,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":70,"unit":"mg","g_l":0.07,"mmol_l":0.513573,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\": 64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\": \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[2].concentration","stored_value":{"value":"0.07","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q59","topic":"Linked solution4178 \u2014 MnCl2 x 4 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[3]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":4,"compound":"MnCl2 x 4 H2O","compound_id":36,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":100,"unit":"mg","g_l":0.1,"mmol_l":0.505293,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\": 36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[3].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q60","topic":"Linked solution4178 \u2014 H3BO3","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[4]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":5,"compound":"H3BO3","compound_id":37,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":6,"unit":"mg","g_l":0.006,"mmol_l":0.0970246,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\": 37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\": \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[4].concentration","stored_value":{"value":"0.006","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q61","topic":"Linked solution4178 \u2014 CoCl2 x 6 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[5]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":6,"compound":"CoCl2 x 6 H2O","compound_id":38,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":190,"unit":"mg","g_l":0.19,"mmol_l":1.46335,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\": 38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\": \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[5].concentration","stored_value":{"value":"0.19","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q62","topic":"Linked solution4178 \u2014 CuCl2 x 2 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[6]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":7,"compound":"CuCl2 x 2 H2O","compound_id":39,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":2,"unit":"mg","g_l":0.002,"mmol_l":0.0117314,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\": 39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\": \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[6].concentration","stored_value":{"value":"0.002","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q63","topic":"Linked solution4178 \u2014 NiCl2 x 6 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[7]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":8,"compound":"NiCl2 x 6 H2O","compound_id":40,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":24,"unit":"mg","g_l":0.024,"mmol_l":0.185187,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\": 40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\": \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[7].concentration","stored_value":{"value":"0.024","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q64","topic":"Linked solution4178 \u2014 Na2MoO4 x 2 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[8]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":9,"compound":"Na2MoO4 x 2 H2O","compound_id":9,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":36,"unit":"mg","g_l":0.036,"mmol_l":0.148791,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\": 9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\": \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[8].concentration","stored_value":{"value":"0.036","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q65","topic":"Linked solution4178 \u2014 Distilled water","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[9]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":10,"compound":"Distilled water","compound_id":4,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":990,"unit":"ml","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining salts."}]},"decision":"correct","rationale":"Source990 ml water is a stock batch solvent input, not990% v/v. DSM124 explicitly makes SL10 up to1000 ml after dissolving salts; preserve water input and final makeup as separate facts.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[9].concentration","stored_value":{"value":"990","unit":"PERCENT_V_V"},"decision":"correct","rationale":"Source990 ml water is a stock batch solvent input, not990% v/v. DSM124 explicitly makes SL10 up to1000 ml after dissolving salts; preserve water input and final makeup as separate facts."}]},{"quantity_id":"q66","topic":"Linked solution4178 placeholder","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe complete ingredient inventory","accessed_at":"2026-10-28T18:56:02.143901Z"},"decision":"not_quantified","rationale":"This VARIABLE placeholder is not a source ingredient and contributes no quantity. The complete composition array already defines the stock; reconcile placeholder/incomplete flags during separate stock curation. It is not evidence for an unknown chemical dose.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"not_quantified","rationale":"This VARIABLE placeholder is not a source ingredient and contributes no quantity. The complete composition array already defines the stock; reconcile placeholder/incomplete flags during separate stock curation. It is not evidence for an unknown chemical dose."}]},{"quantity_id":"q67","topic":"Linked solution6241 \u2014 Cyanocobalamine","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[0]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":2,"compound":"Cyanocobalamine","compound_id":847,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":10,"unit":"mg","g_l":0.1,"mmol_l":0.073779,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\": 847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\": 0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make up to 100 ml with distilled water."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium. The existing0.1 g/L is correct for10 mg in100 ml, but authenticates only the separate three-vitamin stock.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium. The existing0.1 g/L is correct for10 mg in100 ml, but authenticates only the separate three-vitamin stock."}]},{"quantity_id":"q68","topic":"Linked solution6241 \u2014 Thiamine HCl","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[1]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":3,"compound":"Thiamine HCl","compound_id":1207,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":10,"unit":"mg","g_l":0.1,"mmol_l":0.296472,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\": 1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\": \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\": 0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make up to 100 ml with distilled water."}]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium. The existing0.1 g/L is correct for10 mg in100 ml, but authenticates only the separate three-vitamin stock.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium. The existing0.1 g/L is correct for10 mg in100 ml, but authenticates only the separate three-vitamin stock."}]},{"quantity_id":"q69","topic":"Linked solution6241 \u2014 Biotin","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[2]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":4,"compound":"Biotin","compound_id":46,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":200,"unit":"\u03bcg","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Biotin\",\n                \"compound_id\": 46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\": \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make up to 100 ml with distilled water."}]},"decision":"correct","rationale":"Source200 micrograms biotin with an explicit100 ml final makeup gives0.0002 g /0.1 L =0.002 g/L. Current2000 G_PER_L is unsupported by six orders of magnitude. The provider g_l is null, explaining why the guarded historical writer left it unresolved; the primary makeup step now permits this manual derivation. This distinct stock must still be unlinked from the selected medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored_value":{"value":"2000.0","unit":"G_PER_L"},"decision":"correct","rationale":"Source200 micrograms biotin with an explicit100 ml final makeup gives0.0002 g /0.1 L =0.002 g/L. Current2000 G_PER_L is unsupported by six orders of magnitude. The provider g_l is null, explaining why the guarded historical writer left it unresolved; the primary makeup step now permits this manual derivation. This distinct stock must still be unlinked from the selected medium."}]},{"quantity_id":"q70","topic":"Linked solution6241 \u2014 Distilled water","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[3]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":5,"compound":"Distilled water","compound_id":4,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":100,"unit":"ml","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make up to 100 ml with distilled water."}]},"decision":"correct","rationale":"The exact source step is make up to100 ml with distilled water, not1000% v/v. Represent solvent as quantity sufficient to the100 ml final stock volume; do not assert that exactly100 ml must be added after solutes. This is the separate three-vitamin stock.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored_value":{"value":"1000.0","unit":"PERCENT_V_V"},"decision":"correct","rationale":"The exact source step is make up to100 ml with distilled water, not1000% v/v. Represent solvent as quantity sufficient to the100 ml final stock volume; do not assert that exactly100 ml must be added after solutes. This is the separate three-vitamin stock."}]},{"quantity_id":"q71","topic":"Linked solution6241 placeholder","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe complete ingredient inventory","accessed_at":"2026-10-28T18:56:02.144038Z"},"decision":"not_quantified","rationale":"This VARIABLE placeholder is not a source ingredient and contributes no quantity. The complete composition array already defines the stock; reconcile placeholder/incomplete flags during separate stock curation. It is not evidence for an unknown chemical dose.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"not_quantified","rationale":"This VARIABLE placeholder is not a source ingredient and contributes no quantity. The complete composition array already defines the stock; reconcile placeholder/incomplete flags during separate stock curation. It is not evidence for an unknown chemical dose."}]},{"quantity_id":"q72","topic":"Linked solution5543 \u2014 NaOH","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[0]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":1,"compound":"NaOH","compound_id":256,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":0.5,"unit":"g","g_l":0.5,"mmol_l":12.5009,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 1,\n                \"compound\": \"NaOH\",\n                \"compound_id\": 256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\": \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[0].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q73","topic":"Linked solution5543 \u2014 Na2SeO3 x 5 H2O","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[1]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":2,"compound":"Na2SeO3 x 5 H2O","compound_id":107,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":3,"unit":"mg","g_l":0.003,"mmol_l":0.0114062,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\": 107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\": \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[1].concentration","stored_value":{"value":"0.003","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q74","topic":"Linked solution5543 \u2014 Na2WO4 x 2 H2O","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[2]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":3,"compound":"Na2WO4 x 2 H2O","compound_id":249,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":4,"unit":"mg","g_l":0.004,"mmol_l":0.0121267,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\": 249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\": \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[2].concentration","stored_value":{"value":"0.004","unit":"G_PER_L"},"decision":"verified","rationale":"Current amount and attached historical evidence agree with the fresh provider recipe and declared stock volume. Retain this stock-specific quantity; it does not establish the amount or rate in the receiving medium."}]},{"quantity_id":"q75","topic":"Linked solution5543 \u2014 Distilled water","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[3]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":4,"compound":"Distilled water","compound_id":4,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":1000,"unit":"ml","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\": 4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\": 4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\": null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\": \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"The existing1 L water is a supported source batch input, already repaired from1000% v/v. Retain its evidence; provider1000 ml stock volume is a distinct stated basis, not inferred from water alone.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[3].concentration","stored_value":{"value":"1","unit":"L"},"decision":"verified","rationale":"The existing1 L water is a supported source batch input, already repaired from1000% v/v. Retain its evidence; provider1000 ml stock volume is a distinct stated basis, not inferred from water alone."}]},{"quantity_id":"q76","topic":"Linked solution5543 placeholder","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe complete ingredient inventory","accessed_at":"2026-10-28T18:56:02.208431Z"},"decision":"not_quantified","rationale":"This VARIABLE placeholder is not a source ingredient and contributes no quantity. The complete composition array already defines the stock; reconcile placeholder/incomplete flags during separate stock curation. It is not evidence for an unknown chemical dose.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"not_quantified","rationale":"This VARIABLE placeholder is not a source ingredient and contributes no quantity. The complete composition array already defines the stock; reconcile placeholder/incomplete flags during separate stock curation. It is not evidence for an unknown chemical dose."}]},{"quantity_id":"q77","topic":"Main preparation and version boundary","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.comments[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"paragraph_index":3,"comment":"Dissolve ingredients (except bicarbonate, vitamins, and sulfide) and sparge medium with 80% N2and 20% CO2 gas mixture for 30 \u2013 45 min to make it anoxic. Add and dissolve bicarbonate, then dispense medium under 80% N2and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The vitamin solution should be sterilized by filtration. Prior to use check pH of complete medium and adjust to 7.0 - 7.2, if necessary."},"literal_excerpt":"{\n      \"paragraph_index\": 3,\n      \"comment\": \"Dissolve ingredients (except bicarbonate, vitamins, and sulfide) and sparge medium with 80% N2and 20% CO2 gas mixture for 30 \u2013 45 min to make it anoxic. Add and dissolve bicarbonate, then dispense medium under 80% N2and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add vitamins and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The vitamin solution should be sterilized by filtration. Prior to use check pH of complete medium and adjust to 7.0 - 7.2, if necessary.\"\n    }"},"decision":"add","rationale":"Restore the selected source procedure, pH7.0\u20137.2, gas stages and vitamin filter sterilization. Current DSM additionally excludes acetate/butyrate from basal heating, adds them later, and adjusts pH7.0 before dispensing. Preserve or explicitly resolve this version difference; do not mix portions silently. No exact autoclave temperature/time or incubation condition is supplied.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"preparation_steps","stored_value":null,"decision":"add","rationale":"Restore the selected source procedure, pH7.0\u20137.2, gas stages and vitamin filter sterilization. Current DSM additionally excludes acetate/butyrate from basal heating, adds them later, and adjusts pH7.0 before dispensing. Preserve or explicitly resolve this version difference; do not mix portions silently. No exact autoclave temperature/time or incubation condition is supplied.","missing":true},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"preparation_steps","stored_value":null,"decision":"add","rationale":"Restore the selected source procedure, pH7.0\u20137.2, gas stages and vitamin filter sterilization. Current DSM additionally excludes acetate/butyrate from basal heating, adds them later, and adjusts pH7.0 before dispensing. Preserve or explicitly resolve this version difference; do not mix portions silently. No exact autoclave temperature/time or incubation condition is supplied.","missing":true}]},{"quantity_id":"q78","topic":"Main pH","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.meta","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"gm":"http://togomedium.org/medium/M2526","name":"Desulfofarcimen Medium","src_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf","ph":"7.0 - 7.2"},"literal_excerpt":"{\n    \"gm\": \"http://togomedium.org/medium/M2526\",\n    \"name\": \"Desulfofarcimen Medium\",\n    \"src_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf\",\n    \"ph\": \"7.0 - 7.2\"\n  }"},"decision":"add","rationale":"The source meta and complete primary recipe state pH7.0\u20137.2. Add a source-linked range using supported schema fields; no strain growth inference is needed.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ph_range","stored_value":null,"decision":"add","rationale":"The source meta and complete primary recipe state pH7.0\u20137.2. Add a source-linked range using supported schema fields; no strain growth inference is needed.","missing":true},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ph_range","stored_value":null,"decision":"add","rationale":"The source meta and complete primary recipe state pH7.0\u20137.2. Add a source-linked range using supported schema fields; no strain growth inference is needed.","missing":true}]},{"quantity_id":"q79","topic":"Current DSM final volume","source":{"evidence_id":"dsm124","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf","raw_path":"REVIEW_WORK/batch075/source09/dsm124.raw","raw_sha256":"a2c8cb38e72919285a4d77c34d34d13655e07cc32c7b07a6ed6ebf353dfec62a","locator":"Page1 heading: Final volume1003 ml","accessed_at":"2026-10-28T18:56:02.654828Z"},"decision":"evidence_only","rationale":"The current DSM124 explicitly declares final1003 ml, and API Main sol.124 volume equals1003. This is an authoritative version-specific denominator, not the arithmetic sum of water and nominal additions and not automatically the older TOGO denominator.","layer_assessments":[]},{"quantity_id":"q80","topic":"SL10 stock makeup","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.comments[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"paragraph_index":6,"comment":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.0 ml."},"literal_excerpt":"{\n      \"paragraph_index\": 6,\n      \"comment\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.0 ml.\"\n    }"},"decision":"add","rationale":"Explicit final makeup to1000 ml supports SL10 stock mass concentrations; retain separately from990 ml initial water and1 ml receiving dose.","layer_assessments":[]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:009096.

Every selected target/owner asserted ID-label slot and the18 scoped dependency composition rows are inventoried against fresh OLS and exact currentMIM rows. Nickel hexahydrate is wrongly mapped to anhydrous34887, and the legacybutyrate secondary link is absent from the current catalog. Calcium pantothenate31345 preservesD stereochemistry. VitaminB12 remains the source-supported broad class rather than an invented cyanocobalamin assignment. Current mapped, rejected and ontology-linked catalog rows are distinguished; no historic identifier validity is inferred.

### History and evidence scope

provenance: concern. Targets: CultureMech:009096.

Complete selected histories have14 target and13 owner events, with only the merge event and generated lineage/fingerprint differing. The selected target and owner historical reports match current bytes and checked0/41 source claims each; the000709 alias report checked0/35 and is a distinct historical merge. All three standalone stock after hashes and source digests match current bytes, with21 historical claims and14 attached excerpts authenticated. Current writer readings are credited without inferring past execution.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:009096.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:009096.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Stock boundaries and units corrupt the receiving recipe

major / open / confirmed; issue key: culturemech-009096-stock-boundaries-and-units-corrupt-the-receiving-recipe.

Both selected layers flatten22 stock solutes into root ingredients and sum four stock/main water inputs to3990 G_PER_L. Milligram stock numbers become G_PER_L, four stock millilitre doses become mass concentrations, and12 basal batch masses lack the TOGO final-volume basis. Correct stock quantities already present in4178/5543 do not authorize root stock concentrations. The exact inventory separates every current field, existing repair and source version.

### f2: Vitamin link points to a different formulation

major / open / confirmed; issue key: culturemech-009096-vitamin-link-points-to-a-different-formulation.

The selected vitamin descriptor links mediadive.solution:6241, a100 ml stock containing only cyanocobalamin, thiamine HCl and biotin. TOGO specifies ten vitamins at1x/10 ml and currentDSM ten vitamins at10x/1 ml. Their matched strength/dose pairs are nominally mass-equivalent; the wrong6241 identity is independent of that version difference.

### f3: Preparation and pH are absent

major / open / confirmed; issue key: culturemech-009096-preparation-and-ph-are-absent.

Both selected layers omit the source pH7.0–7.2 and preparation, including80:20 gas handling, staged bicarbonate and late additions, and vitamin filtration. CurrentDSM moves acetate/butyrate to late additions and adds an initialpH7.0 adjustment relative toTOGO. Current importer already captures comments; persisted records remain stale.

### f4: Nickel hydrate is mapped to anhydrous nickel chloride

major / open / confirmed; issue key: culturemech-009096-nickel-hydrate-is-mapped-to-anhydrous-nickel-chloride.

NiCl2 x6H2O in the source and both selected layers is mapped in primary and secondary slots toCHEBI34887, whose formulaCl2Ni omits six waters. The linkedSL10 stock repeats this mapping. CurrentCHEBI53542 denotes the required hexahydrate. Calcium pantothenateCHEBI31345 is supported: despite its broad label, current synonyms and stereochemical structure identify theD form; no pantothenate correction is asserted.

### f5: High-metal annotation depends on corrupted quantities

minor / open / confirmed; issue key: culturemech-009096-high-metal-annotation-depends-on-corrupted-quantities.

high_metal=true is a quantitative annotation defined by the schema90th-percentile metal threshold. Both selected layers contain mis-scaled undiluted stock amounts, so this annotation lacks a reliable receiving-medium concentration basis. Do not simply flip it tofalse before correcting quantities and rerunning the documented analysis.

### f6: Legacy sodium butyrate linkage remains

minor / open / confirmed; issue key: culturemech-009096-legacy-sodium-butyrate-linkage-remains.

Both layers retainMediaIngredientMech000481 while their primaryCHEBI64103 correctly denotes sodium butyrate. The packaged current catalog has no exact legacy row and provides mappedNa-butyrateCHEBI64103. This is a current secondary-link maintenance gap, not proof that the historical identifier was never valid.

### f7: Selected scientific claims lack attached source evidence

minor / open / confirmed; issue key: culturemech-009096-selected-scientific-claims-lack-attached-source-evidence.

The selected target and maintained contributor contain source URLs and histories but no attached claim evidence or references. Canonical reference validation checked zero references. Older selected-layer reports likewise made zero external checks. Existing source-backed stock claims must be retained at their stock scope while evidence is added for corrected main quantities, source version, preparation and pH. Attach stock-dose and preparation claims in root evidence with exact solution/stage locators; SolutionDescriptor has no evidence slot.

## Recommended Actions And Acceptance Checks

### action1

Restore main versus stock structure, batch solvent inputs, milligram units and stock addition volumes in the maintainedTOGO contributor. Preserve authenticated stock rates and resolve remaining stock-water/HCl issues before reuse. Select and cite a consistent TOGO/currentDSM version; do not transfer1003 ml silently. Credit current importer fixes and review remaining denominator assumptions, then regenerate compatibly.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Replace the incorrect reference with the exact source ten-vitamin definition/link and retain matched strength, dose and version. Do not rewrite the independent6241 stock into the medium vitamin recipe. Resolve all Unknown solution labels and keep the0.1% w/v resazurin strength explicit.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Restore source-linked structuredpH and full preparation from the explicitly chosen source version. Preserve main versus stock atmosphere and sterilization stages. Do not infer autoclave temperature/time or incubation conditions. Regenerate after maintained input curation.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Correct the nickel source-form mapping in the maintained contributor and any reusedSL10 stock. Verify the canonical53542 label; reconcile the rejected currentMIM lexical row separately rather than forcing a secondaryMIM mapping. Preserve the supportedD-calcium pantothenate identity.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

After source-scoped quantities and stock dilution are corrected, recompute the high_metal annotation with its native definition and preserve calculation provenance; withhold a supported scientific interpretation until then.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action6

Reconcile the legacy secondary slot to the exact current supported catalog key/label, preserving the already correct primary chemical identity and append-only provenance. Do not infer a replacement from a fuzzy name match.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action7

The selected target and maintained contributor contain source URLs and histories but no attached claim evidence or references. Canonical reference validation checked zero references. Older selected-layer reports likewise made zero external checks. Existing source-backed stock claims must be retained at their stock scope while evidence is added for corrected main quantities, source version, preparation and pH.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch075/record09/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| dsm124 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf; Exact source identity and scoped formulation/preparation | supports | Both primary PDF pages read visually and as text: current main formula, declared final1003 ml, pH, preparation, three stock tables and three explicitly separate strain variants. |
| togo2526 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526; Exact source identity and scoped formulation/preparation | supports | Complete four-section structured payload read including all44 rows, original DSM124 identity and all comments. Main/stock boundaries and the older ten-vitamin formulation are preserved. |
| api124 | https://mediadive.dsmz.de/rest/medium/124; Exact source identity and scoped formulation/preparation | supports | Current complete medium and all four solution graphs read. Provider main1003 ml and stock1000 ml bases are explicit, not inferred from water. Stock formulation numeric IDs differ from standalone links; identity compared by complete recipe. |
| solution4178 | https://mediadive.dsmz.de/rest/solution/4178; Exact source identity and scoped formulation/preparation | supports | Complete standalone SL10 recipe, volume and preparation read; matches the source stock ingredients, with current HCl-rate and water defects kept distinct from eight correct stock rates. |
| solution5543 | https://mediadive.dsmz.de/rest/solution/5543; Exact source identity and scoped formulation/preparation | supports | Complete standalone selenium/tungsten stock read. All three current rates and1 L batch water are supported at the provider stock scope; these are not receiving-medium rates. |
| solution6241 | https://mediadive.dsmz.de/rest/solution/6241; Exact source identity and scoped formulation/preparation | supports | Complete standalone three-vitamin recipe and100 ml makeup step read. This source authenticates its own stock only and disproves the selected medium vitamin link. |
| lpsn | https://lpsn.dsmz.de/genus/desulfofarcimen; Genus name, classification, status and child taxa | context_only | Current genus page identifies Desulfofarcimen within Bacteria. Nomenclature supports bacterial filing but does not establish a strain or experimental growth claim. |
| dependency-1 | data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml; Complete document | context_only | Complete linked stock identity/composition, current history, references and attached evidence read. Quantities are scoped to this stock; no receiving-medium rate is inherited. |
| dependency-2 | data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml; Complete document | context_only | Complete linked stock identity/composition, current history, references and attached evidence read. Quantities are scoped to this stock; no receiving-medium rate is inherited. |
| dependency-3 | data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml; Complete document | context_only | Complete linked stock identity/composition, current history, references and attached evidence read. Quantities are scoped to this stock; no receiving-medium rate is inherited. |
| history-report-1 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-3000-3500/records/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-2 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-3 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfofarcimen_medium__e24ac714.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-8 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-report-9 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md; Complete document | context_only | Full historical body read or exact sealed prior-root byte reading reused for6241. The selected/owner reports match current hashes and have zero external checks; the000709 alias is a separate historical merged record. Stock curation reports and parent claims are authenticated against fresh provider bytes without certifying historical execution. |
| history-context-1 | reports/yaml_record_review/20260921T150322Z-Artificial_deep_lake_medium.md; Header and stock-related historical scope; fuller independent reading retained separately when available | context_only | Historical dependency-reference context only. This is a report about another medium, not evidence that the selected formulation, stock doses or growth claims are interchangeable. |
| history-context-2 | reports/yaml_record_review/20260922T191917Z-desulfonatronum_par180_medium__7eef7f75.md; Header and stock-related historical scope; fuller independent reading retained separately when available | context_only | Historical dependency-reference context only. This is a report about another medium, not evidence that the selected formulation, stock doses or growth claims are interchangeable. |
| history-context-3 | reports/yaml_record_review/20260923T131040Z-hydrogen_using_marine_methanogen_medium.md; Header and stock-related historical scope; fuller independent reading retained separately when available | context_only | Historical dependency-reference context only. This is a report about another medium, not evidence that the selected formulation, stock doses or growth claims are interchangeable. |
| history-context-4 | reports/yaml_record_review/20260923T131244Z-hydrogen_using_marine_methanogen_medium__931ca534.md; Header and stock-related historical scope; fuller independent reading retained separately when available | context_only | Historical dependency-reference context only. This is a report about another medium, not evidence that the selected formulation, stock doses or growth claims are interchangeable. |
| history-context-5 | reports/yaml_record_review/20260924T090034Z-mmj_thi_medium__4fbd5200.md; Header and stock-related historical scope; fuller independent reading retained separately when available | context_only | Historical dependency-reference context only. This is a report about another medium, not evidence that the selected formulation, stock doses or growth claims are interchangeable. |
| history-context-6 | reports/yaml_record_review/20260924T102523Z-modified_biebl_and_pennings_medium.md; Header and stock-related historical scope; fuller independent reading retained separately when available | context_only | Historical dependency-reference context only. This is a report about another medium, not evidence that the selected formulation, stock doses or growth claims are interchangeable. |
| history-context-7 | reports/yaml_record_review/20260925T153111Z-togo_medium_m3152.md; Header and stock-related historical scope; fuller independent reading retained separately when available | context_only | Historical dependency-reference context only. This is a report about another medium, not evidence that the selected formulation, stock doses or growth claims are interchangeable. |
| history-plan-1 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-3000-3500/plan.json; Selected exact stock path and every associated claim | context_only | Only the exact4178/5543/6241 selected parent row is assessed; all21 claims,14 attached excerpts, source hashes and current after hashes match. Unrelated plan records are not reviewed. |
| history-plan-2 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/plan.json; Selected exact stock path and every associated claim | context_only | Only the exact4178/5543/6241 selected parent row is assessed; all21 claims,14 attached excerpts, source hashes and current after hashes match. Unrelated plan records are not reviewed. |
| history-plan-3 | reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json; Selected exact stock path and every associated claim | context_only | Only the exact4178/5543/6241 selected parent row is assessed; all21 claims,14 attached excerpts, source hashes and current after hashes match. Unrelated plan records are not reviewed. |
| writer-1 | src/culturemech/import/togo_importer.py; Current relevant full function scopes; exact prior root reading proof where reused | context_only | Full current converter previously read by root and exact bytes rechecked: stock sections are preserved, liquid/mg units improved and comments retained. Existing flattened target/owner predate those repairs. Remaining assumed per-litre bases need source-scoped review. |
| writer-2 | src/culturemech/merge/formulation.py; Current relevant full function scopes; exact prior root reading proof where reused | context_only | Exact previously read bytes require compatible scientific fields before evidence union. Similar names/shared sources do not establish formulation equivalence. |
| writer-3 | src/culturemech/merge/merger.py; Current relevant full function scopes; exact prior root reading proof where reused | context_only | Exact previously read bytes: regenerate from corrected maintained contributors while preserving source/variant boundaries. |
| writer-4 | scripts/cleanup_media_quality.py; Current relevant full function scopes; exact prior root reading proof where reused | context_only | Exact previously read bytes do not blindly sum disagreeing duplicate quantities. The persisted3990 water artifact is not evidence of present behavior. |
| writer-5 | scripts/cleanup_recipe_ingredients.py; Current relevant full function scopes; exact prior root reading proof where reused | context_only | Exact previously read bytes preserve/flag conflicting concentration dictionaries instead of source-authenticating them. |
| writer-6 | scripts/review_solution_concentration_evidence.py; Current relevant full function scopes; exact prior root reading proof where reused | context_only | Current full decision/review functions read. Same-source evidence retained; attribute-bearing rows, water with preparation steps, and missing provider g_l remain guarded. This explains bounded historical outcomes but does not prove past execution. |
| writer-7 | scripts/migrate_legacy_mim_to_chebi.py; Current relevant full function scopes; exact prior root reading proof where reused | context_only | Exact previously read bytes. Current catalog and source forms must support any remaining legacy-link update; historical validity is not inferred. |
| ols53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; Exact CHEBI53542 scientific object | supports | Exact current nickel chloride hexahydrate identity and formula 2Cl.6H2O.Ni verified as the source-specific candidate. Packaged MIM row 6703 rejects the exact preferred spelling 'NiCl2 x 6 H2O'; row 6668 maps preferred 'Nickel (II) chloride hexahydrate' and row 6704 maps the former spelling as its synonym. These lexical statuses are distinct; verify the exact selected linkage without treating the chemical identifier as generically rejected. |
| ols15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols64103 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| ols17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch075/record09/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch075/record09/grounding-inventory.json | context_only | All selected target/owner recursive asserted identifier/label slots and explicitly scoped dependency slots; current OLS scientific objects and packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch075/record09/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch075/record09/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch075/record09/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch075/record09/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch075/record09/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch075/record09/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch075/record09/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- CurrentDSM1003 ml is an explicitly declared version-specific denominator; the olderTOGO formulation does not independently declare final medium makeup. Water plus additions is not a measured final volume. Nominal vitamin mass equivalence requires matched1 L stock basis and strength/dose pairs.
- HCl25% has no stated percentage basis/density. Explicit7.7 M and10 ml support a molar input; the provider2.5 g/L requires reconciliation. No invented density or blanket percentage conversion is used.
- The three linked solutions are scoped dependencies, not additional review targets.6241 remains a different stock even if its own quantities are corrected. Historical reports about other media do not establish formulation equivalence.
- No strain-specific growth claim or experimental optimization is inferred. CurrentDSM strain replacement instructions remain separate variants. No recipe, source file, identifier or generated page was changed.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation or publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T192000Z-batch075-record09-source-review
kind: record
repository: CultureBotAI/CultureMech
title: Review Desulfofarcimen medium and its TOGO contributor
started_at: '2026-10-28T18:55:58.742538Z'
finished_at: '2026-10-28T19:20:00.387353Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: DSM124 and TOGO M2526 establish identity. Stock constituents and solvents
  were flattened into the main recipe, quantities have wrong units or unsupported
  bases, and the vitamin link denotes a different stock. Missing preparation, nickel
  hydrate grounding and provenance require curation. Existing source-backed stock
  repairs and current writer improvements are credited. No recipe was changed.
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
  - path: data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml
    sha256: 279575a6d4a4e5bb7c3c9014c8b8d9dbd8c315034d3445f47527953dfdf2b4f3
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    sha256: 13db63e34297a1249c7945fe7d3377b73875e1db2936d87eaeca78e096f1196e
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    sha256: 34d1e5dcc119569d07097d867f9a50cd44edc797d2c1328ccc4cd2be47a6a0fa
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
    sha256: 0d875aeaae44d83149565716773f50c7d2d1abadb818a0154802ef980d71900a
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3000-3500/plan.json
    sha256: afdfbbf6f5a77d4200d504ceb257a0897b7bd977c16398194749ec21822526b6
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3000-3500/records/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml.md
    sha256: 2ce2cd7d9168af9fc0433465303c5a4df7456e26682ca9f462faf798091e995d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/plan.json
    sha256: 458245c753b023bf5e9b57d7ac836f18fda493553786e735de56d9fdc026c46d
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml.md
    sha256: 788256f1b6cea3107b5f62e1716db4ca299a591ad3875f0ed30ef5adbec346fd
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
    sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
    sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.md
    sha256: a0a8629c5ea3fb87608c4d5f9c7aa6b0d5ec0bdabcbd3891d1a4a840cddcb3d0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfofarcimen_medium__e24ac714.md
    sha256: fd29054b31d27b5e6d5244f8cd2aecd506c0af17bd50198b15cfbe9c19bc6308
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.md
    sha256: 6d6b49318910dda8561f9e632f27737b5e44ad6e48b435b5c36d99b7a9db317f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.md
    sha256: 0cb76708c222eb3ca3bcbea4abcb61d45c402262593879fd773f8aad8076c41f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.md
    sha256: e10f3855f75dafedbbcd0bbcd5b3f4bf43f0ed09d0471783d3ba2518d31ebe75
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
    sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
    role: context
  - path: reports/label_plausibility_2026-07-19.tsv
    sha256: eda647ffbb87d5ea90db812858b2d1d9388393c4d1abc8dec78672324c1509d9
    role: context
  - path: reports/media_content_review_manifest.tsv
    sha256: e5ff2f1241ba046ae7a5dc0d543d340bdba10d31fa1fdc3e36203600cf1ec0ce
    role: context
  - path: reports/yaml_record_review/20260921T150322Z-Artificial_deep_lake_medium.md
    sha256: 55e9950c9507fca8c6a4e8df2b073b1d123b2654017ee8e5915bb5942bb4567f
    role: context
  - path: reports/yaml_record_review/20260922T191917Z-desulfonatronum_par180_medium__7eef7f75.md
    sha256: 972de78446f2829785ba2be14b1fc30f9fbd3d851b59669ce3ef518e10fb0fbc
    role: context
  - path: reports/yaml_record_review/20260923T131040Z-hydrogen_using_marine_methanogen_medium.md
    sha256: 5732eb051e002fc97d9126fd2d67c8a4316997f9c16c6f844546947625c1458b
    role: context
  - path: reports/yaml_record_review/20260923T131244Z-hydrogen_using_marine_methanogen_medium__931ca534.md
    sha256: 30599d3738d18d2c5f677568c9725b1f39578f42b2fa3c03e54c403f34556117
    role: context
  - path: reports/yaml_record_review/20260924T090034Z-mmj_thi_medium__4fbd5200.md
    sha256: 3d187a1f4484627c907f4bd8dc12a99cf58eb26fcab4bb0eea9f78f8be48e6c5
    role: context
  - path: reports/yaml_record_review/20260924T102523Z-modified_biebl_and_pennings_medium.md
    sha256: 03f8694aada87cf5124bce09d1fb1ca6e18d78559bc72075f0a45422e3bb8c7b
    role: context
  - path: reports/yaml_record_review/20260925T153111Z-togo_medium_m3152.md
    sha256: ed6d7e559116cf157f9548cdae93722b67d1ab9d116d2a82f2ec90e4e764de7b
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/fix_primary_term_grounding.py
    sha256: 9d35bef88897003d1ae3af0789103052d8574a3d33b4d1e504e431184d2681b6
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: scripts/review_solution_concentration_evidence.py
    sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
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
scope:
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch075 native selection index 09.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009096
targets:
- target_id: CultureMech:009096
  path: data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml
  label: desulfofarcimen_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009096
  command: just validate-schema data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009096
  command: just validate-strict data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml
    --out REVIEW_WORK/batch075/record09/strict.tsv --workers 1 --quiet
  exit_code: 0
  evidence_ids:
  - validate-strict
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009096
  command: just validate-terms data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Native reference checker performed zero reference checks; this is not claim
    authentication.
  target_ids:
  - CultureMech:009096
  command: just validate-references data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 279575a6d4a4e5bb7c3c9014c8b8d9dbd8c315034d3445f47527953dfdf2b4f3
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 13db63e34297a1249c7945fe7d3377b73875e1db2936d87eaeca78e096f1196e
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch075/record09/identity-search.json
  accessed_at: '2026-10-28T19:07:13.567251Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    only exact resolved owner matches are retained in this result. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: 2efe524a7e0f028dd0dcfdd79a3a242715ac798ef9097a6440019bbead92908b
- evidence_id: dsm124
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T18:56:02.654828Z'
  support: supports
  summary: 'Both primary PDF pages read visually and as text: current main formula,
    declared final1003 ml, pH, preparation, three stock tables and three explicitly
    separate strain variants.'
  snapshot_sha256: a2c8cb38e72919285a4d77c34d34d13655e07cc32c7b07a6ed6ebf353dfec62a
- evidence_id: togo2526
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T18:56:02.830691Z'
  support: supports
  summary: Complete four-section structured payload read including all44 rows, original
    DSM124 identity and all comments. Main/stock boundaries and the older ten-vitamin
    formulation are preserved.
  snapshot_sha256: 92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236
- evidence_id: api124
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/124
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T18:56:02.450935Z'
  support: supports
  summary: Current complete medium and all four solution graphs read. Provider main1003
    ml and stock1000 ml bases are explicit, not inferred from water. Stock formulation
    numeric IDs differ from standalone links; identity compared by complete recipe.
  snapshot_sha256: 24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851
- evidence_id: solution4178
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/4178
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T18:56:02.143901Z'
  support: supports
  summary: Complete standalone SL10 recipe, volume and preparation read; matches the
    source stock ingredients, with current HCl-rate and water defects kept distinct
    from eight correct stock rates.
  snapshot_sha256: 7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da
- evidence_id: solution5543
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/5543
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T18:56:02.208431Z'
  support: supports
  summary: Complete standalone selenium/tungsten stock read. All three current rates
    and1 L batch water are supported at the provider stock scope; these are not receiving-medium
    rates.
  snapshot_sha256: 7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882
- evidence_id: solution6241
  kind: database
  reference: https://mediadive.dsmz.de/rest/solution/6241
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T18:56:02.144038Z'
  support: supports
  summary: Complete standalone three-vitamin recipe and100 ml makeup step read. This
    source authenticates its own stock only and disproves the selected medium vitamin
    link.
  snapshot_sha256: d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1
- evidence_id: lpsn
  kind: database
  reference: https://lpsn.dsmz.de/genus/desulfofarcimen
  locator: Genus name, classification, status and child taxa
  accessed_at: '2026-10-28T18:56:03.269840Z'
  support: context_only
  summary: Current genus page identifies Desulfofarcimen within Bacteria. Nomenclature
    supports bacterial filing but does not establish a strain or experimental growth
    claim.
  snapshot_sha256: 4e0d07a4d5b1b6701119b097a01d80c20cac7cd19c19e02e618ddbdcd7821a19
- evidence_id: dependency-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Complete linked stock identity/composition, current history, references
    and attached evidence read. Quantities are scoped to this stock; no receiving-medium
    rate is inherited.
  snapshot_sha256: 34d1e5dcc119569d07097d867f9a50cd44edc797d2c1328ccc4cd2be47a6a0fa
- evidence_id: dependency-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Complete linked stock identity/composition, current history, references
    and attached evidence read. Quantities are scoped to this stock; no receiving-medium
    rate is inherited.
  snapshot_sha256: 993f6c076ae708ef824e3637f0b5a8eb9afb742877a80f5c6dc445c376efc43f
- evidence_id: dependency-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Complete linked stock identity/composition, current history, references
    and attached evidence read. Quantities are scoped to this stock; no receiving-medium
    rate is inherited.
  snapshot_sha256: 0d875aeaae44d83149565716773f50c7d2d1abadb818a0154802ef980d71900a
- evidence_id: history-report-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3000-3500/records/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: 2ce2cd7d9168af9fc0433465303c5a4df7456e26682ca9f462faf798091e995d
- evidence_id: history-report-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/records/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: 788256f1b6cea3107b5f62e1716db4ca299a591ad3875f0ed30ef5adbec346fd
- evidence_id: history-report-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/records/bacterial/mediadive_6241_Vitamin_solution.yaml.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: b046818181cd0beff24e64f8eebfa16c931e584abdfc1c6474ab1f5d12e359e1
- evidence_id: history-report-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: a0a8629c5ea3fb87608c4d5f9c7aa6b0d5ec0bdabcbd3891d1a4a840cddcb3d0
- evidence_id: history-report-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfofarcimen_medium__e24ac714.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: fd29054b31d27b5e6d5244f8cd2aecd506c0af17bd50198b15cfbe9c19bc6308
- evidence_id: history-report-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: 6d6b49318910dda8561f9e632f27737b5e44ad6e48b435b5c36d99b7a9db317f
- evidence_id: history-report-7
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: 0cb76708c222eb3ca3bcbea4abcb61d45c402262593879fd773f8aad8076c41f
- evidence_id: history-report-8
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: e10f3855f75dafedbbcd0bbcd5b3f4bf43f0ed09d0471783d3ba2518d31ebe75
- evidence_id: history-report-9
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.md
  locator: Complete document
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Full historical body read or exact sealed prior-root byte reading reused
    for6241. The selected/owner reports match current hashes and have zero external
    checks; the000709 alias is a separate historical merged record. Stock curation
    reports and parent claims are authenticated against fresh provider bytes without
    certifying historical execution.
  snapshot_sha256: ae278f0427b8098c7f296fa04798071531424dbe92c198cd777cba5676fd18ce
- evidence_id: history-context-1
  kind: record_content
  reference: reports/yaml_record_review/20260921T150322Z-Artificial_deep_lake_medium.md
  locator: Header and stock-related historical scope; fuller independent reading retained
    separately when available
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Historical dependency-reference context only. This is a report about another
    medium, not evidence that the selected formulation, stock doses or growth claims
    are interchangeable.
  snapshot_sha256: 55e9950c9507fca8c6a4e8df2b073b1d123b2654017ee8e5915bb5942bb4567f
- evidence_id: history-context-2
  kind: record_content
  reference: reports/yaml_record_review/20260922T191917Z-desulfonatronum_par180_medium__7eef7f75.md
  locator: Header and stock-related historical scope; fuller independent reading retained
    separately when available
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Historical dependency-reference context only. This is a report about another
    medium, not evidence that the selected formulation, stock doses or growth claims
    are interchangeable.
  snapshot_sha256: 972de78446f2829785ba2be14b1fc30f9fbd3d851b59669ce3ef518e10fb0fbc
- evidence_id: history-context-3
  kind: record_content
  reference: reports/yaml_record_review/20260923T131040Z-hydrogen_using_marine_methanogen_medium.md
  locator: Header and stock-related historical scope; fuller independent reading retained
    separately when available
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Historical dependency-reference context only. This is a report about another
    medium, not evidence that the selected formulation, stock doses or growth claims
    are interchangeable.
  snapshot_sha256: 5732eb051e002fc97d9126fd2d67c8a4316997f9c16c6f844546947625c1458b
- evidence_id: history-context-4
  kind: record_content
  reference: reports/yaml_record_review/20260923T131244Z-hydrogen_using_marine_methanogen_medium__931ca534.md
  locator: Header and stock-related historical scope; fuller independent reading retained
    separately when available
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Historical dependency-reference context only. This is a report about another
    medium, not evidence that the selected formulation, stock doses or growth claims
    are interchangeable.
  snapshot_sha256: 30599d3738d18d2c5f677568c9725b1f39578f42b2fa3c03e54c403f34556117
- evidence_id: history-context-5
  kind: record_content
  reference: reports/yaml_record_review/20260924T090034Z-mmj_thi_medium__4fbd5200.md
  locator: Header and stock-related historical scope; fuller independent reading retained
    separately when available
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Historical dependency-reference context only. This is a report about another
    medium, not evidence that the selected formulation, stock doses or growth claims
    are interchangeable.
  snapshot_sha256: 3d187a1f4484627c907f4bd8dc12a99cf58eb26fcab4bb0eea9f78f8be48e6c5
- evidence_id: history-context-6
  kind: record_content
  reference: reports/yaml_record_review/20260924T102523Z-modified_biebl_and_pennings_medium.md
  locator: Header and stock-related historical scope; fuller independent reading retained
    separately when available
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Historical dependency-reference context only. This is a report about another
    medium, not evidence that the selected formulation, stock doses or growth claims
    are interchangeable.
  snapshot_sha256: 03f8694aada87cf5124bce09d1fb1ca6e18d78559bc72075f0a45422e3bb8c7b
- evidence_id: history-context-7
  kind: record_content
  reference: reports/yaml_record_review/20260925T153111Z-togo_medium_m3152.md
  locator: Header and stock-related historical scope; fuller independent reading retained
    separately when available
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Historical dependency-reference context only. This is a report about another
    medium, not evidence that the selected formulation, stock doses or growth claims
    are interchangeable.
  snapshot_sha256: ed6d7e559116cf157f9548cdae93722b67d1ab9d116d2a82f2ec90e4e764de7b
- evidence_id: history-plan-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-3000-3500/plan.json
  locator: Selected exact stock path and every associated claim
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Only the exact4178/5543/6241 selected parent row is assessed; all21 claims,14
    attached excerpts, source hashes and current after hashes match. Unrelated plan
    records are not reviewed.
  snapshot_sha256: afdfbbf6f5a77d4200d504ceb257a0897b7bd977c16398194749ec21822526b6
- evidence_id: history-plan-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4000-4500/plan.json
  locator: Selected exact stock path and every associated claim
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Only the exact4178/5543/6241 selected parent row is assessed; all21 claims,14
    attached excerpts, source hashes and current after hashes match. Unrelated plan
    records are not reviewed.
  snapshot_sha256: 458245c753b023bf5e9b57d7ac836f18fda493553786e735de56d9fdc026c46d
- evidence_id: history-plan-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-solutions-4500-4770/plan.json
  locator: Selected exact stock path and every associated claim
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Only the exact4178/5543/6241 selected parent row is assessed; all21 claims,14
    attached excerpts, source hashes and current after hashes match. Unrelated plan
    records are not reviewed.
  snapshot_sha256: 2679e61f2f0f09cc4becc645dea566cd0c93feb1b0d7f13d7e197411d2051cd3
- evidence_id: writer-1
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: Current relevant full function scopes; exact prior root reading proof where
    reused
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: 'Full current converter previously read by root and exact bytes rechecked:
    stock sections are preserved, liquid/mg units improved and comments retained.
    Existing flattened target/owner predate those repairs. Remaining assumed per-litre
    bases need source-scoped review.'
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-2
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Current relevant full function scopes; exact prior root reading proof where
    reused
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Exact previously read bytes require compatible scientific fields before
    evidence union. Similar names/shared sources do not establish formulation equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-3
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: Current relevant full function scopes; exact prior root reading proof where
    reused
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: 'Exact previously read bytes: regenerate from corrected maintained contributors
    while preserving source/variant boundaries.'
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-4
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: Current relevant full function scopes; exact prior root reading proof where
    reused
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Exact previously read bytes do not blindly sum disagreeing duplicate quantities.
    The persisted3990 water artifact is not evidence of present behavior.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-5
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: Current relevant full function scopes; exact prior root reading proof where
    reused
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Exact previously read bytes preserve/flag conflicting concentration dictionaries
    instead of source-authenticating them.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer-6
  kind: record_content
  reference: scripts/review_solution_concentration_evidence.py
  locator: Current relevant full function scopes; exact prior root reading proof where
    reused
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Current full decision/review functions read. Same-source evidence retained;
    attribute-bearing rows, water with preparation steps, and missing provider g_l
    remain guarded. This explains bounded historical outcomes but does not prove past
    execution.
  snapshot_sha256: 40a5bb439caf0791caff746a1eac8d5069525f381c7f3b52556c26937741f65a
- evidence_id: writer-7
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: Current relevant full function scopes; exact prior root reading proof where
    reused
  accessed_at: '2026-10-28T19:07:13.508661Z'
  support: context_only
  summary: Exact previously read bytes. Current catalog and source forms must support
    any remaining legacy-link update; historical validity is not inferred.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: ols53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: Exact CHEBI53542 scientific object
  accessed_at: '2026-10-28T19:01:14.237789Z'
  support: supports
  summary: Exact current nickel chloride hexahydrate identity and formula 2Cl.6H2O.Ni
    verified as the source-specific candidate. Packaged MIM row 6703 rejects the exact
    preferred spelling 'NiCl2 x 6 H2O'; row 6668 maps preferred 'Nickel (II) chloride
    hexahydrate' and row 6704 maps the former spelling as its synonym. These lexical
    statuses are distinct; verify the exact selected linkage without treating the
    chemical identifier as generically rejected.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: ols15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:03.575448Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: ols26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:05.102183Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: ols86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:08.407246Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: ols63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:07.468297Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: ols31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:06.919065Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: ols86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:09.015728Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: ols76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:08.407386Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: ols32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:06.195180Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: ols32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:05.738494Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: ols32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:06.234619Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: ols32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:06.040937Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: ols64103
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:08.084144Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 0499238461b934590c83719736c7a30bf942d95c204daee7da061e0ba99f4a74
- evidence_id: ols17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17997
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:04.969111Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: ea4b3f90994884c49607689e3f3939cfec804c7d17905bbeecfc0ef7f80ead43
- evidence_id: ols16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:04.601232Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 19b976653e14322f23a21b90b537bfcd19bb4e73d8d0de96446a25888cd3caf6
- evidence_id: ols75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:08.407459Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: ols33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:06.423628Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: ols86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:09.160929Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: ols53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:07.264715Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: ols34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:07.161452Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: ols86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:09.007335Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: ols49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:07.161501Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: ols86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:08.595939Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: ols131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:03.575514Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: ols63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:08.084103Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: ols32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:05.889133Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: db4eb7586e3b04f5b2ae39b47bae7c1c533316f9bce15ee2829bf6967ca352f1
- evidence_id: ols15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:04.088276Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: ols30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:05.522188Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: ols49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:06.954354Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: ols30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:05.431533Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: ols27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:05.143533Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: ols176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:04.704803Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: ols17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:04.943480Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: ols15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:03.943482Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: ols16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:04.088135Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: ols31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T18:56:05.578654Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: ols17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T19:01:14.237873Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: ols17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17439
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T19:01:14.226232Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 210a9fbc1db1c75e6053f4e23d098851ad5c63f087c736061f7664d9a393dbdd
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch075/record09/quantity-inventory.json
  accessed_at: '2026-10-28T19:20:00.387353Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: c7ec95df1bcc32c02b40e273c6f303f696635f45b881e11a297711dd5a14c9f5
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch075/record09/grounding-inventory.json
  accessed_at: '2026-10-28T19:07:13.665192Z'
  support: context_only
  summary: All selected target/owner recursive asserted identifier/label slots and
    explicitly scoped dependency slots; current OLS scientific objects and packaged
    MIM preferred-row joins.
  snapshot_sha256: bac0c633cee92eba3e25f0d6d04333b5bc2af500c2ffa9cd57abffac55fabf6a
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch075/record09/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T19:07:13.665383Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 30f1c449f571ef24cf2a9b9d0517583f00ac6537d02e49f7d2c7556c6f57e19d
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch075/record09/scalar-census.json
  accessed_at: '2026-10-28T19:07:13.665421Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 381a70d49f5d42271960063c1459333e95852c29e4448495aeaab40741ff4ca8
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch075/record09/validate-schema.json
  accessed_at: '2026-10-28T18:56:00.094525Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 1db7aa6e95537908ca812e0b2cf603ade184f5fa03a85bb436da5748774b65af
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch075/record09/validate-strict.json
  accessed_at: '2026-10-28T18:56:01.371677Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch075/record09/strict.tsv\n"
  snapshot_sha256: 4a0f93d4193bceaa46ae039b4fba0ef8197164555a1802962b031a6576a93ccc
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch075/record09/validate-terms.json
  accessed_at: '2026-10-28T18:56:03.064183Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: c710459dd1410ced81b077672175af49be5eb3ad3cb48419a17b04b8387b0ee9
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch075/record09/validate-references.json
  accessed_at: '2026-10-28T18:56:03.997085Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 64c6425cc9330b5605b7c2336575ce9c21eea1d3da7de444c0422b861c395c01
assessments:
- assessment_id: a1
  area: identity
  topic: Exact record and source identity
  outcome: supported
  summary: The selected generated record and soleTOGO M2526 maintained contributor
    shareCultureMech009096 and all scientific fields. Current TOGO points exactly
    toDSM124. Historical alias000709 names three different contributors and is not
    the selected target. Standalone4178 and5543 match the relevant stock identities;6241
    is a three-vitamin stock and is not the source ten-vitamin formulation.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - local-target
  - owner-1
  - identity-search
  - togo2526
  - dsm124
  - solution4178
  - solution5543
  - solution6241
- assessment_id: a2
  area: scope
  topic: Classification and claim boundaries
  outcome: supported
  summary: Yeast extract and current DSM/API complex_medium=yes support complex/undefined
    medium; no gelling agent is specified, consistent with liquid form. Genus classification
    supports bacterial filing. Cultivation application is generic, without strain-grounded
    growth claims. Source DSM2925/7213/100382 replacement variants remain separate
    and do not become base recipe ingredients or growth assertions.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - api124
  - dsm124
  - togo2526
  - lpsn
- assessment_id: a3
  area: provenance
  topic: Retain current source-backed stock repairs
  outcome: supported
  summary: Fresh standalone payloads exactly match all three historical source digests.
    All21 plan claims and14 current attached evidence entries reconcile to current
    after hashes. Retain eight SL10 compound rates, three selenium/tungsten rates
    and its1 L water repair, plus two0.1 g/L rates in the separate6241 stock. HCl,
    SL10 water,6241 biotin/water and placeholders were explicitly unresolved. Source
    bytes and plan linkage are authenticated; historical capture times/execution are
    not.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - history-plan-1
  - history-plan-2
  - history-plan-3
  - dependency-1
  - dependency-2
  - dependency-3
  - solution4178
  - solution5543
  - solution6241
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - quantities
  details: '[{"quantity_id":"q1","topic":"Main recipe \u2014 Na-resazurin solution
    (0.1% w/v)","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na-resazurin
    solution (0.1% w/v)","volume":0.5,"unit":"ml","conc_value":0.1,"conc_unit":"(w/v)","gmo":"http://purl.jp/bio/10/gmo/GMO_001453","gmo_id":"GMO_001453","label":"Sodium
    resazurin solution","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000051","uri":"http://purl.jp/bio/10/gmo/GMO_000051","label":"Solution"}],"roles":[{"id":"GMO_000055","uri":"http://purl.jp/bio/10/gmo/GMO_000055","label":"pH
    dependent redox indicator"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Na-resazurin solution (0.1% w/v)\",\n          \"volume\": 0.5,\n          \"unit\":
    \"ml\",\n          \"conc_value\": 0.1,\n          \"conc_unit\": \"(w/v)\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001453\",\n          \"gmo_id\": \"GMO_001453\",\n          \"label\":
    \"Sodium resazurin solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent
    redox indicator\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The
    source specifies0.5 ml of this stock per listed batch, not0.5 G_PER_L. Preserve
    the addition volume, separate stock strength and composition, and keep source
    version/stage explicit. Explicit0.1% w/v means1 g/L stock;0.5 ml supplies0.5 mg
    sodium resazurin per batch. This arithmetic is not a final medium rate.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[0].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies0.5 ml of this stock per listed batch, not0.5 G_PER_L. Preserve
    the addition volume, separate stock strength and composition, and keep source
    version/stage explicit. Explicit0.1% w/v means1 g/L stock;0.5 ml supplies0.5 mg
    sodium resazurin per batch. This arithmetic is not a final medium rate."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[0].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies0.5 ml of this stock per listed batch, not0.5 G_PER_L. Preserve
    the addition volume, separate stock strength and composition, and keep source
    version/stage explicit. Explicit0.1% w/v means1 g/L stock;0.5 ml supplies0.5 mg
    sodium resazurin per batch. This arithmetic is not a final medium rate."}]},{"quantity_id":"q2","topic":"Main
    recipe \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled
    water","volume":1000,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled
    water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating
    media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The
    main source water input is1000 ml (1 L). Current3990 G_PER_L sums this with990/1000/1000
    ml from three separate stock recipes. Separate all four solvent amounts; neither
    this sum nor1 L water is a measured final medium volume.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"3990.0","unit":"G_PER_L"},"decision":"correct","rationale":"The
    main source water input is1000 ml (1 L). Current3990 G_PER_L sums this with990/1000/1000
    ml from three separate stock recipes. Separate all four solvent amounts; neither
    this sum nor1 L water is a measured final medium volume."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"3990.0","unit":"G_PER_L"},"decision":"correct","rationale":"The
    main source water input is1000 ml (1 L). Current3990 G_PER_L sums this with990/1000/1000
    ml from three separate stock recipes. Separate all four solvent amounts; neither
    this sum nor1 L water is a measured final medium volume."}]},{"quantity_id":"q3","topic":"Main
    recipe \u2014 Yeast extract","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Yeast
    extract","volume":1,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001003","gmo_id":"GMO_001003","label":"Yeast
    extract","properties":[{"id":"GMO_000047","uri":"http://purl.jp/bio/10/gmo/GMO_000047","label":"Undefined
    component"}],"roles":[{"id":"GMO_000042","uri":"http://purl.jp/bio/10/gmo/GMO_000042","label":"Nutrient
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"Yeast extract\",\n          \"volume\":
    1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\":
    \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":10,"compound":"Yeast
    extract","compound_id":16,"amount":1,"unit":"g","g_l":0.997009,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.997009,\n                        \"optional\":
    0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical1 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q4","topic":"Main
    recipe \u2014 NaCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NaCl","volume":1.17,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001004","gmo_id":"GMO_001004","label":"Sodium
    chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"NaCl\",\n          \"volume\":
    1.17,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\":
    \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":1,"compound":"NaCl","compound_id":43,"amount":1.17,"unit":"g","g_l":1.1665,"mmol_l":19.9607,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1.17,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.1665,\n                        \"mmol_l\":
    19.9607,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical1.17 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored_value":{"value":"1.17","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1.17 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[2].concentration","stored_value":{"value":"1.17","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1.17 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q5","topic":"Main
    recipe \u2014 CaCl2 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[4]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"CaCl2
    x 2 H2O","volume":0.15,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001005","gmo_id":"GMO_001005","label":"Calcium
    chloride dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"CaCl2 x 2 H2O\",\n          \"volume\":
    0.15,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001005\",\n          \"gmo_id\":
    \"GMO_001005\",\n          \"label\": \"Calcium chloride dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":4,"compound":"CaCl2
    x 2 H2O","compound_id":7,"amount":0.15,"unit":"g","g_l":0.149551,"mmol_l":1.01725,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\":
    1.01725,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical0.15 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored_value":{"value":"0.15","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.15 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[3].concentration","stored_value":{"value":"0.15","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.15 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q6","topic":"Main
    recipe \u2014 KH2PO4","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[5]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"KH2PO4","volume":0.2,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001006","gmo_id":"GMO_001006","label":"Potassium
    phosphate monobasic","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000038","uri":"http://purl.jp/bio/10/gmo/GMO_000038","label":"Buffer"}]},"literal_excerpt":"{\n          \"component_name\":
    \"KH2PO4\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\":
    \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":6,"compound":"KH2PO4","compound_id":11,"amount":0.2,"unit":"g","g_l":0.199402,"mmol_l":1.46527,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\":
    1.46527,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical0.2 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored_value":{"value":"0.2","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.2 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[4].concentration","stored_value":{"value":"0.2","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.2 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q7","topic":"Main
    recipe \u2014 NH4Cl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[6]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NH4Cl","volume":0.27,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001008","gmo_id":"GMO_001008","label":"Ammonium
    chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000062","uri":"http://purl.jp/bio/10/gmo/GMO_000062","label":"Nitrogen
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"NH4Cl\",\n          \"volume\":
    0.27,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\":
    \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":5,"compound":"NH4Cl","compound_id":42,"amount":0.27,"unit":"g","g_l":0.269192,"mmol_l":5.03257,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.27,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.269192,\n                        \"mmol_l\":
    5.03257,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical0.27 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored_value":{"value":"0.27","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.27 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[5].concentration","stored_value":{"value":"0.27","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.27 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q8","topic":"Main
    recipe \u2014 MgCl2x 6 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[7]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"MgCl2x
    6 H2O","volume":0.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001013","gmo_id":"GMO_001013","label":"Magnesium
    chloride hexahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"MgCl2x 6 H2O\",\n          \"volume\":
    0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001013\",\n          \"gmo_id\":
    \"GMO_001013\",\n          \"label\": \"Magnesium chloride hexahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":2,"compound":"MgCl2
    x 6 H2O","compound_id":79,"amount":0.4,"unit":"g","g_l":0.398804,"mmol_l":1.96162,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\":
    1.96162,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical0.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[6].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q9","topic":"Main
    recipe \u2014 Na2S x 9 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[8]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2S
    x 9 H2O","volume":0.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001014","gmo_id":"GMO_001014","label":"Sodium
    sulfide nonahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000064","uri":"http://purl.jp/bio/10/gmo/GMO_000064","label":"Reducing
    agent"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2S x 9 H2O\",\n          \"volume\":
    0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\":
    \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing
    agent\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":16,"compound":"Na2S
    x 9 H2O","compound_id":54,"amount":0.4,"unit":"g","g_l":0.398804,"mmol_l":1.66042,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\":
    1.66042,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical0.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[7].concentration","stored_value":{"value":"0.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q10","topic":"Main
    recipe \u2014 KCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[9]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"KCl","volume":0.3,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001017","gmo_id":"GMO_001017","label":"Potassium
    chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"KCl\",\n          \"volume\":
    0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\":
    \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":3,"compound":"KCl","compound_id":61,"amount":0.3,"unit":"g","g_l":0.299103,"mmol_l":4.01211,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    4.01211,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical0.3 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored_value":{"value":"0.3","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.3 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[8].concentration","stored_value":{"value":"0.3","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical0.3 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q11","topic":"Main
    recipe \u2014 NaHCO3","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[10]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NaHCO3","volume":4.5,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001019","gmo_id":"GMO_001019","label":"Sodium
    bicarbonate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000038","uri":"http://purl.jp/bio/10/gmo/GMO_000038","label":"Buffer"}]},"literal_excerpt":"{\n          \"component_name\":
    \"NaHCO3\",\n          \"volume\": 4.5,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\":
    \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":12,"compound":"NaHCO3","compound_id":55,"amount":4.5,"unit":"g","g_l":4.48654,"mmol_l":53.4067,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 4.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.48654,\n                        \"mmol_l\":
    53.4067,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical4.5 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored_value":{"value":"4.5","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical4.5 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[9].concentration","stored_value":{"value":"4.5","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical4.5 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q12","topic":"Main
    recipe \u2014 Na-acetate","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[11]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na-acetate","volume":1.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001031","gmo_id":"GMO_001031","label":"Sodium
    acetate","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000038","uri":"http://purl.jp/bio/10/gmo/GMO_000038","label":"Buffer"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Na-acetate\",\n          \"volume\": 1.4,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001031\",\n          \"gmo_id\": \"GMO_001031\",\n          \"label\":
    \"Sodium acetate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":13,"compound":"Na-acetate","compound_id":23,"amount":1.4,"unit":"g","g_l":1.39581,"mmol_l":17.0151,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 1.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.39581,\n                        \"mmol_l\":
    17.0151,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical1.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[10].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q13","topic":"Main
    recipe \u2014 Na2SO4","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[12]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2SO4","volume":2.84,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001052","gmo_id":"GMO_001052","label":"Sodium
    sulfate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2SO4\",\n          \"volume\":
    2.84,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001052\",\n          \"gmo_id\":
    \"GMO_001052\",\n          \"label\": \"Sodium sulfate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":7,"compound":"Na2SO4","compound_id":110,"amount":2.84,"unit":"g","g_l":2.83151,"mmol_l":19.9346,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 2.84,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.83151,\n                        \"mmol_l\":
    19.9346,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical2.84 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored_value":{"value":"2.84","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical2.84 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[11].concentration","stored_value":{"value":"2.84","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical2.84 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q14","topic":"Main
    recipe \u2014 Na-butyrate","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[13]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na-butyrate","volume":1.4,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001648","gmo_id":"GMO_001648","label":"Sodium
    butyrate","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"},{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"Na-butyrate\",\n          \"volume\":
    1.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001648\",\n          \"gmo_id\":
    \"GMO_001648\",\n          \"label\": \"Sodium butyrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""},"current_DSM_comparison":{"source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[0].recipe
    exact compound","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":14,"compound":"Na-butyrate","compound_id":232,"amount":1.4,"unit":"g","g_l":1.39581,"mmol_l":12.6792,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na-butyrate\",\n                        \"compound_id\":
    232,\n                        \"amount\": 1.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.39581,\n                        \"mmol_l\":
    12.6792,\n                        \"optional\": 0\n                    }"},"declared_volume_ml":1003}},"decision":"unsupported","rationale":"The
    numerical1.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[12].concentration","stored_value":{"value":"1.4","unit":"G_PER_L"},"decision":"unsupported","rationale":"The
    numerical1.4 matches the statedg batch input. TOGO does not declare final makeup,
    so its G_PER_L basis is unsupported. Current DSM/API explicitly uses1003 ml and
    a revised vitamin/preparation version; use that denominator only after an explicit
    source-version decision, not silently for the TOGO batch."}]},{"quantity_id":"q15","topic":"Main
    recipe \u2014 Trace element solution SL-10","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[14]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Trace
    element solution SL-10","volume":1,"unit":"ml","reference_media_id":"M2526","properties":[],"roles":[]},"literal_excerpt":"{\n          \"component_name\":
    \"Trace element solution SL-10\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M2526\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The
    source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the
    addition volume, separate stock strength and composition, and keep source version/stage
    explicit.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the
    addition volume, separate stock strength and composition, and keep source version/stage
    explicit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[1].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the
    addition volume, separate stock strength and composition, and keep source version/stage
    explicit."}]},{"quantity_id":"q16","topic":"Main recipe \u2014 Selenite-tungstate
    solution","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[15]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Selenite-tungstate
    solution","volume":1,"unit":"ml","reference_media_id":"M2526","properties":[],"roles":[]},"literal_excerpt":"{\n          \"component_name\":
    \"Selenite-tungstate solution\",\n          \"volume\": 1,\n          \"unit\":
    \"ml\",\n          \"reference_media_id\": \"M2526\",\n          \"properties\":
    [],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The
    source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the
    addition volume, separate stock strength and composition, and keep source version/stage
    explicit.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[2].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the
    addition volume, separate stock strength and composition, and keep source version/stage
    explicit."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[2].concentration","stored_value":{"value":"1","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies1 ml of this stock per listed batch, not1 G_PER_L. Preserve the
    addition volume, separate stock strength and composition, and keep source version/stage
    explicit."}]},{"quantity_id":"q17","topic":"Main recipe \u2014 Vitamin solution","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[16]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Vitamin
    solution","volume":10,"unit":"ml","reference_media_id":"M2526","properties":[],"roles":[]},"literal_excerpt":"{\n          \"component_name\":
    \"Vitamin solution\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M2526\",\n          \"properties\": [],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"correct","rationale":"The
    source specifies10 ml of this stock per listed batch, not10 G_PER_L. Preserve
    the addition volume, separate stock strength and composition, and keep source
    version/stage explicit. TOGO uses10 ml of a ten-vitamin1x stock; current DSM uses1
    ml of the corresponding10x stock. On their nominal1 L stock basis these supply
    equal vitamin masses, so this is not a tenfold dose error. Different liquid additions/preparation
    versions remain distinct. Linked6241 is a different three-vitamin stock and cannot
    supply either formulation.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"solutions[3].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies10 ml of this stock per listed batch, not10 G_PER_L. Preserve
    the addition volume, separate stock strength and composition, and keep source
    version/stage explicit. TOGO uses10 ml of a ten-vitamin1x stock; current DSM uses1
    ml of the corresponding10x stock. On their nominal1 L stock basis these supply
    equal vitamin masses, so this is not a tenfold dose error. Different liquid additions/preparation
    versions remain distinct. Linked6241 is a different three-vitamin stock and cannot
    supply either formulation."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"solutions[3].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source specifies10 ml of this stock per listed batch, not10 G_PER_L. Preserve
    the addition volume, separate stock strength and composition, and keep source
    version/stage explicit. TOGO uses10 ml of a ten-vitamin1x stock; current DSM uses1
    ml of the corresponding10x stock. On their nominal1 L stock basis these supply
    equal vitamin masses, so this is not a tenfold dose error. Different liquid additions/preparation
    versions remain distinct. Linked6241 is a different three-vitamin stock and cannot
    supply either formulation."}]},{"quantity_id":"q18","topic":"Main recipe \u2014
    N2","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[17]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"N2","conc_value":100,"conc_unit":"%","gmo":"http://purl.jp/bio/10/gmo/GMO_002261","gmo_id":"GMO_002261","label":"Nitrogen
    gas","properties":[{"id":"GMO_000077","uri":"http://purl.jp/bio/10/gmo/GMO_000077","label":"Gas"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\":
    \"N2\",\n          \"conc_value\": 100,\n          \"conc_unit\": \"%\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\":
    \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\":
    \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"evidence_only","rationale":"Gas
    is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE
    only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100%
    N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into
    a main-medium nutrient concentration.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas
    is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE
    only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100%
    N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into
    a main-medium nutrient concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[13].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas
    is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE
    only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100%
    N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into
    a main-medium nutrient concentration."}]},{"quantity_id":"q19","topic":"Main recipe
    \u2014 Carbon dioxide gas","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[0].items[18]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Carbon
    dioxide gas","gmo":"http://purl.jp/bio/10/gmo/GMO_002260","gmo_id":"GMO_002260","label":"Carbon
    dioxide gas","properties":[{"id":"GMO_000077","uri":"http://purl.jp/bio/10/gmo/GMO_000077","label":"\u30ac\u30b9"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\":
    \"Carbon dioxide gas\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002260\",\n          \"gmo_id\":
    \"GMO_002260\",\n          \"label\": \"Carbon dioxide gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"\u30ac\u30b9\"\n            }\n          ],\n          \"roles\":
    []\n        }","section":{"paragraph_index":1,"subcomponent_name":""}},"decision":"evidence_only","rationale":"Gas
    is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE
    only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100%
    N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into
    a main-medium nutrient concentration.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas
    is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE
    only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100%
    N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into
    a main-medium nutrient concentration."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[14].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"evidence_only","rationale":"Gas
    is an unquantified process atmosphere, not a dissolved nutrient rate. Retain VARIABLE
    only with source process scope: main sparging/dispensing uses80% N2/20% CO2;100%
    N2 applies to late stock preparation. Do not turn the TOGO N2 conc_value100 into
    a main-medium nutrient concentration."}]},{"quantity_id":"q20","topic":"Trace
    element solution SL-10 \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled
    water","volume":990,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled
    water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating
    media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    990,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"add","rationale":"This990 ml is solvent
    for the separate Trace element solution SL-10 stock. Represent it within that
    stock, never in the main3990 G_PER_L sum. The explicit source instruction makes
    SL10 up to1000 ml; this supports the stock final-volume basis, separately from
    the990 ml water input.","layer_assessments":[]},{"quantity_id":"q21","topic":"Trace
    element solution SL-10 \u2014 Na2MoO4 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2MoO4
    x 2 H2O","volume":36,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001011","gmo_id":"GMO_001011","label":"Sodium
    molybdate dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2MoO4 x 2 H2O\",\n          \"volume\":
    36,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\":
    \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source36 mg belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. The explicit source instruction
    makes SL10 up to1000 ml; this supports the stock final-volume basis, separately
    from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored_value":{"value":"36","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source36 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[15].concentration","stored_value":{"value":"36","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source36 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q22","topic":"Trace
    element solution SL-10 \u2014 H3BO3","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"H3BO3","volume":6,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001015","gmo_id":"GMO_001015","label":"Boric
    acid","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"H3BO3\",\n          \"volume\":
    6,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001015\",\n          \"gmo_id\":
    \"GMO_001015\",\n          \"label\": \"Boric acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source6 mg belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. The explicit source instruction
    makes SL10 up to1000 ml; this supports the stock final-volume basis, separately
    from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored_value":{"value":"6","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source6 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[16].concentration","stored_value":{"value":"6","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source6 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q23","topic":"Trace
    element solution SL-10 \u2014 MnCl2 x 4 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"MnCl2
    x 4 H2O","volume":100,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001020","gmo_id":"GMO_001020","label":"Manganese
    chloride tetrahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"MnCl2 x 4 H2O\",\n          \"volume\":
    100,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001020\",\n          \"gmo_id\":
    \"GMO_001020\",\n          \"label\": \"Manganese chloride tetrahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source100 mg belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. The explicit source instruction
    makes SL10 up to1000 ml; this supports the stock final-volume basis, separately
    from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored_value":{"value":"100","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source100 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[17].concentration","stored_value":{"value":"100","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source100 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q24","topic":"Trace
    element solution SL-10 \u2014 CoCl2 x 6 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[4]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"CoCl2
    x 6 H2O","volume":190,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001021","gmo_id":"GMO_001021","label":"Cobalt
    dichloride hexahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"CoCl2 x 6 H2O\",\n          \"volume\":
    190,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001021\",\n          \"gmo_id\":
    \"GMO_001021\",\n          \"label\": \"Cobalt dichloride hexahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source190 mg belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. The explicit source instruction
    makes SL10 up to1000 ml; this supports the stock final-volume basis, separately
    from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored_value":{"value":"190","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source190 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[18].concentration","stored_value":{"value":"190","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source190 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q25","topic":"Trace
    element solution SL-10 \u2014 NiCl2 x 6 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[5]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NiCl2
    x 6 H2O","volume":24,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001022","gmo_id":"GMO_001022","label":"Nickel
    chloride hexahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"NiCl2 x 6 H2O\",\n          \"volume\":
    24,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\":
    \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source24 mg belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. Preserve nickel chloride hexahydrate;
    the current anhydrous CHEBI mapping is a separate identity defect. The explicit
    source instruction makes SL10 up to1000 ml; this supports the stock final-volume
    basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored_value":{"value":"24","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source24 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution. Preserve
    nickel chloride hexahydrate; the current anhydrous CHEBI mapping is a separate
    identity defect."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[19].concentration","stored_value":{"value":"24","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source24 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution. Preserve
    nickel chloride hexahydrate; the current anhydrous CHEBI mapping is a separate
    identity defect."}]},{"quantity_id":"q26","topic":"Trace element solution SL-10
    \u2014 CuCl2 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[6]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"CuCl2
    x 2 H2O","volume":2,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001024","gmo_id":"GMO_001024","label":"Copper(II)
    chloride dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"CuCl2 x 2 H2O\",\n          \"volume\":
    2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001024\",\n          \"gmo_id\":
    \"GMO_001024\",\n          \"label\": \"Copper(II) chloride dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source2 mg belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. The explicit source instruction
    makes SL10 up to1000 ml; this supports the stock final-volume basis, separately
    from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source2 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[20].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source2 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q27","topic":"Trace
    element solution SL-10 \u2014 ZnCl2","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[7]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"ZnCl2","volume":70,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001035","gmo_id":"GMO_001035","label":"Zinc
    chloride","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"ZnCl2\",\n          \"volume\":
    70,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001035\",\n          \"gmo_id\":
    \"GMO_001035\",\n          \"label\": \"Zinc chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source70 mg belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. The explicit source instruction
    makes SL10 up to1000 ml; this supports the stock final-volume basis, separately
    from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored_value":{"value":"70","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source70 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[21].concentration","stored_value":{"value":"70","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source70 mg belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q28","topic":"Trace
    element solution SL-10 \u2014 HCl (25%; 7.7 M)","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[8]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"HCl
    (25%; 7.7 M)","volume":10,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001499","gmo_id":"GMO_001499","label":"Hydrochloric
    acid solution","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000051","uri":"http://purl.jp/bio/10/gmo/GMO_000051","label":"Solution"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating
    media"}]},"literal_excerpt":"{\n          \"component_name\": \"HCl (25%; 7.7
    M)\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001499\",\n          \"gmo_id\": \"GMO_001499\",\n          \"label\":
    \"Hydrochloric acid solution\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source10 ml belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. Preserve the10 ml HCl reagent labeled25%;7.7 M. Percentage basis/density
    is unstated; do not accept the provider2.5 g/L blindly. The explicit source instruction
    makes SL10 up to1000 ml; this supports the stock final-volume basis, separately
    from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source10 ml belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. Preserve the10 ml HCl reagent labeled25%;7.7
    M. Percentage basis/density is unstated; do not accept the provider2.5 g/L blindly."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[22].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source10 ml belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. Preserve the10 ml HCl reagent labeled25%;7.7
    M. Percentage basis/density is unstated; do not accept the provider2.5 g/L blindly."}]},{"quantity_id":"q29","topic":"Trace
    element solution SL-10 \u2014 FeCl2 x 4 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[1].items[9]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"FeCl2
    x 4 H2O","volume":1.5,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001548","gmo_id":"GMO_001548","label":"Iron(II)
    chloride tetrahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"FeCl2 x 4 H2O\",\n          \"volume\":
    1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001548\",\n          \"gmo_id\":
    \"GMO_001548\",\n          \"label\": \"Iron(II) chloride tetrahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":5,"subcomponent_name":"Trace
    element solution SL-10"}},"decision":"correct","rationale":"The source1.5 g belongs
    to the Trace element solution SL-10 stock batch, not a root ingredient concentration.
    Restore stock placement and source units before applying its separately stated
    receiving dose. The explicit source instruction makes SL10 up to1000 ml; this
    supports the stock final-volume basis, separately from the990 ml water input.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored_value":{"value":"1.5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source1.5 g belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[23].concentration","stored_value":{"value":"1.5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source1.5 g belongs to the Trace element solution SL-10 stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose."}]},{"quantity_id":"q30","topic":"Selenite-tungstate
    solution \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled
    water","volume":1000,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled
    water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating
    media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate
    solution"}},"decision":"add","rationale":"This1000 ml is solvent for the separate
    Selenite-tungstate solution stock. Represent it within that stock, never in the
    main3990 G_PER_L sum. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[]},{"quantity_id":"q31","topic":"Selenite-tungstate
    solution \u2014 Na2SeO3 x 5 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2SeO3
    x 5 H2O","volume":3,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001046","gmo_id":"GMO_001046","label":"Sodium
    selenite pentahydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2SeO3 x 5 H2O\",\n          \"volume\":
    3,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001046\",\n          \"gmo_id\":
    \"GMO_001046\",\n          \"label\": \"Sodium selenite pentahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate
    solution"}},"decision":"correct","rationale":"The source3 mg belongs to the Selenite-tungstate
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored_value":{"value":"3","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source3 mg belongs to the Selenite-tungstate solution stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[24].concentration","stored_value":{"value":"3","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source3 mg belongs to the Selenite-tungstate solution stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q32","topic":"Selenite-tungstate
    solution \u2014 Na2WO4 x 2 H2O","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Na2WO4
    x 2 H2O","volume":4,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001057","gmo_id":"GMO_001057","label":"Sodium
    tungstate dihydrate","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000078","uri":"http://purl.jp/bio/10/gmo/GMO_000078","label":"Mineral
    source"}]},"literal_excerpt":"{\n          \"component_name\": \"Na2WO4 x 2 H2O\",\n          \"volume\":
    4,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\":
    \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate
    solution"}},"decision":"correct","rationale":"The source4 mg belongs to the Selenite-tungstate
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored_value":{"value":"4","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source4 mg belongs to the Selenite-tungstate solution stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[25].concentration","stored_value":{"value":"4","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source4 mg belongs to the Selenite-tungstate solution stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose. The raw milligram number stored as G_PER_L
    is also a unit-scale error, independently of the omitted stock dilution."}]},{"quantity_id":"q33","topic":"Selenite-tungstate
    solution \u2014 NaOH","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[2].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"NaOH","volume":0.5,"unit":"g","gmo":"http://purl.jp/bio/10/gmo/GMO_001078","gmo_id":"GMO_001078","label":"Sodium
    hydroxide","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[]},"literal_excerpt":"{\n          \"component_name\": \"NaOH\",\n          \"volume\":
    0.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001078\",\n          \"gmo_id\":
    \"GMO_001078\",\n          \"label\": \"Sodium hydroxide\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    []\n        }","section":{"paragraph_index":8,"subcomponent_name":"Selenite-tungstate
    solution"}},"decision":"correct","rationale":"The source0.5 g belongs to the Selenite-tungstate
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The TOGO
    table supplies1000 ml water without an explicit makeup instruction; current DSM/API
    declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source0.5 g belongs to the Selenite-tungstate solution stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[26].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source0.5 g belongs to the Selenite-tungstate solution stock batch, not a root
    ingredient concentration. Restore stock placement and source units before applying
    its separately stated receiving dose."}]},{"quantity_id":"q34","topic":"Vitamin
    solution \u2014 Distilled water","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[0]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Distilled
    water","volume":1000,"unit":"ml","gmo":"http://purl.jp/bio/10/gmo/GMO_001001","gmo_id":"GMO_001001","label":"Distilled
    water","properties":[{"id":"GMO_000040","uri":"http://purl.jp/bio/10/gmo/GMO_000040","label":"Inorganic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000044","uri":"http://purl.jp/bio/10/gmo/GMO_000044","label":"Solvating
    media"}]},"literal_excerpt":"{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"add","rationale":"This1000 ml is solvent for the separate
    Vitamin solution stock. Represent it within that stock, never in the main3990
    G_PER_L sum. The TOGO table supplies1000 ml water without an explicit makeup instruction;
    current DSM/API declares1000 ml stock volume. Preserve that distinction.","layer_assessments":[]},{"quantity_id":"q35","topic":"Vitamin
    solution \u2014 Biotin","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Biotin","volume":2,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001025","gmo_id":"GMO_001025","label":"Biotin","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\":
    \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source2 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[27].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source2 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q36","topic":"Vitamin
    solution \u2014 p-Aminobenzoic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[2]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"p-Aminobenzoic
    acid","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001026","gmo_id":"GMO_001026","label":"4-Aminobenzoic
    acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"p-Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\":
    \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[28].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q37","topic":"Vitamin
    solution \u2014 Thiamine-HCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Thiamine-HCl","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001027","gmo_id":"GMO_001027","label":"Thiamine
    hydrochloride","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Thiamine-HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\":
    \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[29].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q38","topic":"Vitamin
    solution \u2014 Pyridoxine-HCl","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[4]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Pyridoxine-HCl","volume":10,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001029","gmo_id":"GMO_001029","label":"Pyridoxine
    hydrochloride","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Pyridoxine-HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\":
    \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source10 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[30].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source10 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[30].concentration","stored_value":{"value":"10","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source10 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q39","topic":"Vitamin
    solution \u2014 Folic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[5]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Folic
    acid","volume":2,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001033","gmo_id":"GMO_001033","label":"Folic
    acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\":
    \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source2 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[31].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source2 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[31].concentration","stored_value":{"value":"2","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source2 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q40","topic":"Vitamin
    solution \u2014 Vitamin B12","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[6]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Vitamin
    B12","volume":0.1,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001034","gmo_id":"GMO_001034","label":"Cobalamin","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\":
    \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source0.1 mg belongs to the
    Vitamin solution stock batch, not a root ingredient concentration. Restore stock
    placement and source units before applying its separately stated receiving dose.
    The raw milligram number stored as G_PER_L is also a unit-scale error, independently
    of the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[32].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source0.1 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[32].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source0.1 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q41","topic":"Vitamin
    solution \u2014 Riboflavin","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[7]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Riboflavin","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001037","gmo_id":"GMO_001037","label":"Riboflavin","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\":
    \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[33].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[33].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q42","topic":"Vitamin
    solution \u2014 Nicotinic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[8]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Nicotinic
    acid","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001038","gmo_id":"GMO_001038","label":"Nicotinic
    acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\":
    \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[34].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[34].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q43","topic":"Vitamin
    solution \u2014 Lipoic acid","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[9]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"Lipoic
    acid","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001699","gmo_id":"GMO_001699","label":"Lipoic
    acid","properties":[{"id":"GMO_000041","uri":"http://purl.jp/bio/10/gmo/GMO_000041","label":"Organic
    compound"},{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"},{"id":"GMO_000049","uri":"http://purl.jp/bio/10/gmo/GMO_000049","label":"Simple
    component"}],"roles":[{"id":"GMO_000067","uri":"http://purl.jp/bio/10/gmo/GMO_000067","label":"Growth
    factor"}]},"literal_excerpt":"{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\":
    \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[35].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[35].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q44","topic":"Vitamin
    solution \u2014 D-Ca-pantothenate","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.components[3].items[10]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"component_name":"D-Ca-pantothenate","volume":5,"unit":"mg","gmo":"http://purl.jp/bio/10/gmo/GMO_001940","gmo_id":"GMO_001940","label":"D-Calcium
    pantothenate","properties":[{"id":"GMO_000046","uri":"http://purl.jp/bio/10/gmo/GMO_000046","label":"Defined
    component"}],"roles":[{"id":"GMO_000045","uri":"http://purl.jp/bio/10/gmo/GMO_000045","label":"Vitamin"}]},"literal_excerpt":"{\n          \"component_name\":
    \"D-Ca-pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001940\",\n          \"gmo_id\": \"GMO_001940\",\n          \"label\":
    \"D-Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\":
    \"Vitamin\"\n            }\n          ]\n        }","section":{"paragraph_index":10,"subcomponent_name":"Vitamin
    solution"}},"decision":"correct","rationale":"The source5 mg belongs to the Vitamin
    solution stock batch, not a root ingredient concentration. Restore stock placement
    and source units before applying its separately stated receiving dose. The raw
    milligram number stored as G_PER_L is also a unit-scale error, independently of
    the omitted stock dilution. This is the TOGO1x stock. The current DSM10x stock
    has tenfold component masses and a tenfold smaller receiving volume; keep matched
    stock strength/dose pairs. The TOGO table supplies1000 ml water without an explicit
    makeup instruction; current DSM/API declares1000 ml stock volume. Preserve that
    distinction.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ingredients[36].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ingredients[36].concentration","stored_value":{"value":"5","unit":"G_PER_L"},"decision":"correct","rationale":"The
    source5 mg belongs to the Vitamin solution stock batch, not a root ingredient
    concentration. Restore stock placement and source units before applying its separately
    stated receiving dose. The raw milligram number stored as G_PER_L is also a unit-scale
    error, independently of the omitted stock dilution. This is the TOGO1x stock.
    The current DSM10x stock has tenfold component masses and a tenfold smaller receiving
    volume; keep matched stock strength/dose pairs."}]},{"quantity_id":"q45","topic":"Current
    DSM Wolin10x comparison \u2014 Biotin","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[0]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":1,"compound":"Biotin","compound_id":46,"amount":20,"unit":"mg","g_l":0.02,"mmol_l":0.0818632,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 20 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q46","topic":"Current
    DSM Wolin10x comparison \u2014 Folic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[1]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":2,"compound":"Folic
    acid","compound_id":138,"amount":20,"unit":"mg","g_l":0.02,"mmol_l":0.0453104,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 20 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q47","topic":"Current
    DSM Wolin10x comparison \u2014 Pyridoxine hydrochloride","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[2]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":3,"compound":"Pyridoxine
    hydrochloride","compound_id":519,"amount":100,"unit":"mg","g_l":0.1,"mmol_l":0.486287,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 100 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q48","topic":"Current
    DSM Wolin10x comparison \u2014 Thiamine HCl","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[3]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":4,"compound":"Thiamine
    HCl","compound_id":1207,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.148236,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q49","topic":"Current
    DSM Wolin10x comparison \u2014 Riboflavin","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[4]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":5,"compound":"Riboflavin","compound_id":136,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.132837,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q50","topic":"Current
    DSM Wolin10x comparison \u2014 Nicotinic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[5]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":6,"compound":"Nicotinic
    acid","compound_id":139,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.406141,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q51","topic":"Current
    DSM Wolin10x comparison \u2014 Calcium D-(+)-pantothenate","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[6]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":7,"compound":"Calcium
    D-(+)-pantothenate","compound_id":1512,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.209846,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q52","topic":"Current
    DSM Wolin10x comparison \u2014 Vitamin B12","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[7]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":8,"compound":"Vitamin
    B12","compound_id":18,"amount":1,"unit":"mg","g_l":0.001,"mmol_l":0.00073779,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 1 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q53","topic":"Current
    DSM Wolin10x comparison \u2014 p-Aminobenzoic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[8]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":9,"compound":"p-Aminobenzoic
    acid","compound_id":47,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.364591,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q54","topic":"Current
    DSM Wolin10x comparison \u2014 (DL)-alpha-Lipoic acid","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[9]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":10,"compound":"(DL)-alpha-Lipoic
    acid","compound_id":252,"amount":50,"unit":"mg","g_l":0.05,"mmol_l":0.24233,"optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 50 mg in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together.","layer_assessments":[]},{"quantity_id":"q55","topic":"Current
    DSM Wolin10x comparison \u2014 Distilled water","source":{"evidence_id":"api124","reference":"https://mediadive.dsmz.de/rest/medium/124","raw_path":"REVIEW_WORK/batch075/source09/api124.raw","raw_sha256":"24781681a0b4ef0d46fe505d0abd8b8ce1372f8e9bd00aa0a41d29def94ac851","locator":"$.data.solutions[3].recipe[10]","accessed_at":"2026-10-28T18:56:02.450935Z","source_object":{"recipe_order":11,"compound":"Distilled
    water","compound_id":4,"amount":1000,"unit":"ml","optional":0},"literal_excerpt":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }"},"decision":"evidence_only","rationale":"Current
    DSM/API Wolin10x stock: 1000 ml in provider1000 ml stock, added at1 ml in current
    main recipe. TOGO uses a1x stock at10 ml; preserve corresponding concentration
    and dose together. This is stock water input, not a main ingredient or measured
    final-volume evidence by itself.","layer_assessments":[]},{"quantity_id":"q56","topic":"Linked
    solution4178 \u2014 HCl","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[0]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":1,"compound":"HCl","compound_id":68,"solution":null,"solution_id":null,"condition":null,"attribute":"25%,
    7.7 M","amount":10,"unit":"ml","g_l":2.5,"mmol_l":68.5683,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"HCl\",\n                \"compound_id\": 68,\n                \"solution\":
    null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": \"25%, 7.7 M\",\n                \"amount\":
    10,\n                \"unit\": \"ml\",\n                \"g_l\": 2.5,\n                \"mmol_l\":
    68.5683,\n                \"optional\": 0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"conflict","rationale":"The source gives10 ml HCl25%,7.7
    M into a1000 ml stock. The provider2.5 g/L cannot be accepted without reconciling
    reagent strength:7.7 mol/L \u00d70.010 L gives0.077 mol HCl per stock, about2.8075
    g using OLS36.461 g/mol, versus provider2.5 g. Preserve the explicit reagent volume/strength;
    percentage basis/density is not invented.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[0].concentration","stored_value":{"value":"2.5","unit":"G_PER_L"},"decision":"conflict","rationale":"The
    source gives10 ml HCl25%,7.7 M into a1000 ml stock. The provider2.5 g/L cannot
    be accepted without reconciling reagent strength:7.7 mol/L \u00d70.010 L gives0.077
    mol HCl per stock, about2.8075 g using OLS36.461 g/mol, versus provider2.5 g.
    Preserve the explicit reagent volume/strength; percentage basis/density is not
    invented."}]},{"quantity_id":"q57","topic":"Linked solution4178 \u2014 FeCl2 x
    4 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[1]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":2,"compound":"FeCl2
    x 4 H2O","compound_id":260,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":1.5,"unit":"g","g_l":1.5,"mmol_l":7.54482,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"FeCl2 x 4 H2O\",\n                \"compound_id\":
    260,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 1.5,\n                \"mmol_l\": 7.54482,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[1].concentration","stored_value":{"value":"1.5","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q58","topic":"Linked
    solution4178 \u2014 ZnCl2","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[2]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":3,"compound":"ZnCl2","compound_id":64,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":70,"unit":"mg","g_l":0.07,"mmol_l":0.513573,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"ZnCl2\",\n                \"compound_id\":
    64,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 70,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.07,\n                \"mmol_l\": 0.513573,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[2].concentration","stored_value":{"value":"0.07","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q59","topic":"Linked
    solution4178 \u2014 MnCl2 x 4 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[3]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":4,"compound":"MnCl2
    x 4 H2O","compound_id":36,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":100,"unit":"mg","g_l":0.1,"mmol_l":0.505293,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"MnCl2 x 4 H2O\",\n                \"compound_id\":
    36,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.505293,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[3].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q60","topic":"Linked
    solution4178 \u2014 H3BO3","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[4]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":5,"compound":"H3BO3","compound_id":37,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":6,"unit":"mg","g_l":0.006,"mmol_l":0.0970246,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"H3BO3\",\n                \"compound_id\":
    37,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 6,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.006,\n                \"mmol_l\": 0.0970246,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[4].concentration","stored_value":{"value":"0.006","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q61","topic":"Linked
    solution4178 \u2014 CoCl2 x 6 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[5]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":6,"compound":"CoCl2
    x 6 H2O","compound_id":38,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":190,"unit":"mg","g_l":0.19,"mmol_l":1.46335,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    6,\n                \"compound\": \"CoCl2 x 6 H2O\",\n                \"compound_id\":
    38,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 190,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.19,\n                \"mmol_l\": 1.46335,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[5].concentration","stored_value":{"value":"0.19","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q62","topic":"Linked
    solution4178 \u2014 CuCl2 x 2 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[6]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":7,"compound":"CuCl2
    x 2 H2O","compound_id":39,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":2,"unit":"mg","g_l":0.002,"mmol_l":0.0117314,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    7,\n                \"compound\": \"CuCl2 x 2 H2O\",\n                \"compound_id\":
    39,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 2,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.002,\n                \"mmol_l\": 0.0117314,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[6].concentration","stored_value":{"value":"0.002","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q63","topic":"Linked
    solution4178 \u2014 NiCl2 x 6 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[7]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":8,"compound":"NiCl2
    x 6 H2O","compound_id":40,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":24,"unit":"mg","g_l":0.024,"mmol_l":0.185187,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    8,\n                \"compound\": \"NiCl2 x 6 H2O\",\n                \"compound_id\":
    40,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 24,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.024,\n                \"mmol_l\": 0.185187,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[7].concentration","stored_value":{"value":"0.024","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q64","topic":"Linked
    solution4178 \u2014 Na2MoO4 x 2 H2O","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[8]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":9,"compound":"Na2MoO4
    x 2 H2O","compound_id":9,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":36,"unit":"mg","g_l":0.036,"mmol_l":0.148791,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    9,\n                \"compound\": \"Na2MoO4 x 2 H2O\",\n                \"compound_id\":
    9,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 36,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.036,\n                \"mmol_l\": 0.148791,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"verified","rationale":"Current amount and attached historical
    evidence agree with the fresh provider recipe and declared stock volume. Retain
    this stock-specific quantity; it does not establish the amount or rate in the
    receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[8].concentration","stored_value":{"value":"0.036","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q65","topic":"Linked
    solution4178 \u2014 Distilled water","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe[9]","accessed_at":"2026-10-28T18:56:02.143901Z","source_object":{"recipe_order":10,"compound":"Distilled
    water","compound_id":4,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":990,"unit":"ml","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    10,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 990,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[{"recipe_order":null,"step":"Dissolve
    FeCl2 x 4H2O first in HCl. Then dilute in distilled water and add the remaining
    salts."}]},"decision":"correct","rationale":"Source990 ml water is a stock batch
    solvent input, not990% v/v. DSM124 explicitly makes SL10 up to1000 ml after dissolving
    salts; preserve water input and final makeup as separate facts.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"composition[9].concentration","stored_value":{"value":"990","unit":"PERCENT_V_V"},"decision":"correct","rationale":"Source990
    ml water is a stock batch solvent input, not990% v/v. DSM124 explicitly makes
    SL10 up to1000 ml after dissolving salts; preserve water input and final makeup
    as separate facts."}]},{"quantity_id":"q66","topic":"Linked solution4178 placeholder","source":{"evidence_id":"solution4178","reference":"https://mediadive.dsmz.de/rest/solution/4178","raw_path":"REVIEW_WORK/batch075/source09/solution4178.raw","raw_sha256":"7f9c7798263a6d818cfba38c5618fde4aa106a881b0413b50ff72da4f80a03da","locator":"$.data.recipe
    complete ingredient inventory","accessed_at":"2026-10-28T18:56:02.143901Z"},"decision":"not_quantified","rationale":"This
    VARIABLE placeholder is not a source ingredient and contributes no quantity. The
    complete composition array already defines the stock; reconcile placeholder/incomplete
    flags during separate stock curation. It is not evidence for an unknown chemical
    dose.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"not_quantified","rationale":"This
    VARIABLE placeholder is not a source ingredient and contributes no quantity. The
    complete composition array already defines the stock; reconcile placeholder/incomplete
    flags during separate stock curation. It is not evidence for an unknown chemical
    dose."}]},{"quantity_id":"q67","topic":"Linked solution6241 \u2014 Cyanocobalamine","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[0]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":2,"compound":"Cyanocobalamine","compound_id":847,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":10,"unit":"mg","g_l":0.1,"mmol_l":0.073779,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Cyanocobalamine\",\n                \"compound_id\":
    847,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.073779,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make
    up to 100 ml with distilled water."}]},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium. The existing0.1 g/L is correct for10
    mg in100 ml, but authenticates only the separate three-vitamin stock.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[0].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium. The existing0.1 g/L is correct for10
    mg in100 ml, but authenticates only the separate three-vitamin stock."}]},{"quantity_id":"q68","topic":"Linked
    solution6241 \u2014 Thiamine HCl","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[1]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":3,"compound":"Thiamine
    HCl","compound_id":1207,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":10,"unit":"mg","g_l":0.1,"mmol_l":0.296472,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Thiamine HCl\",\n                \"compound_id\":
    1207,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 10,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.1,\n                \"mmol_l\": 0.296472,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make
    up to 100 ml with distilled water."}]},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium. The existing0.1 g/L is correct for10
    mg in100 ml, but authenticates only the separate three-vitamin stock.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[1].concentration","stored_value":{"value":"0.1","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium. The existing0.1 g/L is correct for10
    mg in100 ml, but authenticates only the separate three-vitamin stock."}]},{"quantity_id":"q69","topic":"Linked
    solution6241 \u2014 Biotin","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[2]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":4,"compound":"Biotin","compound_id":46,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":200,"unit":"\u03bcg","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Biotin\",\n                \"compound_id\":
    46,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 200,\n                \"unit\":
    \"\\u03bcg\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make
    up to 100 ml with distilled water."}]},"decision":"correct","rationale":"Source200
    micrograms biotin with an explicit100 ml final makeup gives0.0002 g /0.1 L =0.002
    g/L. Current2000 G_PER_L is unsupported by six orders of magnitude. The provider
    g_l is null, explaining why the guarded historical writer left it unresolved;
    the primary makeup step now permits this manual derivation. This distinct stock
    must still be unlinked from the selected medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[2].concentration","stored_value":{"value":"2000.0","unit":"G_PER_L"},"decision":"correct","rationale":"Source200
    micrograms biotin with an explicit100 ml final makeup gives0.0002 g /0.1 L =0.002
    g/L. Current2000 G_PER_L is unsupported by six orders of magnitude. The provider
    g_l is null, explaining why the guarded historical writer left it unresolved;
    the primary makeup step now permits this manual derivation. This distinct stock
    must still be unlinked from the selected medium."}]},{"quantity_id":"q70","topic":"Linked
    solution6241 \u2014 Distilled water","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe[3]","accessed_at":"2026-10-28T18:56:02.144038Z","source_object":{"recipe_order":5,"compound":"Distilled
    water","compound_id":4,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":100,"unit":"ml","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    5,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 100,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":100,"source_steps":[{"recipe_order":null,"step":"Make
    up to 100 ml with distilled water."}]},"decision":"correct","rationale":"The exact
    source step is make up to100 ml with distilled water, not1000% v/v. Represent
    solvent as quantity sufficient to the100 ml final stock volume; do not assert
    that exactly100 ml must be added after solutes. This is the separate three-vitamin
    stock.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"composition[3].concentration","stored_value":{"value":"1000.0","unit":"PERCENT_V_V"},"decision":"correct","rationale":"The
    exact source step is make up to100 ml with distilled water, not1000% v/v. Represent
    solvent as quantity sufficient to the100 ml final stock volume; do not assert
    that exactly100 ml must be added after solutes. This is the separate three-vitamin
    stock."}]},{"quantity_id":"q71","topic":"Linked solution6241 placeholder","source":{"evidence_id":"solution6241","reference":"https://mediadive.dsmz.de/rest/solution/6241","raw_path":"REVIEW_WORK/batch075/source09/solution6241.raw","raw_sha256":"d3f3868c63c222e602cc1c7d6fa8c0bc395005f8ed2f91f9c92e9fc782d26ab1","locator":"$.data.recipe
    complete ingredient inventory","accessed_at":"2026-10-28T18:56:02.144038Z"},"decision":"not_quantified","rationale":"This
    VARIABLE placeholder is not a source ingredient and contributes no quantity. The
    complete composition array already defines the stock; reconcile placeholder/incomplete
    flags during separate stock curation. It is not evidence for an unknown chemical
    dose.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_6241_Vitamin_solution.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"not_quantified","rationale":"This
    VARIABLE placeholder is not a source ingredient and contributes no quantity. The
    complete composition array already defines the stock; reconcile placeholder/incomplete
    flags during separate stock curation. It is not evidence for an unknown chemical
    dose."}]},{"quantity_id":"q72","topic":"Linked solution5543 \u2014 NaOH","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[0]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":1,"compound":"NaOH","compound_id":256,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":0.5,"unit":"g","g_l":0.5,"mmol_l":12.5009,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    1,\n                \"compound\": \"NaOH\",\n                \"compound_id\":
    256,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 0.5,\n                \"unit\":
    \"g\",\n                \"g_l\": 0.5,\n                \"mmol_l\": 12.5009,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[0].concentration","stored_value":{"value":"0.5","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q73","topic":"Linked
    solution5543 \u2014 Na2SeO3 x 5 H2O","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[1]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":2,"compound":"Na2SeO3
    x 5 H2O","compound_id":107,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":3,"unit":"mg","g_l":0.003,"mmol_l":0.0114062,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    2,\n                \"compound\": \"Na2SeO3 x 5 H2O\",\n                \"compound_id\":
    107,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 3,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.003,\n                \"mmol_l\": 0.0114062,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[1].concentration","stored_value":{"value":"0.003","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q74","topic":"Linked
    solution5543 \u2014 Na2WO4 x 2 H2O","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[2]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":3,"compound":"Na2WO4
    x 2 H2O","compound_id":249,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":4,"unit":"mg","g_l":0.004,"mmol_l":0.0121267,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    3,\n                \"compound\": \"Na2WO4 x 2 H2O\",\n                \"compound_id\":
    249,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 4,\n                \"unit\":
    \"mg\",\n                \"g_l\": 0.004,\n                \"mmol_l\": 0.0121267,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[2].concentration","stored_value":{"value":"0.004","unit":"G_PER_L"},"decision":"verified","rationale":"Current
    amount and attached historical evidence agree with the fresh provider recipe and
    declared stock volume. Retain this stock-specific quantity; it does not establish
    the amount or rate in the receiving medium."}]},{"quantity_id":"q75","topic":"Linked
    solution5543 \u2014 Distilled water","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe[3]","accessed_at":"2026-10-28T18:56:02.208431Z","source_object":{"recipe_order":4,"compound":"Distilled
    water","compound_id":4,"solution":null,"solution_id":null,"condition":null,"attribute":null,"amount":1000,"unit":"ml","g_l":null,"mmol_l":null,"optional":0},"literal_excerpt":"{\n                \"recipe_order\":
    4,\n                \"compound\": \"Distilled water\",\n                \"compound_id\":
    4,\n                \"solution\": null,\n                \"solution_id\": null,\n                \"condition\":
    null,\n                \"attribute\": null,\n                \"amount\": 1000,\n                \"unit\":
    \"ml\",\n                \"g_l\": null,\n                \"mmol_l\": null,\n                \"optional\":
    0\n            }","declared_stock_volume_ml":1000,"source_steps":[]},"decision":"verified","rationale":"The
    existing1 L water is a supported source batch input, already repaired from1000%
    v/v. Retain its evidence; provider1000 ml stock volume is a distinct stated basis,
    not inferred from water alone.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"composition[3].concentration","stored_value":{"value":"1","unit":"L"},"decision":"verified","rationale":"The
    existing1 L water is a supported source batch input, already repaired from1000%
    v/v. Retain its evidence; provider1000 ml stock volume is a distinct stated basis,
    not inferred from water alone."}]},{"quantity_id":"q76","topic":"Linked solution5543
    placeholder","source":{"evidence_id":"solution5543","reference":"https://mediadive.dsmz.de/rest/solution/5543","raw_path":"REVIEW_WORK/batch075/source09/solution5543.raw","raw_sha256":"7b5d86f10be6336aedb100e37d264cff76d3fec1bdd37a4de990fd9152e45882","locator":"$.data.recipe
    complete ingredient inventory","accessed_at":"2026-10-28T18:56:02.208431Z"},"decision":"not_quantified","rationale":"This
    VARIABLE placeholder is not a source ingredient and contributes no quantity. The
    complete composition array already defines the stock; reconcile placeholder/incomplete
    flags during separate stock curation. It is not evidence for an unknown chemical
    dose.","layer_assessments":[{"path":"data/normalized_yaml/bacterial/mediadive_5543_Selenite-tungstate_solution.yaml","field_path":"ingredients[0].concentration","stored_value":{"value":"variable","unit":"VARIABLE"},"decision":"not_quantified","rationale":"This
    VARIABLE placeholder is not a source ingredient and contributes no quantity. The
    complete composition array already defines the stock; reconcile placeholder/incomplete
    flags during separate stock curation. It is not evidence for an unknown chemical
    dose."}]},{"quantity_id":"q77","topic":"Main preparation and version boundary","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.comments[1]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"paragraph_index":3,"comment":"Dissolve
    ingredients (except bicarbonate, vitamins, and sulfide) and sparge medium with
    80% N2and 20% CO2 gas mixture for 30 \u2013 45 min to make it anoxic. Add and
    dissolve bicarbonate, then dispense medium under 80% N2and 20% CO2 gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add vitamins and
    sulfide from sterile anoxic stock solutions prepared under 100% N2 gas. The vitamin
    solution should be sterilized by filtration. Prior to use check pH of complete
    medium and adjust to 7.0 - 7.2, if necessary."},"literal_excerpt":"{\n      \"paragraph_index\":
    3,\n      \"comment\": \"Dissolve ingredients (except bicarbonate, vitamins, and
    sulfide) and sparge medium with 80% N2and 20% CO2 gas mixture for 30 \u2013 45
    min to make it anoxic. Add and dissolve bicarbonate, then dispense medium under
    80% N2and 20% CO2 gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Add vitamins and sulfide from sterile anoxic stock solutions prepared
    under 100% N2 gas. The vitamin solution should be sterilized by filtration. Prior
    to use check pH of complete medium and adjust to 7.0 - 7.2, if necessary.\"\n    }"},"decision":"add","rationale":"Restore
    the selected source procedure, pH7.0\u20137.2, gas stages and vitamin filter sterilization.
    Current DSM additionally excludes acetate/butyrate from basal heating, adds them
    later, and adjusts pH7.0 before dispensing. Preserve or explicitly resolve this
    version difference; do not mix portions silently. No exact autoclave temperature/time
    or incubation condition is supplied.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"preparation_steps","stored_value":null,"decision":"add","rationale":"Restore
    the selected source procedure, pH7.0\u20137.2, gas stages and vitamin filter sterilization.
    Current DSM additionally excludes acetate/butyrate from basal heating, adds them
    later, and adjusts pH7.0 before dispensing. Preserve or explicitly resolve this
    version difference; do not mix portions silently. No exact autoclave temperature/time
    or incubation condition is supplied.","missing":true},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"preparation_steps","stored_value":null,"decision":"add","rationale":"Restore
    the selected source procedure, pH7.0\u20137.2, gas stages and vitamin filter sterilization.
    Current DSM additionally excludes acetate/butyrate from basal heating, adds them
    later, and adjusts pH7.0 before dispensing. Preserve or explicitly resolve this
    version difference; do not mix portions silently. No exact autoclave temperature/time
    or incubation condition is supplied.","missing":true}]},{"quantity_id":"q78","topic":"Main
    pH","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.meta","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"gm":"http://togomedium.org/medium/M2526","name":"Desulfofarcimen
    Medium","src_url":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf","ph":"7.0
    - 7.2"},"literal_excerpt":"{\n    \"gm\": \"http://togomedium.org/medium/M2526\",\n    \"name\":
    \"Desulfofarcimen Medium\",\n    \"src_url\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf\",\n    \"ph\":
    \"7.0 - 7.2\"\n  }"},"decision":"add","rationale":"The source meta and complete
    primary recipe state pH7.0\u20137.2. Add a source-linked range using supported
    schema fields; no strain growth inference is needed.","layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOFARCIMEN_MEDIUM.yaml","field_path":"ph_range","stored_value":null,"decision":"add","rationale":"The
    source meta and complete primary recipe state pH7.0\u20137.2. Add a source-linked
    range using supported schema fields; no strain growth inference is needed.","missing":true},{"path":"data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml","field_path":"ph_range","stored_value":null,"decision":"add","rationale":"The
    source meta and complete primary recipe state pH7.0\u20137.2. Add a source-linked
    range using supported schema fields; no strain growth inference is needed.","missing":true}]},{"quantity_id":"q79","topic":"Current
    DSM final volume","source":{"evidence_id":"dsm124","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium124.pdf","raw_path":"REVIEW_WORK/batch075/source09/dsm124.raw","raw_sha256":"a2c8cb38e72919285a4d77c34d34d13655e07cc32c7b07a6ed6ebf353dfec62a","locator":"Page1
    heading: Final volume1003 ml","accessed_at":"2026-10-28T18:56:02.654828Z"},"decision":"evidence_only","rationale":"The
    current DSM124 explicitly declares final1003 ml, and API Main sol.124 volume equals1003.
    This is an authoritative version-specific denominator, not the arithmetic sum
    of water and nominal additions and not automatically the older TOGO denominator.","layer_assessments":[]},{"quantity_id":"q80","topic":"SL10
    stock makeup","source":{"evidence_id":"togo2526","reference":"https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2526","raw_path":"REVIEW_WORK/batch075/source09/togo2526.raw","raw_sha256":"92529942b4def42cb82107726e6d6459fa6089844f06184b834f29153a144236","locator":"$.comments[3]","accessed_at":"2026-10-28T18:56:02.830691Z","source_object":{"paragraph_index":6,"comment":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.0 ml."},"literal_excerpt":"{\n      \"paragraph_index\":
    6,\n      \"comment\": \"First dissolve FeCl2 in the HCl, then dilute in water,
    add and dissolve the other salts. Finally make up to 1000.0 ml.\"\n    }"},"decision":"add","rationale":"Explicit
    final makeup to1000 ml supports SL10 stock mass concentrations; retain separately
    from990 ml initial water and1 ml receiving dose.","layer_assessments":[]}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: Every selected target/owner asserted ID-label slot and the18 scoped dependency
    composition rows are inventoried against fresh OLS and exact currentMIM rows.
    Nickel hexahydrate is wrongly mapped to anhydrous34887, and the legacybutyrate
    secondary link is absent from the current catalog. Calcium pantothenate31345 preservesD
    stereochemistry. VitaminB12 remains the source-supported broad class rather than
    an invented cyanocobalamin assignment. Current mapped, rejected and ontology-linked
    catalog rows are distinguished; no historic identifier validity is inferred.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete selected histories have14 target and13 owner events, with only
    the merge event and generated lineage/fingerprint differing. The selected target
    and owner historical reports match current bytes and checked0/41 source claims
    each; the000709 alias report checked0/35 and is a distinct historical merge. All
    three standalone stock after hashes and source digests match current bytes, with21
    historical claims and14 attached excerpts authenticated. Current writer readings
    are credited without inferring past execution.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - history
  - scalars
  - history-plan-1
  - history-plan-2
  - history-plan-3
  - solution4178
  - solution5543
  - solution6241
- assessment_id: a7
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:009096
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009096-stock-boundaries-and-units-corrupt-the-receiving-recipe
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock boundaries and units corrupt the receiving recipe
  description: Both selected layers flatten22 stock solutes into root ingredients
    and sum four stock/main water inputs to3990 G_PER_L. Milligram stock numbers become
    G_PER_L, four stock millilitre doses become mass concentrations, and12 basal batch
    masses lack the TOGO final-volume basis. Correct stock quantities already present
    in4178/5543 do not authorize root stock concentrations. The exact inventory separates
    every current field, existing repair and source version.
  target_ids:
  - CultureMech:009096
  field_paths:
  - ingredients[*].concentration
  - solutions[*].concentration
  evidence_ids:
  - togo2526
  - dsm124
  - api124
  - quantities
  - dependency-1
  - dependency-3
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-009096-vitamin-link-points-to-a-different-formulation
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Vitamin link points to a different formulation
  description: The selected vitamin descriptor links mediadive.solution:6241, a100
    ml stock containing only cyanocobalamin, thiamine HCl and biotin. TOGO specifies
    ten vitamins at1x/10 ml and currentDSM ten vitamins at10x/1 ml. Their matched
    strength/dose pairs are nominally mass-equivalent; the wrong6241 identity is independent
    of that version difference.
  target_ids:
  - CultureMech:009096
  field_paths:
  - solutions[3].term
  - solutions[3].name
  - solutions[3].concentration
  evidence_ids:
  - togo2526
  - dsm124
  - api124
  - solution6241
  - dependency-2
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-009096-preparation-and-ph-are-absent
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preparation and pH are absent
  description: Both selected layers omit the source pH7.0–7.2 and preparation, including80:20
    gas handling, staged bicarbonate and late additions, and vitamin filtration. CurrentDSM
    moves acetate/butyrate to late additions and adds an initialpH7.0 adjustment relative
    toTOGO. Current importer already captures comments; persisted records remain stale.
  target_ids:
  - CultureMech:009096
  field_paths:
  - ph_range
  - preparation_steps
  evidence_ids:
  - togo2526
  - dsm124
  - writer-1
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-009096-nickel-hydrate-is-mapped-to-anhydrous-nickel-chloride
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate is mapped to anhydrous nickel chloride
  description: 'NiCl2 x6H2O in the source and both selected layers is mapped in primary
    and secondary slots toCHEBI34887, whose formulaCl2Ni omits six waters. The linkedSL10
    stock repeats this mapping. CurrentCHEBI53542 denotes the required hexahydrate.
    Calcium pantothenateCHEBI31345 is supported: despite its broad label, current
    synonyms and stereochemical structure identify theD form; no pantothenate correction
    is asserted.'
  target_ids:
  - CultureMech:009096
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml::composition[7].chebi_term
  evidence_ids:
  - togo2526
  - dsm124
  - grounding
  - ols34887
  - ols53542
  - ols31345
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-009096-high-metal-annotation-depends-on-corrupted-quantities
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: High-metal annotation depends on corrupted quantities
  description: high_metal=true is a quantitative annotation defined by the schema90th-percentile
    metal threshold. Both selected layers contain mis-scaled undiluted stock amounts,
    so this annotation lacks a reliable receiving-medium concentration basis. Do not
    simply flip it tofalse before correcting quantities and rerunning the documented
    analysis.
  target_ids:
  - CultureMech:009096
  field_paths:
  - high_metal
  evidence_ids:
  - local-target
  - owner-1
  - quantities
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f6
  issue_key: culturemech-009096-legacy-sodium-butyrate-linkage-remains
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy sodium butyrate linkage remains
  description: Both layers retainMediaIngredientMech000481 while their primaryCHEBI64103
    correctly denotes sodium butyrate. The packaged current catalog has no exact legacy
    row and provides mappedNa-butyrateCHEBI64103. This is a current secondary-link
    maintenance gap, not proof that the historical identifier was never valid.
  target_ids:
  - CultureMech:009096
  field_paths:
  - ingredients[12].mediaingredientmech_term
  evidence_ids:
  - grounding
  - ols64103
  - writer-7
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f7
  issue_key: culturemech-009096-selected-scientific-claims-lack-attached-source-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Selected scientific claims lack attached source evidence
  description: The selected target and maintained contributor contain source URLs
    and histories but no attached claim evidence or references. Canonical reference
    validation checked zero references. Older selected-layer reports likewise made
    zero external checks. Existing source-backed stock claims must be retained at
    their stock scope while evidence is added for corrected main quantities, source
    version, preparation and pH. Attach stock-dose and preparation claims in root
    evidence with exact solution/stage locators; SolutionDescriptor has no evidence
    slot.
  target_ids:
  - CultureMech:009096
  field_paths:
  - evidence
  - references
  - ingredients[*].evidence
  evidence_ids:
  - local-target
  - owner-1
  - history-report-4
  - history-report-6
  - togo2526
  - dsm124
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Restore main versus stock structure, batch solvent inputs, milligram
    units and stock addition volumes in the maintainedTOGO contributor. Preserve authenticated
    stock rates and resolve remaining stock-water/HCl issues before reuse. Select
    and cite a consistent TOGO/currentDSM version; do not transfer1003 ml silently.
    Credit current importer fixes and review remaining denominator assumptions, then
    regenerate compatibly.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/togo_importer.py
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Replace the incorrect reference with the exact source ten-vitamin definition/link
    and retain matched strength, dose and version. Do not rewrite the independent6241
    stock into the medium vitamin recipe. Resolve all Unknown solution labels and
    keep the0.1% w/v resazurin strength explicit.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Restore source-linked structuredpH and full preparation from the explicitly
    chosen source version. Preserve main versus stock atmosphere and sterilization
    stages. Do not infer autoclave temperature/time or incubation conditions. Regenerate
    after maintained input curation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Correct the nickel source-form mapping in the maintained contributor
    and any reusedSL10 stock. Verify the canonical53542 label; reconcile the rejected
    currentMIM lexical row separately rather than forcing a secondaryMIM mapping.
    Preserve the supportedD-calcium pantothenate identity.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/mediadive_4178_Trace_element_solution_SL-10.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: After source-scoped quantities and stock dilution are corrected, recompute
    the high_metal annotation with its native definition and preserve calculation
    provenance; withhold a supported scientific interpretation until then.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:009096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action6
  description: Reconcile the legacy secondary slot to the exact current supported
    catalog key/label, preserving the already correct primary chemical identity and
    append-only provenance. Do not infer a replacement from a fuzzy name match.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:009096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action7
  description: The selected target and maintained contributor contain source URLs
    and histories but no attached claim evidence or references. Canonical reference
    validation checked zero references. Older selected-layer reports likewise made
    zero external checks. Existing source-backed stock claims must be retained at
    their stock scope while evidence is added for corrected main quantities, source
    version, preparation and pH.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:009096
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2526_Desulfofarcimen_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- CurrentDSM1003 ml is an explicitly declared version-specific denominator; the olderTOGO
  formulation does not independently declare final medium makeup. Water plus additions
  is not a measured final volume. Nominal vitamin mass equivalence requires matched1
  L stock basis and strength/dose pairs.
- HCl25% has no stated percentage basis/density. Explicit7.7 M and10 ml support a
  molar input; the provider2.5 g/L requires reconciliation. No invented density or
  blanket percentage conversion is used.
- The three linked solutions are scoped dependencies, not additional review targets.6241
  remains a different stock even if its own quantities are corrected. Historical reports
  about other media do not establish formulation equivalence.
- No strain-specific growth claim or experimental optimization is inferred. CurrentDSM
  strain replacement instructions remain separate variants. No recipe, source file,
  identifier or generated page was changed.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation
  or publication.
```
