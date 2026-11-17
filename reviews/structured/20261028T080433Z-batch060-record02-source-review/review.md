# Carnobacterium Pleistocaenium Medium: restore source units and scoped dependencies

- Review: 20261028T080433Z-batch060-record02-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T07:46:03.954885Z
- Finished UTC: 2026-10-28T08:04:33.456937Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M374 is the JCM379 source lineage. Five stored amount/unit pairs are wrong, ten further mass-per-liter assertions lack the asserted denominator, both named stock references are empty shells, and source preparation/pH are absent. Current M190 vitamin repairs are credited; the M221 trace dependency has separate topology, source-conflict and nickel-form limits.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch060 native selection index 02.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009755 | data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml | generated | carnobacterium_pleistocaenium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009755 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:009755 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:009755 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:009755 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### JCM and TOGO namespace

identity: supported. Targets: CultureMech:009755.

M374 explicitly identifies JCM_M379; M190 is JCM197 and M221 is JCM228. The dependency references select vitamin and trace-mineral subsections, not their parent media. The current generated record has one maintained owner. Source-name spelling is retained without inferring a strain-growth assertion or forced duplicate merge.

### Source process and existing repairs

completeness: concern. Targets: CultureMech:009755.

Current M190 vitamin batch notes and water are already repaired and credited. M374 still lacks its preparation/pH and stock definitions. Current importer stages and merge compatibility guards reduce recurrence; they do not prove historical execution or authorize a source-variant collapse.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:009755.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Distilled water", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The source gives 1 L as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 1 L as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 1 L as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled."}]}, {"quantity_id": "q2", "topic": "MgSO4・7H2O", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\": \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "MgSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001002", "gmo_id": "GMO_001002", "label": "Magnesium sulfate heptahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.098912,\n                        \"mmol_l\": 0.401305,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.1, "unit": "g", "g_l": 0.098912, "mmol_l": 0.401305, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 0.1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q3", "topic": "NaCl", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\": \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NaCl", "volume": 5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001004", "gmo_id": "GMO_001004", "label": "Sodium chloride", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9456,\n                        \"mmol_l\": 84.6269,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "NaCl", "compound_id": 43, "amount": 5, "unit": "g", "g_l": 4.9456, "mmol_l": 84.6269, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 5 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q4", "topic": "KH2PO4", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\": \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KH2PO4", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001006", "gmo_id": "GMO_001006", "label": "Potassium phosphate monobasic", "properties": [{"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.296736,\n                        \"mmol_l\": 2.1805,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "KH2PO4", "compound_id": 11, "amount": 0.3, "unit": "g", "g_l": 0.296736, "mmol_l": 2.1805, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q5", "topic": "NH4Cl", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\": \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NH4Cl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001008", "gmo_id": "GMO_001008", "label": "Ammonium chloride", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000062", "uri": "http://purl.jp/bio/10/gmo/GMO_000062", "label": "Nitrogen source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\": 18.4917,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "NH4Cl", "compound_id": 42, "amount": 1, "unit": "g", "g_l": 0.98912, "mmol_l": 18.4917, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q6", "topic": "D--Glucose", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"D--Glucose\",\n          \"volume\": 5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001010\",\n          \"gmo_id\": \"GMO_001010\",\n          \"label\": \"D-Glucose\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\": \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "D--Glucose", "volume": 5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001010", "gmo_id": "GMO_001010", "label": "D-Glucose", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063", "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.9456,\n                        \"mmol_l\": 27.4511,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "D-Glucose", "compound_id": 211, "amount": 5, "unit": "g", "g_l": 4.9456, "mmol_l": 27.4511, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 5 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q7", "topic": "Resazurin", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\": 1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\": \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\": \"pH dependent redox indicator\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Resazurin", "volume": 1, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001012", "gmo_id": "GMO_001012", "label": "Resazurin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}], "roles": [{"id": "GMO_000055", "uri": "http://purl.jp/bio/10/gmo/GMO_000055", "label": "pH dependent redox indicator"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.00098912,\n                        \"mmol_l\": 0.00431572,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound": "Resazurin", "compound_id": 25, "amount": 1, "unit": "mg", "g_l": 0.00098912, "mmol_l": 0.00431572, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The source gives 1 mg as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 1 mg as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 1 mg as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled."}]}, {"quantity_id": "q8", "topic": "Na2S・9H2O", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Na2S・9H2O\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\": \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\": \"Reducing agent\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2S・9H2O", "volume": 0.4, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001014", "gmo_id": "GMO_001014", "label": "Sodium sulfide nonahydrate", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}], "roles": [{"id": "GMO_000064", "uri": "http://purl.jp/bio/10/gmo/GMO_000064", "label": "Reducing agent"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.395648,\n                        \"mmol_l\": 1.64728,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 0.4, "unit": "g", "g_l": 0.395648, "mmol_l": 1.64728, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q9", "topic": "KCl", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\": \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KCl", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001017", "gmo_id": "GMO_001017", "label": "Potassium chloride", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.296736,\n                        \"mmol_l\": 3.98036,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "KCl", "compound_id": 61, "amount": 0.3, "unit": "g", "g_l": 0.296736, "mmol_l": 3.98036, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q10", "topic": "NaHCO3", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"NaHCO3\",\n          \"volume\": 0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\": \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\": \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NaHCO3", "volume": 0.4, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001019", "gmo_id": "GMO_001019", "label": "Sodium bicarbonate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038", "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.395648,\n                        \"mmol_l\": 4.7097,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "NaHCO3", "compound_id": 55, "amount": 0.4, "unit": "g", "g_l": 0.395648, "mmol_l": 4.7097, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q11", "topic": "CaSO4・2H2O", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"CaSO4・2H2O\",\n          \"volume\": 12.5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001087\",\n          \"gmo_id\": \"GMO_001087\",\n          \"label\": \"Calcium sulfate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CaSO4・2H2O", "volume": 12.5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001087", "gmo_id": "GMO_001087", "label": "Calcium sulfate dihydrate", "properties": [{"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaSO4 x 2 H2O\",\n                        \"compound_id\": 190,\n                        \"amount\": 12.5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.012364,\n                        \"mmol_l\": 0.0718119,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "CaSO4 x 2 H2O", "compound_id": 190, "amount": 12.5, "unit": "mg", "g_l": 0.012364, "mmol_l": 0.0718119, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The source gives 12.5 mg as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "12.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 12.5 mg as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "12.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 12.5 mg as a batch input, not the stored G_PER_L value. Preserve water as volume or the stated mg amount; do not infer a final liter. The provider's separate declared normalization remains explicitly labelled."}]}, {"quantity_id": "q12", "topic": "Yeast extract (BD-Difco)", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[11]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\": \"GMO_001018\",\n          \"label\": \"Bacto &amp;trade; Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Yeast extract (BD-Difco)", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001018", "gmo_id": "GMO_001018", "label": "Bacto &amp;trade; Yeast extract", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.197824,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Yeast extract", "compound_id": 16, "attribute": "BD-Difco", "amount": 0.2, "unit": "g", "g_l": 0.197824, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 0.2 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.2 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 0.2 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q13", "topic": "Bacto peptone (BD-Difco)", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[12]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Bacto peptone (BD-Difco)\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001089\",\n          \"gmo_id\": \"GMO_001089\",\n          \"label\": \"Bacto &amp;trade; Peptone\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Bacto peptone (BD-Difco)", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001089", "gmo_id": "GMO_001089", "label": "Bacto &amp;trade; Peptone", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Bacto peptone\",\n                        \"compound_id\": 19,\n                        \"attribute\": \"BD-Difco\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Bacto peptone", "compound_id": 19, "attribute": "BD-Difco", "amount": 1, "unit": "g", "g_l": 0.98912, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "The source supports 1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 1 g per recipe batch, but not this same number as G_PER_L. One liter of water plus stock additions does not establish final volume; current provider explicitly declares a different g_l on its1011 ml basis. Preserve source batch support separately, not an unqualified local concentration."}]}, {"quantity_id": "q14", "topic": "N2", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[15]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\": \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "N2", "gmo": "http://purl.jp/bio/10/gmo/GMO_002261", "gmo_id": "GMO_002261", "label": "Nitrogen gas", "properties": [{"id": "GMO_000077", "uri": "http://purl.jp/bio/10/gmo/GMO_000077", "label": "Gas"}], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Nitrogen is explicitly used during preparation; VARIABLE has no measured gas amount. Retain this as preparation context without treating it as a quantified medium ingredient.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "evidence_only", "rationale": "Nitrogen is explicitly used during preparation; VARIABLE has no measured gas amount. Retain this as preparation context without treating it as a quantified medium ingredient."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "evidence_only", "rationale": "Nitrogen is explicitly used during preparation; VARIABLE has no measured gas amount. Retain this as preparation context without treating it as a quantified medium ingredient."}]}, {"quantity_id": "q15", "topic": "Trace vitamins (see Medium [M190])", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id": "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "solution": "Trace vitamins", "solution_id": 3861, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The source explicitly adds 10 ml of the named stock per receiving batch. Correct the stored G_PER_L unit to an actual stock addition volume; preserve the reference namespace and do not inherit the parent medium's receiving dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 10 ml of the named stock per receiving batch. Correct the stored G_PER_L unit to an actual stock addition volume; preserve the reference namespace and do not inherit the parent medium's receiving dose."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 10 ml of the named stock per receiving batch. Correct the stored G_PER_L unit to an actual stock addition volume; preserve the reference namespace and do not inherit the parent medium's receiving dose."}]}, {"quantity_id": "q16", "topic": "Existing stock1 name", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id": "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "Replace the placeholder Unknown solution with the exact referenced stock name; retain the already informative preferred_term.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Replace the placeholder Unknown solution with the exact referenced stock name; retain the already informative preferred_term."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Replace the placeholder Unknown solution with the exact referenced stock name; retain the already informative preferred_term."}]}, {"quantity_id": "q17", "topic": "Existing stock1 composition", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id": "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Resolve only the referenced vitamin or trace-mineral subsection; the existing empty composition supplies no stock chemistry.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Resolve only the referenced vitamin or trace-mineral subsection; the existing empty composition supplies no stock chemistry."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[0].composition", "stored_value": [], "decision": "add", "rationale": "Resolve only the referenced vitamin or trace-mineral subsection; the existing empty composition supplies no stock chemistry."}]}, {"quantity_id": "q18", "topic": "Existing stock1 preferred_term", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\": 10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id": "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current preferred_term already preserves the stock identity and TOGO reference; credit it.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[0].preferred_term", "stored_value": "Trace vitamins (see Medium [M190])", "decision": "evidence_only", "rationale": "The current preferred_term already preserves the stock identity and TOGO reference; credit it."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[0].preferred_term", "stored_value": "Trace vitamins (see Medium [M190])", "decision": "evidence_only", "rationale": "The current preferred_term already preserves the stock identity and TOGO reference; credit it."}]}, {"quantity_id": "q19", "topic": "Trace minerals solution (see Medium [M221])", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Trace minerals solution\",\n                        \"solution_id\": 3903,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "solution": "Trace minerals solution", "solution_id": 3903, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "The source explicitly adds 1 ml of the named stock per receiving batch. Correct the stored G_PER_L unit to an actual stock addition volume; preserve the reference namespace and do not inherit the parent medium's receiving dose.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 1 ml of the named stock per receiving batch. Correct the stored G_PER_L unit to an actual stock addition volume; preserve the reference namespace and do not inherit the parent medium's receiving dose."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 1 ml of the named stock per receiving batch. Correct the stored G_PER_L unit to an actual stock addition volume; preserve the reference namespace and do not inherit the parent medium's receiving dose."}]}, {"quantity_id": "q20", "topic": "Existing stock2 name", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "Replace the placeholder Unknown solution with the exact referenced stock name; retain the already informative preferred_term.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Replace the placeholder Unknown solution with the exact referenced stock name; retain the already informative preferred_term."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision": "correct", "rationale": "Replace the placeholder Unknown solution with the exact referenced stock name; retain the already informative preferred_term."}]}, {"quantity_id": "q21", "topic": "Existing stock2 composition", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Resolve only the referenced vitamin or trace-mineral subsection; the existing empty composition supplies no stock chemistry.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[1].composition", "stored_value": [], "decision": "add", "rationale": "Resolve only the referenced vitamin or trace-mineral subsection; the existing empty composition supplies no stock chemistry."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[1].composition", "stored_value": [], "decision": "add", "rationale": "Resolve only the referenced vitamin or trace-mineral subsection; the existing empty composition supplies no stock chemistry."}]}, {"quantity_id": "q22", "topic": "Existing stock2 preferred_term", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "The current preferred_term already preserves the stock identity and TOGO reference; credit it.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "solutions[1].preferred_term", "stored_value": "Trace minerals solution (see Medium [M221])", "decision": "evidence_only", "rationale": "The current preferred_term already preserves the stock identity and TOGO reference; credit it."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "solutions[1].preferred_term", "stored_value": "Trace minerals solution (see Medium [M221])", "decision": "evidence_only", "rationale": "The current preferred_term already preserves the stock identity and TOGO reference; credit it."}]}, {"quantity_id": "q23", "topic": "Vitamin stock: Distilled water", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[0].concentration", "stored_value": {"value": "1", "unit": "L"}, "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q24", "topic": "Vitamin stock: Biotin", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\": \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Biotin", "volume": 2, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001025", "gmo_id": "GMO_001025", "label": "Biotin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.00818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[1].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q25", "topic": "Vitamin stock: p--Aminobenzoic acid", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[2]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\": \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "p--Aminobenzoic acid", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001026", "gmo_id": "GMO_001026", "label": "4-Aminobenzoic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "p-Aminobenzoic acid", "compound_id": 47, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[2].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q26", "topic": "Vitamin stock: Thiamine・HCl", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[3]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\": \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Thiamine・HCl", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001027", "gmo_id": "GMO_001027", "label": "Thiamine hydrochloride", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Thiamine HCl", "compound_id": 1207, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0148236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[3].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q27", "topic": "Vitamin stock: Calcium pantothenate", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[4]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\": \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Calcium pantothenate", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001028", "gmo_id": "GMO_001028", "label": "Calcium pantothenate", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0104925, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[4].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q28", "topic": "Vitamin stock: Pyridoxine・HCl", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[5]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\": 10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\": \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Pyridoxine・HCl", "volume": 10, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001029", "gmo_id": "GMO_001029", "label": "Pyridoxine hydrochloride", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 10,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "amount": 10, "unit": "mg", "g_l": 0.01, "mmol_l": 0.0486287, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[5].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 10 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q29", "topic": "Vitamin stock: Folic acid", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[6]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\": 2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\": \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Folic acid", "volume": 2, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001033", "gmo_id": "GMO_001033", "label": "Folic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Folic acid", "compound_id": 138, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.00453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[6].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 2 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q30", "topic": "Vitamin stock: Vitamin B12", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[7]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\": 0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\": \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Vitamin B12", "volume": 0.1, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001034", "gmo_id": "GMO_001034", "label": "Cobalamin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Vitamin B12", "compound_id": 18, "amount": 0.1, "unit": "mg", "g_l": 0.0001, "mmol_l": 7.3779e-05, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[7].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 0.1 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q31", "topic": "Vitamin stock: Riboflavin", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[8]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\": \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Riboflavin", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001037", "gmo_id": "GMO_001037", "label": "Riboflavin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[8].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q32", "topic": "Vitamin stock: Nicotinic acid", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[9]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\": \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Nicotinic acid", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001038", "gmo_id": "GMO_001038", "label": "Nicotinic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045", "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Nicotinic acid", "compound_id": 139, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.0406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[9].notes", "stored_value": "Role: Vitamin; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q33", "topic": "Vitamin stock: Lipoic acid", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528", "locator": "$.components[1].items[10]", "accessed_at": "2026-10-28T07:48:22.592228Z", "quote": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\": 5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\": \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Lipoic acid", "volume": 5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001699", "gmo_id": "GMO_001699", "label": "Lipoic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000067", "uri": "http://purl.jp/bio/10/gmo/GMO_000067", "label": "Growth factor"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\": 5,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Lipoic acid", "compound_id": 368, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l": 0.024233, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[10].notes", "stored_value": "Role: Growth factor; Properties: Organic compound, Defined component, Simple component\n\nSource batch input: 5 mg. Final preparation volume is not independently established; the unsupported g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.", "decision": "verified", "rationale": "The current dependency repair correctly preserves this source batch amount and withdraws an unsupported final-liter assertion. Credit the existing scoped composition; the parent receiving dose does not transfer. Current JCM197 and provider stock3861 agree on the amount; provider stock g_l remains a separate declared basis. Existing attached claim snippets match the freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id": "q34", "topic": "Trace stock: Na2MoO4・2H2O", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[1]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\": \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2MoO4・2H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001011", "gmo_id": "GMO_001011", "label": "Sodium molybdate dihydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.413309,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.413309, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement."}]}, {"quantity_id": "q35", "topic": "Trace stock: NiCl2・6H2O", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[2]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\": 0.025,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\": \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "NiCl2・6H2O", "volume": 0.025, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001022", "gmo_id": "GMO_001022", "label": "Nickel chloride hexahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.025,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.025,\n                        \"mmol_l\": 0.192903,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.025, "unit": "g", "g_l": 0.025, "mmol_l": 0.192903, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.025", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement."}]}, {"quantity_id": "q36", "topic": "Trace stock: ZnSO4・7H2O", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[3]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\": \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "ZnSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001023", "gmo_id": "GMO_001023", "label": "Zinc sulfate heptahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement."}]}, {"quantity_id": "q37", "topic": "Trace stock: CuSO4・5H2O", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[4]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\": 0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\": \"GMO_001039\",\n          \"label\": \"Copper(II) sulfate pentahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "CuSO4・5H2O", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001039", "gmo_id": "GMO_001039", "label": "Copper(II) sulfate pentahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "CuSO4 x 5 H2O", "compound_id": 121, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0400503, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement."}]}, {"quantity_id": "q38", "topic": "Trace stock: Nitrilotriacetic acid", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[5]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\": 1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\": \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Nitrilotriacetic acid", "volume": 1.5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001053", "gmo_id": "GMO_001053", "label": "Nitrilotriacetic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l": 7.84765, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement."}]}, {"quantity_id": "q39", "topic": "Trace stock: Na2WO4・2H2O", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[6]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"Na2WO4・2H2O\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\": \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2WO4・2H2O", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001057", "gmo_id": "GMO_001057", "label": "Sodium tungstate dihydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 3.03168,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Na2WO4 x 2 H2O", "compound_id": 249, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 3.03168, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement."}]}, {"quantity_id": "q40", "topic": "Trace stock: MnSO4・xH2O", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[7]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\": 0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\": \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "MnSO4・xH2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001065", "gmo_id": "GMO_001065", "label": "Manganese sulfate n-hydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "MnSO4 x n H2O", "compound_id": 1000, "amount": 0.1, "unit": "g", "g_l": 0.1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement."}]}, {"quantity_id": "q41", "topic": "Trace stock: Fe(NH4)2(SO4)2・6H2O", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[8]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"Fe(NH4)2(SO4)2・6H2O\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001076\",\n          \"gmo_id\": \"GMO_001076\",\n          \"label\": \"Ammonium iron(II) sulfate hexahydrate\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Fe(NH4)2(SO4)2・6H2O", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001076", "gmo_id": "GMO_001076", "label": "Ammonium iron(II) sulfate hexahydrate", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Fe(NH4)2(SO4)2 x 6 H2O\",\n                        \"compound_id\": 247,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Fe(NH4)2(SO4)2 x 6 H2O", "compound_id": 247, "amount": 0.2, "unit": "g", "g_l": 0.2, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement. The current cleanup collapsed equal iron entries, but trace stock and the separate parent iron stock are still distinct stages; no iron-stock dose transfers.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock component, not a directly transferable receiving-medium rate. Preserve its source batch amount in the referenced stock and the separate1 ml receiving addition. Explicit API stock g_l does not validate the flattened parent-stage placement. The current cleanup collapsed equal iron entries, but trace stock and the separate parent iron stock are still distinct stages; no iron-stock dose transfers."}]}, {"quantity_id": "q42", "topic": "Trace stock: Na2SeO3", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[9]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"Na2SeO3\",\n          \"volume\": 0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001093\",\n          \"gmo_id\": \"GMO_001093\",\n          \"label\": \"Sodium selenite\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Na2SeO3", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001093", "gmo_id": "GMO_001093", "label": "Sodium selenite", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SeO3\",\n                        \"compound_id\": 699,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Na2SeO3", "compound_id": 699, "amount": 0.1, "unit": "g", "g_l": 0.1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "conflict", "rationale": "TOGO M221 and its local ingredient give0.2 g, while primary JCM228 and current J379/J228 provider trace stock give0.1 g. Preserve this genuine source discrepancy and resolve exact stock identity/version before transfer; do not silently choose the convenient value.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.2", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "TOGO M221 and its local ingredient give0.2 g, while primary JCM228 and current J379/J228 provider trace stock give0.1 g. Preserve this genuine source discrepancy and resolve exact stock identity/version before transfer; do not silently choose the convenient value."}]}, {"quantity_id": "q43", "topic": "Trace-stock water", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[0]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\": 1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\": \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001", "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044", "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].recipe[9]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "One liter of stock water is explicit; it is not the parent water total or an independently stated final-volume makeup. Preserve the solvent within the stock.", "layer_assessments": []}, {"quantity_id": "q44", "topic": "Trace-stock KOH adjustment", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6", "locator": "$.components[2].items[10]", "accessed_at": "2026-10-28T07:48:22.724427Z", "quote": "{\n          \"component_name\": \"KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\": \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name": "KOH", "gmo": "http://purl.jp/bio/10/gmo/GMO_001903", "gmo_id": "GMO_001903", "label": "Potassium hydroxide solution", "properties": [{"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id": "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078", "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Scope KOH to the trace-stock pH procedure; no numeric amount is inferred.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "variable", "unit": "VARIABLE"}, "decision": "evidence_only", "rationale": "VARIABLE is nonquantitative adjustment context only; no KOH dose or concentration is supplied for this stock."}]}, {"quantity_id": "q45", "topic": "Trace-stock pH step 1", "source": [{"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"step\": \"Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH. Then proceed to add minerals.\"\n                    }", "exact_decoded_object": {"step": "Dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH. Then proceed to add minerals."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Keep trace-stock pH6.5 followed by7.0 separate from the receiving medium pH7.2–7.4.", "layer_assessments": []}, {"quantity_id": "q46", "topic": "Trace-stock pH step 2", "source": [{"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[2].steps[1]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"step\": \"Adjust final pH to 7.0.\"\n                    }", "exact_decoded_object": {"step": "Adjust final pH to 7.0."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "Keep trace-stock pH6.5 followed by7.0 separate from the receiving medium pH7.2–7.4.", "layer_assessments": []}, {"quantity_id": "q47", "topic": "Missing complete main preparation including all numeric conditions", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.comments[0]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients, except NaHCO3 and Na2S・9H2O, and bring to a boilfor 5--10 sec. Cool down under a stream of N2 and add NaHCO3 to the medium. Anaerobically dispense the medium into culture vessels, seal with butyl rubber stoppers and autoclave. Separately autoclave 5% Na2S・9H2O solution under a N2 atmosphere. Prior to inoculation, aseptically and anaerobically add the Na2S・9H2O solution to the medium. Check final pH tobe 7.2--7.4.\"\n    }", "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix ingredients, except NaHCO3 and Na2S・9H2O, and bring to a boilfor 5--10 sec. Cool down under a stream of N2 and add NaHCO3 to the medium. Anaerobically dispense the medium into culture vessels, seal with butyl rubber stoppers and autoclave. Separately autoclave 5% Na2S・9H2O solution under a N2 atmosphere. Prior to inoculation, aseptically and anaerobically add the Na2S・9H2O solution to the medium. Check final pH tobe 7.2--7.4."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T07:48:20.745563Z", "quote": "{\n                        \"step\": \"Mix ingredients, except NaHCO3 and Na2S x 9H2O, and bring to a boil for 5-10 sec. Cool down under a stream of N2 and add NaHCO3 to the medium. Anaerobically dispense the medium into culture vessels, seal with butyl rubber stoppers and autoclave. Separately autoclave 5% Na2S x 9H2O solution under a N2 atmosphere. Prior to inoculation, aseptically and anaerobically add the Na2S x 9H2O solution to the medium. Check final pH to be 7.2-7.4.\"\n                    }", "exact_decoded_object": {"step": "Mix ingredients, except NaHCO3 and Na2S x 9H2O, and bring to a boil for 5-10 sec. Cool down under a stream of N2 and add NaHCO3 to the medium. Anaerobically dispense the medium into culture vessels, seal with butyl rubber stoppers and autoclave. Separately autoclave 5% Na2S x 9H2O solution under a N2 atmosphere. Prior to inoculation, aseptically and anaerobically add the Na2S x 9H2O solution to the medium. Check final pH to be 7.2-7.4."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "add", "rationale": "The primary default autoclave121°C15 minutes is explicitly stated unless overridden; the separate5% sulfide stock has no stated percentage basis or addition volume. Do not infer these missing quantities.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The explicit boiling5–10 seconds, cooling under N2, staged bicarbonate/sulfide handling, butyl closure and autoclaving are absent. Restore exact source process without guessing unspecified doses.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The explicit boiling5–10 seconds, cooling under N2, staged bicarbonate/sulfide handling, butyl closure and autoclaving are absent. Restore exact source process without guessing unspecified doses.", "missing": true}]}, {"quantity_id": "q48", "topic": "Missing final pH range", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5", "locator": "$.meta.ph", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote": "\"ph\": \"7.2 - 7.4\""}], "decision": "add", "rationale": "Restore the stated range, not the scalar provider midpoint.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale": "Primary and TOGO support7.2–7.4; provider7.3 is not a replacement for the explicit range.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml", "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale": "Primary and TOGO support7.2–7.4; provider7.3 is not a replacement for the explicit range.", "missing": true}]}, {"quantity_id": "q49", "topic": "Primary default sterilization", "source": [{"evidence_id": "jcm379", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=379", "raw_path": "REVIEW_WORK/batch060/source01-03/jcm379.bin", "raw_sha256": "e940e22473f4f6ff4f0aeb6ce1a7a5bf4372b7d66afe6ea0b9c46213230a36bf", "locator": "Header default", "accessed_at": "2026-10-28T07:48:20.429444Z", "quote": "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min."}], "decision": "add", "rationale": "The default is explicit source context and applies only where not overridden; no additional culture conditions are inferred.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:009755.

All current target/owner IDs and scoped dependency forms were checked against exact OLS objects and current catalog rows. Current Mg31795, Ca32583 and sulfide76209 are supported. M221 nickel34887 is too narrow in the wrong supplied form;53542 is the exact hexahydrate candidate. Mn hydrate count and generic vitamin stereochemical/vitamer specificity remain unresolved; no automatic mirror creation is proposed.

### History and evidence scope

provenance: concern. Targets: CultureMech:009755.

Current source bytes, complete histories and scoped historical reports were read. Missing claim-level linkage and any malformed historical metadata are distinguished from authenticated source bytes; originals remain append-only.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:009755.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:009755.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Restore source units and honest concentration bases

major / open / confirmed; issue key: culturemech-009755-restore-source-units-and-honest-concentration-bases.

Water1 L, resazurin1 mg, calcium sulfate dihydrate12.5 mg and stock additions10 ml/1 ml were stored as G_PER_L. Ten additional gram-batch numbers were treated as identical g/L without an explicit final-volume basis. Current API main g_l is explicitly declared on its1011 ml basis and differs from those digits; retain that as provider data instead of conflating it with primary batch input.

### f2: Resolve only the referenced stock subsections

major / open / confirmed; issue key: culturemech-009755-resolve-only-the-referenced-stock-subsections.

Both stock names are placeholders and compositions empty, while preferred_term already names the correct references. Reuse only M190/JCM197 vitamins and M221/JCM228 trace minerals. Credit repaired M190 batch notes. The M221 selenite0.2 g conflicts with JCM228/API0.1 g and must be explicitly resolved before propagation; its nickel hexahydrate is grounded to anhydrous34887, and its unspecified manganese hydrate must not be silently converted to a chosen hydrate.

### f3: Restore source-specific preparation and pH

major / open / confirmed; issue key: culturemech-009755-restore-source-specific-preparation-and-ph.

The main source process and final pH range7.2–7.4 are absent. Nitrogen is stored as a default VARIABLE ingredient despite its preparation role. Restore the exact staged process and scoped root evidence; do not add fictional nested evidence fields or infer a5% basis or stock volume.

### f4: Preserve current chemical repairs and append-only provenance

minor / open / confirmed; issue key: culturemech-009755-preserve-current-chemical-repairs-and-append-only-provenance.

MgSO4 heptahydrate, calcium sulfate dihydrate and sodium sulfide nonahydrate primary IDs are already appropriate; absent mirrors are not wrong chemistry. D--Glucose is an imported display label and lacks a verified local grounding. Current quantity/preparation evidence needs claim linkage; old September final-volume and forced duplicate-merging recommendations are not automatically adopted.

## Recommended Actions And Acceptance Checks

### action1

Water1 L, resazurin1 mg, calcium sulfate dihydrate12.5 mg and stock additions10 ml/1 ml were stored as G_PER_L. Ten additional gram-batch numbers were treated as identical g/L without an explicit final-volume basis. Current API main g_l is explicitly declared on its1011 ml basis and differs from those digits; retain that as provider data instead of conflating it with primary batch input.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Both stock names are placeholders and compositions empty, while preferred_term already names the correct references. Reuse only M190/JCM197 vitamins and M221/JCM228 trace minerals. Credit repaired M190 batch notes. The M221 selenite0.2 g conflicts with JCM228/API0.1 g and must be explicitly resolved before propagation; its nickel hexahydrate is grounded to anhydrous34887, and its unspecified manganese hydrate must not be silently converted to a chosen hydrate.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

The main source process and final pH range7.2–7.4 are absent. Nitrogen is stored as a default VARIABLE ingredient despite its preparation role. Restore the exact staged process and scoped root evidence; do not add fictional nested evidence fields or infer a5% basis or stock volume.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Link exact current source claims, reconcile the D-glucose display label and verify its identity before adding a term. Preserve all original history events; append verified new context. Retain current hydrate repairs and source-variant distinctions rather than forcing the separately named J379 record to merge.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch060/record02/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| historical-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-3 | reports/yaml_record_review/20260922T042554Z-CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-reader | REVIEW_WORK/batch060/record02/historical-reader.json | context_only | All exact target/owner historical report texts and current raw/literal/locator joins; historical recommendations remain subject to current stage and volume evidence. |
| dependency-vitamins | data/normalized_yaml/bacterial/togo_medium_m190.yaml; Complete document | context_only | Only solutions[1].composition is the referenced JCM197 vitamin stock. Parent receiving dose, all main ingredients, trace minerals, gases and parent process are excluded. |
| dependency-trace | data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml; Complete document | context_only | Only the JCM228 trace-mineral composition and its pH preparation are referenced. Parent medium, general salts, iron stock and their doses/conditions are excluded. |
| jcm379 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=379; Exact source identity and scoped formulation/preparation | supports | Complete primary main table, explicit JCM197/JCM228 stock references, preparation and default sterilization. Water is an input, not an explicit final volume. |
| togoM374 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374; Exact source identity and scoped formulation/preparation | supports | Complete exact M374 payload: original JCM_M379 identity, meta.ph range, original units, two stock references and full comment. |
| apiJ379 | https://mediadive.dsmz.de/rest/medium/J379; Exact source identity and scoped formulation/preparation | supports | Current provider main volume1011 and explicit main g_l differ from the local mass-as-rate digits. Full stock3861/3903 definitions and scoped preparation are retained separately. |
| jcm197 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197; Exact source identity and scoped formulation/preparation | supports | Only Trace vitamins subsection supplies the ten components and1 L water. Parent medium, trace minerals and their receiving doses/conditions are excluded. |
| jcm228 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=228; Exact source identity and scoped formulation/preparation | supports | Only Trace minerals solution subsection and its two pH steps are transferred. Selenite is0.1 g; no parent recipe, general salts or iron-stock prescription transfers. |
| togoM190 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190; Exact source identity and scoped formulation/preparation | supports | Only components[1] vitamin subsection is compared with the already repaired local vitamin composition. Original main receiving dose is outside this review. |
| togoM221 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221; Exact source identity and scoped formulation/preparation | supports | Only components[2] trace minerals and the matching stock comments are assessed; its selenite0.2 g conflicts with primary JCM2280.1 g. |
| apiJ197 | https://mediadive.dsmz.de/rest/medium/J197; Exact source identity and scoped formulation/preparation | supports | Only solution3861 Trace vitamins is an independent provider comparison; no parent pH or formula transfer. |
| apiJ228 | https://mediadive.dsmz.de/rest/medium/J228; Exact source identity and scoped formulation/preparation | supports | Only solution3903 Trace minerals is compared; explicit g_l applies to this stock, not the receiving medium. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components, _solution_from_item, _extract_preparation_steps, _extract_ph | context_only | Current _extract_primary_components separates main sections and stock references; _solution_from_item preserves amounts/references and avoids flattening. _extract_preparation_steps retains comments. _extract_ph reads root ph while M374 stores meta.ph, so that path does not recover this range. Current code is not proof of past execution. |
| writer-solution-migration | scripts/migrate_solutions_from_ingredients.py; _resolve_solution and _migrate_media_file | context_only | Current unresolved-solution path retains preferred_term, empty composition and copied concentration; it does not authenticate that unit or supply stock chemistry. |
| writer-mg-repair | scripts/migrate_mgso4_heptahydrate_term.py; iter_ingredients and main | context_only | The specific current migration changes generic32599 only for heptahydrate-labelled primary terms. Current Mg31795 is correct; missing secondary grounding is not a chemical error. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32583 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32583; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17997 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17997; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16526 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16526; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi35696 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_35696; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86249; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32035 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32035; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49105; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16494; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi18276 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18276; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63939; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86360 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86360; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76181 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76181; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi48843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_48843; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch060/record02/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch060/record02/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch060/record02/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch060/record02/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch060/record02/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch060/record02/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch060/record02/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch060/record02/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch060/record02/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Primary JCM379 gives1 L water plus stock additions, not an explicit measured final volume. Provider1011 ml and g_l are declared normalization metadata; local same-digit G_PER_L is not authenticated by the batch table.
- M221/TOGO trace selenite0.2 g conflicts with primary JCM228 and API0.1 g. Both source versions remain visible; the discrepancy is not silently repaired by copying the dependency.
- The separate sulfide stock has a bare5% label but no stated percentage basis or addition volume. No missing quantity is guessed.
- Only M190 vitamins and M221 trace minerals are assessed for transfer. Other parent composition, receiving doses, iron/general-salt stocks, gas prescriptions and culture conditions are excluded; their scalar/history inventory is context only.
- Calcium pantothenate in the vitamin source is generic; its D-specific current31345 structure is not independently confirmed by that wording. Unspecified manganese hydrate, biotin stereochemistry, vitamin B12 vitamer and lipoic-acid stereochemistry are not narrowed. D-glucose is a verified source name, but no replacement accession is proposed without its own verification.
- Historical reports are derivative: two October reports explicitly performed zero source checks; September unit observations are reassessed, and its assumed1011 ml physical final-volume and forced source-collapse recommendations are not adopted. No strain-specific growth evidence is asserted.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T080433Z-batch060-record02-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Carnobacterium Pleistocaenium Medium: restore source units and scoped dependencies'
started_at: '2026-10-28T07:46:03.954885Z'
finished_at: '2026-10-28T08:04:33.456937Z'
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
summary: TOGO M374 is the JCM379 source lineage. Five stored amount/unit pairs are
  wrong, ten further mass-per-liter assertions lack the asserted denominator, both
  named stock references are empty shells, and source preparation/pH are absent. Current
  M190 vitamin repairs are credited; the M221 trace dependency has separate topology,
  source-conflict and nickel-form limits.
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
  - path: data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml
    sha256: 9c2bc0fd56de18631e46948e9db8534eeef36680db11c4fc1f018b9d688f42f5
    role: target
  - path: data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml
    sha256: e7343894bbbb4ac7e5ca584e384eae31ead5cc04b4e09a5db39efa7a9ed4930c
    role: context
  - path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    sha256: cf22094de35bf56a49112d9bb392a04278fe0db621adf332ad13958502d07923
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.md
    sha256: 0801af2ad793d2facd373edbed9e3c69753f3e5543a27bf057ded93ff8fd0034
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.md
    sha256: 6194d13782939e98264ffb65c22817366409317a9ae62d0db2a3070caebbc5ff
    role: context
  - path: reports/yaml_record_review/20260922T042554Z-CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.md
    sha256: d993c8a9f280201d32db2a7ec32bbca6112cb937018c04a7db13625fbf9a6231
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  selection: Actual batch060 native selection index 02.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009755
targets:
- target_id: CultureMech:009755
  path: data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml
  label: carnobacterium_pleistocaenium_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:009755
  command: just validate-schema data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml
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
  - CultureMech:009755
  command: just validate-strict data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml
    --out REVIEW_WORK/batch060/record02/strict.tsv --workers 1
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
  - CultureMech:009755
  command: just validate-terms data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml
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
  - CultureMech:009755
  command: just validate-references data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 9c2bc0fd56de18631e46948e9db8534eeef36680db11c4fc1f018b9d688f42f5
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: cf22094de35bf56a49112d9bb392a04278fe0db621adf332ad13958502d07923
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch060/record02/identity-search.json
  accessed_at: '2026-10-28T08:03:18.608890Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems resolved uniquely. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: a68ef490b9ccbffc6783916b1591285e7af8ec87c37e2cc3dfd050e70c6ad70b
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Current composition parser restricts ingredients to the primary solution,
    excludes solvent and recognized stock additions, and retains explicit g_l. The
    solution parser preserves referenced or percent-defined stocks and source attributes.
    Preparation parsing still concatenates all solution steps into root preparation_steps;
    source-stage annotation remains important. These present functions do not prove
    the historical execution that produced this record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Current compatibility preserves scientific fields and list order and rejects
    unequal formulations; only specified provenance/evidence lists are unioned. It
    performs no concentration conversion or stock expansion and does not authenticate
    historical merges.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients, merge_ingredient_group
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 0801af2ad793d2facd373edbed9e3c69753f3e5543a27bf057ded93ff8fd0034
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 6194d13782939e98264ffb65c22817366409317a9ae62d0db2a3070caebbc5ff
- evidence_id: historical-3
  kind: record_content
  reference: reports/yaml_record_review/20260922T042554Z-CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: d993c8a9f280201d32db2a7ec32bbca6112cb937018c04a7db13625fbf9a6231
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch060/record02/historical-reader.json
  accessed_at: '2026-10-28T08:03:18.612455Z'
  support: context_only
  summary: All exact target/owner historical report texts and current raw/literal/locator
    joins; historical recommendations remain subject to current stage and volume evidence.
  snapshot_sha256: 8ffe040227a6f5b72219e3d960758e02ae1a78292aa836695ab030878974d111
- evidence_id: dependency-vitamins
  kind: record_content
  reference: data/normalized_yaml/bacterial/togo_medium_m190.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Only solutions[1].composition is the referenced JCM197 vitamin stock. Parent
    receiving dose, all main ingredients, trace minerals, gases and parent process
    are excluded.
  snapshot_sha256: b1924e7eb436d56c5bd4826f07cafff130341054acfd808fb1c9e5bca914e3fa
- evidence_id: dependency-trace
  kind: record_content
  reference: data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Only the JCM228 trace-mineral composition and its pH preparation are referenced.
    Parent medium, general salts, iron stock and their doses/conditions are excluded.
  snapshot_sha256: e7343894bbbb4ac7e5ca584e384eae31ead5cc04b4e09a5db39efa7a9ed4930c
- evidence_id: jcm379
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=379
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:20.429444Z'
  support: supports
  summary: Complete primary main table, explicit JCM197/JCM228 stock references, preparation
    and default sterilization. Water is an input, not an explicit final volume.
  snapshot_sha256: e940e22473f4f6ff4f0aeb6ce1a7a5bf4372b7d66afe6ea0b9c46213230a36bf
- evidence_id: togoM374
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:22.477016Z'
  support: supports
  summary: 'Complete exact M374 payload: original JCM_M379 identity, meta.ph range,
    original units, two stock references and full comment.'
  snapshot_sha256: e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5
- evidence_id: apiJ379
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J379
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:20.745563Z'
  support: supports
  summary: Current provider main volume1011 and explicit main g_l differ from the
    local mass-as-rate digits. Full stock3861/3903 definitions and scoped preparation
    are retained separately.
  snapshot_sha256: 7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b
- evidence_id: jcm197
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:20.811258Z'
  support: supports
  summary: Only Trace vitamins subsection supplies the ten components and1 L water.
    Parent medium, trace minerals and their receiving doses/conditions are excluded.
  snapshot_sha256: 39580c63dd4a26cd4a98ee1d836b658683fcbff3e0df2adcb4208907cac40532
- evidence_id: jcm228
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=228
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:20.995175Z'
  support: supports
  summary: Only Trace minerals solution subsection and its two pH steps are transferred.
    Selenite is0.1 g; no parent recipe, general salts or iron-stock prescription transfers.
  snapshot_sha256: 0e685d7f7df6ca1cb736757312a37ef8db9619d9d1e6726f17a15970696f75be
- evidence_id: togoM190
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:22.592228Z'
  support: supports
  summary: Only components[1] vitamin subsection is compared with the already repaired
    local vitamin composition. Original main receiving dose is outside this review.
  snapshot_sha256: 61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528
- evidence_id: togoM221
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:22.724427Z'
  support: supports
  summary: Only components[2] trace minerals and the matching stock comments are assessed;
    its selenite0.2 g conflicts with primary JCM2280.1 g.
  snapshot_sha256: f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6
- evidence_id: apiJ197
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J197
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:20.766991Z'
  support: supports
  summary: Only solution3861 Trace vitamins is an independent provider comparison;
    no parent pH or formula transfer.
  snapshot_sha256: 779da00f024a3dd2cf334054533a6126405cc0ec8afd169902d02e5e893f75fb
- evidence_id: apiJ228
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J228
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T07:48:21.282164Z'
  support: supports
  summary: Only solution3903 Trace minerals is compared; explicit g_l applies to this
    stock, not the receiving medium.
  snapshot_sha256: b05c0f4969d00ff1f9437ab345e34cbec81c23900ba2fcaf1909672cc2bd195e
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components, _solution_from_item, _extract_preparation_steps,
    _extract_ph
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Current _extract_primary_components separates main sections and stock references;
    _solution_from_item preserves amounts/references and avoids flattening. _extract_preparation_steps
    retains comments. _extract_ph reads root ph while M374 stores meta.ph, so that
    path does not recover this range. Current code is not proof of past execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer-solution-migration
  kind: record_content
  reference: scripts/migrate_solutions_from_ingredients.py
  locator: _resolve_solution and _migrate_media_file
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: Current unresolved-solution path retains preferred_term, empty composition
    and copied concentration; it does not authenticate that unit or supply stock chemistry.
  snapshot_sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
- evidence_id: writer-mg-repair
  kind: record_content
  reference: scripts/migrate_mgso4_heptahydrate_term.py
  locator: iter_ingredients and main
  accessed_at: '2026-10-28T08:03:18.534516Z'
  support: context_only
  summary: The specific current migration changes generic32599 only for heptahydrate-labelled
    primary terms. Current Mg31795 is correct; missing secondary grounding is not
    a chemical error.
  snapshot_sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:22.883097Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42561686e12ba0831d99216248ea8c0b3338b461b0b77dd988f3096ad8678e59
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.672076Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.600268Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:28.507407Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 913baf38abc38dd61f05c5d636fd6532b70a668673a1f5762f290d2b67270164
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.230031Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.886467Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.309113Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3eece7d96d2433ff020ece90db55323d138c5c828b78198f91d26b3eafa91f9f
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.473452Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8fc333e98ee953346b5c291b9e5765e77d03cc46740a1282af3e5f4ad355de1a
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.925820Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 314c75cd12ea5d1343b4c0bafd40e0ad72c15b19d64f8cb9152000c0d8839f56
- evidence_id: chebi32583
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32583
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.276350Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: bb76fa6464f579ff9218bf3c39d0374635193572c64fffc9e98c9d20aca283b1
- evidence_id: chebi17997
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17997
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.184945Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3072b950418eb270c362b75526cb52e64d918480d57dcafd96d75961002f3d3e
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:22.265747Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.191625Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 015a33a158257cc5cba8a8e62de382053399be060366af5d95074883bb22b86e
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32954
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.516578Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 34c7d0dea7bc001a0a3b3b388138837cb1aba3b252017bc1ff8625b7a3ff655d
- evidence_id: chebi16526
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16526
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.557895Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a46d1979945f86fa259f0c40d36d152254b9b4a949a60bbfbb7ef7d01b247561
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.594002Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:28.978650Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.677867Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.505165Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2bb4588e6734285b5536bdac78701f9800fdb8d17236d12cf5a1c30490f1614d
- evidence_id: chebi35696
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_35696
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.139032Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b0671d570f256f8479ecacea745d00f94a953ac336192c6b41bd8a6dcd527e57
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.082549Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.769771Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d2305ca671adbbd3b0cc07b2331373a768bb44d41f32f61ba894594ae470eff
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.306683Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 371aa3b809db6c5d1ec8f8b8be40011e6b1132b1c0be40e70fb927788728d65a
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86249
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.604638Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 69797bf2582679b3f621fa4f982077ed90f48f3a5e1293c7444a3aaacbb25ba2
- evidence_id: chebi32035
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32035
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.877190Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: beb9265e17aebd20539ab8a464558e2820b9155c520635a44f77fa3e48f51ad4
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.253093Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0d2e75e0bd98dbffff14d85a41dfd0af8aae2a8d65a945d34a4126a17091c2b8
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.830018Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42ea4022bd68e8fa28962bc496ca757174da7bbd18ce06b7f3d521885609a50c
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.692039Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: fc6b8e9d8657914ed8fd568c69d8a5b2cf41b26767bd6361a5e2d258883be97d
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.316800Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d2a04309eb6976fd395f9684ec4c3f5192362e2b6b75464b0af128a28e188d25
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.064130Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 491af523ba70d13857fcb828561d0556e46382fa0591011a06693d7db24ad91f
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.718246Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dcee85bb585d3a73341ab66eff772dc6361330b3c899c4daecbda49d5e84e590
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.841698Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5c42e2236866d0314bc8d45947ddf9eb2fdf6364d08e802b0fb271011cbfe563
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.977351Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f8bec809c7ba5a36faea58b8fe1b5110f0d75dbd4ac1929a121cd352bce63309
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.237820Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2890ef915cd546e70c1e638af285a3cc19b8299ae7722d00b43a40170a57ab8a
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.355188Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: db6824ffab0d71efc11d1e64b505ae583949e9d5837086a4b0e7b364b2933a22
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.993081Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 98a5682728cfda4162de150a88ae8c4b3a70c2d7c248634a5108be50a888a692
- evidence_id: chebi18276
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18276
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:24.459497Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ce8012cf1de413b6c7fbf591125f8a666316a00f6cf7a1add46293e860b9fc13
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:26.037813Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:25.442414Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63939
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:28.919753Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f2fb7b5c3e7fec44d19e40f18cfbfa699c6010ad22cb76a9d2acd2b60950d98e
- evidence_id: chebi86360
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86360
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:30.222866Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d7fa588a0312e9c257c235a7219db2e63b9d8a1ae7c8af0af9d549739f00aa6d
- evidence_id: chebi76181
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76181
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:29.142134Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a87ea29ff8c63f729fb352f5ee6651e79b50d28f84f791164a4a8c4c771758ff
- evidence_id: chebi48843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_48843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:27.504735Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b0f375d805b7a7f9be7bcee85303ca0b1a5cec772abb2bc7dd7ca646771d766e
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T07:48:23.970715Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5f7b2f292559b9033f3c62c8403ed552842a28535010d6af5daa018a0977c28d
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch060/record02/quantity-inventory.json
  accessed_at: '2026-10-28T08:03:18.692816Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: bb4911ff4d1acbc2541bb900a14865ee6e18052d7d00202dc4502224bd33898b
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch060/record02/grounding-inventory.json
  accessed_at: '2026-10-28T08:03:18.692919Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 0c0cb76a3e5afaf33e77a0885935816f91e14cc44333c062925b42287c9a50ce
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch060/record02/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T08:03:18.693062Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 6adefb3358d97cc158d0f16805ebba172ad31a25af5cae7f9e516db384aba0d5
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch060/record02/scalar-census.json
  accessed_at: '2026-10-28T08:03:18.693104Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 739639cfe332f72eadf460d389af3663f7745d6132c3f9e31104a71e085031fa
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch060/record02/validate-schema.json
  accessed_at: '2026-10-28T07:46:05.134823Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: f6ab7ded0b2a1a12d80a1b272852e6155a49e9835de4c91ae0a996f948638e67
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch060/record02/validate-strict.json
  accessed_at: '2026-10-28T07:46:06.178920Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch060/record02/strict.tsv\n"
  snapshot_sha256: 5b5a5b133a5573cccb16587adae6397548e15de865efd18b40d0bddcef727447
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch060/record02/validate-terms.json
  accessed_at: '2026-10-28T07:46:07.303825Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 3bef48b474cb80642757e03ef656971b6314c228a5362521cf6380cd3f5f244a
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch060/record02/validate-references.json
  accessed_at: '2026-10-28T07:46:08.169965Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 7764a7d47787914c95dee556b19bd98bd881fd7214350b5654c085d15b086c25
assessments:
- assessment_id: a1
  area: identity
  topic: JCM and TOGO namespace
  outcome: supported
  summary: M374 explicitly identifies JCM_M379; M190 is JCM197 and M221 is JCM228.
    The dependency references select vitamin and trace-mineral subsections, not their
    parent media. The current generated record has one maintained owner. Source-name
    spelling is retained without inferring a strain-growth assertion or forced duplicate
    merge.
  target_ids:
  - CultureMech:009755
  evidence_ids:
  - identity-search
  - togoM374
  - jcm379
  - togoM190
  - togoM221
- assessment_id: a2
  area: completeness
  topic: Source process and existing repairs
  outcome: concern
  summary: Current M190 vitamin batch notes and water are already repaired and credited.
    M374 still lacks its preparation/pH and stock definitions. Current importer stages
    and merge compatibility guards reduce recurrence; they do not prove historical
    execution or authorize a source-variant collapse.
  target_ids:
  - CultureMech:009755
  evidence_ids:
  - dependency-vitamins
  - dependency-trace
  - writer-togo
  - writer-mg-repair
  - writer-merge
  - historical-reader
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:009755
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Distilled water", "source": [{"evidence_id":
    "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[0]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001",
    "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044",
    "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "correct", "rationale": "The source
    gives 1 L as a batch input, not the stored G_PER_L value. Preserve water as volume
    or the stated mg amount; do not infer a final liter. The provider''s separate
    declared normalization remains explicitly labelled.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The source gives 1 L as a batch input, not
    the stored G_PER_L value. Preserve water as volume or the stated mg amount; do
    not infer a final liter. The provider''s separate declared normalization remains
    explicitly labelled."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source gives 1 L as a batch
    input, not the stored G_PER_L value. Preserve water as volume or the stated mg
    amount; do not infer a final liter. The provider''s separate declared normalization
    remains explicitly labelled."}]}, {"quantity_id": "q2", "topic": "MgSO4・7H2O",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"MgSO4・7H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001002\",\n          \"gmo_id\":
    \"GMO_001002\",\n          \"label\": \"Magnesium sulfate heptahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "MgSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001002",
    "gmo_id": "GMO_001002", "label": "Magnesium sulfate heptahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.098912,\n                        \"mmol_l\": 0.401305,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.1, "unit": "g", "g_l": 0.098912,
    "mmol_l": 0.401305, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "unsupported", "rationale": "The source supports 0.1 g per recipe batch, but not
    this same number as G_PER_L. One liter of water plus stock additions does not
    establish final volume; current provider explicitly declares a different g_l on
    its1011 ml basis. Preserve source batch support separately, not an unqualified
    local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.1 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.1 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q3", "topic": "NaCl",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[2]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"NaCl\",\n          \"volume\": 5,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001004\",\n          \"gmo_id\":
    \"GMO_001004\",\n          \"label\": \"Sodium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "NaCl", "volume": 5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001004",
    "gmo_id": "GMO_001004", "label": "Sodium chloride", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    4.9456,\n                        \"mmol_l\": 84.6269,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "NaCl", "compound_id": 43, "amount": 5, "unit": "g", "g_l": 4.9456, "mmol_l":
    84.6269, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "The source supports 5 g per recipe batch, but not this same number
    as G_PER_L. One liter of water plus stock additions does not establish final volume;
    current provider explicitly declares a different g_l on its1011 ml basis. Preserve
    source batch support separately, not an unqualified local concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per
    recipe batch, but not this same number as G_PER_L. One liter of water plus stock
    additions does not establish final volume; current provider explicitly declares
    a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per
    recipe batch, but not this same number as G_PER_L. One liter of water plus stock
    additions does not establish final volume; current provider explicitly declares
    a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q4", "topic": "KH2PO4",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[3]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"KH2PO4\",\n          \"volume\":
    0.3,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001006\",\n          \"gmo_id\":
    \"GMO_001006\",\n          \"label\": \"Potassium phosphate monobasic\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "KH2PO4", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001006",
    "gmo_id": "GMO_001006", "label": "Potassium phosphate monobasic", "properties":
    [{"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label":
    "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.296736,\n                        \"mmol_l\": 2.1805,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "KH2PO4", "compound_id": 11, "amount": 0.3, "unit": "g", "g_l": 0.296736, "mmol_l":
    2.1805, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "The source supports 0.3 g per recipe batch, but not this same number
    as G_PER_L. One liter of water plus stock additions does not establish final volume;
    current provider explicitly declares a different g_l on its1011 ml basis. Preserve
    source batch support separately, not an unqualified local concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q5", "topic": "NH4Cl",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[4]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"NH4Cl\",\n          \"volume\": 1,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001008\",\n          \"gmo_id\":
    \"GMO_001008\",\n          \"label\": \"Ammonium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000062\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000062\",\n              \"label\": \"Nitrogen
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "NH4Cl", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001008",
    "gmo_id": "GMO_001008", "label": "Ammonium chloride", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000062", "uri": "http://purl.jp/bio/10/gmo/GMO_000062",
    "label": "Nitrogen source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.98912,\n                        \"mmol_l\": 18.4917,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "NH4Cl", "compound_id": 42, "amount": 1, "unit": "g", "g_l": 0.98912, "mmol_l":
    18.4917, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "The source supports 1 g per recipe batch, but not this same number
    as G_PER_L. One liter of water plus stock additions does not establish final volume;
    current provider explicitly declares a different g_l on its1011 ml basis. Preserve
    source batch support separately, not an unqualified local concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 1 g per
    recipe batch, but not this same number as G_PER_L. One liter of water plus stock
    additions does not establish final volume; current provider explicitly declares
    a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 1 g per
    recipe batch, but not this same number as G_PER_L. One liter of water plus stock
    additions does not establish final volume; current provider explicitly declares
    a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q6", "topic": "D--Glucose",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[5]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"D--Glucose\",\n          \"volume\":
    5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001010\",\n          \"gmo_id\":
    \"GMO_001010\",\n          \"label\": \"D-Glucose\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000063\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000063\",\n              \"label\":
    \"Carbon source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "D--Glucose", "volume": 5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001010",
    "gmo_id": "GMO_001010", "label": "D-Glucose", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}], "roles": [{"id": "GMO_000063", "uri": "http://purl.jp/bio/10/gmo/GMO_000063",
    "label": "Carbon source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"D-Glucose\",\n                        \"compound_id\": 211,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    4.9456,\n                        \"mmol_l\": 27.4511,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "D-Glucose", "compound_id": 211, "amount": 5, "unit": "g", "g_l": 4.9456, "mmol_l":
    27.4511, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "The source supports 5 g per recipe batch, but not this same number
    as G_PER_L. One liter of water plus stock additions does not establish final volume;
    current provider explicitly declares a different g_l on its1011 ml basis. Preserve
    source batch support separately, not an unqualified local concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per
    recipe batch, but not this same number as G_PER_L. One liter of water plus stock
    additions does not establish final volume; current provider explicitly declares
    a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports 5 g per
    recipe batch, but not this same number as G_PER_L. One liter of water plus stock
    additions does not establish final volume; current provider explicitly declares
    a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q7", "topic": "Resazurin",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[6]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Resazurin\",\n          \"volume\":
    1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001012\",\n          \"gmo_id\":
    \"GMO_001012\",\n          \"label\": \"Resazurin\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000055\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000055\",\n              \"label\":
    \"pH dependent redox indicator\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "Resazurin", "volume": 1, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001012",
    "gmo_id": "GMO_001012", "label": "Resazurin", "properties": [{"id": "GMO_000041",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic compound"}, {"id":
    "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}], "roles": [{"id": "GMO_000055", "uri": "http://purl.jp/bio/10/gmo/GMO_000055",
    "label": "pH dependent redox indicator"}]}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path":
    "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"Resazurin\",\n                        \"compound_id\": 25,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.00098912,\n                        \"mmol_l\": 0.00431572,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound":
    "Resazurin", "compound_id": 25, "amount": 1, "unit": "mg", "g_l": 0.00098912,
    "mmol_l": 0.00431572, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The source gives 1 mg as a batch input, not the stored
    G_PER_L value. Preserve water as volume or the stated mg amount; do not infer
    a final liter. The provider''s separate declared normalization remains explicitly
    labelled.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source gives 1 mg as a batch
    input, not the stored G_PER_L value. Preserve water as volume or the stated mg
    amount; do not infer a final liter. The provider''s separate declared normalization
    remains explicitly labelled."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source gives 1 mg as a batch
    input, not the stored G_PER_L value. Preserve water as volume or the stated mg
    amount; do not infer a final liter. The provider''s separate declared normalization
    remains explicitly labelled."}]}, {"quantity_id": "q8", "topic": "Na2S・9H2O",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[7]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Na2S・9H2O\",\n          \"volume\":
    0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001014\",\n          \"gmo_id\":
    \"GMO_001014\",\n          \"label\": \"Sodium sulfide nonahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000064\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000064\",\n              \"label\":
    \"Reducing agent\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "Na2S・9H2O", "volume": 0.4, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001014",
    "gmo_id": "GMO_001014", "label": "Sodium sulfide nonahydrate", "properties": [{"id":
    "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}], "roles": [{"id": "GMO_000064", "uri": "http://purl.jp/bio/10/gmo/GMO_000064",
    "label": "Reducing agent"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.395648,\n                        \"mmol_l\": 1.64728,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 0.4, "unit": "g", "g_l": 0.395648,
    "mmol_l": 1.64728, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "unsupported", "rationale": "The source supports 0.4 g per recipe batch, but not
    this same number as G_PER_L. One liter of water plus stock additions does not
    establish final volume; current provider explicitly declares a different g_l on
    its1011 ml basis. Preserve source batch support separately, not an unqualified
    local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.4",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.4",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q9", "topic": "KCl",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[8]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"KCl\",\n          \"volume\": 0.3,\n          \"unit\":
    \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001017\",\n          \"gmo_id\":
    \"GMO_001017\",\n          \"label\": \"Potassium chloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "KCl", "volume": 0.3, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001017",
    "gmo_id": "GMO_001017", "label": "Potassium chloride", "properties": [{"id": "GMO_000046",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"},
    {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.296736,\n                        \"mmol_l\": 3.98036,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "KCl", "compound_id": 61, "amount": 0.3, "unit": "g", "g_l": 0.296736, "mmol_l":
    3.98036, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "The source supports 0.3 g per recipe batch, but not this same number
    as G_PER_L. One liter of water plus stock additions does not establish final volume;
    current provider explicitly declares a different g_l on its1011 ml basis. Preserve
    source batch support separately, not an unqualified local concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.3",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.3 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q10", "topic": "NaHCO3",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[9]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"NaHCO3\",\n          \"volume\":
    0.4,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001019\",\n          \"gmo_id\":
    \"GMO_001019\",\n          \"label\": \"Sodium bicarbonate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000046\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\":
    \"Defined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000038\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000038\",\n              \"label\":
    \"Buffer\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "NaHCO3", "volume": 0.4, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001019",
    "gmo_id": "GMO_001019", "label": "Sodium bicarbonate", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}], "roles": [{"id": "GMO_000038", "uri": "http://purl.jp/bio/10/gmo/GMO_000038",
    "label": "Buffer"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    0.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.395648,\n                        \"mmol_l\": 4.7097,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "NaHCO3", "compound_id": 55, "amount": 0.4, "unit": "g", "g_l": 0.395648, "mmol_l":
    4.7097, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "The source supports 0.4 g per recipe batch, but not this same number
    as G_PER_L. One liter of water plus stock additions does not establish final volume;
    current provider explicitly declares a different g_l on its1011 ml basis. Preserve
    source batch support separately, not an unqualified local concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.4",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "0.4",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.4 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q11", "topic": "CaSO4・2H2O",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[10]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"CaSO4・2H2O\",\n          \"volume\":
    12.5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001087\",\n          \"gmo_id\":
    \"GMO_001087\",\n          \"label\": \"Calcium sulfate dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            },\n            {\n              \"id\":
    \"GMO_000040\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\":
    \"Inorganic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000078\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\":
    \"Mineral source\"\n            }\n          ]\n        }", "exact_decoded_object":
    {"component_name": "CaSO4・2H2O", "volume": 12.5, "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001087",
    "gmo_id": "GMO_001087", "label": "Calcium sulfate dihydrate", "properties": [{"id":
    "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049", "label": "Simple
    component"}, {"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040",
    "label": "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"CaSO4 x 2 H2O\",\n                        \"compound_id\": 190,\n                        \"amount\":
    12.5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.012364,\n                        \"mmol_l\": 0.0718119,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "CaSO4 x 2 H2O", "compound_id": 190, "amount": 12.5, "unit": "mg", "g_l": 0.012364,
    "mmol_l": 0.0718119, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "The source gives 12.5 mg as a batch input, not the stored
    G_PER_L value. Preserve water as volume or the stated mg amount; do not infer
    a final liter. The provider''s separate declared normalization remains explicitly
    labelled.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "12.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 12.5
    mg as a batch input, not the stored G_PER_L value. Preserve water as volume or
    the stated mg amount; do not infer a final liter. The provider''s separate declared
    normalization remains explicitly labelled."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "12.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source gives 12.5
    mg as a batch input, not the stored G_PER_L value. Preserve water as volume or
    the stated mg amount; do not infer a final liter. The provider''s separate declared
    normalization remains explicitly labelled."}]}, {"quantity_id": "q12", "topic":
    "Yeast extract (BD-Difco)", "source": [{"evidence_id": "togoM374", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path":
    "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[11]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Yeast extract (BD-Difco)\",\n          \"volume\":
    0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001018\",\n          \"gmo_id\":
    \"GMO_001018\",\n          \"label\": \"Bacto &trade; Yeast extract\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "exact_decoded_object": {"component_name": "Yeast extract (BD-Difco)", "volume":
    0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001018", "gmo_id": "GMO_001018",
    "label": "Bacto &trade; Yeast extract", "properties": [{"id": "GMO_000047", "uri":
    "http://purl.jp/bio/10/gmo/GMO_000047", "label": "Undefined component"}], "roles":
    []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379",
    "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\":
    \"BD-Difco\",\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.197824,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Yeast extract", "compound_id": 16, "attribute": "BD-Difco", "amount": 0.2, "unit":
    "g", "g_l": 0.197824, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "unsupported", "rationale": "The source supports 0.2 g per recipe batch, but not
    this same number as G_PER_L. One liter of water plus stock additions does not
    establish final volume; current provider explicitly declares a different g_l on
    its1011 ml basis. Preserve source batch support separately, not an unqualified
    local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.2 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    0.2 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q13", "topic": "Bacto
    peptone (BD-Difco)", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[12]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Bacto peptone (BD-Difco)\",\n          \"volume\":
    1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001089\",\n          \"gmo_id\":
    \"GMO_001089\",\n          \"label\": \"Bacto &trade; Peptone\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined
    component\"\n            }\n          ],\n          \"roles\": []\n        }",
    "exact_decoded_object": {"component_name": "Bacto peptone (BD-Difco)", "volume":
    1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001089", "gmo_id": "GMO_001089",
    "label": "Bacto &trade; Peptone", "properties": [{"id": "GMO_000047", "uri": "http://purl.jp/bio/10/gmo/GMO_000047",
    "label": "Undefined component"}], "roles": []}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379",
    "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Bacto peptone\",\n                        \"compound_id\": 19,\n                        \"attribute\":
    \"BD-Difco\",\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.98912,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Bacto peptone", "compound_id": 19, "attribute": "BD-Difco", "amount": 1, "unit":
    "g", "g_l": 0.98912, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "unsupported", "rationale": "The source supports 1 g per recipe batch, but not
    this same number as G_PER_L. One liter of water plus stock additions does not
    establish final volume; current provider explicitly declares a different g_l on
    its1011 ml basis. Preserve source batch support separately, not an unqualified
    local concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    1 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The source supports
    1 g per recipe batch, but not this same number as G_PER_L. One liter of water
    plus stock additions does not establish final volume; current provider explicitly
    declares a different g_l on its1011 ml basis. Preserve source batch support separately,
    not an unqualified local concentration."}]}, {"quantity_id": "q14", "topic": "N2",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[15]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"N2\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_002261\",\n          \"gmo_id\":
    \"GMO_002261\",\n          \"label\": \"Nitrogen gas\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000077\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000077\",\n              \"label\": \"Gas\"\n            }\n          ],\n          \"roles\":
    []\n        }", "exact_decoded_object": {"component_name": "N2", "gmo": "http://purl.jp/bio/10/gmo/GMO_002261",
    "gmo_id": "GMO_002261", "label": "Nitrogen gas", "properties": [{"id": "GMO_000077",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000077", "label": "Gas"}], "roles": []},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "evidence_only", "rationale": "Nitrogen
    is explicitly used during preparation; VARIABLE has no measured gas amount. Retain
    this as preparation context without treating it as a quantified medium ingredient.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "evidence_only", "rationale": "Nitrogen is explicitly
    used during preparation; VARIABLE has no measured gas amount. Retain this as preparation
    context without treating it as a quantified medium ingredient."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "evidence_only", "rationale": "Nitrogen is explicitly
    used during preparation; VARIABLE has no measured gas amount. Retain this as preparation
    context without treating it as a quantified medium ingredient."}]}, {"quantity_id":
    "q15", "topic": "Trace vitamins (see Medium [M190])", "source": [{"evidence_id":
    "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id":
    "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path":
    "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\":
    \"Trace vitamins\",\n                        \"solution_id\": 3861,\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "solution":
    "Trace vitamins", "solution_id": 3861, "amount": 10, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "correct", "rationale": "The source
    explicitly adds 10 ml of the named stock per receiving batch. Correct the stored
    G_PER_L unit to an actual stock addition volume; preserve the reference namespace
    and do not inherit the parent medium''s receiving dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 10
    ml of the named stock per receiving batch. Correct the stored G_PER_L unit to
    an actual stock addition volume; preserve the reference namespace and do not inherit
    the parent medium''s receiving dose."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[0].concentration", "stored_value": {"value": "10", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 10
    ml of the named stock per receiving batch. Correct the stored G_PER_L unit to
    an actual stock addition volume; preserve the reference namespace and do not inherit
    the parent medium''s receiving dose."}]}, {"quantity_id": "q16", "topic": "Existing
    stock1 name", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id":
    "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "Replace the placeholder Unknown solution with the exact
    referenced stock name; retain the already informative preferred_term.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Replace the placeholder Unknown solution with the exact
    referenced stock name; retain the already informative preferred_term."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[0].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Replace the placeholder Unknown solution with the exact
    referenced stock name; retain the already informative preferred_term."}]}, {"quantity_id":
    "q17", "topic": "Existing stock1 composition", "source": [{"evidence_id": "togoM374",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id":
    "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "add", "rationale": "Resolve only the referenced vitamin or trace-mineral subsection;
    the existing empty composition supplies no stock chemistry.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Resolve only the referenced vitamin or trace-mineral subsection;
    the existing empty composition supplies no stock chemistry."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[0].composition", "stored_value": [], "decision": "add",
    "rationale": "Resolve only the referenced vitamin or trace-mineral subsection;
    the existing empty composition supplies no stock chemistry."}]}, {"quantity_id":
    "q18", "topic": "Existing stock1 preferred_term", "source": [{"evidence_id": "togoM374",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[13]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace vitamins (see Medium [M190])\",\n          \"volume\":
    10,\n          \"unit\": \"ml\",\n          \"reference_media_id\": \"M190\",\n          \"properties\":
    [],\n          \"roles\": []\n        }", "exact_decoded_object": {"component_name":
    "Trace vitamins (see Medium [M190])", "volume": 10, "unit": "ml", "reference_media_id":
    "M190", "properties": [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "evidence_only", "rationale": "The current preferred_term already preserves the
    stock identity and TOGO reference; credit it.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path":
    "solutions[0].preferred_term", "stored_value": "Trace vitamins (see Medium [M190])",
    "decision": "evidence_only", "rationale": "The current preferred_term already
    preserves the stock identity and TOGO reference; credit it."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[0].preferred_term", "stored_value": "Trace vitamins (see
    Medium [M190])", "decision": "evidence_only", "rationale": "The current preferred_term
    already preserves the stock identity and TOGO reference; credit it."}]}, {"quantity_id":
    "q19", "topic": "Trace minerals solution (see Medium [M221])", "source": [{"evidence_id":
    "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium
    [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium
    [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties":
    [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\":
    \"Trace minerals solution\",\n                        \"solution_id\": 3903,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 12, "solution":
    "Trace minerals solution", "solution_id": 3903, "amount": 1, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "correct", "rationale": "The source
    explicitly adds 1 ml of the named stock per receiving batch. Correct the stored
    G_PER_L unit to an actual stock addition volume; preserve the reference namespace
    and do not inherit the parent medium''s receiving dose.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 1
    ml of the named stock per receiving batch. Correct the stored G_PER_L unit to
    an actual stock addition volume; preserve the reference namespace and do not inherit
    the parent medium''s receiving dose."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "correct", "rationale": "The source explicitly adds 1
    ml of the named stock per receiving batch. Correct the stored G_PER_L unit to
    an actual stock addition volume; preserve the reference namespace and do not inherit
    the parent medium''s receiving dose."}]}, {"quantity_id": "q20", "topic": "Existing
    stock2 name", "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium
    [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium
    [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties":
    [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "correct", "rationale":
    "Replace the placeholder Unknown solution with the exact referenced stock name;
    retain the already informative preferred_term.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path":
    "solutions[1].name", "stored_value": "Unknown solution", "decision": "correct",
    "rationale": "Replace the placeholder Unknown solution with the exact referenced
    stock name; retain the already informative preferred_term."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[1].name", "stored_value": "Unknown solution", "decision":
    "correct", "rationale": "Replace the placeholder Unknown solution with the exact
    referenced stock name; retain the already informative preferred_term."}]}, {"quantity_id":
    "q21", "topic": "Existing stock2 composition", "source": [{"evidence_id": "togoM374",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium
    [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium
    [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties":
    [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "add", "rationale":
    "Resolve only the referenced vitamin or trace-mineral subsection; the existing
    empty composition supplies no stock chemistry.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml", "field_path":
    "solutions[1].composition", "stored_value": [], "decision": "add", "rationale":
    "Resolve only the referenced vitamin or trace-mineral subsection; the existing
    empty composition supplies no stock chemistry."}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[1].composition", "stored_value": [], "decision": "add",
    "rationale": "Resolve only the referenced vitamin or trace-mineral subsection;
    the existing empty composition supplies no stock chemistry."}]}, {"quantity_id":
    "q22", "topic": "Existing stock2 preferred_term", "source": [{"evidence_id": "togoM374",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.components[0].items[14]", "accessed_at": "2026-10-28T07:48:22.477016Z",
    "quote": "{\n          \"component_name\": \"Trace minerals solution (see Medium
    [M221])\",\n          \"volume\": 1,\n          \"unit\": \"ml\",\n          \"reference_media_id\":
    \"M221\",\n          \"properties\": [],\n          \"roles\": []\n        }",
    "exact_decoded_object": {"component_name": "Trace minerals solution (see Medium
    [M221])", "volume": 1, "unit": "ml", "reference_media_id": "M221", "properties":
    [], "roles": []}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "The current preferred_term already preserves the stock identity
    and TOGO reference; credit it.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "solutions[1].preferred_term", "stored_value": "Trace minerals solution
    (see Medium [M221])", "decision": "evidence_only", "rationale": "The current preferred_term
    already preserves the stock identity and TOGO reference; credit it."}, {"path":
    "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "solutions[1].preferred_term", "stored_value": "Trace minerals solution
    (see Medium [M221])", "decision": "evidence_only", "rationale": "The current preferred_term
    already preserves the stock identity and TOGO reference; credit it."}]}, {"quantity_id":
    "q23", "topic": "Vitamin stock: Distilled water", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[0]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001",
    "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044",
    "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "verified", "rationale": "The current
    dependency repair correctly preserves this source batch amount and withdraws an
    unsupported final-liter assertion. Credit the existing scoped composition; the
    parent receiving dose does not transfer. Current JCM197 and provider stock3861
    agree on the amount; provider stock g_l remains a separate declared basis. Existing
    attached claim snippets match the freshly captured TOGO M190 bytes and cited raw
    digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates
    the source bytes, not the old retrieval event.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path": "solutions[1].composition[0].concentration",
    "stored_value": {"value": "1", "unit": "L"}, "decision": "verified", "rationale":
    "The current dependency repair correctly preserves this source batch amount and
    withdraws an unsupported final-liter assertion. Credit the existing scoped composition;
    the parent receiving dose does not transfer. Current JCM197 and provider stock3861
    agree on the amount; provider stock g_l remains a separate declared basis. Existing
    attached claim snippets match the freshly captured TOGO M190 bytes and cited raw
    digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528; this authenticates
    the source bytes, not the old retrieval event."}]}, {"quantity_id": "q24", "topic":
    "Vitamin stock: Biotin", "source": [{"evidence_id": "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[1]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Biotin\",\n          \"volume\":
    2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001025\",\n          \"gmo_id\":
    \"GMO_001025\",\n          \"label\": \"Biotin\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000041\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\":
    \"Organic compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Biotin", "volume": 2, "unit": "mg",
    "gmo": "http://purl.jp/bio/10/gmo/GMO_001025", "gmo_id": "GMO_001025", "label":
    "Biotin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.00818632,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Biotin", "compound_id": 46, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l":
    0.00818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "verified",
    "rationale": "The current dependency repair correctly preserves this source batch
    amount and withdraws an unsupported final-liter assertion. Credit the existing
    scoped composition; the parent receiving dose does not transfer. Current JCM197
    and provider stock3861 agree on the amount; provider stock g_l remains a separate
    declared basis. Existing attached claim snippets match the freshly captured TOGO
    M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[1].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 2
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q25", "topic": "Vitamin stock: p--Aminobenzoic acid", "source": [{"evidence_id":
    "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[2]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"p--Aminobenzoic acid\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001026\",\n          \"gmo_id\":
    \"GMO_001026\",\n          \"label\": \"4-Aminobenzoic acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "p--Aminobenzoic acid", "volume": 5,
    "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001026", "gmo_id": "GMO_001026",
    "label": "4-Aminobenzoic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0364591,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "p-Aminobenzoic acid", "compound_id": 47, "amount": 5, "unit": "mg", "g_l": 0.005,
    "mmol_l": 0.0364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "verified", "rationale": "The current dependency repair correctly preserves this
    source batch amount and withdraws an unsupported final-liter assertion. Credit
    the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[2].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 5
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q26", "topic": "Vitamin stock: Thiamine・HCl", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[3]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Thiamine・HCl\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001027\",\n          \"gmo_id\":
    \"GMO_001027\",\n          \"label\": \"Thiamine hydrochloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Thiamine・HCl", "volume": 5, "unit":
    "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001027", "gmo_id": "GMO_001027", "label":
    "Thiamine hydrochloride", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0148236,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Thiamine HCl", "compound_id": 1207, "amount": 5, "unit": "mg", "g_l": 0.005,
    "mmol_l": 0.0148236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "verified", "rationale": "The current dependency repair correctly preserves this
    source batch amount and withdraws an unsupported final-liter assertion. Credit
    the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[3].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 5
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q27", "topic": "Vitamin stock: Calcium pantothenate", "source": [{"evidence_id":
    "togoM190", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[4]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Calcium pantothenate\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001028\",\n          \"gmo_id\":
    \"GMO_001028\",\n          \"label\": \"Calcium pantothenate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Calcium pantothenate", "volume": 5,
    "unit": "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001028", "gmo_id": "GMO_001028",
    "label": "Calcium pantothenate", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0104925,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Calcium pantothenate", "compound_id": 518, "amount": 5, "unit": "mg", "g_l":
    0.005, "mmol_l": 0.0104925, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "verified", "rationale": "The current dependency repair correctly preserves this
    source batch amount and withdraws an unsupported final-liter assertion. Credit
    the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[4].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 5
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q28", "topic": "Vitamin stock: Pyridoxine・HCl", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[5]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Pyridoxine・HCl\",\n          \"volume\":
    10,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001029\",\n          \"gmo_id\":
    \"GMO_001029\",\n          \"label\": \"Pyridoxine hydrochloride\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Pyridoxine・HCl", "volume": 10, "unit":
    "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001029", "gmo_id": "GMO_001029", "label":
    "Pyridoxine hydrochloride", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    10,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0486287,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Pyridoxine hydrochloride", "compound_id": 519, "amount": 10, "unit": "mg", "g_l":
    0.01, "mmol_l": 0.0486287, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "verified", "rationale": "The current dependency repair correctly preserves this
    source batch amount and withdraws an unsupported final-liter assertion. Credit
    the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[5].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 10
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q29", "topic": "Vitamin stock: Folic acid", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[6]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Folic acid\",\n          \"volume\":
    2,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001033\",\n          \"gmo_id\":
    \"GMO_001033\",\n          \"label\": \"Folic acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Folic acid", "volume": 2, "unit":
    "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001033", "gmo_id": "GMO_001033", "label":
    "Folic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.00453104,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Folic acid", "compound_id": 138, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l":
    0.00453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "verified",
    "rationale": "The current dependency repair correctly preserves this source batch
    amount and withdraws an unsupported final-liter assertion. Credit the existing
    scoped composition; the parent receiving dose does not transfer. Current JCM197
    and provider stock3861 agree on the amount; provider stock g_l remains a separate
    declared basis. Existing attached claim snippets match the freshly captured TOGO
    M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[6].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 2
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q30", "topic": "Vitamin stock: Vitamin B12", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[7]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Vitamin B12\",\n          \"volume\":
    0.1,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001034\",\n          \"gmo_id\":
    \"GMO_001034\",\n          \"label\": \"Cobalamin\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Vitamin B12", "volume": 0.1, "unit":
    "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001034", "gmo_id": "GMO_001034", "label":
    "Cobalamin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    0.1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0001,\n                        \"mmol_l\": 7.3779e-5,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "Vitamin B12", "compound_id": 18, "amount": 0.1, "unit": "mg", "g_l": 0.0001,
    "mmol_l": 7.3779e-05, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "verified", "rationale": "The current dependency repair correctly preserves this
    source batch amount and withdraws an unsupported final-liter assertion. Credit
    the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[7].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 0.1
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q31", "topic": "Vitamin stock: Riboflavin", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[8]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Riboflavin\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001037\",\n          \"gmo_id\":
    \"GMO_001037\",\n          \"label\": \"Riboflavin\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Riboflavin", "volume": 5, "unit":
    "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001037", "gmo_id": "GMO_001037", "label":
    "Riboflavin", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0132837,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Riboflavin", "compound_id": 136, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l":
    0.0132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "verified",
    "rationale": "The current dependency repair correctly preserves this source batch
    amount and withdraws an unsupported final-liter assertion. Credit the existing
    scoped composition; the parent receiving dose does not transfer. Current JCM197
    and provider stock3861 agree on the amount; provider stock g_l remains a separate
    declared basis. Existing attached claim snippets match the freshly captured TOGO
    M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[8].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 5
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q32", "topic": "Vitamin stock: Nicotinic acid", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[9]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Nicotinic acid\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001038\",\n          \"gmo_id\":
    \"GMO_001038\",\n          \"label\": \"Nicotinic acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000045\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000045\",\n              \"label\": \"Vitamin\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Nicotinic acid", "volume": 5, "unit":
    "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001038", "gmo_id": "GMO_001038", "label":
    "Nicotinic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000045", "uri": "http://purl.jp/bio/10/gmo/GMO_000045",
    "label": "Vitamin"}]}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.0406141,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "Nicotinic acid", "compound_id": 139, "amount": 5, "unit": "mg", "g_l": 0.005,
    "mmol_l": 0.0406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "verified", "rationale": "The current dependency repair correctly preserves this
    source batch amount and withdraws an unsupported final-liter assertion. Credit
    the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[9].notes", "stored_value": "Role: Vitamin; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 5
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q33", "topic": "Vitamin stock: Lipoic acid", "source": [{"evidence_id": "togoM190",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M190",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM190.bin", "raw_sha256": "61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528",
    "locator": "$.components[1].items[10]", "accessed_at": "2026-10-28T07:48:22.592228Z",
    "quote": "{\n          \"component_name\": \"Lipoic acid\",\n          \"volume\":
    5,\n          \"unit\": \"mg\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001699\",\n          \"gmo_id\":
    \"GMO_001699\",\n          \"label\": \"Lipoic acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000067\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000067\",\n              \"label\": \"Growth factor\"\n            }\n          ]\n        }",
    "exact_decoded_object": {"component_name": "Lipoic acid", "volume": 5, "unit":
    "mg", "gmo": "http://purl.jp/bio/10/gmo/GMO_001699", "gmo_id": "GMO_001699", "label":
    "Lipoic acid", "properties": [{"id": "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041",
    "label": "Organic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000067", "uri": "http://purl.jp/bio/10/gmo/GMO_000067",
    "label": "Growth factor"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Lipoic acid\",\n                        \"compound_id\": 368,\n                        \"amount\":
    5,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.005,\n                        \"mmol_l\": 0.024233,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Lipoic acid", "compound_id": 368, "amount": 5, "unit": "mg", "g_l": 0.005, "mmol_l":
    0.024233, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "verified",
    "rationale": "The current dependency repair correctly preserves this source batch
    amount and withdraws an unsupported final-liter assertion. Credit the existing
    scoped composition; the parent receiving dose does not transfer. Current JCM197
    and provider stock3861 agree on the amount; provider stock g_l remains a separate
    declared basis. Existing attached claim snippets match the freshly captured TOGO
    M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/togo_medium_m190.yaml", "field_path":
    "solutions[1].composition[10].notes", "stored_value": "Role: Growth factor; Properties:
    Organic compound, Defined component, Simple component\n\nSource batch input: 5
    mg. Final preparation volume is not independently established; the unsupported
    g/L assertion is withdrawn, not replaced by an assumed one-liter concentration.",
    "decision": "verified", "rationale": "The current dependency repair correctly
    preserves this source batch amount and withdraws an unsupported final-liter assertion.
    Credit the existing scoped composition; the parent receiving dose does not transfer.
    Current JCM197 and provider stock3861 agree on the amount; provider stock g_l
    remains a separate declared basis. Existing attached claim snippets match the
    freshly captured TOGO M190 bytes and cited raw digest61c69f48450ab6c5f9328553ae143b64eeb8b7aab88fa1e966e00a19317cf528;
    this authenticates the source bytes, not the old retrieval event."}]}, {"quantity_id":
    "q34", "topic": "Trace stock: Na2MoO4・2H2O", "source": [{"evidence_id": "togoM221",
    "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[1]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"Na2MoO4・2H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001011\",\n          \"gmo_id\":
    \"GMO_001011\",\n          \"label\": \"Sodium molybdate dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Na2MoO4・2H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001011",
    "gmo_id": "GMO_001011", "label": "Sodium molybdate dihydrate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.413309,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l":
    0.413309, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This current dependency ingredient is a trace-stock component, not
    a directly transferable receiving-medium rate. Preserve its source batch amount
    in the referenced stock and the separate1 ml receiving addition. Explicit API
    stock g_l does not validate the flattened parent-stage placement.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement."}]}, {"quantity_id": "q35", "topic": "Trace stock: NiCl2・6H2O",
    "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[2]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"NiCl2・6H2O\",\n          \"volume\":
    0.025,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001022\",\n          \"gmo_id\":
    \"GMO_001022\",\n          \"label\": \"Nickel chloride hexahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "NiCl2・6H2O", "volume": 0.025, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001022",
    "gmo_id": "GMO_001022", "label": "Nickel chloride hexahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    0.025,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.025,\n                        \"mmol_l\": 0.192903,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.025, "unit": "g", "g_l": 0.025,
    "mmol_l": 0.192903, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This current dependency ingredient is a trace-stock component,
    not a directly transferable receiving-medium rate. Preserve its source batch amount
    in the referenced stock and the separate1 ml receiving addition. Explicit API
    stock g_l does not validate the flattened parent-stage placement.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.025",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement."}]}, {"quantity_id": "q36", "topic": "Trace stock: ZnSO4・7H2O",
    "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[3]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"ZnSO4・7H2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001023\",\n          \"gmo_id\":
    \"GMO_001023\",\n          \"label\": \"Zinc sulfate heptahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "ZnSO4・7H2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001023",
    "gmo_id": "GMO_001023", "label": "Zinc sulfate heptahydrate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.347752,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l":
    0.347752, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This current dependency ingredient is a trace-stock component, not
    a directly transferable receiving-medium rate. Preserve its source batch amount
    in the referenced stock and the separate1 ml receiving addition. Explicit API
    stock g_l does not validate the flattened parent-stage placement.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement."}]}, {"quantity_id": "q37", "topic": "Trace stock: CuSO4・5H2O",
    "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[4]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"CuSO4・5H2O\",\n          \"volume\":
    0.01,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001039\",\n          \"gmo_id\":
    \"GMO_001039\",\n          \"label\": \"Copper(II) sulfate pentahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "CuSO4・5H2O", "volume": 0.01, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001039",
    "gmo_id": "GMO_001039", "label": "Copper(II) sulfate pentahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "CuSO4 x 5 H2O", "compound_id": 121, "amount": 0.01, "unit": "g", "g_l": 0.01,
    "mmol_l": 0.0400503, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This current dependency ingredient is a trace-stock component,
    not a directly transferable receiving-medium rate. Preserve its source batch amount
    in the referenced stock and the separate1 ml receiving addition. Explicit API
    stock g_l does not validate the flattened parent-stage placement.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement."}]}, {"quantity_id": "q38", "topic": "Trace stock: Nitrilotriacetic
    acid", "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[5]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"Nitrilotriacetic acid\",\n          \"volume\":
    1.5,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001053\",\n          \"gmo_id\":
    \"GMO_001053\",\n          \"label\": \"Nitrilotriacetic acid\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000041\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000041\",\n              \"label\": \"Organic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Nitrilotriacetic acid", "volume": 1.5, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001053",
    "gmo_id": "GMO_001053", "label": "Nitrilotriacetic acid", "properties": [{"id":
    "GMO_000041", "uri": "http://purl.jp/bio/10/gmo/GMO_000041", "label": "Organic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Nitrilotriacetic acid", "compound_id": 189, "amount": 1.5, "unit": "g", "g_l":
    1.5, "mmol_l": 7.84765, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This current dependency ingredient is a trace-stock component,
    not a directly transferable receiving-medium rate. Preserve its source batch amount
    in the referenced stock and the separate1 ml receiving addition. Explicit API
    stock g_l does not validate the flattened parent-stage placement.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement."}]}, {"quantity_id": "q39", "topic": "Trace stock: Na2WO4・2H2O",
    "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[6]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"Na2WO4・2H2O\",\n          \"volume\":
    1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001057\",\n          \"gmo_id\":
    \"GMO_001057\",\n          \"label\": \"Sodium tungstate dihydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Na2WO4・2H2O", "volume": 1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001057",
    "gmo_id": "GMO_001057", "label": "Sodium tungstate dihydrate", "properties": [{"id":
    "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic
    compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 3.03168,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Na2WO4 x 2 H2O", "compound_id": 249, "amount": 1, "unit": "g", "g_l": 1, "mmol_l":
    3.03168, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "correct",
    "rationale": "This current dependency ingredient is a trace-stock component, not
    a directly transferable receiving-medium rate. Preserve its source batch amount
    in the referenced stock and the separate1 ml receiving addition. Explicit API
    stock g_l does not validate the flattened parent-stage placement.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement."}]}, {"quantity_id": "q40", "topic": "Trace stock: MnSO4・xH2O",
    "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[7]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"MnSO4・xH2O\",\n          \"volume\":
    0.1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001065\",\n          \"gmo_id\":
    \"GMO_001065\",\n          \"label\": \"Manganese sulfate n-hydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "MnSO4・xH2O", "volume": 0.1, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001065",
    "gmo_id": "GMO_001065", "label": "Manganese sulfate n-hydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"MnSO4 x n H2O\",\n                        \"compound_id\": 1000,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 6, "compound": "MnSO4 x n H2O", "compound_id": 1000, "amount":
    0.1, "unit": "g", "g_l": 0.1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "correct", "rationale": "This current dependency ingredient is a trace-stock component,
    not a directly transferable receiving-medium rate. Preserve its source batch amount
    in the referenced stock and the separate1 ml receiving addition. Explicit API
    stock g_l does not validate the flattened parent-stage placement.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement."}]}, {"quantity_id": "q41", "topic": "Trace stock: Fe(NH4)2(SO4)2・6H2O",
    "source": [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[8]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"Fe(NH4)2(SO4)2・6H2O\",\n          \"volume\":
    0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001076\",\n          \"gmo_id\":
    \"GMO_001076\",\n          \"label\": \"Ammonium iron(II) sulfate hexahydrate\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Fe(NH4)2(SO4)2・6H2O", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001076",
    "gmo_id": "GMO_001076", "label": "Ammonium iron(II) sulfate hexahydrate", "properties":
    [{"id": "GMO_000040", "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label":
    "Inorganic compound"}, {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046",
    "label": "Defined component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Fe(NH4)2(SO4)2 x 6 H2O\",\n                        \"compound_id\": 247,\n                        \"amount\":
    0.2,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.2,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 2, "compound": "Fe(NH4)2(SO4)2 x 6 H2O", "compound_id": 247,
    "amount": 0.2, "unit": "g", "g_l": 0.2, "optional": 0}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "correct", "rationale": "This current dependency ingredient is a trace-stock
    component, not a directly transferable receiving-medium rate. Preserve its source
    batch amount in the referenced stock and the separate1 ml receiving addition.
    Explicit API stock g_l does not validate the flattened parent-stage placement.
    The current cleanup collapsed equal iron entries, but trace stock and the separate
    parent iron stock are still distinct stages; no iron-stock dose transfers.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "This current dependency
    ingredient is a trace-stock component, not a directly transferable receiving-medium
    rate. Preserve its source batch amount in the referenced stock and the separate1
    ml receiving addition. Explicit API stock g_l does not validate the flattened
    parent-stage placement. The current cleanup collapsed equal iron entries, but
    trace stock and the separate parent iron stock are still distinct stages; no iron-stock
    dose transfers."}]}, {"quantity_id": "q42", "topic": "Trace stock: Na2SeO3", "source":
    [{"evidence_id": "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[9]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"Na2SeO3\",\n          \"volume\":
    0.2,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001093\",\n          \"gmo_id\":
    \"GMO_001093\",\n          \"label\": \"Sodium selenite\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Na2SeO3", "volume": 0.2, "unit": "g", "gmo": "http://purl.jp/bio/10/gmo/GMO_001093",
    "gmo_id": "GMO_001093", "label": "Sodium selenite", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Na2SeO3\",\n                        \"compound_id\": 699,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 3, "compound": "Na2SeO3", "compound_id": 699, "amount": 0.1,
    "unit": "g", "g_l": 0.1, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "conflict", "rationale": "TOGO M221 and its local ingredient give0.2 g, while
    primary JCM228 and current J379/J228 provider trace stock give0.1 g. Preserve
    this genuine source discrepancy and resolve exact stock identity/version before
    transfer; do not silently choose the convenient value.", "layer_assessments":
    [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.2",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "TOGO M221 and its local
    ingredient give0.2 g, while primary JCM228 and current J379/J228 provider trace
    stock give0.1 g. Preserve this genuine source discrepancy and resolve exact stock
    identity/version before transfer; do not silently choose the convenient value."}]},
    {"quantity_id": "q43", "topic": "Trace-stock water", "source": [{"evidence_id":
    "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[0]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"Distilled water\",\n          \"volume\":
    1,\n          \"unit\": \"L\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001001\",\n          \"gmo_id\":
    \"GMO_001001\",\n          \"label\": \"Distilled water\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000040\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000040\",\n              \"label\": \"Inorganic
    compound\"\n            },\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000049\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000049\",\n              \"label\": \"Simple component\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating
    media\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "Distilled water", "volume": 1, "unit": "L", "gmo": "http://purl.jp/bio/10/gmo/GMO_001001",
    "gmo_id": "GMO_001001", "label": "Distilled water", "properties": [{"id": "GMO_000040",
    "uri": "http://purl.jp/bio/10/gmo/GMO_000040", "label": "Inorganic compound"},
    {"id": "GMO_000046", "uri": "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined
    component"}, {"id": "GMO_000049", "uri": "http://purl.jp/bio/10/gmo/GMO_000049",
    "label": "Simple component"}], "roles": [{"id": "GMO_000044", "uri": "http://purl.jp/bio/10/gmo/GMO_000044",
    "label": "Solvating media"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].recipe[9]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "add", "rationale": "One liter of stock
    water is explicit; it is not the parent water total or an independently stated
    final-volume makeup. Preserve the solvent within the stock.", "layer_assessments":
    []}, {"quantity_id": "q44", "topic": "Trace-stock KOH adjustment", "source": [{"evidence_id":
    "togoM221", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M221",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM221.bin", "raw_sha256": "f48133b53150b54b396f07b659f8abcc3220538aa0dc0911159b7f61c21ecce6",
    "locator": "$.components[2].items[10]", "accessed_at": "2026-10-28T07:48:22.724427Z",
    "quote": "{\n          \"component_name\": \"KOH\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001903\",\n          \"gmo_id\":
    \"GMO_001903\",\n          \"label\": \"Potassium hydroxide solution\",\n          \"properties\":
    [\n            {\n              \"id\": \"GMO_000046\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000046\",\n              \"label\": \"Defined
    component\"\n            },\n            {\n              \"id\": \"GMO_000051\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000051\",\n              \"label\": \"Solution\"\n            }\n          ],\n          \"roles\":
    [\n            {\n              \"id\": \"GMO_000078\",\n              \"uri\":
    \"http://purl.jp/bio/10/gmo/GMO_000078\",\n              \"label\": \"Mineral
    source\"\n            }\n          ]\n        }", "exact_decoded_object": {"component_name":
    "KOH", "gmo": "http://purl.jp/bio/10/gmo/GMO_001903", "gmo_id": "GMO_001903",
    "label": "Potassium hydroxide solution", "properties": [{"id": "GMO_000046", "uri":
    "http://purl.jp/bio/10/gmo/GMO_000046", "label": "Defined component"}, {"id":
    "GMO_000051", "uri": "http://purl.jp/bio/10/gmo/GMO_000051", "label": "Solution"}],
    "roles": [{"id": "GMO_000078", "uri": "http://purl.jp/bio/10/gmo/GMO_000078",
    "label": "Mineral source"}]}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "evidence_only",
    "rationale": "Scope KOH to the trace-stock pH procedure; no numeric amount is
    inferred.", "layer_assessments": [{"path": "data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "variable",
    "unit": "VARIABLE"}, "decision": "evidence_only", "rationale": "VARIABLE is nonquantitative
    adjustment context only; no KOH dose or concentration is supplied for this stock."}]},
    {"quantity_id": "q45", "topic": "Trace-stock pH step 1", "source": [{"evidence_id":
    "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path":
    "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"step\": \"Dissolve nitrilotriacetic acid
    and adjust pH to 6.5 with KOH. Then proceed to add minerals.\"\n                    }",
    "exact_decoded_object": {"step": "Dissolve nitrilotriacetic acid and adjust pH
    to 6.5 with KOH. Then proceed to add minerals."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "add", "rationale": "Keep trace-stock pH6.5 followed by7.0 separate
    from the receiving medium pH7.2–7.4.", "layer_assessments": []}, {"quantity_id":
    "q46", "topic": "Trace-stock pH step 2", "source": [{"evidence_id": "apiJ379",
    "reference": "https://mediadive.dsmz.de/rest/medium/J379", "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin",
    "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[2].steps[1]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"step\": \"Adjust final pH to 7.0.\"\n                    }",
    "exact_decoded_object": {"step": "Adjust final pH to 7.0."}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "add", "rationale": "Keep trace-stock pH6.5 followed by7.0 separate
    from the receiving medium pH7.2–7.4.", "layer_assessments": []}, {"quantity_id":
    "q47", "topic": "Missing complete main preparation including all numeric conditions",
    "source": [{"evidence_id": "togoM374", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374",
    "raw_path": "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.comments[0]", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote":
    "{\n      \"paragraph_index\": 2,\n      \"comment\": \"Mix ingredients, except
    NaHCO3 and Na2S・9H2O, and bring to a boilfor 5--10 sec. Cool down under a stream
    of N2 and add NaHCO3 to the medium. Anaerobically dispense the medium into culture
    vessels, seal with butyl rubber stoppers and autoclave. Separately autoclave 5%
    Na2S・9H2O solution under a N2 atmosphere. Prior to inoculation, aseptically and
    anaerobically add the Na2S・9H2O solution to the medium. Check final pH tobe 7.2--7.4.\"\n    }",
    "exact_decoded_object": {"paragraph_index": 2, "comment": "Mix ingredients, except
    NaHCO3 and Na2S・9H2O, and bring to a boilfor 5--10 sec. Cool down under a stream
    of N2 and add NaHCO3 to the medium. Anaerobically dispense the medium into culture
    vessels, seal with butyl rubber stoppers and autoclave. Separately autoclave 5%
    Na2S・9H2O solution under a N2 atmosphere. Prior to inoculation, aseptically and
    anaerobically add the Na2S・9H2O solution to the medium. Check final pH tobe 7.2--7.4."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "apiJ379", "reference": "https://mediadive.dsmz.de/rest/medium/J379",
    "raw_path": "REVIEW_WORK/batch060/source01-03/apiJ379.bin", "raw_sha256": "7b9f5ac84c7c8c8fe3950a6da702248084f937568ad18fb7afcd640eecd3520b",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T07:48:20.745563Z",
    "quote": "{\n                        \"step\": \"Mix ingredients, except NaHCO3
    and Na2S x 9H2O, and bring to a boil for 5-10 sec. Cool down under a stream of
    N2 and add NaHCO3 to the medium. Anaerobically dispense the medium into culture
    vessels, seal with butyl rubber stoppers and autoclave. Separately autoclave 5%
    Na2S x 9H2O solution under a N2 atmosphere. Prior to inoculation, aseptically
    and anaerobically add the Na2S x 9H2O solution to the medium. Check final pH to
    be 7.2-7.4.\"\n                    }", "exact_decoded_object": {"step": "Mix ingredients,
    except NaHCO3 and Na2S x 9H2O, and bring to a boil for 5-10 sec. Cool down under
    a stream of N2 and add NaHCO3 to the medium. Anaerobically dispense the medium
    into culture vessels, seal with butyl rubber stoppers and autoclave. Separately
    autoclave 5% Na2S x 9H2O solution under a N2 atmosphere. Prior to inoculation,
    aseptically and anaerobically add the Na2S x 9H2O solution to the medium. Check
    final pH to be 7.2-7.4."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "add",
    "rationale": "The primary default autoclave121°C15 minutes is explicitly stated
    unless overridden; the separate5% sulfide stock has no stated percentage basis
    or addition volume. Do not infer these missing quantities.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The explicit boiling5–10 seconds, cooling under N2, staged bicarbonate/sulfide
    handling, butyl closure and autoclaving are absent. Restore exact source process
    without guessing unspecified doses.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The explicit boiling5–10 seconds, cooling under N2, staged bicarbonate/sulfide
    handling, butyl closure and autoclaving are absent. Restore exact source process
    without guessing unspecified doses.", "missing": true}]}, {"quantity_id": "q48",
    "topic": "Missing final pH range", "source": [{"evidence_id": "togoM374", "reference":
    "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M374", "raw_path":
    "REVIEW_WORK/batch060/source01-03/togoM374.bin", "raw_sha256": "e9ae5d70d623990cff0a8a354f4d25b96bbc2ee2e8d3f70830c9bcf8329462c5",
    "locator": "$.meta.ph", "accessed_at": "2026-10-28T07:48:22.477016Z", "quote":
    "\"ph\": \"7.2 - 7.4\""}], "decision": "add", "rationale": "Restore the stated
    range, not the scalar provider midpoint.", "layer_assessments": [{"path": "data/merge_yaml/merged/CARNOBACTERIUM_PLEISTOCAENIUM_MEDIUM.yaml",
    "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale":
    "Primary and TOGO support7.2–7.4; provider7.3 is not a replacement for the explicit
    range.", "missing": true}, {"path": "data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml",
    "field_path": "ph_range", "stored_value": null, "decision": "add", "rationale":
    "Primary and TOGO support7.2–7.4; provider7.3 is not a replacement for the explicit
    range.", "missing": true}]}, {"quantity_id": "q49", "topic": "Primary default
    sterilization", "source": [{"evidence_id": "jcm379", "reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=379",
    "raw_path": "REVIEW_WORK/batch060/source01-03/jcm379.bin", "raw_sha256": "e940e22473f4f6ff4f0aeb6ce1a7a5bf4372b7d66afe6ea0b9c46213230a36bf",
    "locator": "Header default", "accessed_at": "2026-10-28T07:48:20.429444Z", "quote":
    "Unless otherwise stated, sterilize media by autoclaving at 121°C for 15 min."}],
    "decision": "add", "rationale": "The default is explicit source context and applies
    only where not overridden; no additional culture conditions are inferred.", "layer_assessments":
    []}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All current target/owner IDs and scoped dependency forms were checked against
    exact OLS objects and current catalog rows. Current Mg31795, Ca32583 and sulfide76209
    are supported. M221 nickel34887 is too narrow in the wrong supplied form;53542
    is the exact hexahydrate candidate. Mn hydrate count and generic vitamin stereochemical/vitamer
    specificity remain unresolved; no automatic mirror creation is proposed.
  target_ids:
  - CultureMech:009755
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Current source bytes, complete histories and scoped historical reports
    were read. Missing claim-level linkage and any malformed historical metadata are
    distinguished from authenticated source bytes; originals remain append-only.
  target_ids:
  - CultureMech:009755
  evidence_ids:
  - history
  - scalars
- assessment_id: a6
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:009755
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:009755
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-009755-restore-source-units-and-honest-concentration-bases
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore source units and honest concentration bases
  description: Water1 L, resazurin1 mg, calcium sulfate dihydrate12.5 mg and stock
    additions10 ml/1 ml were stored as G_PER_L. Ten additional gram-batch numbers
    were treated as identical g/L without an explicit final-volume basis. Current
    API main g_l is explicitly declared on its1011 ml basis and differs from those
    digits; retain that as provider data instead of conflating it with primary batch
    input.
  target_ids:
  - CultureMech:009755
  field_paths:
  - ingredients
  - solutions[0].concentration
  - solutions[1].concentration
  evidence_ids:
  - jcm379
  - togoM374
  - apiJ379
  - quantities
  rule_id: P2.2-unit-and-basis
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-009755-resolve-only-the-referenced-stock-subsections
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Resolve only the referenced stock subsections
  description: Both stock names are placeholders and compositions empty, while preferred_term
    already names the correct references. Reuse only M190/JCM197 vitamins and M221/JCM228
    trace minerals. Credit repaired M190 batch notes. The M221 selenite0.2 g conflicts
    with JCM228/API0.1 g and must be explicitly resolved before propagation; its nickel
    hexahydrate is grounded to anhydrous34887, and its unspecified manganese hydrate
    must not be silently converted to a chosen hydrate.
  target_ids:
  - CultureMech:009755
  field_paths:
  - solutions[0].name
  - solutions[0].composition
  - solutions[1].name
  - solutions[1].composition
  - data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml::ingredients[25].concentration
  - data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml::ingredients[18].term
  - data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml::ingredients[23].term
  evidence_ids:
  - jcm197
  - jcm228
  - togoM190
  - togoM221
  - apiJ379
  - dependency-vitamins
  - dependency-trace
  - grounding
  rule_id: P2.2-stock-scope
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-009755-restore-source-specific-preparation-and-ph
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Restore source-specific preparation and pH
  description: The main source process and final pH range7.2–7.4 are absent. Nitrogen
    is stored as a default VARIABLE ingredient despite its preparation role. Restore
    the exact staged process and scoped root evidence; do not add fictional nested
    evidence fields or infer a5% basis or stock volume.
  target_ids:
  - CultureMech:009755
  field_paths:
  - preparation_steps
  - ph_range
  - ingredients[13]
  - evidence
  evidence_ids:
  - jcm379
  - togoM374
  - apiJ379
  - writer-togo
  rule_id: P3-preparation-completeness
  native_severity: P3
  normalization_reason: Native P3 preparation omission is normalized to major because
    the entire source-specific staged anoxic procedure and final pH range are absent,
    affecting interpretation of the formulation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-009755-preserve-current-chemical-repairs-and-append-only-provenance
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve current chemical repairs and append-only provenance
  description: MgSO4 heptahydrate, calcium sulfate dihydrate and sodium sulfide nonahydrate
    primary IDs are already appropriate; absent mirrors are not wrong chemistry. D--Glucose
    is an imported display label and lacks a verified local grounding. Current quantity/preparation
    evidence needs claim linkage; old September final-volume and forced duplicate-merging
    recommendations are not automatically adopted.
  target_ids:
  - CultureMech:009755
  field_paths:
  - ingredients[5].preferred_term
  - ingredients[5].term
  - ingredients
  - evidence
  - curation_history
  evidence_ids:
  - grounding
  - history
  - historical-reader
  - writer-mg-repair
  - writer-formulation
  rule_id: P3-traceability
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Water1 L, resazurin1 mg, calcium sulfate dihydrate12.5 mg and stock
    additions10 ml/1 ml were stored as G_PER_L. Ten additional gram-batch numbers
    were treated as identical g/L without an explicit final-volume basis. Current
    API main g_l is explicitly declared on its1011 ml basis and differs from those
    digits; retain that as provider data instead of conflating it with primary batch
    input.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009755
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Both stock names are placeholders and compositions empty, while preferred_term
    already names the correct references. Reuse only M190/JCM197 vitamins and M221/JCM228
    trace minerals. Credit repaired M190 batch notes. The M221 selenite0.2 g conflicts
    with JCM228/API0.1 g and must be explicitly resolved before propagation; its nickel
    hexahydrate is grounded to anhydrous34887, and its unspecified manganese hydrate
    must not be silently converted to a chosen hydrate.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009755
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/archaea/TOGO_M221_Methanococcus_McC_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: The main source process and final pH range7.2–7.4 are absent. Nitrogen
    is stored as a default VARIABLE ingredient despite its preparation role. Restore
    the exact staged process and scoped root evidence; do not add fictional nested
    evidence fields or infer a5% basis or stock volume.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009755
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Link exact current source claims, reconcile the D-glucose display label
    and verify its identity before adding a term. Preserve all original history events;
    append verified new context. Retain current hydrate repairs and source-variant
    distinctions rather than forcing the separately named J379 record to merge.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:009755
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M374_Carnobacterium_Pleistocaenium_Medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- Primary JCM379 gives1 L water plus stock additions, not an explicit measured final
  volume. Provider1011 ml and g_l are declared normalization metadata; local same-digit
  G_PER_L is not authenticated by the batch table.
- M221/TOGO trace selenite0.2 g conflicts with primary JCM228 and API0.1 g. Both source
  versions remain visible; the discrepancy is not silently repaired by copying the
  dependency.
- The separate sulfide stock has a bare5% label but no stated percentage basis or
  addition volume. No missing quantity is guessed.
- Only M190 vitamins and M221 trace minerals are assessed for transfer. Other parent
  composition, receiving doses, iron/general-salt stocks, gas prescriptions and culture
  conditions are excluded; their scalar/history inventory is context only.
- Calcium pantothenate in the vitamin source is generic; its D-specific current31345
  structure is not independently confirmed by that wording. Unspecified manganese
  hydrate, biotin stereochemistry, vitamin B12 vitamer and lipoic-acid stereochemistry
  are not narrowed. D-glucose is a verified source name, but no replacement accession
  is proposed without its own verification.
- 'Historical reports are derivative: two October reports explicitly performed zero
  source checks; September unit observations are reassessed, and its assumed1011 ml
  physical final-volume and forced source-collapse recommendations are not adopted.
  No strain-specific growth evidence is asserted.'
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
